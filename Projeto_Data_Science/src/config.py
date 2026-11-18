"""Caminhos e definições de colunas usados em todo o projeto."""
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DADOS_BRUTOS = RAIZ / "dados" / "brutos"
DADOS_TRATADOS = RAIZ / "dados" / "tratados"

# Se existir uma amostra real extraída do EMBER, ela tem prioridade.
ARQ_EMBER = DADOS_BRUTOS / "ember_amostra.csv"
ARQ_SINTETICO = DADOS_BRUTOS / "arquivos_pe_sintetico.csv"
ARQ_TRATADO = DADOS_TRATADOS / "arquivos_pe_tratado.csv"
ARQ_RELATORIO = DADOS_TRATADOS / "relatorio_transformacoes.json"

ALVO = "label"  # 0 = seguro (benigno), 1 = malicioso

COLUNAS_BOOLEANAS = [
    "possui_assinatura",
    "possui_debug",
    "possui_recursos",
    "secao_exec_gravavel",
]

COLUNAS_NUMERICAS = [
    "tamanho_bytes",
    "num_secoes",
    "entropia_media_secao",
    "entropia_max_secao",
    "num_importacoes",
    "num_exportacoes",
    "num_strings",
    "entropia_strings",
    "num_urls",
    "num_paths",
    "num_registro",
]

# Variáveis usadas pelos modelos (após o tratamento).
FEATURES = [
    "log10_tamanho",
    "num_secoes",
    "entropia_media_secao",
    "entropia_max_secao",
    "num_importacoes",
    "num_exportacoes",
    "num_strings",
    "entropia_strings",
    "num_urls",
    "num_paths",
    "num_registro",
] + COLUNAS_BOOLEANAS


def caminho_bruto() -> Path:
    """Retorna a base bruta a usar: EMBER real se disponível, senão a sintética."""
    return ARQ_EMBER if ARQ_EMBER.exists() else ARQ_SINTETICO


def usando_dados_sinteticos() -> bool:
    return not ARQ_EMBER.exists()
