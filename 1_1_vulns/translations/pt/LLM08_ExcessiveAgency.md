## LLM08: Autoridade Excessiva

### Descrição

Um sistema baseado em LLM frequentemente é concedido um grau de agência pelo seu desenvolvedor - a capacidade de interagir com outros sistemas e realizar ações em resposta a um prompt. A decisão sobre quais funções invocar também pode ser delegada a um 'agente' LLM para determinar dinamicamente com base no prompt de entrada ou saída do LLM.

A Autoridade Excessiva é a vulnerabilidade que permite a realização de ações prejudiciais em resposta a saídas inesperadas/ambíguas de um LLM (independentemente do que está causando o mau funcionamento do LLM; seja alucinação/confabulação, injeção de prompt direta/indireta, plugin malicioso, prompts benignos mal projetados ou apenas um modelo com desempenho ruim). A causa raiz da Autoridade Excessiva geralmente é um ou mais dos seguintes: funcionalidade excessiva, permissões excessivas ou autonomia excessiva. Isso difere do tratamento inadequado de saída, que se preocupa com a falta de escrutínio nas saídas do LLM.

A Autoridade Excessiva pode levar a uma ampla variedade de impactos em relação à confidencialidade, integridade e disponibilidade, e depende dos sistemas com os quais um aplicativo baseado em LLM pode interagir.

### Exemplos Comuns desta Vulnerabilidade

1. Funcionalidade Excessiva: Um agente LLM tem acesso a plugins que incluem funções desnecessárias para a operação pretendida do sistema. Por exemplo, um desenvolvedor precisa conceder a um agente LLM a capacidade de ler documentos de um repositório, mas o plugin de terceiros que eles escolhem também inclui a capacidade de modificar e excluir documentos.
2. Funcionalidade Excessiva: Um plugin pode ter sido testado durante a fase de desenvolvimento e descartado em favor de uma alternativa melhor, mas o plugin original permanece disponível para o agente LLM.
3. Funcionalidade Excessiva: Um plugin LLM com funcionalidade em aberto não filtra corretamente as instruções de entrada para comandos fora do necessário para a operação pretendida do aplicativo. Por exemplo, um plugin para executar um comando shell específico falha em prevenir adequadamente a execução de outros comandos shell.
4. Permissões Excessivas: Um plugin LLM tem permissões em outros sistemas que não são necessárias para a operação pretendida do aplicativo. Por exemplo, um plugin destinado a ler dados se conecta a um servidor de banco de dados usando uma identidade que não apenas possui permissões SELECT, mas também permissões UPDATE, INSERT e DELETE.
5. Permissões Excessivas: Um plugin LLM projetado para realizar operações em nome de um usuário acessa sistemas downstream com uma identidade genérica de alta privilégio. Por exemplo, um plugin para ler a loja de documentos do usuário atual se conecta ao repositório de documentos com uma conta privilegiada que tem acesso aos arquivos de todos os usuários.
6. Autonomia Excessiva: Um aplicativo ou plugin baseado em LLM falha em verificar e aprovar independentemente ações de alto impacto. Por exemplo, um plugin que permite a exclusão de documentos de um usuário realiza exclusões sem qualquer confirmação do usuário.

### Estratégias de Prevenção e Mitigação

As seguintes ações podem prevenir a Autoridade Excessiva:

1. Limitar os plugins/ferramentas que os agentes LLM têm permissão para chamar apenas às funções mínimas necessárias. Por exemplo, se um sistema baseado em LLM não requer a capacidade de buscar o conteúdo de uma URL, tal plugin não deve ser oferecido ao agente LLM.
2. Limitar as funções implementadas nos plugins/ferramentas LLM para o mínimo necessário. Por exemplo, um plugin que acessa a caixa de correio de um usuário para resumir e-mails pode precisar apenas da capacidade de ler e-mails, então o plugin não deve conter outras funcionalidades, como excluir ou enviar mensagens.
3. Evitar funções em aberto sempre que possível (por exemplo, executar um comando shell, buscar uma URL, etc.) e usar plugins/ferramentas com funcionalidades mais granulares. Por exemplo, um aplicativo baseado em LLM pode precisar escrever alguma saída em um arquivo. Se isso fosse implementado usando um plugin para executar uma função shell, o escopo para ações indesejadas seria muito grande (qualquer outro comando shell poderia ser executado). Uma alternativa mais segura seria construir um plugin de gravação de arquivos que só pudesse suportar aquela funcionalidade específica.
4. Limitar as permissões concedidas a outros sistemas pelos plugins/ferramentas LLM para o mínimo necessário, a fim de limitar o escopo de ações indesejadas. Por exemplo, um agente LLM que usa um banco de dados de produtos para fazer recomendações de compra a um cliente pode precisar apenas de acesso de leitura a uma tabela de 'produtos'; não deve ter acesso a outras tabelas, nem a capacidade de inserir, atualizar ou excluir registros. Isso deve ser aplicado por meio da concessão de permissões apropriadas no banco de dados para a identidade que o plugin LLM usa para se conectar ao banco de dados.
5. Rastrear a autorização do usuário e o escopo de segurança para garantir que as ações realizadas em nome de um usuário sejam executadas em sistemas downstream no contexto desse usuário específico e com as permissões mínimas necessárias. Por exemplo, um plugin LLM que lê o repositório de código de um usuário deve exigir que o usuário se autentique via OAuth e com o escopo mínimo necessário.
6. Utilizar controle humano no loop para exigir que um humano aprove todas as ações antes que sejam realizadas. Isso pode ser implementado em um sistema downstream (fora do escopo do aplicativo LLM) ou dentro do próprio plugin/ferramenta LLM. Por exemplo, um aplicativo baseado em LLM que cria e publica conteúdo em mídias sociais em nome de um usuário deve incluir um procedimento de aprovação do usuário dentro do plugin/ferramenta/API que implementa a operação 'publicar'.
7. Implementar autorização em sistemas downstream em vez de depender de um LLM para decidir se uma ação é permitida ou não. Ao implementar ferramentas/plugins, aplicar o princípio de mediação completa para que todas as solicitações feitas a sistemas downstream por meio dos plugins/ferramentas sejam validadas em relação às políticas de segurança.

As seguintes opções não impedirão a Autoridade Excessiva, mas podem limitar o nível de dano causado:

1. Registrar e monitorar a atividade de plugins/ferramentas LLM e sistemas downstream para identificar onde ações indesejadas estão ocorrendo e responder adequadamente.
2. Implementar limitação de taxa para reduzir o número de ações indesejadas que podem ocorrer dentro de um determinado período de tempo, aumentando a oportunidade de descobrir ações indesejadas por meio de monitoramento antes que ocorra um dano significativo.

### Exemplos de Cenários de Ataque

Um aplicativo de assistente pessoal baseado em LLM recebe acesso à caixa de correio de um indivíduo por meio de um plugin para resumir o conteúdo dos e-mails recebidos. Para alcançar essa funcionalidade, o plugin de e-mail requer a capacidade de ler mensagens, no entanto, o plugin escolhido pelo desenvolvedor do sistema também inclui funções para enviar mensagens. O LLM é vulnerável a um ataque de injeção de prompt indireto, em que um e-mail maliciosamente elaborado engana o LLM para comandar o plugin de e-mail a chamar a função 'enviar mensagens' para enviar spam da caixa de correio do usuário. Isso poderia ser evitado das seguintes maneiras:
(a) eliminar funcionalidades excessivas, usando um plugin que oferece apenas capacidades de leitura de e-mails,
(b) eliminar permissões excessivas, autenticando-se no serviço de e-mail do usuário por meio de uma sessão OAuth com escopo somente leitura, e/ou
(c) eliminar autonomia excessiva, exigindo que o usuário revise manualmente e clique em 'enviar' em cada e-mail redigido pelo plugin LLM.
Alternativamente, o dano causado poderia ser reduzido implementando limitação de taxa na interface de envio de e-mails.

### Links de Referência

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
2. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
3. [LangChain: Human-approval for tools](https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval): **Langchain Documentation**
4. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
