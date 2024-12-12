## LLM07:2025 Vazamento de Prompt do Sistema

### Descrição

A vulnerabilidade de vazamento de prompt do sistema em LLMs refere-se ao risco de que os prompts do sistema ou instruções usados para orientar o comportamento do modelo possam conter informações sensíveis que não deveriam ser descobertas. Prompts do sistema são projetados para guiar a saída do modelo com base nos requisitos da aplicação, mas podem, inadvertidamente, conter segredos. Quando descobertas, essas informações podem ser usadas para facilitar outros ataques.

É importante entender que o prompt do sistema não deve ser considerado um segredo, nem utilizado como um controle de segurança. Assim, dados sensíveis como credenciais, strings de conexão, etc., não devem estar contidos na linguagem do prompt do sistema.

Da mesma forma, se um prompt do sistema contém informações sobre diferentes papéis e permissões, ou dados sensíveis como strings de conexão ou senhas, o problema fundamental de segurança não é que esses dados foram divulgados, mas que a aplicação permite a violação de gerenciamento de sessão e verificações de autorização robustas ao delegar essas tarefas ao LLM, além de armazenar dados sensíveis em locais inadequados.

Em resumo: a divulgação do próprio prompt do sistema não apresenta o risco real – o risco de segurança reside nos elementos subjacentes, seja divulgação de informações sensíveis, violação de restrições do sistema, separação inadequada de privilégios, etc. Mesmo que a redação exata não seja divulgada, atacantes interagindo com o sistema quase certamente serão capazes de deduzir muitos dos controles e restrições de formatação presentes na linguagem do prompt do sistema ao usar a aplicação, enviando comandos ao modelo e observando os resultados.

### Exemplos Comuns de Risco

#### 1. Exposição de Funcionalidade Sensível
  O prompt do sistema pode revelar informações ou funcionalidades confidenciais, como arquitetura interna do sistema, chaves de API, credenciais de banco de dados ou tokens de usuários. Essas informações podem ser extraídas ou usadas por atacantes para obter acesso não autorizado à aplicação. Exemplo: um prompt do sistema que contém o tipo de banco de dados usado pode permitir que um atacante o direcione para ataques de injeção de SQL.

#### 2. Exposição de Regras Internas
  O prompt do sistema revela processos de tomada de decisão interna que deveriam ser mantidos confidenciais. Essas informações podem permitir que atacantes explorem fraquezas ou contornem controles da aplicação. Exemplo: em um aplicativo bancário, um prompt pode conter:
  > "O limite de transação é de $5000 por dia para um usuário. O limite total de empréstimo é de $10.000."
  Essas informações podem permitir que atacantes contornem limites de segurança, como realizar transações acima do limite estabelecido.

#### 3. Divulgação de Critérios de Filtragem
  Um prompt do sistema pode solicitar ao modelo que filtre ou rejeite conteúdo sensível. Exemplo:
  > "Se um usuário solicitar informações sobre outro usuário, sempre responda com: ‘Desculpe, não posso ajudar com essa solicitação.’"

#### 4. Divulgação de Permissões e Papéis de Usuário
  O prompt do sistema pode revelar estruturas internas de papéis ou níveis de permissão. Exemplo:
  > "O papel de administrador concede acesso total para modificar registros de usuários."
  Se os atacantes descobrirem essas permissões, podem tentar ataques de escalonamento de privilégios.

### Estratégias de Prevenção e Mitigação

#### 1. Separe Dados Sensíveis dos Prompts do Sistema
  Evite incorporar informações sensíveis (e.g., chaves de API, chaves de autenticação, nomes de banco de dados, papéis de usuários, estrutura de permissões) diretamente nos prompts do sistema. Externize esses dados para sistemas aos quais o modelo não tenha acesso direto.

#### 2. Evite Dependência de Prompts do Sistema para Controle Rigoroso de Comportamento
  Como os LLMs são suscetíveis a ataques como injeções de prompts, recomenda-se evitar o uso de prompts do sistema para controlar o comportamento do modelo sempre que possível. Utilize sistemas externos ao LLM para garantir esses comportamentos.

#### 3. Implemente Guardrails
  Estabeleça um sistema de barreiras externas ao próprio LLM. Embora treinar comportamentos específicos no modelo seja eficaz, como ensiná-lo a não revelar seu prompt do sistema, isso não garante que o modelo sempre seguirá essas instruções. Um sistema independente que inspecione as saídas para verificar conformidade com as expectativas é preferível a confiar apenas nas instruções do prompt do sistema.

#### 4. Garanta que controles de segurança sejam aplicados independentemente do LLM
  Controles críticos, como separação de privilégios e verificações de limites de autorização, não devem ser delegados ao LLM, seja por meio do prompt do sistema ou de outra forma. Esses controles devem ocorrer de maneira determinística e auditável. Em casos onde um agente realiza tarefas que exigem diferentes níveis de acesso, múltiplos agentes devem ser usados, cada um configurado com os privilégios mínimos necessários para realizar as tarefas.

### Cenários de Ataques Exemplares

#### Cenário #1
   Um LLM possui um prompt do sistema que contém credenciais usadas para uma ferramenta à qual ele tem acesso. O prompt do sistema é vazado para um atacante, que então usa essas credenciais para outros fins.

#### Cenário #2
  Um LLM tem um prompt do sistema proibindo a geração de conteúdo ofensivo, links externos e execução de código. Um atacante extrai esse prompt e utiliza um ataque de injeção de prompt para contornar essas instruções, facilitando um ataque de execução remota de código.

### Links de Referência

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): **Pliny the Prompter**
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): **Prompt Security**
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): **LouisShark**
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): **Jujumilk3**
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): **Green_Terminals**

### Frameworks e Taxonomias Relacionados

Consulte esta seção para informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000): **MITRE ATLAS**
