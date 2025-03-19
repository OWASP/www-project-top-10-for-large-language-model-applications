## LLM04: Envenenamento de Dados e Modelos

### Descrição

O envenenamento de dados ocorre quando dados de pré-treinamento, ajuste fino ou embeddings são manipulados para introduzir vulnerabilidades, backdoors ou vieses. Essa manipulação pode comprometer a segurança, o desempenho ou o comportamento ético do modelo, resultando em saídas prejudiciais ou capacidades comprometidas. Os riscos comuns incluem degradação do desempenho do modelo, conteúdos tendenciosos ou tóxicos e exploração de sistemas subsequentes.

O envenenamento de dados pode ocorrer em diferentes estágios do ciclo de vida do LLM, incluindo pré-treinamento (aprendizado a partir de dados gerais), ajuste fino (adaptação do modelo para tarefas específicas) e embeddings (conversão de texto em vetores numéricos). Entender esses estágios ajuda a identificar onde as vulnerabilidades podem se originar. O envenenamento de dados é considerado um ataque de integridade, pois a manipulação dos dados de treinamento impacta a capacidade do modelo de fazer previsões precisas. Os riscos são particularmente altos com fontes de dados externas, que podem conter conteúdo não verificado ou malicioso.

Além disso, modelos distribuídos através de repositórios compartilhados ou plataformas de código aberto podem apresentar riscos adicionais além do envenenamento de dados, como malware embutido por meio de técnicas como *pickling* malicioso, que podem executar código prejudicial ao carregar o modelo. Considere também que o envenenamento pode permitir a implementação de backdoors. Esses backdoors podem deixar o comportamento do modelo inalterado até que um certo gatilho cause sua ativação, dificultando os testes e a detecção, criando efetivamente uma oportunidade para o modelo se tornar um agente adormecido (sleeper agent).

### Exemplos Comuns de Vulnerabilidades

1. Atores maliciosos introduzem dados prejudiciais durante o treinamento, levando a saídas tendenciosas. Técnicas como "Envenenamento de Dados por Divisão de Visão" ou "Envenenamento por Frontrunning (preempção)" exploram dinâmicas de treinamento de modelo para alcançar isso.
   (Ref. link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
   (Ref. link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Atacantes injetam conteúdo prejudicial diretamente no processo de treinamento, comprometendo a qualidade da saída do modelo.
3. Usuários injetam, sem saber, informações sensíveis ou proprietárias durante as interações, que podem ser expostas em saídas subsequentes.
4. Dados de treinamento não verificados aumentam o risco de saídas tendenciosas ou errôneas.
5. Falta de restrições de acesso a recursos pode permitir a ingestão de dados inseguros, resultando em saídas tendenciosas.

### Estratégias de Prevenção e Mitigação

1. Acompanhe as origens e transformações dos dados usando ferramentas como OWASP CycloneDX ou ML-BOM. Verifique a legitimidade dos dados durante todas as etapas de desenvolvimento do modelo.
2. Avalie rigorosamente os fornecedores de dados e valide as saídas do modelo em relação a fontes confiáveis para detectar sinais de envenenamento.
3. Implemente sandboxes rigorosos para limitar a exposição do modelo a fontes de dados não verificadas. Use técnicas de detecção de anomalias para filtrar dados adversários.
4. Adapte modelos para diferentes casos de uso utilizando conjuntos de dados específicos para ajuste fino, ajudando a produzir saídas mais precisas com base em objetivos definidos.
5. Assegure controles de infraestrutura suficientes para evitar que o modelo acesse fontes de dados não intencionais.
6. Use controle de versão de dados (DVC) para rastrear mudanças em conjuntos de dados e detectar manipulações. A versionagem é crucial para manter a integridade do modelo.
7. Armazene informações fornecidas por usuários em um banco de dados de vetores, permitindo ajustes sem a necessidade de re-treinar todo o modelo.
8. Teste a robustez do modelo com campanhas de equipes de Red Team e técnicas adversárias, como aprendizado federado, para minimizar o impacto de perturbações nos dados.
9. Monitore a perda de treinamento e analise o comportamento do modelo para sinais de envenenamento. Use limiares (valores de corte) para detectar saídas anômalas.
10. Integre técnicas de Geração Aumentada por Recuperação (RAG) e grounding (fundamentação) para reduzir riscos de alucinações durante a inferência.

### Exemplos de Cenários de Ataques

#### Cenário #1
  Um atacante enviesa as saídas do modelo ao manipular dados de treinamento ou usando técnicas de injeção de *prompt* para espalhar desinformação.
#### Cenário #2
  Dados tóxicos sem o devido filtro podem levar a saídas prejudiciais ou tendenciosas, propagando informações perigosas.
#### Cenário #3
  Um ator malicioso ou concorrente cria documentos falsificados para o treinamento, resultando em saídas que refletem essas imprecisões.
#### Cenário #4
  Filtros inadequados permitem que um atacante insira dados enganosos por meio de injeção de prompt, comprometendo as saídas.
#### Cenário #5
  Um atacante usa técnicas de envenenamento para inserir um gatilho de *backdoor* no modelo. Isso pode permitir a evasão de autenticação, exfiltração de dados ou execução oculta de comandos.

### Links de Referência

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target): **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/): **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/): **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training): **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models): **Cobalt**

### Frameworks e Taxonomias Relacionados

Consulte esta seção para obter informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018): **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Estratégias para garantir a integridade da IA. **NIST**
