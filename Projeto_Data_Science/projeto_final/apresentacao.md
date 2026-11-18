# Roteiro da Apresentação — Projeto Final (25/11)

**Aula:** 25/11 (A1) · Unidade V – Integração e apresentação do projeto final

Duração sugerida: **10 minutos + 5 de discussão**. Um slide por tópico.

| # | Slide | Conteúdo | Tempo |
|---:|---|---|---|
| 1 | Título | Nome do projeto, aluna/equipe, disciplina | 0:20 |
| 2 | Problema | Anexos maliciosos; por que a análise manual não escala; público-alvo | 1:00 |
| 3 | Perguntas de negócio | As 5 perguntas e as hipóteses H1 a H3 | 0:40 |
| 4 | Dados | EMBER: o que é e as 15 variáveis usadas; base de demonstração × base real | 1:00 |
| 5 | Tratamento | Antes → depois (6.150 → 5.700 linhas); as 9 transformações em uma tabela | 1:00 |
| 6 | EDA | Figuras `v2_entropia.png` e `v3_binarios.png`: entropia e assinatura | 1:00 |
| 7 | Deriva temporal | Figura `v5_temporal.png`: os malwares mudam com o tempo | 0:40 |
| 8 | Agrupamento | Figura `agrupamento_pca.png` + tabela dos 3 grupos | 1:00 |
| 9 | Modelos | Tabela comparativa + figura `avaliacao_roc_matriz.png` | 1:20 |
| 10 | Respostas e decisão | Tabela de respostas; recomendação de duas faixas de decisão | 1:00 |
| 11 | Limitações e próximos passos | Base sintética → EMBER real, vazamento na imputação, escopo | 0:40 |
| 12 | Conclusão | "Dados ajudam a priorizar, não a substituir a análise humana" | 0:20 |

Figuras em [`../figuras/`](../figuras/).

## Perguntas prováveis na discussão

- **Por que não usar só a acurácia?** Porque o erro mais caro é o falso negativo, e a acurácia esconde isso.
- **Por que a regressão logística ganhou?** Nestes dados, a relação entre as variáveis e o rótulo é quase linear e há ruído de rótulo. Com mais variáveis (EMBER completo), a literatura indica vantagem para Gradient Boosting.
- **O modelo pode ser enganado?** Sim. Ataques adversariais estão fora do escopo e são citados como limitação.
- **Os dados são reais?** Explicar a base de demonstração e o script de extração do EMBER.
