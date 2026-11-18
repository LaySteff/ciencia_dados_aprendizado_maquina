"""Extrai uma amostra tabular do conjunto EMBER 2018 (dados REAIS).

1. Baixe o EMBER 2018 (características brutas em JSON Lines) a partir do
   repositório oficial: https://github.com/elastic/ember
2. Descompacte e aponte este script para a pasta com os arquivos
   `train_features_*.jsonl` e `test_features.jsonl`.

Uso:
    python -m src.extrair_amostra_ember CAMINHO_DA_PASTA_EMBER --n 50000

O resultado é salvo em dados/brutos/ember_amostra.csv, com as mesmas colunas
da base sintética. A partir daí todos os notebooks passam a usar os dados
reais automaticamente (ver src/config.py).

Segurança: o EMBER contém apenas características já extraídas. Nenhum arquivo
executável é baixado ou executado.
"""
import argparse
import json
import random
from pathlib import Path

import pandas as pd

from src.config import ARQ_EMBER, DADOS_BRUTOS


def achatar(registro: dict) -> dict:
    geral = registro.get("general", {})
    secoes = registro.get("section", {}).get("sections", []) or []
    strings = registro.get("strings", {})
    entropias = [s.get("entropy", 0.0) for s in secoes]
    exec_grav = any(
        "MEM_EXECUTE" in s.get("props", []) and "MEM_WRITE" in s.get("props", [])
        for s in secoes
    )
    return {
        "sha256": registro.get("sha256"),
        "mes_aparicao": registro.get("appeared"),
        "tamanho_bytes": geral.get("size"),
        "num_secoes": len(secoes),
        "entropia_media_secao": sum(entropias) / len(entropias) if entropias else None,
        "entropia_max_secao": max(entropias) if entropias else None,
        "num_importacoes": geral.get("imports"),
        "num_exportacoes": geral.get("exports"),
        "num_strings": strings.get("numstrings"),
        "entropia_strings": strings.get("entropy"),
        "num_urls": strings.get("urls"),
        "num_paths": strings.get("paths"),
        "num_registro": strings.get("registry"),
        "possui_assinatura": geral.get("has_signature"),
        "possui_debug": geral.get("has_debug"),
        "possui_recursos": geral.get("has_resources"),
        "secao_exec_gravavel": int(exec_grav),
        "label": registro.get("label"),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("pasta", type=Path, help="pasta com os .jsonl do EMBER")
    parser.add_argument("--n", type=int, default=50000, help="tamanho da amostra")
    parser.add_argument("--semente", type=int, default=42)
    args = parser.parse_args()

    arquivos = sorted(args.pasta.glob("*features*.jsonl"))
    if not arquivos:
        raise SystemExit(f"Nenhum arquivo *features*.jsonl em {args.pasta}")

    # Amostragem por reservatório: não carrega o EMBER inteiro na memória.
    rnd = random.Random(args.semente)
    amostra, vistos = [], 0
    for arq in arquivos:
        with arq.open(encoding="utf-8") as f:
            for linha in f:
                vistos += 1
                if len(amostra) < args.n:
                    amostra.append(linha)
                else:
                    j = rnd.randrange(vistos)
                    if j < args.n:
                        amostra[j] = linha

    df = pd.DataFrame(achatar(json.loads(l)) for l in amostra)
    DADOS_BRUTOS.mkdir(parents=True, exist_ok=True)
    df.to_csv(ARQ_EMBER, index=False)
    print(f"{len(df)} amostras (de {vistos}) salvas em {ARQ_EMBER}")


if __name__ == "__main__":
    main()
