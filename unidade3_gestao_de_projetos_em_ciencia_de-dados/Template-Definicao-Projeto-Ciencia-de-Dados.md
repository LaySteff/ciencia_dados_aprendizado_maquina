# Template - Definição do Projeto de Ciência de Dados

**Unidade:** III - Gestão de Projetos  
**Metodologia:** PBL + trabalho em equipes  
**Entregável:** Documento de definição do projeto

> **Finalidade:** delimitar um problema real e orientar o desenvolvimento do projeto de Ciência de Dados. Preencha todos os campos com informações objetivas, verificáveis e coerentes entre si.

## 1. Identificação do projeto

| Campo | Preenchimento |
|---|---|
| Título provisório do projeto | Classificação Automática de Arquivos Seguros e Potencialmente Maliciosos com Aprendizagem de Máquina |
| Curso / disciplina | Sistemas de Informação |
| Turma | Ciência de Dados e Aprendizagem de Máquina |
| Equipe | Equipe Layse Steffany (a completar se houver mais integrantes) |
| Integrantes e funções iniciais | Layse Steffany: coordenação, preparação dos dados, modelagem e redação |
| Professor(a) | Kadidja |
| Data de elaboração | 16/09/2026 |
| Versão do documento | 1.0 |

## 2. Visão geral

### 2.1 Resumo do projeto

Usuários recebem diariamente arquivos por e-mail e nem sempre conseguem saber se um anexo é seguro. Arquivos maliciosos podem danificar dispositivos e expor informações. O projeto propõe analisar características estáticas de arquivos (tamanho, cabeçalhos, seções, strings e entropia) e treinar modelos de aprendizagem de máquina que os classifiquem como seguros ou potencialmente maliciosos. O resultado esperado é um modelo avaliado e documentado, com métricas claras, que apoie a triagem automática de anexos suspeitos.

### 2.2 Declaração do projeto em uma frase

Desenvolver um modelo de aprendizagem de máquina capaz de classificar arquivos como seguros ou potencialmente maliciosos, utilizando características dos próprios arquivos.

**Versão da equipe:** Construir e comparar modelos de classificação que identifiquem arquivos potencialmente maliciosos a partir de suas características estáticas, reduzindo o risco de abertura de anexos perigosos.

## 3. Contexto e definição do problema

### 3.1 Contexto

- **Onde ocorre:** na caixa de entrada de e-mail e em downloads de pessoas e organizações, em computadores e celulares.
- **Quem é afetado:** usuários comuns, estudantes, profissionais e equipes de TI de pequenas e médias organizações, que recebem anexos de remetentes conhecidos e desconhecidos.
- **Sinais que indicam o problema:** relatórios de segurança que apontam o e-mail como um dos principais meios de entrega de malware, e o grande número de novas amostras maliciosas que surgem diariamente, o que torna a análise manual inviável.
- **Por que agora:** o volume de arquivos cresce, os ataques mudam rápido e a detecção apenas por assinaturas conhecidas deixa passar variantes novas. Técnicas de aprendizagem de máquina permitem generalizar a partir de características dos arquivos.

### 3.2 Problema central

Usuários de e-mail e de dispositivos conectados enfrentam dificuldade de distinguir anexos seguros de maliciosos no contexto do recebimento diário de arquivos, produzindo risco de infecção por malware, perda ou vazamento de dados e danos aos dispositivos.

### 3.3 Evidências iniciais

| Evidência | Fonte | O que ela indica? | Confiabilidade / limitação |
|---|---|---|---|
| 1. Relatórios anuais de incidentes de segurança apontam o e-mail como vetor frequente de entrega de malware | Verizon, Data Breach Investigations Report (DBIR) | O anexo malicioso é um problema recorrente e atual | Alta, mas os dados vêm de organizações que reportam incidentes e podem não representar usuários individuais |
| 2. Centenas de milhares de novas amostras de malware são registradas por dia | AV-TEST Institute (estatísticas de malware) | O volume torna a inspeção manual impraticável e favorece a automação | Alta; os números mudam todo ano e precisam ser conferidos na data de entrega |
| 3. Modelos treinados com características estáticas de executáveis conseguem separar arquivos benignos de maliciosos | Anderson e Roth (2018), artigo do conjunto EMBER | Há base científica de que a abordagem proposta é viável | Média a alta; o estudo trata de executáveis Windows (PE) e o desempenho cai com amostras mais novas (deriva de conceito) |

*Antes de entregar, confira os números atualizados nas fontes citadas.*

## 4. Público-alvo e partes interessadas

### 4.1 Público-alvo principal

| Aspecto | Descrição |
|---|---|
| Quem são os usuários ou beneficiários? | Usuários de e-mail e computadores, e equipes de TI ou segurança de pequenas e médias organizações |
| Quais necessidades possuem? | Saber rapidamente se um anexo é seguro antes de abri-lo, sem precisar de conhecimento técnico avançado |
| Como são afetados pelo problema? | Correm o risco de abrir arquivos maliciosos, com perda de dados, indisponibilidade do equipamento e vazamento de informações |
| Que decisão ou ação poderão tomar com os resultados? | Abrir, bloquear, colocar em quarentena ou encaminhar para análise aprofundada um arquivo, conforme a classificação e o grau de confiança do modelo |

### 4.2 Partes interessadas

| Parte interessada | Interesse no projeto | Influência | Forma de envolvimento |
|---|---|---|---|
| Professora Kadidja | Avaliar a qualidade metodológica e técnica do projeto | Alta | Orientação, validação do escopo e avaliação final |
| Equipe do projeto | Entregar um modelo confiável e bem documentado | Alta | Execução de todas as etapas |
| Usuários finais (pessoas e organizações) | Proteção contra anexos maliciosos | Média | Beneficiários; podem validar a utilidade dos resultados |
| Equipes de TI e segurança | Apoio à triagem de arquivos suspeitos | Média | Consulta sobre critérios de decisão e taxa aceitável de alertas falsos |
| Mantenedores dos conjuntos de dados públicos | Uso correto e citação das bases | Baixa | Atendimento às licenças e citação das fontes |

## 5. Objetivos do projeto

### 5.1 Objetivo geral

Desenvolver e avaliar modelos de aprendizagem de máquina que classifiquem arquivos como seguros ou potencialmente maliciosos a partir de suas características estáticas, a fim de apoiar a triagem automática de anexos recebidos por e-mail.

### 5.2 Objetivos específicos

| Nº | Objetivo específico | Evidência de conclusão |
|---:|---|---|
| 1 | Obter e documentar um conjunto de dados público de arquivos rotulados como benignos e maliciosos | Dicionário de dados e relatório com origem, volume e licença da base |
| 2 | Limpar, tratar e transformar os dados, verificando duplicidades, valores ausentes e equilíbrio entre classes | Base tratada e notebook de preparação reproduzível |
| 3 | Realizar análise exploratória para identificar características que diferenciam arquivos seguros e maliciosos | Gráficos e tabelas com pelo menos 5 variáveis discriminantes analisadas |
| 4 | Treinar e comparar ao menos 3 algoritmos de classificação (por exemplo regressão logística, Random Forest e gradiente boosting) | Tabela comparativa com acurácia, precisão, recall, F1 e AUC-ROC |
| 5 | Validar o melhor modelo e comunicar resultados, limitações e recomendações de uso | Relatório final e apresentação com matriz de confusão e análise de erros |

### 5.3 Verificação dos objetivos

- [x] São específicos e escritos com clareza.
- [x] Podem ser verificados por meio de entregáveis ou métricas.
- [x] São viáveis com os dados, recursos e tempo disponíveis.
- [x] Estão diretamente relacionados ao problema central.
- [x] Consideram os usuários e a decisão que será apoiada.

## 6. Perguntas de negócio

| Nº | Pergunta de negócio | Decisão apoiada | Dados necessários | Análise ou indicador possível |
|---:|---|---|---|---|
| 1 | Quais características dos arquivos mais diferenciam os maliciosos dos seguros? | Quais sinais o usuário ou a equipe de TI devem observar na triagem | Variáveis de cabeçalho, seções, entropia, strings e importações | Importância das variáveis, comparação de distribuições entre classes |
| 2 | Com que precisão um modelo consegue classificar um arquivo como malicioso ou seguro? | Se o modelo é confiável o bastante para apoiar a triagem | Base rotulada com arquivos benignos e maliciosos | Acurácia, precisão, recall, F1 e AUC-ROC em dados de teste |
| 3 | Qual é o custo de cada tipo de erro, bloquear um arquivo seguro ou deixar passar um malicioso? | Que limiar de decisão adotar para bloquear ou liberar | Previsões do modelo e rótulos reais | Matriz de confusão, taxas de falso positivo e falso negativo, curva ROC |
| 4 | Como o desempenho do modelo muda com arquivos de períodos diferentes? | Com que frequência o modelo precisa ser retreinado | Amostras com data de coleta ou de primeira observação | Desempenho por período, comparando treino em dados antigos e teste em dados recentes |
| 5 | Quais perfis de arquivos o modelo erra com mais frequência? | Quais casos exigem revisão humana ou análise complementar | Erros do modelo com suas características | Análise de erros e agrupamento dos falsos positivos e falsos negativos |

## 7. Hipóteses iniciais

| Hipótese | Como poderá ser testada? | Resultado que a refutaria? |
|---|---|---|
| H1. Arquivos maliciosos apresentam entropia média maior que a dos arquivos seguros, por causa de compactação e ofuscação do código | Comparar a entropia entre as duas classes com teste estatístico (por exemplo Mann-Whitney) e gráficos de distribuição | Diferença sem significância estatística ou entropia média igual ou menor nos maliciosos |
| H2. Modelos baseados em árvores (Random Forest e gradiente boosting) superam a regressão logística na classificação | Treinar os três modelos com a mesma divisão e validação cruzada e comparar F1 e AUC-ROC | Regressão logística com desempenho igual ou superior ao dos modelos de árvores |
| H3. O desempenho do modelo cai quando testado em arquivos mais recentes que os usados no treino | Treinar com dados antigos e testar com dados de períodos posteriores, comparando com o teste aleatório | Desempenho estável, sem queda relevante, entre os períodos |

## 8. Dados necessários e viabilidade

| Conjunto ou fonte de dados | Variáveis principais | Formato | Acesso / responsável | Qualidade esperada |
|---|---|---|---|---|
| EMBER (conjunto público de arquivos executáveis PE, com cerca de 1 milhão de amostras) | Rótulo (benigno ou malicioso), informações de cabeçalho, seções, importações, strings, entropia, histograma de bytes | JSON e vetores de características | Download público; Layse Steffany | Alta; já rotulado e documentado, com amostras sem rótulo que podem ser descartadas |
| MalwareBazaar (abuse.ch), amostras maliciosas recentes (opcional) | Tipo de arquivo, família, data de envio, hash | CSV e JSON | Acesso público à lista de metadados; Layse Steffany | Média; rótulos vindos de envios da comunidade |
| Conjunto complementar de metadados de arquivos benignos (opcional) | Tipo, tamanho, hash e características estáticas | CSV | A definir pela equipe | Média; depende da fonte escolhida |

### 8.1 Avaliação inicial dos dados

- **Disponibilidade:** o EMBER e as listas de metadados do MalwareBazaar são públicos. Os arquivos maliciosos em si não serão baixados nem executados, apenas suas características já extraídas.
- **Volume e período coberto:** cerca de 1 milhão de amostras no EMBER, coletadas em um período de alguns meses de 2017 e 2018. A cobertura temporal é limitada e será discutida como limitação (hipótese H3).
- **Dados ausentes, duplicados ou inconsistentes previstos:** amostras sem rótulo, características com valor zero em excesso, possíveis duplicatas e desequilíbrio entre classes.
- **Necessidade de integração entre fontes:** baixa na versão inicial, que usa uma base principal. A integração com outra fonte só ocorrerá se houver tempo e padronização de variáveis.
- **Restrições legais, contratuais ou institucionais:** respeitar as licenças e os termos de uso de cada base e citar as fontes. Os dados dos conjuntos públicos não contêm informações pessoais.

### 8.2 Privacidade, ética e segurança

- [x] A equipe verificou se há dados pessoais ou sensíveis.
- [x] A coleta e o uso dos dados possuem finalidade legítima e explícita.
- [x] O acesso será limitado às pessoas autorizadas.
- [x] Dados pessoais serão minimizados, anonimizados ou pseudonimizados quando necessário.
- [x] Possíveis vieses e impactos sobre grupos serão analisados.
- [x] A divulgação dos resultados evitará reidentificação ou exposição indevida.

**Cuidados específicos deste projeto:**

- Trabalhar apenas com características extraídas, sem executar arquivos maliciosos. Qualquer teste com arquivos reais deve ocorrer em ambiente isolado (máquina virtual sem acesso à rede).
- Não usar anexos reais de e-mails de pessoas, para evitar exposição de dados pessoais e de correspondência.
- Registrar que os falsos positivos podem bloquear arquivos legítimos e que o modelo apoia a decisão humana, sem substituí-la.
- Analisar o viés de tipos de arquivo: a base cobre sobretudo executáveis Windows, então os resultados não se aplicam a outros formatos.

## 9. Escopo do projeto

| Dentro do escopo | Fora do escopo |
|---|---|
| Classificação binária (seguro ou malicioso) com base em características estáticas | Análise dinâmica, com execução do arquivo em sandbox |
| Uso de base pública rotulada, com foco em executáveis PE | Classificação por família de malware |
| Comparação de pelo menos 3 algoritmos de aprendizagem de máquina | Integração com clientes de e-mail ou antivírus em produção |
| Análise de erros e avaliação por período | Defesa contra ataques que tentam enganar o modelo de propósito |
| Relatório e apresentação dos resultados | Análise de links, do corpo da mensagem ou do remetente do e-mail |

**Restrições conhecidas:**

- **Tempo:** prazo da disciplina, que limita o número de modelos e ajustes.
- **Dados:** a base principal cobre um período antigo e um tipo de arquivo, o que limita a generalização.
- **Ferramentas e infraestrutura:** uso de ferramentas gratuitas (Python, bibliotecas de aprendizagem de máquina e notebooks) e de computador pessoal ou nuvem gratuita.
- **Conhecimento técnico:** conhecimento inicial em segurança de arquivos, a ser aprofundado durante o projeto.
- **Normas:** uso ético dos dados e cumprimento das licenças das bases.

## 10. Resultados e entregáveis previstos

| Entregável | Descrição | Formato | Responsável | Critério de aceite |
|---|---|---|---|---|
| Base tratada | Conjunto de dados limpo, com variáveis documentadas e divisão em treino, validação e teste | CSV ou Parquet, e dicionário de dados | Layse Steffany | Sem duplicatas nem valores inválidos, e código de preparação que reproduz o resultado |
| Análise exploratória | Estudo das distribuições e das diferenças entre arquivos seguros e maliciosos | Notebook (Jupyter) | Layse Steffany | Ao menos 5 variáveis analisadas, com gráficos e interpretação |
| Visualizações / painel | Gráficos de importância das variáveis, curva ROC e matriz de confusão | Imagens no relatório ou painel simples | Layse Steffany | Gráficos legíveis, com títulos e eixos identificados |
| Relatório ou apresentação | Documento com problema, método, resultados, limitações e recomendações | PDF e slides | Layse Steffany | Cobre todos os objetivos específicos e responde às perguntas de negócio |
| Outro | Repositório com código e instruções de execução | Repositório no GitHub | Layse Steffany | Outra pessoa consegue rodar o projeto seguindo o README |

## 11. Critérios de sucesso

| Critério | Indicador ou evidência | Meta | Forma de verificação |
|---|---|---|---|
| Relevância para o problema | Modelo classifica arquivos como seguros ou maliciosos e responde às 5 perguntas de negócio | 5 de 5 perguntas respondidas com evidência | Conferência do relatório pelo professor |
| Qualidade dos dados | Percentual de duplicatas e de valores inválidos após o tratamento | 0% de duplicatas e nenhum valor inválido na base final | Verificação no notebook de preparação |
| Qualidade da análise | F1 e AUC-ROC no conjunto de teste, e comparação de ao menos 3 modelos | F1 igual ou superior a 0,90 e AUC-ROC igual ou superior a 0,95 no melhor modelo | Métricas calculadas em dados de teste separados e validação cruzada |
| Utilidade para o público-alvo | Taxa de falsos positivos e de falsos negativos em um limiar definido | Falsos positivos abaixo de 5% e falsos negativos abaixo de 10% | Matriz de confusão e curva ROC |
| Comunicação dos resultados | Clareza do relatório e da apresentação, e reprodutibilidade do código | Relatório completo e código executável por outra pessoa | Avaliação do professor e teste de execução com o README |

*As metas numéricas são iniciais e podem ser ajustadas após a análise exploratória.*

## 12. Plano inicial de trabalho

| Etapa | Atividades principais | Responsável(is) | Prazo | Dependências |
|---|---|---|---|---|
| 1. Definição | Delimitar o problema, os objetivos, as perguntas e o escopo; validar com a professora | Layse Steffany | Semana 1 | Nenhuma |
| 2. Obtenção dos dados | Baixar o EMBER, ler a documentação e conferir licença, volume e variáveis | Layse Steffany | Semana 2 | Etapa 1 aprovada |
| 3. Preparação dos dados | Limpar, remover duplicatas e amostras sem rótulo, tratar o desequilíbrio e dividir treino, validação e teste | Layse Steffany | Semanas 3 e 4 | Etapa 2 |
| 4. Análise / modelagem | Análise exploratória; treinar e ajustar regressão logística, Random Forest e gradiente boosting | Layse Steffany | Semanas 5 a 7 | Etapa 3 |
| 5. Validação | Calcular métricas, avaliar por período, analisar erros e testar as hipóteses H1 a H3 | Layse Steffany | Semana 8 | Etapa 4 |
| 6. Comunicação | Redigir o relatório, montar a apresentação e organizar o repositório | Layse Steffany | Semanas 9 e 10 | Etapa 5 |

## 13. Riscos do projeto

| Risco | Probabilidade | Impacto | Estratégia de resposta | Responsável |
|---|---|---|---|---|
| Base de dados antiga ou de um só tipo de arquivo, com baixa generalização | Alta | Médio | Declarar a limitação, testar por período (H3) e, se houver tempo, incluir uma segunda fonte | Layse Steffany |
| Desequilíbrio entre classes ou rótulos incorretos, que distorcem as métricas | Média | Alto | Usar métricas além da acurácia (F1, recall, AUC-ROC), reponderar as classes e revisar uma amostra dos rótulos | Layse Steffany |
| Atraso no cronograma ou equipe reduzida, com muitas tarefas para poucas pessoas | Média | Alto | Priorizar os 3 algoritmos principais, deixar itens opcionais para o final e revisar o plano a cada semana | Layse Steffany |
| Manuseio inseguro de arquivos maliciosos | Baixa | Alto | Usar apenas características extraídas; qualquer teste com arquivos reais só em máquina virtual isolada | Layse Steffany |

## 14. Organização da equipe

| Integrante | Papel principal | Responsabilidades | Apoio necessário |
|---|---|---|---|
| Layse Steffany | Coordenação e ciência de dados | Planejamento, obtenção e preparação dos dados, análise exploratória, modelagem, validação e redação | Orientação da professora Kadidja sobre métricas e metodologia |
| (a definir) | Revisão e documentação | Revisão do código e do relatório, e organização do repositório | Definição de quem assume o papel, caso a equipe tenha mais integrantes |
| (a definir) | Visualização e comunicação | Gráficos, slides e apresentação final | Definição de quem assume o papel, caso a equipe tenha mais integrantes |

## 15. Validação da definição do projeto

- [x] O problema é real, relevante e delimitado.
- [x] O público-alvo e as partes interessadas estão identificados.
- [x] O objetivo geral e os objetivos específicos são coerentes.
- [x] As perguntas de negócio orientam decisões concretas.
- [x] Há dados potencialmente disponíveis para responder às perguntas.
- [x] O escopo é compatível com o prazo e os recursos.
- [x] Os critérios de sucesso são mensuráveis.
- [x] Riscos, privacidade, ética e segurança foram considerados.
- [x] Funções e responsabilidades foram distribuídas.

## 16. Aprovação e registro de ajustes

| Responsável | Validação / observação | Data |
|---|---|---|
| Representante da equipe: Layse Steffany | Definição elaborada e revisada pela equipe | 16/09/2026 |
| Professor(a) / orientador(a): Kadidja | Aguardando validação | |

### Ajustes solicitados após a apresentação inicial

Nenhum ajuste registrado até o momento.
