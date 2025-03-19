## LLM10:2025 Consumo Irrestrito

### Descrição

Consumo Irrestrito ocorre quando um Grande Modelo de Linguagem (LLM) processa consultas ou prompts sem restrições adequadas, gerando respostas ilimitadas e potencialmente prejudiciais. A inferência é uma função crítica dos LLMs, envolvendo a aplicação de padrões e conhecimentos aprendidos para produzir respostas ou previsões relevantes.

Ataques podem explorar essa vulnerabilidade para interromper serviços, esgotar recursos financeiros ou clonar o comportamento de um modelo, resultando em roubo de propriedade intelectual. O Consumo Irrestrito ocorre quando uma aplicação de LLM permite que usuários realizem inferências excessivas e descontroladas, levando a riscos como negação de serviço (DoS), perdas econômicas, roubo de modelos e degradação de serviços. As altas demandas computacionais dos LLMs, especialmente em ambientes de nuvem, os tornam vulneráveis à exploração de recursos e ao uso não autorizado.

### Exemplos Comuns de Vulnerabilidades

#### 1. Ataque de Sobrecarga por Entradas Variáveis
  Atacantes enviam uma grande quantidade de entradas com tamanhos variados para explorar falhas no processamento do LLM, causando lentidão ou indisponibilidade. Isso pode esgotar recursos e potencialmente tornar o sistema não responsivo, impactando significativamente a disponibilidade do serviço.

#### 2. Ataque de Exaustão Financeira (DoW)
  Atacantes disparam um grande volume de requisições para explorar o custo por uso de serviços de IA, forçando o provedor a pagar quantias exorbitantes até o serviço se tornar inviável.

#### 3. Ataque de Entrada Contínua
  Ao enviar repetidamente entradas que excedem a capacidade do LLM, o atacante força a realocação excessiva de memória e processamento, degradando o serviço e interrupções operacionais.

#### 4. Ataque por Consultas Exigentes
  Consultas extremamente complexas forçam o LLM a consumir grandes quantidades de memória e processamento, tornando o sistema lento ou indisponível. Isso pode levar a tempos de processamento prolongados e possíveis falhas do sistema.

#### 5. Extração de Modelos via API
  Por meio de consultas repetidas e manipulação de prompts, atacantes extraem respostas suficientes para reconstruir parte do modelo original ou criar uma cópia não autorizada. Isso representa riscos de roubo de propriedade intelectual e compromete a integridade do modelo original.

#### 6. Criação de Modelo Clandestino
  Atacantes usam o modelo-alvo para gerar dados sintéticos e treinar um novo modelo clandestino, replicando seu comportamento sem necessidade de acesso direto ao original. Isso contorna métodos tradicionais de extração baseados em consultas, representando riscos significativos para modelos e tecnologias proprietárias.

#### 7. Ataques Laterais para Coleta de Dados
  Atacantes analisam padrões de resposta do LLM para inferir detalhes da arquitetura e dos pesos do modelo, possibilitando sua replicação ou exploração de vulnerabilidades. Isso pode comprometer a segurança do modelo e levar a explorações adicionais.

### Estratégias de Prevenção e Mitigação

#### 1. Validação de Entrada
  Implemente validação estrita para garantir que as entradas não excedam limites de tamanho razoáveis.

#### 2. Limitação de Exposição de Logits e Logprobs
  Restrinja ou ofusque a exposição de `logit_bias` e `logprobs` nas respostas da API, fornecendo apenas as informações necessárias sem revelar probabilidades detalhadas.

#### 3. Rate Limit (controle de taxa) e Cotas de Uso
  Aplique limitação de taxa e cotas de usuários para restringir o número de solicitações que uma única entidade pode fazer em um determinado período.

#### 4. Gestão Inteligente de Recursos
  Monitore e gerencie a alocação de recursos dinamicamente para evitar que um único usuário ou solicitação consuma recursos excessivos.

#### 5. Timeouts e Controle de Velocidade
  Configure limites de tempo e controle de velocidade para operações de alto consumo de recursos, prevenindo o uso prolongado de recursos.

#### 6. Técnicas de Sandbox
  Restrinja o acesso do LLM a recursos de rede, serviços internos e APIs, reduzindo riscos internos e ameaças externas.

#### 7. Monitoramento Contínuo e Detecção de Anomalias
  Monitore continuamente o uso de recursos e implemente registros para detectar e responder a padrões incomuns de consumo de recursos.

#### 8. Marca d'Água de Conteúdo
  Aplique técnicas de *watermarking* (marca d'água) para rastrear e identificar o uso não autorizado das respostas do LLM, dificultando tentativas de cópia e extração do modelo.

#### 9. Gerenciamento de Degradação Sob Carga
  Projete o sistema para degradar gradualmente sob carga pesada, mantendo funcionalidade parcial em vez de falha completa.

#### 10. Limite de Ações Enfileiradas e Escalabilidade Robusta
  Restrinja o número de ações enfileiradas e totais, enquanto incorpora escalabilidade dinâmica e balanceamento de carga para lidar com demandas variáveis.

#### 11. Treinamento de Robustez Adversarial
  Treine modelos para detectar e mitigar consultas adversariais e tentativas de extração.

#### 12. Detecção e Bloqueio de Tokens Anômalos
  Construa listas de tokens problemáticos conhecidos e analise a saída antes de adicioná-los à janela de contexto do modelo.

#### 13. Controles de Acesso
  Implemente controles de acesso fortes, incluindo controle de acesso baseado em função (RBAC) e o princípio do menor privilégio, para limitar o acesso não autorizado a repositórios e ambientes de treinamento de modelos LLM.

#### 14. Inventário Centralizado de Modelos de ML
  Use um inventário ou registro centralizado de modelos para garantir governança e controle de acesso adequados.

#### 15. Implantação Automatizada de MLOps
  Implemente implantação automatizada de MLOps com governança, rastreamento e fluxos de trabalho de aprovação para restringir o acesso e controle dentro da infraestrutura.

### Exemplos de Cenários de Ataques

#### Cenário #1: Ataque de Sobrecarga com Entradas Massivas
  Um atacante submete uma entrada incomumente grande a uma aplicação LLM que processa dados textuais, resultando em uso excessivo de memória e CPU, potencialmente travando o sistema ou desacelerando significativamente o serviço.

#### Cenário #2: Ataque de Exaustão por Solicitações Repetitivas
  Um atacante transmite um alto volume de solicitações para a API do LLM, causando consumo excessivo de recursos computacionais e tornando o serviço indisponível para usuários legítimos.

#### Cenário #3: Exploração de Consultas para Esgotamento de Recursos
  Um atacante elabora entradas específicas projetadas para acionar os processos mais exigentes do LLM, levando a uso prolongado de CPU e possíveis falhas do sistema.

#### Cenário #4: Exploração Financeira via Denial of Wallet (DoW)
  Um atacante gera operações excessivas para explorar o modelo de pagamento por uso de serviços de IA em nuvem, causando custos insustentáveis para o provedor.

#### Cenário #5: Roubo de Modelo via Treinamento com Dados Sintéticos
  Um atacante usa a API do LLM para gerar dados de treinamento sintéticos e ajusta outro modelo, criando um equivalente funcional e contornando as limitações tradicionais de extração de modelos.

#### Cenário #6: Evasão de Filtros para Vazamento de Dados
  Um atacante malicioso contorna técnicas de filtragem de entrada e preâmbulos do LLM para realizar um ataque de canal lateral e recuperar informações do modelo para um recurso remoto sob seu controle.

### Links de Referência

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Frameworks e Taxonomias Relacionados

Consulte esta seção para obter informações abrangentes, cenários e estratégias relacionadas à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
