# Documentação das Transformações de Dados

**Aulas:** 18/11 e 09/12 (Avaliação Final) · Unidade V – Tratamento de Dados
**Atividade:** tratar dados ausentes, inconsistentes e duplicados e preparar a base para análise.
**Entregável:** dataset tratado + notebook/documentação das transformações.

| Item | Arquivo |
|---|---|
| Base bruta | [`dados/brutos/arquivos_pe_sintetico.csv`](../dados/brutos/arquivos_pe_sintetico.csv) (ou `ember_amostra.csv`, se gerada) |
| Código das regras | [`src/preparacao.py`](../src/preparacao.py) |
| Notebook (antes → transformação → verificação) | [`tratamento_de_dados.ipynb`](tratamento_de_dados.ipynb) |
| **Dataset tratado** | [`dados/tratados/arquivos_pe_tratado.csv`](../dados/tratados/arquivos_pe_tratado.csv) |
| Registro automático | [`dados/tratados/relatorio_transformacoes.json`](../dados/tratados/relatorio_transformacoes.json) |

Para reproduzir: `python -m src.preparacao`

> Os números abaixo são da base sintética de demonstração (semente 42).

---

## 1. Resumo

| | Linhas | Seguros | Maliciosos |
|---|---|---|---|
| Base bruta | 6.150 | — | — |
| Base tratada | **5.700** | 3.056 (53,6%) | 2.644 (46,4%) |

## 2. Transformações aplicadas (na ordem)

| # | Problema encontrado | Ocorrências | Transformação | Justificativa |
|---:|---|---|---|---|
| 1 | `sha256` com espaços e letras maiúsculas; datas em `MM/AAAA` | 304 hashes, 489 datas | `strip()` + minúsculas; datas convertidas para `AAAA-MM` | o hash é a chave do arquivo: sem padronizar, duplicatas passariam despercebidas |
| 2 | Linhas duplicadas | 150 exatas | `drop_duplicates()` e depois `drop_duplicates(subset="sha256")` | o mesmo arquivo contado duas vezes enviesa o treino e pode aparecer no treino e no teste ao mesmo tempo (vazamento) |
| 3 | Amostras sem rótulo (`label = −1`) | 300 (após remover duplicatas) | removidas | não servem para aprendizado supervisionado |
| 4 | Booleanos inconsistentes (`sim`, `Sim`, `S`, `true`, `não`, `nao`, `N`, `false`) | 1.133 valores | mapeados para 1/0 | uma variável precisa ter um único formato para ser usada pelo modelo |
| 5 | Valores impossíveis: entropia > 8, tamanho ≤ 0 | 32 + 18 na base bruta (47 nas linhas restantes) | convertidos em ausentes | a entropia por byte vai de 0 a 8, e um arquivo não tem tamanho negativo: são erros de registro |
| 6 | Valores ausentes (originais + inválidos da etapa 5) | 6 colunas, até ~3% cada (650 valores no total) | mediana (numéricas), moda (booleanas e data) | mediana é robusta a outliers; a perda de linhas seria maior que o viés da imputação; não imputamos por classe para não vazar o rótulo |
| 7 | `entropia_max_secao` menor que a média (efeito da imputação) | 50 linhas | máximo ajustado para o valor da média | consistência lógica entre colunas |
| 8 | `tamanho_bytes` muito assimétrico (KB a dezenas de MB) | — | nova coluna `log10_tamanho` | reduz a influência dos valores extremos e melhora modelos lineares |
| 9 | Outliers pelo critério IQR (base tratada) | ex.: 1.326 em `num_exportacoes`, 635 em `tamanho_bytes` | **mantidos** e só registrados | são valores legítimos: muitos arquivos não exportam nada (mediana 0), e valores extremos são justamente sinais de malware |

## 3. Verificações após o tratamento

Todas passam no notebook (`assert`):

- [x] nenhuma célula vazia nas variáveis do modelo
- [x] nenhum `sha256` repetido
- [x] `label` só com 0 e 1
- [x] booleanos só com 0 e 1
- [x] entropias entre 0 e 8
- [x] tamanho > 0
- [x] `mes_aparicao` no formato `AAAA-MM`
- [x] `entropia_max_secao >= entropia_media_secao`

## 4. Decisões e limitações

- **Imputação antes da divisão treino/teste:** foi simples de documentar, mas causa um pequeno vazamento
  de informação. Melhoria: mover a imputação para um `sklearn.pipeline.Pipeline` ajustado só no treino.
- **Remover amostras sem rótulo** descarta informação que poderia ser usada no aprendizado não supervisionado.
- **Outliers mantidos:** se um modelo sensível a escala for usado, é preciso padronizar (já é feito com
  `StandardScaler` na regressão logística e no K-Means).
- Com o EMBER real, as etapas 1 e 4 terão menos ocorrências (os campos já vêm padronizados), mas as
  etapas 2, 3, 5 e 6 continuam necessárias.
