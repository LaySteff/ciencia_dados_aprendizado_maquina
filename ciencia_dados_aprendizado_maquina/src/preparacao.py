"""Limpeza, tratamento e transformação da base de arquivos PE.

Cada etapa registra o que foi feito e quantas linhas/valores foram afetados,
gerando a documentação das transformações exigida na Unidade V.

Uso:
    python -m src.preparacao
"""
import json

import numpy as np
import pandas as pd

from src.config import (ALVO, ARQ_RELATORIO, ARQ_TRATADO, COLUNAS_BOOLEANAS,
                        COLUNAS_NUMERICAS, DADOS_TRATADOS, caminho_bruto,
                        usando_dados_sinteticos)

MAPA_BOOLEANO = {
    "1": 1, "1.0": 1, "sim": 1, "s": 1, "true": 1, "verdadeiro": 1,
    "0": 0, "0.0": 0, "não": 0, "nao": 0, "n": 0, "false": 0, "falso": 0,
}


def carregar_bruto() -> pd.DataFrame:
    return pd.read_csv(caminho_bruto(), dtype={"sha256": str, "mes_aparicao": str})


def _padronizar_mes(valor):
    if pd.isna(valor):
        return np.nan
    v = str(valor).strip()
    if "/" in v:  # MM/AAAA -> AAAA-MM
        mes, ano = v.split("/")
        return f"{ano}-{int(mes):02d}"
    return v[:7]


def preparar(df: pd.DataFrame):
    """Retorna (df_tratado, relatorio) a partir da base bruta."""
    rel = {"fonte": str(caminho_bruto().name),
           "dados_sinteticos": usando_dados_sinteticos(),
           "linhas_iniciais": int(len(df)),
           "etapas": []}

    def registrar(etapa, descricao, **numeros):
        rel["etapas"].append({"etapa": etapa, "descricao": descricao,
                              **{k: int(v) for k, v in numeros.items()},
                              "linhas_apos": int(len(df))})

    df = df.copy()

    # 1. Padronização de texto (identificador e data).
    df["sha256"] = df["sha256"].astype(str).str.strip().str.lower()
    antes = df["mes_aparicao"].astype(str).str.contains("/").sum()
    df["mes_aparicao"] = df["mes_aparicao"].map(_padronizar_mes)
    registrar("1. Padronização de texto",
              "sha256 sem espaços e em minúsculas; mes_aparicao convertido para AAAA-MM",
              datas_convertidas=antes)

    # 2. Duplicatas (exatas e pelo identificador do arquivo).
    n0 = len(df)
    df = df.drop_duplicates()
    exatas = n0 - len(df)
    n1 = len(df)
    df = df.drop_duplicates(subset="sha256", keep="first")
    registrar("2. Remoção de duplicatas",
              "linhas idênticas e arquivos repetidos (mesmo sha256)",
              duplicatas_exatas=exatas, duplicatas_sha256=n1 - len(df))

    # 3. Amostras sem rótulo não servem para aprendizado supervisionado.
    n0 = len(df)
    df = df[df[ALVO].isin([0, 1])].copy()
    df[ALVO] = df[ALVO].astype(int)
    registrar("3. Remoção de amostras sem rótulo",
              "label = -1 (não rotulado) ou ausente", removidas=n0 - len(df))

    # 4. Booleanos em formatos inconsistentes -> 0/1.
    convertidos = 0
    for col in COLUNAS_BOOLEANAS:
        texto = df[col].astype(str).str.strip().str.lower()
        novo = texto.map(MAPA_BOOLEANO)
        ja_numerico = texto.isin(["0", "1", "0.0", "1.0", "nan"])
        convertidos += int((~ja_numerico & novo.notna()).sum())
        df[col] = novo  # valores não reconhecidos viram NaN e serão imputados
    registrar("4. Padronização de booleanos",
              "sim/não/S/N/true/false convertidos para 1/0",
              valores_convertidos=convertidos)

    # 5. Valores inválidos -> ausentes.
    for col in COLUNAS_NUMERICAS:
        df[col] = pd.to_numeric(df[col], errors="coerce")
    invalidos = 0
    for col in ["entropia_media_secao", "entropia_max_secao", "entropia_strings"]:
        mask = (df[col] < 0) | (df[col] > 8)  # entropia de Shannon por byte: [0, 8]
        invalidos += int(mask.sum())
        df.loc[mask, col] = np.nan
    mask = df["tamanho_bytes"] <= 0
    invalidos += int(mask.sum())
    df.loc[mask, "tamanho_bytes"] = np.nan
    contagens = [c for c in COLUNAS_NUMERICAS if c.startswith("num_")]
    for col in contagens:
        mask = df[col] < 0
        invalidos += int(mask.sum())
        df.loc[mask, col] = np.nan
    registrar("5. Valores inválidos",
              "entropia fora de [0, 8], tamanho <= 0 e contagens negativas marcados como ausentes",
              valores_invalidados=invalidos)

    # 6. Imputação de ausentes: mediana (numéricos) e moda (booleanos).
    #    Não imputamos por classe, pois isso vazaria o rótulo para as variáveis.
    ausentes = df[COLUNAS_NUMERICAS + COLUNAS_BOOLEANAS].isna().sum()
    rel["ausentes_por_coluna"] = {k: int(v) for k, v in ausentes.items() if v}
    for col in COLUNAS_NUMERICAS:
        df[col] = df[col].fillna(df[col].median())
    for col in COLUNAS_BOOLEANAS:
        df[col] = df[col].fillna(df[col].mode()[0]).astype(int)
    df["mes_aparicao"] = df["mes_aparicao"].fillna(df["mes_aparicao"].mode()[0])
    registrar("6. Imputação de ausentes",
              "mediana para numéricos, moda para booleanos e mes_aparicao",
              valores_imputados=int(ausentes.sum()))

    # 7. Consistência entre colunas: entropia máxima >= média.
    mask = df["entropia_max_secao"] < df["entropia_media_secao"]
    df.loc[mask, "entropia_max_secao"] = df.loc[mask, "entropia_media_secao"]
    registrar("7. Consistência entre colunas",
              "entropia_max_secao ajustada quando menor que a média",
              linhas_ajustadas=mask.sum())

    # 8. Transformação: tamanho em escala logarítmica (distribuição muito assimétrica).
    df["log10_tamanho"] = np.log10(df["tamanho_bytes"])
    registrar("8. Transformação logarítmica",
              "log10_tamanho criado a partir de tamanho_bytes")

    # 9. Outliers: apenas sinalizados (IQR). Não são removidos porque valores
    #    extremos são legítimos e informativos em arquivos maliciosos.
    outliers = {}
    for col in COLUNAS_NUMERICAS:
        q1, q3 = df[col].quantile([0.25, 0.75])
        iqr = q3 - q1
        outliers[col] = int(((df[col] < q1 - 1.5 * iqr) | (df[col] > q3 + 1.5 * iqr)).sum())
    rel["outliers_iqr_mantidos"] = outliers
    registrar("9. Outliers", "identificados pelo critério IQR e mantidos")

    rel["linhas_finais"] = int(len(df))
    rel["distribuicao_classes"] = {str(k): int(v) for k, v in df[ALVO].value_counts().items()}
    return df.reset_index(drop=True), rel


def salvar(df: pd.DataFrame, rel: dict) -> None:
    DADOS_TRATADOS.mkdir(parents=True, exist_ok=True)
    df.to_csv(ARQ_TRATADO, index=False)
    ARQ_RELATORIO.write_text(json.dumps(rel, indent=2, ensure_ascii=False), encoding="utf-8")


def carregar_tratado() -> pd.DataFrame:
    """Carrega a base tratada; gera a partir da bruta se ainda não existir."""
    if not ARQ_TRATADO.exists():
        salvar(*preparar(carregar_bruto()))
    return pd.read_csv(ARQ_TRATADO)


if __name__ == "__main__":
    tratado, relatorio = preparar(carregar_bruto())
    salvar(tratado, relatorio)
    print(json.dumps(relatorio, indent=2, ensure_ascii=False))
