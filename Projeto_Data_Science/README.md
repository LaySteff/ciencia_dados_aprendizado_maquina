# Ciência de Dados e Aprendizado de Máquina — 2026/2

**UDF · Sistemas de Informação** · Aluna: Layse Steffany Pereira de Souza

Repositório com as atividades da disciplina, organizado pelas unidades do plano de aulas, e o projeto
**Classificação Automática de Arquivos Seguros e Potencialmente Maliciosos com Aprendizagem de Máquina**.

## Entregas por aula

| Aula | Unidade | Tema | Entregável | Arquivo |
|---|---|---|---|---|
| 05/08 | I – Big Data | Introdução à Ciência de Dados e Big Data | Mapa conceitual | [`01_mapa_conceitual_ciencia_dados_big_data.md`](unidade1_big_data/01_mapa_conceitual_ciencia_dados_big_data.md) · [`detetives_de_dados.md`](unidade1_big_data/detetives_de_dados.md) (atividade em equipe) |
| 12/08 | I – Big Data | Fundamentos de Big Data: 5 Vs | Análise do caso dos 5 Vs | [`atividade.md`](unidade1_big_data/atividade.md) |
| 19/08 | II – Análise e CD | Ciclo de dados | Pipeline de Ciência de Dados | [`03_pipeline_ciencia_de_dados.md`](unidade2_analise_e_ciencia_de_dados/03_pipeline_ciencia_de_dados.md) |
| 26/08 | II – Análise e CD | Análise exploratória (EDA) | Notebook de EDA | [`04_analise_exploratoria.ipynb`](unidade2_analise_e_ciencia_de_dados/04_analise_exploratoria.ipynb) |
| 02/09 | II – Análise e CD | Visualização e interpretação | Visualizações comentadas | [`05_visualizacoes_comentadas.ipynb`](unidade2_analise_e_ciencia_de_dados/05_visualizacoes_comentadas.ipynb) · [`python_ciencia_dados.ipynb`](unidade2_analise_e_ciencia_de_dados/python_ciencia_dados.ipynb) |
| 09/09 | III – Gestão de Projetos | Problema e objetivos | Documento de definição do projeto | [`01_definicao_do_projeto.md`](unidade3_gestao_de_projetos/01_definicao_do_projeto.md) |
| 16/09 | III – Gestão de Projetos | Planejamento | Plano do projeto | [`02_plano_do_projeto.md`](unidade3_gestao_de_projetos/02_plano_do_projeto.md) |
| 23/09 | ENADE | Simulado | Atividades no Blackboard | — (fora do repositório) |
| 30/09 | III – Gestão de Projetos | Apresentação / tratamento dos dados | Datasets acessíveis | [`03_datasets.md`](unidade3_gestao_de_projetos/03_datasets.md) · [`dados/`](dados/) · [`Capitulo2_Python.ipynb`](unidade2_analise_e_ciencia_de_dados/Capitulo2_Python.ipynb) (livro do Bonidia) |
| 07/10 | IV – Aprendizado de Máquina | Introdução ao ML | Quadro comparativo + classificação de problemas | [`01_quadro_comparativo_supervisionado_nao_supervisionado.md`](unidade4_aprendizado_maquina/01_quadro_comparativo_supervisionado_nao_supervisionado.md) |
| 14/10 | IV – Aprendizado de Máquina | Supervisionado: classificação e regressão | Notebook com modelo e resultados | [`02_modelo_supervisionado.ipynb`](unidade4_aprendizado_maquina/02_modelo_supervisionado.ipynb) |
| 21/10 | — | Sem aula presencial | — | — |
| 28/10 | IV – Aprendizado de Máquina | Não supervisionado: agrupamento | Análise dos agrupamentos | [`03_agrupamento.ipynb`](unidade4_aprendizado_maquina/03_agrupamento.ipynb) |
| 11/11 | IV – Aprendizado de Máquina | Avaliação de modelos | Tabela comparativa + conclusão | [`04_avaliacao_modelos.ipynb`](unidade4_aprendizado_maquina/04_avaliacao_modelos.ipynb) · [`05_tabela_comparativa_modelos.md`](unidade4_aprendizado_maquina/05_tabela_comparativa_modelos.md) |
| 18/11 | V – Tratamento de Dados | Preparação, limpeza e transformação | Dataset tratado + documentação | [`tratamento_de_dados.ipynb`](unidade5_tratamento_de_dados/tratamento_de_dados.ipynb) · [`documentacao_transformacoes.md`](unidade5_tratamento_de_dados/documentacao_transformacoes.md) · [`arquivos_pe_tratado.csv`](dados/tratados/arquivos_pe_tratado.csv) |
| 25/11 (A1) | V – Tratamento de Dados | Integração e apresentação | Projeto final | [`relatorio_final.md`](projeto_final/relatorio_final.md) · [`apresentacao.md`](projeto_final/apresentacao.md) |
| 09/12 (AF) | V – Tratamento de Dados | Avaliação final | Dataset tratado + documentação | mesma entrega de 18/11 ([`unidade5_tratamento_de_dados/`](unidade5_tratamento_de_dados/)) |

## Estrutura

```
├── unidade1_big_data/                  mapa conceitual, 5 Vs, atividade em equipe
├── unidade2_analise_e_ciencia_de_dados/ pipeline, EDA, visualizações, exercícios de Pandas
├── unidade3_gestao_de_projetos/        definição, plano e datasets do projeto
├── unidade4_aprendizado_maquina/       quadro comparativo, modelos, agrupamento, avaliação
├── unidade5_tratamento_de_dados/       notebook e documentação do tratamento
├── projeto_final/                      relatório e roteiro da apresentação
├── src/                                código compartilhado (dados, limpeza)
├── dados/brutos | dados/tratados       bases de dados
└── figuras/                            gráficos gerados pelos notebooks
```

## Sobre os dados

Os notebooks usam por padrão uma **base sintética de demonstração** (`dados/brutos/arquivos_pe_sintetico.csv`),
gerada por `src/gerar_dados_sinteticos.py` no formato das características do **EMBER 2018**. Ela permite
rodar tudo sem baixar ~1,6 GB, mas **os resultados são ilustrativos**. Para usar dados reais, siga
[`03_datasets.md`](unidade3_gestao_de_projetos/03_datasets.md). Depois de criar `dados/brutos/ember_amostra.csv`,
todos os notebooks passam a usá-la automaticamente.

## Como executar

```bash
pip install -r requirements.txt
python -m src.preparacao          # gera dados/tratados/
jupyter notebook                  # abrir os notebooks na ordem da tabela acima
```

No Google Colab: clone o repositório (`!git clone ...`), entre na pasta do notebook com `%cd` e rode as células.
