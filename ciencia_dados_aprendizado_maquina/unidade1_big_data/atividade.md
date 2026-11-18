# Análise de Caso — Os 5 Vs do Big Data

**Aula:** 12/08 · Unidade I – Big Data
**Metodologia:** exposição dialogada + aprendizagem baseada em problemas
**Atividade:** analisar um caso real e identificar Volume, Velocidade, Variedade, Veracidade e Valor.
**Entregável:** análise do caso dos 5 Vs.

---

## O que é Big Data?

Big Data é o conjunto de dados cujo **volume, velocidade de geração e variedade** ultrapassam a
capacidade das ferramentas tradicionais de armazenar, processar e analisar. Para que esses dados
sejam úteis, também precisam ser **confiáveis (veracidade)** e gerar **valor** para quem decide.
Esse conjunto de características é conhecido como **5 Vs**.

## Caso analisado: detecção de malware em anexos de e-mail

Provedores de e-mail e empresas de antivírus precisam decidir, em segundos, se um anexo recebido
é seguro. O e-mail é um dos principais meios de entrega de malware (Verizon DBIR), e laboratórios
como o AV-TEST registram centenas de milhares de novas amostras maliciosas por dia. Inspecionar
tudo manualmente é impossível, então a triagem depende de dados e de modelos automáticos. Esse
caso também é a base do [projeto da disciplina](../unidade3_gestao_de_projetos/01_definicao_do_projeto.md).

| V | Pergunta | Análise do caso |
|---|---|---|
| **Volume** | Existe uma grande quantidade de dados? | Sim. São bilhões de e-mails por dia e milhões de arquivos analisados. Só o conjunto público EMBER, usado como referência no projeto, tem cerca de 1 milhão de arquivos com milhares de características cada. |
| **Velocidade** | Os dados chegam ou precisam ser processados rapidamente? | Sim. A decisão precisa sair antes de o usuário abrir o anexo, ou seja, em segundos. Novas variantes surgem todos os dias, então o modelo também precisa ser atualizado com frequência. |
| **Variedade** | Existem diferentes tipos ou formatos? | Sim. Executáveis, PDFs, documentos Office com macros e arquivos compactados. Além disso, há metadados estruturados (tamanho, cabeçalhos), semiestruturados (JSON de análise, logs) e não estruturados (texto do e-mail, strings internas). |
| **Veracidade** | Os dados podem ter erros? | Sim. Os rótulos vêm de vários antivírus que às vezes discordam, há amostras sem rótulo e duplicadas, e os atacantes manipulam os arquivos de propósito para parecerem legítimos. |
| **Valor** | Os dados geram benefício ou apoiam decisões? | Sim. Permitem bloquear ou colocar em quarentena arquivos perigosos antes da infecção, reduzindo perda de dados e prejuízo. Também reduzem o trabalho manual das equipes de segurança. |

### Qual V é mais relevante para o caso?

**Velocidade**, junto com a **Veracidade**.

**Justificativa:** um modelo excelente que responde tarde demais não tem utilidade, porque o
usuário já abriu o anexo. Além disso, os atacantes mudam as amostras o tempo todo, então dados
antigos perdem validade rapidamente (deriva de conceito, testada na hipótese H3 do projeto). A
veracidade vem logo em seguida: rótulos errados ensinam o modelo a errar, e um falso positivo
bloqueia um arquivo legítimo importante.

## Reflexão

Ter muitos dados não basta. No caso do malware, **dados antigos ou mal rotulados**, mesmo em
grande volume, podem dar uma falsa sensação de segurança. O valor vem de dados atualizados,
confiáveis e de uma decisão rápida.

## Referências

- VERIZON. *Data Breach Investigations Report (DBIR)*. Disponível em: https://www.verizon.com/business/resources/reports/dbir/.
- AV-TEST INSTITUTE. *Malware statistics*. Disponível em: https://www.av-test.org/en/statistics/malware/.
- ANDERSON, H. S.; ROTH, P. *EMBER: An Open Dataset for Training Static PE Malware Machine Learning Models*. arXiv:1804.04637, 2018.

> Confira os números atualizados nas fontes antes da entrega.
