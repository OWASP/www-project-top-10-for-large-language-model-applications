## LLM06:2025 Agência Excessiva

### Descrição

Um sistema baseado em LLM frequentemente recebe um grau de autonomia pelo desenvolvedor – a capacidade de chamar funções ou interagir com outros sistemas por meio de extensões (às vezes referidas como ferramentas, habilidades ou plugins por diferentes fornecedores) para realizar ações em resposta a um prompt. A decisão sobre qual extensão invocar pode ser delegada a um 'agente' LLM para determinar dinamicamente com base na entrada do prompt ou saída do LLM. Sistemas baseados em agentes geralmente fazem chamadas repetidas a um LLM usando a saída de invocações anteriores para direcionar subsequentes.

Agência Excessiva é a vulnerabilidade que permite que ações prejudiciais sejam realizadas em resposta a saídas inesperadas, ambíguas ou manipuladas de um LLM, independentemente do que esteja causando o mau funcionamento do LLM. Os gatilhos comuns incluem:
- alucinação/confabulação causada por prompts mal projetados ou por um modelo de desempenho insatisfatório;
- injeção direta/indireta de prompts por um usuário mal-intencionado, uma invocação anterior de uma extensão mal-intencionada/comprometida, ou (em sistemas colaborativos/multiagentes) um agente par mal-intencionado/comprometido.

As causas principais da Agência Excessiva geralmente incluem:
- funcionalidade excessiva;
- permissões excessivas;
- autonomia excessiva.

Agência Excessiva pode levar a uma ampla gama de impactos sobre confidencialidade, integridade e disponibilidade, dependendo dos sistemas com os quais uma aplicação baseada em LLM pode interagir.

Nota: Agência Excessiva difere de Tratamento Impróprio de Saída, que está relacionado à falta de análise rigorosa das saídas do LLM.

### Exemplos Comuns de Riscos

#### 1. Funcionalidade Excessiva
  Um agente LLM tem acesso a extensões que incluem funções desnecessárias para a operação pretendida do sistema. Exemplo: um desenvolvedor precisa conceder ao agente a capacidade de ler documentos de um repositório, mas a extensão de terceiros escolhida também permite modificar e excluir documentos.

#### 2. Funcionalidade Excessiva
  Uma extensão foi testada durante uma fase de desenvolvimento e substituída por uma alternativa melhor, mas o plugin original permanece acessível ao agente LLM.

#### 3. Funcionalidade Excessiva
  Um plugin LLM com funcionalidade aberta não filtra adequadamente instruções de entrada para comandos fora do necessário para a operação pretendida. Exemplo: uma extensão para executar um comando shell específico não impede adequadamente outros comandos shell de serem executados.

#### 4. Permissões Excessivas
  Uma extensão LLM tem permissões em sistemas downstream que não são necessárias para a operação pretendida da aplicação. Exemplo: uma extensão destinada a ler dados conecta-se a um servidor de banco de dados com uma identidade que também tem permissões de UPDATE, INSERT e DELETE.

#### 5. Permissões Excessivas
  Uma extensão projetada para operações no contexto de um usuário acessa sistemas downstream com uma identidade genérica altamente privilegiada. Exemplo: uma extensão para ler o repositório de documentos de um usuário conecta-se ao repositório com uma conta privilegiada que acessa arquivos de todos os usuários.

#### 6. Autonomia Excessiva
  Uma aplicação ou extensão baseada em LLM não verifica ou aprova independentemente ações de alto impacto. Exemplo: uma extensão que permite a exclusão de documentos de um usuário realiza as exclusões sem qualquer confirmação do usuário.

### Estratégias de Prevenção e Mitigação

As seguintes ações podem prevenir Agência Excessiva:

#### 1. Minimize extensões
  Limite as extensões que agentes LLM podem chamar ao mínimo necessário. Exemplo: se um sistema baseado em LLM não precisa buscar o conteúdo de uma URL, essa extensão não deve ser disponibilizada ao agente.

#### 2. Minimize a funcionalidade das extensões
  Limite as funções implementadas em extensões LLM ao mínimo necessário. Exemplo: uma extensão que acessa a caixa de entrada de um usuário para resumir e-mails deve apenas permitir a leitura, sem funcionalidade adicional como exclusão ou envio.

#### 3. Evite extensões de escopo aberto
  Sempre que possível, evite extensões de escopo aberto (e.g., executar um comando shell, buscar uma URL) e prefira extensões com funcionalidade mais granular.

#### 4. Minimize permissões de extensão
  Limite as permissões que extensões LLM recebem para outros sistemas ao mínimo necessário. Exemplo: um agente que usa um banco de dados de produtos para fazer recomendações deve ter apenas acesso de leitura à tabela de produtos.

#### 5. Execute extensões no contexto do usuário
  Acompanhe autorização e escopo de segurança para garantir que ações realizadas em nome de um usuário sejam executadas no contexto do usuário específico e com os privilégios mínimos necessários.

#### 6. Requerer aprovação do usuário
  Utilize controle humano para exigir aprovação para ações de alto impacto antes de serem realizadas.

#### 7. Mediação completa
  Implemente autorização em sistemas downstream e não confie em um LLM para decidir se uma ação é permitida ou não.

#### 8. Sanitize entradas e saídas de LLM
  Siga as melhores práticas de codificação segura, aplicando recomendações da OWASP ASVS, com forte foco na sanitização de entrada.

Além disso, para limitar o impacto de Agência Excessiva:
- Monitore atividades de extensões LLM e sistemas downstream para identificar ações indesejadas.
- Implemente limitação de taxa para reduzir o número de ações indesejadas em um período de tempo.

### Cenários de Ataques Exemplares

Um aplicativo assistente pessoal baseado em LLM tem acesso à caixa de entrada de um usuário via extensão para resumir o conteúdo de e-mails recebidos. Para essa funcionalidade, a extensão precisa apenas ler mensagens. No entanto, o plugin escolhido pelo desenvolvedor também contém funções para enviar mensagens. Adicionalmente, o app é vulnerável a uma injeção de prompt indireta, onde um e-mail malicioso leva o LLM a instruir o agente a escanear a caixa de entrada do usuário para informações sensíveis e enviá-las ao e-mail do atacante. 

Isso poderia ser evitado por:
- Eliminar funcionalidade excessiva com uma extensão que apenas lê e-mails;
- Eliminar permissões excessivas autenticando via OAuth com escopo apenas de leitura;
- Eliminar autonomia excessiva exigindo que o usuário revise e aprove manualmente mensagens redigidas pelo LLM.

A redução de danos também poderia ser alcançada implementando limitação de taxa na interface de envio de e-mails.

### Links de Referência

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
5. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
