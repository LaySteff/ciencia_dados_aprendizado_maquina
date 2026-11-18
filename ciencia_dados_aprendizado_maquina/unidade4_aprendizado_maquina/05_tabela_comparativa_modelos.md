# Tabela Comparativa dos Modelos + Conclusão

**Aula:** 11/11 · Unidade IV – Aprendizado de Máquina
**Metodologia:** estudo de caso + TBL + prática
**Atividade:** comparar modelos, analisar métricas e discutir limitações e possíveis erros.
**Entregável:** tabela comparativa dos modelos + conclusão.

Notebook com todos os cálculos: [`04_avaliacao_modelos.ipynb`](04_avaliacao_modelos.ipynb) ·
dados da tabela: [`tabela_comparativa_modelos.csv`](tabela_comparativa_modelos.csv)

> ⚠️ **Resultados obtidos com a base sintética de demonstração.** Eles mostram o método, mas **não**
> são descobertas sobre malware real. Refaça com a amostra do EMBER (`03_datasets.md`) antes de apresentar.

---

## 1. Configuração

- 5.700 arquivos após o tratamento (53,6% seguros, 46,4% maliciosos), 15 variáveis.
- Divisão estratificada: 75% treino / 25% teste (1.425 arquivos), semente 42.
- Validação cruzada estratificada de 5 dobras no conjunto de treino.
- Limiar de decisão padrão = 0,5.

## 2. Tabela comparativa

| Modelo | F1 (CV) | AUC (CV) | Acurácia | Precisão | Recall | F1 | AUC-ROC | Taxa FP | Taxa FN |
|---|---|---|---|---|---|---|---|---|---|
| Linha de base (classe majoritária) | — | — | 0,536 | — | 0,000 | 0,000 | 0,500 | 0,000 | 1,000 |
| Árvore de decisão (prof. 4) ¹ | — | — | 0,733 | 0,772 | 0,601 | 0,676 | — | — | — |
| **Regressão logística** | **0,788 ± 0,011** | **0,877 ± 0,006** | 0,785 | 0,794 | 0,725 | **0,758** | **0,865** | 0,162 | 0,275 |
| Random Forest | 0,771 ± 0,003 | 0,871 ± 0,005 | 0,781 | **0,802** | 0,700 | 0,748 | 0,856 | **0,149** | 0,300 |
| Gradient Boosting | 0,769 ± 0,010 | 0,865 ± 0,003 | 0,783 | 0,789 | **0,728** | 0,757 | 0,851 | 0,169 | **0,272** |

¹ do notebook [`02_modelo_supervisionado.ipynb`](02_modelo_supervisionado.ipynb).

### Desempenho em arquivos mais recentes (H3)

| Modelo | AUC (divisão aleatória) | AUC (treino jan–ago → teste set–dez) | Queda |
|---|---|---|---|
| Regressão logística | 0,865 | 0,835 | 0,030 |
| Random Forest | 0,856 | 0,831 | 0,025 |
| Gradient Boosting | 0,851 | 0,826 | 0,025 |

## 3. Hipóteses

| Hipótese | Resultado | Evidência |
|---|---|---|
| H1. Maliciosos têm entropia maior | ✅ Confirmada | mediana 6,11 × 5,34; Mann-Whitney p < 0,001 |
| H2. Árvores superam a regressão logística | ❌ Refutada | regressão logística igual ou melhor em F1 e AUC |
| H3. Desempenho cai em arquivos recentes | ✅ Confirmada | queda de AUC de 0,025 a 0,030 |

## 4. Conclusão

1. **Escolha:** **regressão logística**. As diferenças entre os três modelos cabem no desvio da validação
   cruzada, e ela é a mais simples, rápida e interpretável (os coeficientes mostram o efeito de cada variável).
2. **As metas iniciais não foram atingidas** (F1 ≥ 0,90; AUC ≥ 0,95; FP < 5% com FN < 10%). Nenhum limiar
   atinge as duas taxas ao mesmo tempo: para FN ≈ 10% (limiar 0,25), a taxa de FP sobe para ~41%.
3. **Recomendação de uso:** usar o modelo como **ferramenta de priorização**. Probabilidade alta vai para
   a quarentena, faixa intermediária vai para revisão humana, e o modelo não deve bloquear arquivos sozinho.
4. **Erros:** os falsos negativos são malwares com entropia normal, muitas importações e, às vezes,
   assinatura digital, ou seja, parecidos com software legítimo. As características estáticas não bastam
   para esses casos.
5. **Manutenção:** como o desempenho cai com arquivos novos, é preciso **retreinar periodicamente** e monitorar as métricas.

## 5. Limitações e possíveis erros

- **Base sintética:** os padrões foram simulados. Com o EMBER real, a literatura reporta AUC bem mais alta
  para modelos de árvore usando todas as ~2.300 características; aqui usamos só 15.
- **Vazamento leve:** a imputação de ausentes usou a mediana da base inteira, antes da divisão treino/teste.
  O ideal é imputar dentro de um `Pipeline` ajustado só no treino.
- **Ruído de rótulo:** ~3% dos rótulos foram invertidos de propósito, o que limita o desempenho máximo possível.
- **Hiperparâmetros:** os modelos não passaram por busca de hiperparâmetros, então o resultado de Random
  Forest e Gradient Boosting pode melhorar com ajuste.
- **Escopo:** só executáveis Windows e só análise estática. Não vale para PDFs, documentos com macro ou análise dinâmica.
