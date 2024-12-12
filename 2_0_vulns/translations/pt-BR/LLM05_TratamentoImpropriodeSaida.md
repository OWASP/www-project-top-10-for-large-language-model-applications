## LLM05:2025 Tratamento Impróprio de Saída

### Descrição

Tratamento Impróprio de Saída refere-se à validação, sanitização e manipulação insuficientes das saídas geradas por grandes modelos de linguagem (LLMs) antes de serem passadas para outros componentes e sistemas. Como o conteúdo gerado pelos LLMs pode ser controlado pela entrada de prompts, esse comportamento é semelhante a fornecer aos usuários acesso indireto a funcionalidades adicionais. 

Tratamento Impróprio de Saída difere de Dependência Excessiva, pois aborda as saídas geradas pelos LLMs antes de serem transmitidas, enquanto Dependência Excessiva enfoca preocupações mais amplas sobre a precisão e adequação das saídas dos LLMs.

A exploração bem-sucedida de uma vulnerabilidade de Tratamento Impróprio de Saída pode resultar em XSS e CSRF em navegadores da web, bem como SSRF, escalonamento de privilégios ou execução remota de código em sistemas de backend. 

As seguintes condições podem aumentar o impacto dessa vulnerabilidade:
- A aplicação concede ao LLM privilégios além do que é intencionado para os usuários finais, possibilitando escalonamento de privilégios ou execução remota de código.
- A aplicação é vulnerável a ataques indiretos de injeção de prompts, permitindo que um invasor obtenha acesso privilegiado ao ambiente de um usuário-alvo.
- Extensões de terceiros não validam adequadamente as entradas.
- Falta de codificação de saída apropriada para diferentes contextos (e.g., HTML, JavaScript, SQL).
- Monitoramento e registro insuficientes das saídas dos LLMs.
- Ausência de limitação de taxa ou detecção de anomalias para o uso de LLMs.

### Exemplos Comuns de Vulnerabilidades

1. A saída do LLM é inserida diretamente em um shell do sistema ou função similar, como `exec` ou `eval`, resultando em execução remota de código.
2. JavaScript ou Markdown gerado pelo LLM é retornado ao usuário e interpretado pelo navegador, resultando em XSS.
3. Consultas SQL geradas pelo LLM são executadas sem a devida parametrização, levando a injeção de SQL.
4. A saída do LLM é usada para construir caminhos de arquivos sem sanitização adequada, resultando em vulnerabilidades de travessia de diretórios.
5. Conteúdo gerado pelo LLM é usado em modelos de e-mail sem escape adequado, possibilitando ataques de phishing.

### Estratégias de Prevenção e Mitigação

1. Trate o modelo como qualquer outro usuário, adotando uma abordagem de confiança zero e aplicando validação adequada nas respostas provenientes do modelo para funções de backend.
2. Siga as diretrizes do OWASP ASVS (Padrão de Verificação de Segurança de Aplicações) para garantir validação e sanitização de entrada eficazes.
3. Codifique as saídas do modelo para os usuários, mitigando a execução indesejada de código em JavaScript ou Markdown. O OWASP ASVS fornece orientações detalhadas sobre codificação de saída.
4. Implemente codificação de saída sensível ao contexto com base no uso das saídas do LLM (e.g., codificação HTML para conteúdo da web, escape SQL para consultas de banco de dados).
5. Use consultas parametrizadas ou instruções preparadas para todas as operações de banco de dados envolvendo saídas do LLM.
6. Adote Políticas de Segurança de Conteúdo (CSP) rigorosas para mitigar o risco de ataques XSS provenientes de conteúdo gerado por LLMs.
7. Implemente sistemas robustos de registro e monitoramento para detectar padrões incomuns nas saídas dos LLMs que possam indicar tentativas de exploração.

### Cenários de Ataques Exemplares

#### Cenário #1
  Uma aplicação utiliza uma extensão LLM para gerar respostas para um recurso de chatbot. A extensão também oferece diversas funções administrativas acessíveis a outro LLM privilegiado. O LLM de uso geral passa diretamente sua resposta, sem validação adequada, para a extensão, fazendo com que ela entre em manutenção.

#### Cenário #2
  Um usuário utiliza uma ferramenta de resumo de websites alimentada por um LLM para gerar um resumo de um artigo. O site inclui uma injeção de prompt instruindo o LLM a capturar conteúdo sensível do site ou da conversa do usuário. O LLM então envia os dados capturados, sem validação ou filtragem, para um servidor controlado pelo invasor.

#### Cenário #3
  Um LLM permite que usuários criem consultas SQL para um banco de dados de backend por meio de uma interface de chat. Um usuário solicita uma consulta para excluir todas as tabelas do banco de dados. Se a consulta criada pelo LLM não for analisada, todas as tabelas do banco de dados serão excluídas.

#### Cenário #4
  Um aplicativo da web usa um LLM para gerar conteúdo a partir de prompts de texto de usuários sem sanitização das saídas. Um invasor pode enviar um prompt criado para fazer o LLM retornar um payload JavaScript não sanitizado, levando a XSS ao ser renderizado no navegador de uma vítima.

#### Cenário #5
  Um LLM é usado para gerar modelos dinâmicos de e-mails para uma campanha de marketing. Um invasor manipula o LLM para incluir JavaScript malicioso no conteúdo do e-mail. Se a aplicação não sanitizar adequadamente a saída do LLM, isso pode levar a ataques XSS em destinatários que visualizem o e-mail em clientes vulneráveis.

#### Cenário #6
  Um LLM é usado para gerar código a partir de entradas em linguagem natural em uma empresa de software, visando simplificar tarefas de desenvolvimento. Esse método pode expor informações sensíveis, criar métodos inseguros de manipulação de dados ou introduzir vulnerabilidades como injeção de SQL. A revisão minuciosa do código e a verificação de pacotes sugeridos são cruciais para evitar violações de segurança, acessos não autorizados e comprometimentos do sistema.

### Links de Referência

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/): **Theregister**
