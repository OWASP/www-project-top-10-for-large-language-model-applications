## LLM01: Injeção de Prompt

### Descrição

A Vulnerabilidade de Injeção de Prompt ocorre quando um atacante manipula um grande modelo de linguagem (LLM) por meio de entradas manipuladas, fazendo com que o LLM execute as intenções do atacante sem o seu conhecimento. Isso pode ser feito diretamente fazendo "jailbreak" no prompt do sistema ou indiretamente por meio de entradas externas manipuladas, potencialmente levando à exfiltração de dados, engenharia social e outros problemas.

* **Injeções Diretas de Prompt**, também conhecidas como "jailbreaking", ocorrem quando um usuário mal-intencionado sobrescreve ou revela o prompt *do sistema* subjacente. Isso pode permitir que os atacantes explorem sistemas de backend interagindo com funções inseguras e repositórios de dados acessíveis por meio do LLM.
* **Injeções Indiretas de Prompt** ocorrem quando um LLM aceita entrada de fontes externas controladas por um atacante, como sites ou arquivos. O atacante pode incorporar uma injeção de prompt no conteúdo externo, sequestrando o contexto da conversa. Isso faria com que o direcionamento de saída do LLM se torne menos estável, permitindo que o atacante manipule o usuário ou outros sistemas acessíveis pelo LLM. Além disso, injeções indiretas de prompt não precisam ser visíveis/legíveis pelo humano, desde que o texto seja interpretado pelo LLM.

Os resultados de um ataque bem-sucedido de injeção de prompt podem variar consideravelmente, desde a solicitação de informações sensíveis até a influência em processos críticos de tomada de decisão sob o disfarce de operação normal.

Em ataques avançados, o LLM pode ser manipulado para imitar uma persona prejudicial ou interagir com plugins nas configurações do usuário. Isso pode resultar no vazamento de dados sensíveis, uso não autorizado de plugins ou engenharia social. Em tais casos, o LLM comprometido auxilia o atacante, ultrapassando as salvaguardas padrão e mantendo o usuário inconsciente da intrusão. Nessas instâncias, o LLM comprometido age efetivamente como um agente para o atacante, avançando em seus objetivos sem acionar as salvaguardas usuais ou alertar o usuário final para a intrusão.

### Exemplos Comuns desta Vulnerabilidade

1. Um usuário mal-intencionado cria uma injeção direta de prompt no LLM, instruindo-o a ignorar os prompts do sistema do criador da aplicação e, em vez disso, executar um prompt que retorne informações privadas, perigosas ou indesejáveis.
2. Um usuário utiliza um LLM para resumir uma página da web contendo uma injeção indireta de prompt. Isso faz com que o LLM solicite informações sensíveis ao usuário e realize a exfiltração via JavaScript ou Markdown.
3. Um usuário mal-intencionado faz upload de um currículo contendo uma injeção indireta de prompt. O documento contém uma injeção de prompt com instruções para fazer o LLM informar aos usuários que este é um excelente documento, por exemplo, um excelente candidato para uma vaga de emprego. Um usuário interno executa o documento no LLM para resumir o conteúdo. A saída do LLM retorna informações indicando que este é um excelente documento.
4. Um usuário habilita um plugin vinculado a um site de comércio eletrônico. Uma instrução maliciosa incorporada em um site visitado explora esse plugin, resultando em compras não autorizadas.
5. Uma instrução e conteúdo maliciosos incorporados em um site visitado exploram outros plugins para enganar os usuários.

### Estratégias de Prevenção e Mitigação

Vulnerabilidades de injeção de prompt são possíveis devido à natureza dos LLMs, que não segregam instruções e dados externos entre si. Como os LLMs usam linguagem natural, eles consideram ambas as formas de entrada como fornecidas pelo usuário. Consequentemente, não há prevenção infalível dentro do LLM, mas as seguintes medidas podem mitigar o impacto das injeções de prompt:

1. Reforce o controle de privilégios no acesso do LLM aos sistemas de backend. Forneça ao LLM seus próprios tokens de API para funcionalidades extensíveis, como plugins, acesso a dados e permissões de nível de função. Siga o princípio do menor privilégio, restringindo o LLM apenas ao nível mínimo de acesso necessário para suas operações pretendidas.
2. Adicione um humano no processo para funcionalidades estendidas. Ao realizar operações privilegiadas, como enviar ou excluir e-mails, faça com que a aplicação exija a aprovação do usuário antes da ação. Isso reduz a oportunidade para injeções indiretas de prompt resultarem em ações não autorizadas em nome do usuário sem o conhecimento ou consentimento dele.
3. Separe o conteúdo externo dos prompts do usuário. Separe e denote onde o conteúdo não confiável está sendo usado para limitar sua influência nos prompts do usuário. Por exemplo, use ChatML para chamadas de API da OpenAI para indicar ao LLM a fonte da entrada do prompt.
4. Estabeleça fronteiras de confiança entre o LLM, fontes externas e funcionalidades extensíveis (por exemplo, plugins ou funções downstream). Trate o LLM como um usuário não confiável e mantenha o controle final do usuário nos processos de tomada de decisão. No entanto, um LLM comprometido ainda pode agir como um intermediário (homem-no-meio) entre as APIs de sua aplicação e o usuário, ocultando ou manipulando informações antes de apresentá-las ao usuário. Destaque visualmente respostas potencialmente não confiáveis para o usuário.
5. Monitore manualmente a entrada e saída do LLM periodicamente, para garantir que estejam conforme o esperado. Embora não seja uma mitigação direta, isso pode fornecer dados necessários para detectar vulnerabilidades e abordá-las.

### Exemplos de Cenários de Ataque

1. Um atacante fornece uma injeção direta de prompt a um chatbot de suporte baseado em LLM. A injeção contém "esquecer todas as instruções anteriores" e novas instruções para consultar bancos de dados de dados privados e explorar vulnerabilidades em pacotes, aproveitando a falta de validação de saída na função do backend para enviar e-mails. Isso leva à execução remota de código, obtenção de acesso não autorizado e escalada de privilégios.
2. Um atacante incorpora uma injeção indireta de prompt em uma página da web instruindo o LLM a ignorar instruções anteriores do usuário e usar um plugin do LLM para excluir os e-mails do usuário. Quando o usuário utiliza o LLM para resumir esta página da web, o plugin do LLM exclui os e-mails do usuário.
3. Um usuário usa um LLM para resumir uma página da web contendo texto instruindo um modelo a ignorar instruções anteriores do usuário e, em vez disso, inserir uma imagem vinculada a uma URL que contenha um resumo da conversa. A saída do LLM cumpre, fazendo com que o navegador do usuário exfiltre a conversa privada.
4. Um usuário mal-intencionado faz upload de um currículo com uma injeção de prompt. O usuário do backend usa um LLM para resumir o currículo e perguntar se a pessoa é um bom candidato. Devido à injeção de prompt, a resposta do LLM é sim, apesar do conteúdo real do currículo.
5. Um atacante envia mensagens para um modelo proprietário que depende de um prompt de sistema, pedindo ao modelo que ignore suas instruções anteriores e, em vez disso, repita seu prompt de sistema. O modelo gera o prompt proprietário e o atacante pode usar essas instruções em outro lugar ou para construir ataques mais sutis.

### Links de Referência

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) **Simon Willison**
2. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
3. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
5. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
6. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
7. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
8. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
9. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
10. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
11. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
12. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
13. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
14. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**
