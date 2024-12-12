## LLM02:2025 Divulgação de Informações Sensíveis

### Descrição

Informações sensíveis podem afetar tanto o LLM quanto o contexto de sua aplicação. Isso inclui informações pessoais identificáveis (PII), detalhes financeiros, registros de saúde, dados confidenciais de negócios, credenciais de segurança e documentos legais. Modelos proprietários também podem ter métodos de treinamento exclusivos e código-fonte considerados sensíveis, especialmente em modelos fechados ou fundacionais.

LLMs, especialmente quando integrados em aplicações, correm o risco de expor dados sensíveis, algoritmos proprietários ou detalhes confidenciais através de suas saídas. Isso pode resultar em acesso não autorizado a dados, violações de privacidade e infrações de propriedade intelectual. Consumidores devem estar cientes de como interagir de forma segura com LLMs, entendendo os riscos de fornecer informações sensíveis que podem ser inadvertidamente divulgadas nas respostas do modelo.

Para reduzir esse risco, aplicações que utilizam LLMs devem realizar uma sanitização de dados adequada para evitar que dados dos usuários sejam incluídos no treinamento do modelo. Os proprietários das aplicações também devem oferecer políticas claras de Termos de Uso, permitindo que os usuários optem por não incluir seus dados no treinamento do modelo. Restrições dentro do prompt do sistema sobre os tipos de dados que o LLM deve retornar podem ajudar a mitigar a divulgação de informações sensíveis. No entanto, tais restrições podem não ser sempre respeitadas e podem ser contornadas via injeção de prompt ou outros métodos.

### Exemplos Comuns de Vulnerabilidades

#### 1. Vazamento de PII
  Informações pessoais identificáveis (PII) podem ser divulgadas durante interações com o LLM.
#### 2. Exposição de Algoritmo Proprietário
  Saídas de modelo mal configuradas podem revelar algoritmos ou dados proprietários. A divulgação de dados de treinamento pode expor modelos a ataques de inversão, nos quais atacantes extraem informações sensíveis ou reconstroem entradas. Por exemplo, como demonstrado no ataque 'Proof Pudding' (CVE-2019-20634), dados de treinamento divulgados facilitaram a extração e inversão do modelo, permitindo que atacantes contornassem controles de segurança em algoritmos de aprendizado de máquina e burlassem filtros de e-mail.
#### 3. Divulgação de Dados Sensíveis de Negócios
  Respostas geradas podem, inadvertidamente, incluir informações confidenciais de negócios.

### Estratégias de Prevenção e Mitigação

###@ Sanitização:

#### 1. Integrar Técnicas de Sanitização de Dados
  Implemente sanitização de dados para evitar que dados dos usuários sejam incluídos no treinamento do modelo. Isso inclui limpar ou mascarar conteúdos sensíveis antes que sejam utilizados no treinamento.
#### 2. Validação Rigorosa de Entradas
  Aplique métodos rigorosos de validação de entradas para detectar e filtrar dados potencialmente prejudiciais ou sensíveis, garantindo que não comprometam o modelo.

###@ Controles de Acesso:

#### 1. Impor Controles de Acesso Rigorosos
  Limite o acesso a dados sensíveis com base no princípio do menor privilégio. Conceda acesso somente aos dados necessários para o usuário ou processo específico.
#### 2. Restringir Fontes de Dados
  Limite o acesso do modelo a fontes de dados externas e gerencie a orquestração de dados em tempo de execução de forma segura para evitar vazamentos de dados não intencionais.

###@ Aprendizado Federado e Técnicas de Privacidade:

#### 1. Utilizar Aprendizado Federado
  Treine modelos utilizando dados descentralizados armazenados em múltiplos servidores ou dispositivos. Essa abordagem minimiza a necessidade de coleta centralizada de dados e reduz os riscos de exposição.
#### 2. Incorporar Privacidade Diferencial
  Aplique técnicas que adicionam ruído aos dados ou saídas, dificultando que atacantes façam engenharia reversa de dados individuais.

###@ Educação e Transparência do Usuário:

#### 1. Educar Usuários sobre o Uso Seguro de LLMs
  Forneça orientações sobre como evitar inserir informações sensíveis. Ofereça treinamento sobre melhores práticas para interagir com LLMs de forma segura.
#### 2. Garantir Transparência no Uso de Dados
  Mantenha políticas claras sobre retenção, uso e exclusão de dados. Permita que os usuários optem por não incluir seus dados nos processos de treinamento.

###@ Configuração Segura do Sistema:

#### 1. Ocultar Pré-configuração do Sistema
  Limite a capacidade dos usuários de sobrescrever ou acessar as configurações iniciais do sistema, reduzindo o risco de exposição de configurações internas.
#### 2. Referenciar Melhores Práticas de Configuração de Segurança
  Siga diretrizes como "OWASP API8:2023 Configuração de Segurança" para evitar o vazamento de informações sensíveis através de mensagens de erro ou detalhes de configuração.
  (Ref. link: [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))

###@ Técnicas Avançadas:

#### 1. Criptografia Homomórfica
  Use criptografia homomórfica para possibilitar análise de dados segura e aprendizado de máquina preservando a privacidade. Isso garante que os dados permaneçam confidenciais enquanto são processados pelo modelo.
#### 2. Tokenização e Redação
  Implemente tokenização para pré-processar e sanitizar informações sensíveis. Técnicas como correspondência de padrões podem detectar e redigir conteúdos confidenciais antes do processamento.

### Cenários de Ataques Exemplares

#### Cenário #1: Exposição de Dados Não Intencional
  Um usuário recebe uma resposta contendo dados pessoais de outro usuário devido à sanitização inadequada de dados.
#### Cenário #2: Injeção de Prompt Direcionada
  Um atacante contorna filtros de entrada para extrair informações sensíveis.
#### Cenário #3: Vazamento de Dados via Dados de Treinamento
  Inclusão negligente de dados no treinamento leva à divulgação de informações sensíveis.

### Links de Referência

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### Frameworks e Taxonomias Relacionados

Consulte esta seção para informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**
