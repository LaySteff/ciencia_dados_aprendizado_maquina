"""Gera uma base SINTÉTICA de características estáticas de arquivos PE.

ATENÇÃO: estes dados NÃO são reais. Eles imitam o formato das características
do conjunto EMBER apenas para que todos os notebooks possam ser executados
de ponta a ponta sem baixar ~1,6 GB de dados. Os resultados obtidos com esta
base são ilustrativos e devem ser refeitos com a amostra real do EMBER
(ver src/extrair_amostra_ember.py) antes de qualquer conclusão.

A base é propositalmente "suja" (valores ausentes, duplicatas, formatos
inconsistentes, valores inválidos e amostras sem rótulo) para servir de
material à aula de tratamento de dados.

Uso:
    python -m src.gerar_dados_sinteticos
"""
import numpy as np
import pandas as pd

from src.config import ARQ_SINTETICO, DADOS_BRUTOS

SEMENTE = 42
N_AMOSTRAS = 6000


def gerar(n: int = N_AMOSTRAS, semente: int = SEMENTE) -> pd.DataFrame:
    rng = np.random.default_rng(semente)

    mes = rng.integers(1, 13, size=n)  # 2018-01 .. 2018-12
    label = (rng.random(n) < 0.45).astype(int)
    mal = label == 1

    # Deriva de conceito: malwares mais recentes "se parecem" mais com benignos.
    deriva = (mes - 1) / 11.0  # 0 em janeiro, 1 em dezembro

    # Dois perfis de malware: "empacotado" (compactado/ofuscado: entropia alta,
    # poucas importações) e "comum" (parecido com software legítimo). A fração
    # de malwares comuns cresce ao longo do ano.
    empacotado = mal & (rng.random(n) < 0.55 - 0.30 * deriva)
    comum = mal & ~empacotado

    def escolher(cond_emp, cond_com, cond_ben):
        return np.where(empacotado, cond_emp, np.where(comum, cond_com, cond_ben))

    tamanho = escolher(rng.lognormal(11.9, 1.0, n), rng.lognormal(12.6, 1.3, n),
                       rng.lognormal(12.9, 1.4, n))
    num_secoes = escolher(rng.poisson(4.0, n), rng.poisson(5.5, n), rng.poisson(4.8, n)) + 1

    ent_media = escolher(rng.normal(7.0, 0.45, n),
                         rng.normal(5.7 - 0.3 * deriva, 0.85, n),
                         rng.normal(5.3, 0.85, n))
    ent_media = np.clip(ent_media, 0.5, 7.95)
    ent_max = np.clip(ent_media + np.abs(rng.normal(0.8, 0.5, n)), 0, 8)

    num_imp = escolher(rng.negative_binomial(3, 3 / (3 + 18), n),
                       rng.negative_binomial(4, 4 / (4 + 80 + 25 * deriva), n),
                       rng.negative_binomial(4, 4 / (4 + 115), n))
    num_exp = np.where(rng.random(n) < np.where(mal, 0.15, 0.30), rng.poisson(12, n), 0)
    num_strings = escolher(rng.lognormal(6.3, 0.6, n), rng.lognormal(7.0, 0.6, n),
                           rng.lognormal(7.2, 0.6, n)).round()
    ent_strings = np.clip(escolher(rng.normal(6.2, 0.4, n), rng.normal(5.7, 0.45, n),
                                   rng.normal(5.5, 0.45, n)), 0, 8)
    num_urls = escolher(rng.poisson(2.0, n), rng.poisson(3.0 - deriva, n), rng.poisson(1.6, n))
    num_paths = rng.poisson(np.where(mal, 2.8, 3.3))
    num_registro = escolher(rng.poisson(1.2, n), rng.poisson(2.6 - 0.8 * deriva, n),
                            rng.poisson(1.1, n))

    assinatura = rng.random(n) < escolher(0.05, 0.25 + 0.25 * deriva, 0.55)
    debug = rng.random(n) < np.where(mal, 0.20, 0.40)
    recursos = rng.random(n) < np.where(mal, 0.75, 0.85)
    exec_grav = rng.random(n) < escolher(0.55, 0.12, 0.05)

    # 3% de ruído de rótulo (rótulos errados também existem em bases reais).
    ruido = rng.random(n) < 0.03
    label = np.where(ruido, 1 - label, label)

    df = pd.DataFrame({
        "sha256": [f"{rng.integers(0, 2**63):016x}{i:048x}" for i in range(n)],
        "mes_aparicao": [f"2018-{m:02d}" for m in mes],
        "tamanho_bytes": tamanho.round().astype("int64"),
        "num_secoes": num_secoes,
        "entropia_media_secao": ent_media.round(4),
        "entropia_max_secao": ent_max.round(4),
        "num_importacoes": num_imp,
        "num_exportacoes": num_exp,
        "num_strings": num_strings,
        "entropia_strings": ent_strings.round(4),
        "num_urls": num_urls,
        "num_paths": num_paths,
        "num_registro": num_registro,
        "possui_assinatura": assinatura.astype(int),
        "possui_debug": debug.astype(int),
        "possui_recursos": recursos.astype(int),
        "secao_exec_gravavel": exec_grav.astype(int),
        "label": label,
    })
    return sujar(df, rng)


def sujar(df: pd.DataFrame, rng: np.random.Generator) -> pd.DataFrame:
    """Insere problemas típicos de qualidade de dados."""
    df = df.copy()
    n = len(df)

    # Booleanos em formatos misturados (texto livre vindo de fontes diferentes).
    for col in ["possui_assinatura", "possui_debug"]:
        df[col] = df[col].astype(object)
        idx = rng.choice(n, size=int(n * 0.10), replace=False)
        df.loc[idx, col] = [
            rng.choice(["sim", "Sim", "S", "true"]) if v == 1
            else rng.choice(["não", "nao", "N", "false"])
            for v in df.loc[idx, col]
        ]

    # Datas em dois formatos.
    idx = rng.choice(n, size=int(n * 0.08), replace=False)
    df.loc[idx, "mes_aparicao"] = [
        f"{m[5:]}/{m[:4]}" for m in df.loc[idx, "mes_aparicao"]
    ]

    # Hash com espaços e letras maiúsculas.
    idx = rng.choice(n, size=int(n * 0.05), replace=False)
    df.loc[idx, "sha256"] = [f"  {h.upper()} " for h in df.loc[idx, "sha256"]]

    # Valores ausentes.
    for col, frac in [("entropia_media_secao", 0.03), ("num_importacoes", 0.025),
                      ("num_strings", 0.02), ("possui_recursos", 0.02),
                      ("tamanho_bytes", 0.01)]:
        idx = rng.choice(n, size=int(n * frac), replace=False)
        df[col] = df[col].astype("float64") if col != "possui_recursos" else df[col].astype(object)
        df.loc[idx, col] = np.nan

    # Valores inválidos: entropia fora de [0, 8] e tamanho negativo.
    idx = rng.choice(n, size=int(n * 0.005), replace=False)
    df.loc[idx, "entropia_max_secao"] = rng.uniform(8.5, 12, size=len(idx)).round(4)
    idx = rng.choice(n, size=int(n * 0.003), replace=False)
    df.loc[idx, "tamanho_bytes"] = -1

    # Amostras sem rótulo (no EMBER, label = -1).
    idx = rng.choice(n, size=int(n * 0.05), replace=False)
    df.loc[idx, "label"] = -1

    # Duplicatas exatas.
    dup = df.sample(n=150, random_state=7)
    df = pd.concat([df, dup], ignore_index=True)
    return df.sample(frac=1, random_state=11).reset_index(drop=True)


if __name__ == "__main__":
    DADOS_BRUTOS.mkdir(parents=True, exist_ok=True)
    base = gerar()
    base.to_csv(ARQ_SINTETICO, index=False)
    print(f"Base sintética salva em {ARQ_SINTETICO} ({len(base)} linhas)")
