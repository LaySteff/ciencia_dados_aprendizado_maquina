# Datasets do Projeto

**Aula:** 30/09 · Unidade III – Gestão de Projetos (apresentação dos projetos)
**Atividade:** tratamento dos dados (em grupo).
**Entregável:** datasets acessíveis.

---

## 1. Base principal: EMBER 2018 (dados reais)

| Item | Descrição |
|---|---|
| O que é | Conjunto público de características estáticas de ~1 milhão de executáveis Windows (PE), rotulados como benignos, maliciosos ou sem rótulo |
| Referência | ANDERSON, H. S.; ROTH, P. *EMBER: An Open Dataset for Training Static PE Malware Machine Learning Models*. arXiv:1804.04637, 2018 |
| Onde obter | https://github.com/elastic/ember (links para download na página do repositório) |
| Formato | JSON Lines (`train_features_*.jsonl`, `test_features.jsonl`), um arquivo por linha |
| Tamanho | ~1,6 GB compactado (versão 2018) |
| Licença | ver o repositório oficial antes de usar |
| Segurança | contém **só características extraídas**: nenhum executável é baixado ou executado |

### Como gerar a amostra usada nos notebooks

```bash
pip install -r requirements.txt
# depois de baixar e descompactar o EMBER 2018:
python -m src.extrair_amostra_ember CAMINHO/ember2018 --n 50000
python -m src.preparacao
```

Isso cria `dados/brutos/ember_amostra.csv` (ignorado pelo Git, por causa do tamanho). A partir daí,
**todos os notebooks passam a usar os dados reais automaticamente** (`src/config.py`).

## 2. Base de demonstração (sintética)

| Item | Descrição |
|---|---|
| Arquivo | [`dados/brutos/arquivos_pe_sintetico.csv`](../dados/brutos/arquivos_pe_sintetico.csv) (6.150 linhas) |
| Como é gerada | `python -m src.gerar_dados_sinteticos` (semente fixa = 42, reproduzível) |
| Para que serve | permitir que todos os notebooks rodem sem baixar o EMBER, e servir de exercício de limpeza (tem problemas inseridos de propósito) |
| Limitação | **não são dados reais**. Os resultados são ilustrativos e não podem ser apresentados como descobertas sobre malware |

## 3. Base tratada

| Arquivo | Conteúdo |
|---|---|
| [`dados/tratados/arquivos_pe_tratado.csv`](../dados/tratados/arquivos_pe_tratado.csv) | base limpa usada pelos modelos |
| [`dados/tratados/relatorio_transformacoes.json`](../dados/tratados/relatorio_transformacoes.json) | registro automático de cada transformação |

## 4. Dicionário de dados

| Coluna | Tipo | Descrição | Origem no EMBER |
|---|---|---|---|
| `sha256` | texto | identificador (hash) do arquivo | `sha256` |
| `mes_aparicao` | AAAA-MM | mês em que o arquivo foi visto pela primeira vez | `appeared` |
| `tamanho_bytes` | inteiro | tamanho do arquivo | `general.size` |
| `log10_tamanho` | real | log10 do tamanho (criada no tratamento) | — |
| `num_secoes` | inteiro | nº de seções do executável | `len(section.sections)` |
| `entropia_media_secao` | real [0, 8] | entropia média das seções (bits/byte) | média de `section.sections[].entropy` |
| `entropia_max_secao` | real [0, 8] | maior entropia entre as seções | máx. de `section.sections[].entropy` |
| `secao_exec_gravavel` | 0/1 | alguma seção é executável e gravável | `props` contém `MEM_EXECUTE` e `MEM_WRITE` |
| `num_importacoes` | inteiro | nº de funções importadas | `general.imports` |
| `num_exportacoes` | inteiro | nº de funções exportadas | `general.exports` |
| `num_strings` | inteiro | nº de strings imprimíveis | `strings.numstrings` |
| `entropia_strings` | real | entropia dos caracteres das strings | `strings.entropy` |
| `num_urls` / `num_paths` / `num_registro` | inteiro | strings que parecem URL, caminho de arquivo ou chave de registro | `strings.urls` / `paths` / `registry` |
| `possui_assinatura` / `possui_debug` / `possui_recursos` | 0/1 | tem assinatura digital / informação de debug / recursos | `general.has_signature` / `has_debug` / `has_resources` |
| `label` | 0/1 (−1 na bruta) | 0 = seguro, 1 = malicioso | `label` |

## 5. Fonte complementar (opcional)

**MalwareBazaar (abuse.ch)**, https://bazaar.abuse.ch/: metadados de amostras maliciosas recentes.
Pode ser usado para estudar a deriva temporal (H3). Usar **só os metadados**. Os arquivos maliciosos
não devem ser baixados fora de um ambiente isolado.
