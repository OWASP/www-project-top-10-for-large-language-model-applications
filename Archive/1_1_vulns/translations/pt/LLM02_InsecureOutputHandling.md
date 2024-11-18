## LLM02: Manipulação Insegura de Output

### Descrição

A Manipulação Insegura de Output refere-se especificamente à validação, sanitização e tratamento insuficientes das saídas geradas por modelos de linguagem grandes (LLMs) antes de serem encaminhadas para outros componentes e sistemas. Como o conteúdo gerado pelo LLM pode ser controlado pela entrada do prompt, esse comportamento é semelhante a fornecer aos usuários acesso indireto a funcionalidades adicionais.

A Manipulação Insegura de Output difere da Dependência Excessiva, pois lida com as saídas geradas pelo LLM antes de serem encaminhadas, enquanto a Dependência Excessiva se concentra em preocupações mais amplas em torno da superdependência da precisão e adequação das saídas do LLM.

A exploração bem-sucedida de uma vulnerabilidade de Manipulação Insegura de Output pode resultar em XSS e CSRF em navegadores da web, bem como SSRF, escalonamento de privilégios ou execução remota de código em sistemas de backend.

As seguintes condições podem aumentar o impacto dessa vulnerabilidade:

- A aplicação concede privilégios ao LLM além do que é destinado aos usuários finais, possibilitando a escalada de privilégios ou a execução remota de código.
- A aplicação é vulnerável a ataques de injeção de prompt indireta, o que pode permitir que um atacante ganhe acesso privilegiado ao ambiente de um usuário-alvo.
- Plugins de terceiros que não validam adequadamente as entradas.

### Exemplos Comuns desta Vulnerabilidade

- A saída do LLM é inserida diretamente em um shell do sistema ou função semelhante, como exec ou eval, resultando na execução remota de código.
- JavaScript ou Markdown é gerado pelo LLM e retornado a um usuário. O código é então interpretado pelo navegador, resultando em XSS.

### Estratégias de Prevenção e Mitigação

- Trate o modelo como qualquer outro usuário, adotando uma abordagem de confiança zero, e aplique validação adequada nas respostas provenientes do modelo para funções de backend.
- Siga as diretrizes do OWASP ASVS (Application Security Verification Standard) para garantir uma validação e sanitização eficazes de entrada.
- Codifique a saída do modelo de volta para os usuários para mitigar a execução indesejada de código JavaScript ou Markdown. O OWASP ASVS fornece orientações detalhadas sobre codificação de saída.

### Exemplos de Cenários de Ataque

1. Uma aplicação utiliza um plugin de LLM para gerar respostas para uma funcionalidade de chatbot. O plugin também oferece diversas funções administrativas acessíveis a outro LLM privilegiado. O LLM de propósito geral passa diretamente sua resposta, sem uma validação adequada de saída, para o plugin, causando o desligamento do plugin para manutenção.
2. Um usuário utiliza uma ferramenta de resumo de site alimentada por um LLM para gerar um resumo conciso de um artigo. O site inclui uma injeção de prompt instruindo o LLM a capturar conteúdo sensível do site ou da conversa do usuário. A partir daí, o LLM pode codificar os dados sensíveis e enviá-los, sem validação ou filtragem adequada de saída, para um servidor controlado pelo atacante.
3. Um LLM permite que os usuários criem consultas SQL para um banco de dados de backend por meio de uma funcionalidade semelhante a um chat. Um usuário solicita uma consulta para excluir todas as tabelas do banco de dados. Se a consulta elaborada pelo LLM não for examinada cuidadosamente, todas as tabelas do banco de dados serão excluídas.
4. Um aplicativo da web usa um LLM para gerar conteúdo a partir de prompts de texto do usuário sem sanitização de saída. Um atacante pode enviar um prompt manipulado fazendo com que o LLM retorne uma carga útil de JavaScript não sanitizada, resultando em XSS quando renderizado no navegador da vítima. A validação insuficiente dos prompts possibilitou esse ataque.

### Links de Referência

1. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
