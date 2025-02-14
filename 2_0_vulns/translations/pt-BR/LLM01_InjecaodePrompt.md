## LLM01:2025 Injeção de Prompt

### Descrição

Uma Vulnerabilidade de Injeção de Prompt ocorre quando prompts de usuários alteram o comportamento ou a saída de um LLM de maneiras não intencionais. Esses inputs podem afetar o modelo mesmo que sejam imperceptíveis para humanos; portanto, injeções de prompt não precisam ser visíveis ou compreensíveis por humanos, desde que o conteúdo seja interpretado pelo modelo.

As vulnerabilidades de injeção de prompt existem na forma como os modelos processam os prompts e como os inputs podem forçar o modelo a passar dados incorretamente para outras partes do modelo, potencialmente violando diretrizes, gerando conteúdo prejudicial, permitindo acesso não autorizado ou influenciando decisões críticas. Embora técnicas como Geração Aumentada por Recuperação (RAG) e fine-tuning busquem tornar as saídas dos LLMs mais relevantes e precisas, pesquisas mostram que essas técnicas não mitigam completamente as vulnerabilidades de injeção de prompt.

Embora injeção de prompt e jailbreak sejam conceitos relacionados à segurança de LLMs, eles frequentemente são usados como sinônimos. Injeção de prompt envolve manipular as respostas do modelo por meio de entradas específicas para alterar seu comportamento, o que pode incluir a violação de medidas de segurança. Jailbreak é uma forma de injeção de prompt onde o atacante fornece entradas que fazem o modelo ignorar completamente seus protocolos de segurança. Desenvolvedores podem implementar salvaguardas nos prompts do sistema e no tratamento de inputs para ajudar a mitigar ataques de injeção de prompt, mas a prevenção eficaz de jailbreaks requer atualizações contínuas no treinamento e nos mecanismos de segurança do modelo.

### Tipos de Vulnerabilidades de Injeção de Prompt

#### Injeções de Prompt Diretas
Injeções diretas de prompt ocorrem quando a entrada de um usuário altera diretamente o comportamento do modelo de maneiras não intencionais ou inesperadas. A entrada pode ser intencional (i.e., um ator malicioso elaborando deliberadamente um prompt para explorar o modelo) ou não intencional (i.e., um usuário fornecendo inadvertidamente uma entrada que desencadeia um comportamento inesperado).

#### Injeções de Prompt Indiretas
Injeções indiretas de prompt ocorrem quando um LLM aceita *inputs* de fontes externas, como websites ou arquivos. O conteúdo externo pode conter dados que, quando interpretados pelo modelo, alteram seu comportamento de maneiras não intencionais ou inesperadas. Assim como as injeções diretas, as injeções indiretas podem ser intencionais ou não intencionais.

A gravidade e a natureza do impacto de um ataque de injeção de prompt bem-sucedido podem variar amplamente, dependendo do contexto de negócios em que o modelo opera e do grau de autonomia com que o modelo foi arquitetado. Geralmente, injeções de prompt podem levar a resultados não intencionais, incluindo, mas não se limitando a:

- Divulgação de informações sensíveis
- Revelação de informações sensíveis sobre infraestrutura de IA ou prompts do sistema
- Manipulação de conteúdo que leva a saídas incorretas ou tendenciosas
- Fornecimento de acesso não autorizado a funções disponíveis para o LLM
- Execução de comandos arbitrários em sistemas conectados
- Manipulação de processos críticos de tomada de decisão

O avanço da IA multimodal, que processa múltiplos tipos de dados simultaneamente, introduz riscos únicos de injeção de prompt. Atacantes maliciosos podem explorar interações entre modalidades, como esconder instruções em imagens que acompanham texto benigno. A complexidade desses sistemas expande a superfície de ataque. Modelos multimodais também podem ser vulneráveis a novos ataques intermodais que são difíceis de detectar e mitigar com as técnicas disponíveis atualmente. Defesas robustas específicas para modelos multimodais são uma área crucial para pesquisa e desenvolvimento futuros.

### Estratégias de Prevenção e Mitigação

Vulnerabilidades de injeção de prompt são possíveis devido à natureza da IA generativa. Dada influência estocástico inerente ao funcionamento dos modelos, ainda não é claro se existem métodos infalíveis de prevenção para injeção de prompt. No entanto, as seguintes medidas podem mitigar os impactos:

#### 1. Restringir o comportamento do modelo
  Forneça instruções específicas sobre o papel, as capacidades e as limitações do modelo dentro do prompt do sistema. Implemente adesão estrita ao contexto, limite respostas a tarefas ou tópicos específicos e oriente o modelo a desconsiderar tentativas de alterar as instruções principais.

#### 2. Definir e validar formatos de saída esperados
  Defina formatos de saída claros, requisitando raciocínio detalhado e citações de fontes, e utilize código determinístico para verificar a conformidade com esses formatos.

#### 3. Implementar filtragem de entrada e saída
  Defina categorias sensíveis e construa regras para identificar e lidar com esses conteúdos. Aplique filtros semânticos e use verificações de strings para identificar conteúdo não permitido. Avalie respostas utilizando o Tríade RAG: Relevância do contexto, fundamentação e relevância pergunta/resposta para identificar saídas potencialmente maliciosas.

###$ 4. Reforçar o controle de privilégios e implementar o princípio de menor privilégio para acesso
  Forneça tokens de API exclusivos para funcionalidades extensíveis da aplicação e gerencie essas funções diretamente no código em vez de fornecê-las ao modelo. Restrinja os privilégios de acesso do modelo ao mínimo necessário para suas operações previstas.

#### 5. Requerer aprovação humana para ações de alto risco
  Implemente controles de humanos no processo para operações privilegiadas a fim de prevenir ações não autorizadas.

#### 6. Segregar e identificar conteúdo externo
  Separe e identifique claramente conteúdos não confiáveis para limitar sua influência nos prompts dos usuários.

#### 7. Realizar testes adversariais e simulações de ataques
  Realize testes de penetração regulares e simulações de violação, tratando o modelo como um usuário não confiável, para testar a eficácia das barreiras de confiança e controles de acesso.

### Exemplos de Cenários de Ataques

#### Cenário #1: Injeção Direta
  Um atacante injeta um prompt em um chatbot de suporte ao cliente, instruindo-o a ignorar diretrizes anteriores, consultar bases de dados privadas e enviar e-mails, resultando em acesso não autorizado e elevação de privilégios.

#### Cenário #2: Injeção Indireta
  Um usuário utiliza um LLM para resumir uma página da web que contém instruções ocultas que fazem o LLM inserir uma imagem vinculando a uma URL, resultando na exfiltração de uma conversa privada.

#### Cenário #3: Injeção Não Intencional
  Uma empresa inclui uma instrução em uma descrição de vaga para identificar aplicações geradas por IA. Um candidato, sem saber dessa instrução, usa um LLM para otimizar seu currículo, acionando inadvertidamente a detecção de IA.

#### Cenário #4: Influência Intencional no Modelo
  Um atacante modifica um documento em um repositório usado por uma aplicação RAG. Quando a consulta de um usuário retorna o conteúdo modificado, as instruções maliciosas alteram a saída do LLM, gerando resultados enganosos.

#### Cenário #5: Injeção de Código
  Um atacante explora uma vulnerabilidade (CVE-2024-5184) em um assistente de e-mail alimentado por LLM para injetar prompts maliciosos, permitindo acesso a informações sensíveis e manipulação de conteúdo de e-mail.

#### Cenário #6: Divisão de Payload
  Um atacante carrega um currículo com prompts maliciosos divididos. Quando um LLM é usado para avaliar o candidato, os prompts combinados manipulam a resposta do modelo, resultando em uma recomendação positiva, apesar do conteúdo real do currículo.

#### Cenário #7: Injeção Multimodal
  Um atacante incorpora um prompt malicioso em uma imagem que acompanha texto benigno. Quando uma IA multimodal processa a imagem e o texto simultaneamente, o prompt oculto altera o comportamento do modelo, possivelmente levando a ações não autorizadas ou divulgação de informações sensíveis.

#### Cenário #8: Sufixo Adversarial
  Um atacante adiciona uma sequência aparentemente sem sentido de caracteres a um prompt, que influencia a saída do LLM de forma maliciosa, contornando medidas de segurança.

#### Cenário #9: Ataque Multilíngue/Ofuscado
  Um atacante utiliza múltiplos idiomas ou codifica instruções maliciosas (e.g., usando Base64 ou emojis) para escapar de filtros e manipular o comportamento do LLM.

### Links de Referência

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
9. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### Frameworks e Taxonomias Relacionados

Consulte esta seção para obter informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
