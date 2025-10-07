## LLM06:2025 Autonomia Excessiva

### Descrição

Um sistema baseado em LLM frequentemente recebe um grau de autonomia pelo desenvolvedor – a capacidade de chamar funções ou interagir com outros sistemas por meio de extensões (às vezes referidas como ferramentas, habilidades ou plugins por diferentes fornecedores) para realizar ações em resposta a um prompt. A decisão sobre qual extensão invocar pode ser delegada a um 'agente' LLM para determinar dinamicamente com base na entrada do prompt ou saída do LLM. Sistemas baseados em agentes costumam realizar múltiplas chamadas a um LLM, utilizando a saída de invocações anteriores para fundamentar e direcionar as próximas ações.

Autonomia Excessiva é a vulnerabilidade que permite que ações prejudiciais sejam realizadas em resposta a saídas inesperadas, ambíguas ou manipuladas de um LLM, independentemente do que esteja causando o mau funcionamento do LLM. Os gatilhos comuns incluem:

- alucinação/confabulação causada por prompts mal projetados ou por um modelo de desempenho insatisfatório;
- injeção direta/indireta de prompts por um usuário mal-intencionado, por uma extensão comprometida em invocações anteriores, ou por um agente mal-intencionado em sistemas colaborativos/multiagentes.

As causas principais da Autonomia Excessiva geralmente incluem:

- capacidade excessiva;
- permissões excessivas;
- autonomia excessiva.

Autonomia Excessiva pode levar a uma ampla gama de impactos sobre confidencialidade, integridade e disponibilidade, dependendo dos sistemas com os quais uma aplicação baseada em LLM pode interagir.

Nota: Autonomia Excessiva difere de Manipulação Imprópria de Saída, que está relacionado à falta de análise rigorosa das saídas do LLM.

### Exemplos Comuns de Riscos

#### 1. Funcionalidade Excessiva

  Um agente LLM tem acesso a extensões que incluem funções desnecessárias para a operação pretendida do sistema. Exemplo: um desenvolvedor precisa conceder ao agente a capacidade de ler documentos de um repositório, mas a extensão de terceiros escolhida também permite modificar e excluir documentos.

#### 2. Extensão Obsoleta

  Uma extensão foi testada durante uma fase de desenvolvimento e substituída por uma alternativa melhor, mas o plugin original permanece acessível ao agente LLM.

#### 3. Controle Inadequado de Comandos

  Um plugin LLM com funcionalidade aberta não filtra adequadamente instruções de entrada para comandos fora do necessário para a operação pretendida. Exemplo: uma extensão para executar um comando shell específico não impede adequadamente outros comandos shell de serem executados.

#### 4. Permissões Excessivas

  Uma extensão LLM tem permissões em sistemas downstream que não são necessárias para a operação pretendida da aplicação. Exemplo: uma extensão destinada a ler dados conecta-se a um servidor de banco de dados com uma identidade que também tem permissões de UPDATE, INSERT e DELETE.

#### 5. Permissões Excessivas

  Uma extensão projetada para operar no contexto de um único usuário acessa sistemas downstream com uma identidade genérica excessivamente privilegiada. Exemplo: uma extensão para ler o repositório de documentos de um usuário conecta-se ao repositório com uma conta privilegiada que acessa arquivos de todos os usuários.

#### 6. Autonomia Excessiva

  Uma aplicação ou extensão baseada em LLM executa ações de alto impacto sem verificação ou aprovação independente. Exemplo: uma extensão que permite a exclusão de documentos de um usuário realiza as exclusões sem qualquer confirmação do usuário.

### Estratégias de Prevenção e Mitigação

As seguintes ações podem prevenir Autonomia Excessiva:

#### 1. Reduza o uso de extensões

  Limite as extensões que agentes LLM podem chamar ao mínimo necessário. Por exemplo, se um sistema baseado em LLM não precisa buscar o conteúdo de uma URL, essa extensão não deve ser disponibilizada ao agente.

#### 2. Reduza a funcionalidade das extensões

  Limite as funções implementadas em extensões LLM ao mínimo necessário. Por exemplo, uma extensão que acessa a caixa de entrada de um usuário para resumir e-mails deve apenas permitir a leitura, sem funcionalidade adicional como exclusão ou envio.

#### 3. Evite extensões de escopo aberto

  Sempre que possível, evite extensões que executem comandos genéricos (e.g., rodar comandos shell, buscar URLs) e prefira extensões com funcionalidade específica e restrita. Por exemplo, em vez de permitir a execução de comandos shell para gravar arquivos, crie uma extensão específica apenas para escrita de arquivos.

#### 4. Reduza as permissões das extensões

  Restrinja as permissões concedidas às extensões LLM para limitar o escopo de ações indesejadas. Por exemplo, um agente que usa um banco de dados para recomendar produtos deve ter apenas permissão de leitura e nunca poder modificar ou excluir dados.

#### 5. Execute extensões no contexto do usuário

  Garanta que ações realizadas em nome de um usuário sejam executadas com os menores privilégios necessários. Por exemplo, uma extensão que acessa repositórios de código deve exigir autenticação via OAuth e restringir o escopo de acesso ao mínimo essencial.

#### 6. Requeira aprovação do usuário

  Implemente um processo de revisão humana para aprovar ações de alto impacto antes de sua execução. Por exemplo, um aplicativo que gera e publica posts em redes sociais deve exigir que o usuário aprove cada publicação antes de enviá-la.

#### 7. Garanta autorização no sistema de destino

  Aplique controle de permissões diretamente nos sistemas que executam as ações, sem depender do LLM para validar se uma operação é permitida. Por exemplo, caso um LLM faça chamadas a uma API de um serviço financeiro, a API deve validar permissões e não apenas confiar no LLM.

#### 8. Sanitize e valide entradas e saídas do LLM

  Siga as melhores práticas de codificação segura, aplicando recomendações da OWASP ASVS, com forte foco na sanitização de entrada.

Embora essas medidas não evitem completamente a Autonomia Excessiva, elas podem limitar os danos causados:

- Monitore atividades de extensões LLM e sistemas *downstream* para identificar ações indesejadas.
- Aplique limitação de taxa para restringir a frequência de ações indesejadas, aumentando a chance de detectar atividades maliciosas antes que causem danos significativos.

### Exemplos de Cenários de Ataques

Um aplicativo assistente pessoal baseado em LLM tem acesso à caixa de entrada de um usuário via extensão para resumir o conteúdo de e-mails recebidos. Para essa funcionalidade, a extensão precisa apenas ler mensagens. Porém, o plugin utilizado pelo desenvolvedor inclui também funções desnecessárias, como o envio de mensagens. Além disso, o aplicativo é vulnerável a uma injeção de prompt indireta: um e-mail malicioso pode manipular o LLM para induzir o agente a varrer a caixa de entrada do usuário em busca de informações sensíveis e enviá-las para o endereço de e-mail do atacante.

Isso poderia ser evitado ao se:

- Reduzir funcionalidades desnecessárias utilizando uma extensão que apenas leia e-mails;
- Restringir permissões, autenticando via OAuth com escopo apenas de leitura; e/ou
- Controlar a autonomia do LLM, exigindo que o usuário revise e aprove manualmente qualquer mensagem antes do envio..

Além disso, a implementação de limitação de taxa na interface de envio de e-mails ajudaria a mitigar o impacto, restringindo o número de mensagens enviadas e permitindo detectar atividades suspeitas antes que causem danos maiores.

### Links de Referência

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
5. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
