## LLM07: Design Inseguro de Plugins

### Descrição

Os plugins LLM são extensões que, quando habilitadas, são chamadas automaticamente pelo modelo durante as interações do usuário. A plataforma de integração do modelo os controla, e a aplicação pode não ter controle sobre a execução, especialmente quando o modelo é hospedado por outra parte. Além disso, os plugins provavelmente implementam entradas de texto livre do modelo sem validação ou verificação de tipo para lidar com limitações de tamanho de contexto. Isso permite que um potencial atacante construa uma solicitação maliciosa para o plugin, o que pode resultar em uma ampla gama de comportamentos indesejados, incluindo execução remota de código.

O dano de inputs maliciosos muitas vezes depende de controles de acesso insuficientes e da falha no rastreamento de autorização em plugins. O controle de acesso inadequado permite que um plugin confie cegamente em outros plugins e assuma que o usuário final forneceu as entradas. Esse controle de acesso inadequado pode permitir que inputs maliciosos tenham consequências prejudiciais que vão desde exfiltração de dados, execução remota de código até escalonamento de privilégios.

Este item foca na criação de plugins LLM, em vez de plugins de terceiros, que são abordados nas Vulnerabilidades de Cadeia de Suprimentos LLM.

### Exemplos Comuns de Vulnerabilidade

1. Um plugin aceita todos os parâmetros em um único campo de texto em vez de parâmetros de entrada distintos.
2. Um plugin aceita strings de configuração em vez de parâmetros que podem substituir configurações inteiras.
3. Um plugin aceita instruções SQL ou de programação em bruto em vez de parâmetros.
4. A autenticação é realizada sem autorização explícita para um plugin específico.
5. Um plugin trata todo o conteúdo do LLM como se fosse criado inteiramente pelo usuário e executa quaisquer ações solicitadas sem exigir autorização adicional.

### Estratégias de Prevenção e Mitigação

1. Os plugins devem impor uma entrada estritamente parametrizada sempre que possível e incluir verificações de tipo e intervalo nas entradas. Quando isso não for possível, uma segunda camada de chamadas tipadas deve ser introduzida, analisando solicitações e aplicando validação e sanitização. Quando a entrada de formulário livre deve ser aceita devido à semântica da aplicação, ela deve ser cuidadosamente inspecionada para garantir que nenhum método potencialmente prejudicial esteja sendo chamado.
2. Os desenvolvedores de plugins devem aplicar as recomendações da OWASP no ASVS (Application Security Verification Standard) para garantir validação e sanitização adequadas de entrada.
3. Os plugins devem ser inspecionados e testados minuciosamente para garantir validação adequada. Use varreduras de Teste Estático de Segurança de Aplicações (SAST) e Teste Dinâmico e Interativo de Aplicações (DAST, IAST) nos pipelines de desenvolvimento.
4. Os plugins devem ser projetados para minimizar o impacto de qualquer exploração de parâmetro de entrada insegura seguindo as Diretrizes de Controle de Acesso da OWASP ASVS. Isso inclui controle de acesso de menor privilégio, expondo o mínimo de funcionalidade possível enquanto ainda realiza a função desejada.
5. Os plugins devem usar identidades de autenticação apropriadas, como OAuth2, para aplicar autorização e controle de acesso eficazes. Além disso, as Chaves de API devem ser usadas para fornecer contexto para decisões de autorização personalizadas que reflitam a rota do plugin, em vez do usuário interativo padrão.
6. Exigir autorização e confirmação manual do usuário para qualquer ação realizada por plugins sensíveis.
7. Os plugins são, tipicamente, APIs REST, então os desenvolvedores devem aplicar as recomendações encontradas nas Principais 10 Vulnerabilidades de Segurança em APIs da OWASP - 2023 para minimizar vulnerabilidades genéricas.

### Cenários de Ataque Exemplo

1. Um plugin aceita uma URL base e instrui o LLM a combinar a URL com uma consulta para obter previsões do tempo, que são incluídas no tratamento da solicitação do usuário. Um usuário mal-intencionado pode criar uma solicitação para que a URL aponte para um domínio que eles controlam, permitindo que eles injetem seu próprio conteúdo no sistema LLM por meio de seu domínio.
2. Um plugin aceita uma entrada de formulário livre em um único campo que não valida. Um atacante fornece cargas cuidadosamente elaboradas para realizar reconhecimento a partir de mensagens de erro. Em seguida, ele explora vulnerabilidades conhecidas de terceiros para executar código e realizar exfiltração de dados ou escalonamento de privilégios.
3. Um plugin usado para recuperar embeddings de um repositório de vetores aceita parâmetros de configuração como uma string de conexão sem validação. Isso permite que um atacante experimente e acesse outros repositórios de vetores alterando nomes ou parâmetros de host e exfiltra embeddings aos quais não deveria ter acesso.
4. Um plugin aceita cláusulas WHERE SQL como filtros avançados, que são então anexadas ao SQL de filtragem. Isso permite que um atacante execute um ataque SQL.
5. Um atacante usa injeção de prompt indireto para explorar um plugin de gerenciamento de código inseguro, sem validação de entrada e controle de acesso fraco, para transferir a propriedade do repositório e bloquear o usuário de seus repositórios.

### Links de Referência

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): **ChatGPT Developer’s Guide**
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI Documentation**
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI Documentation**
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace The Red**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
9. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**
