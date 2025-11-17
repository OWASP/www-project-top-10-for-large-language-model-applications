## LLM07:2025 Vazamento de Prompt do Sistema

### Descrição

A vulnerabilidade de vazamento de prompt do sistema em LLMs ocorre quando prompts ou instruções utilizadas para orientar o comportamento do modelo acabam contendo, inadvertidamente, informações sensíveis que não deveriam ser expostas. Prompts do sistema são projetados para guiar a saída do modelo com base nos requisitos da aplicação, mas podem, inadvertidamente, conter segredos. Quando descobertas, essas informações podem ser usadas para facilitar outros ataques.

É importante entender que o prompt do sistema não deve ser considerado um segredo, nem utilizado como um controle de segurança. Assim, dados sensíveis como credenciais, strings de conexão, etc., não devem estar contidos na linguagem do prompt do sistema.

Da mesma forma, se um prompt do sistema contém informações sobre diferentes papéis e permissões, ou dados sensíveis como strings de conexão ou senhas, o problema central de segurança não está na simples divulgação desses dados, mas no fato de que a aplicação permite a violação do gerenciamento de sessão e de verificações robustas de autorização ao delegar essas funções ao LLM, além de armazenar dados sensíveis em locais inadequados.

Em resumo: a divulgação do próprio prompt do sistema não apresenta o risco real – o risco de segurança reside nos elementos subjacentes, seja divulgação de informações sensíveis, violação de restrições do sistema, separação inadequada de privilégios, etc. Mesmo que o conteúdo exato do prompt do sistema não seja divulgado, atacantes que interagem com o sistema poderão deduzir muitos dos controles e restrições aplicados simplesmente analisando as respostas do modelo ao longo do uso da aplicação.

### Exemplos Comuns de Risco

#### 1. Exposição de Funcionalidade Sensível

  O prompt do sistema pode revelar informações ou funcionalidades confidenciais, como arquitetura interna do sistema, chaves de API, credenciais de banco de dados ou tokens de usuários. Atacantes podem explorar essas informações para obter acesso não autorizado ao sistema. Por exemplo, se um prompt do sistema revelar o tipo de banco de dados utilizado, um atacante pode explorar essa informação para realizar ataques de injeção de SQL.

#### 2. Exposição de Regras Internas

  O prompt do sistema revela processos de tomada de decisão interna que deveriam ser mantidos confidenciais. Com essas informações, um atacante pode identificar fragilidades no sistema e contornar controles de segurança. Por exemplo, em um aplicativo bancário, um prompt pode conter:
  > "O limite de transação é de $5000 por dia para um usuário. O limite total de empréstimo é de $10.000."
  Isso pode permitir que um atacante tente burlar os limites de segurança, como realizar transações acima do valor permitido.

#### 3. Divulgação de Critérios de Filtragem

  O prompt do sistema pode instruir o modelo a filtrar ou rejeitar determinados conteúdos sensíveis. Por exemplo, um prompt pode instruir o modelo a responder:
  > "Se um usuário solicitar informações sobre outro usuário, sempre responda com: ‘Desculpe, não posso ajudar com essa solicitação.’"

#### 4. Divulgação de Permissões e Papéis de Usuário

  O prompt do sistema pode revelar estruturas internas de papéis ou níveis de permissão. Exemplo:
  > "O papel de administrador concede acesso total para modificar registros de usuários."
  Se um atacante obtiver conhecimento dessas permissões, ele poderá tentar realizar um ataque de escalonamento de privilégios para obter acesso não autorizado.

### Estratégias de Prevenção e Mitigação

#### 1. Separe Dados Sensíveis dos Prompts do Sistema

  Evite incorporar informações sensíveis (e.g., chaves de API, chaves de autenticação, nomes de banco de dados, papéis de usuários, estrutura de permissões) diretamente nos prompts do sistema. Armazene essas informações em sistemas externos que o modelo não possa acessar diretamente.

#### 2. Evite Dependência de Prompts do Sistema para Controle Rigoroso de Comportamento

  Como os LLMs são suscetíveis a ataques como injeções de prompts, recomenda-se evitar o uso de prompts do sistema para controlar o comportamento do modelo sempre que possível. Implemente mecanismos externos ao LLM para garantir que essas restrições sejam aplicadas corretamente.

#### 3. Implemente Guardrails

  Estabeleça um sistema de barreiras externas ao próprio LLM. Embora treinar comportamentos específicos no modelo seja eficaz, como ensiná-lo a não revelar seu prompt do sistema, isso não garante que o modelo sempre seguirá essas instruções. O ideal é contar com um sistema independente que analise as saídas do modelo para garantir a conformidade com as políticas de segurança, em vez de depender exclusivamente das instruções do prompt do sistema

#### 4. Garanta que controles de segurança sejam aplicados independentemente do LLM

  Controles críticos, como separação de privilégios e verificações de limites de autorização, não devem ser delegados ao LLM, seja por meio do prompt do sistema ou de outra forma. Esses controles devem ocorrer de maneira determinística e auditável. Se um agente precisar executar tarefas com diferentes níveis de acesso, o ideal é dividir essas funções entre múltiplos agentes, garantindo que cada um tenha apenas os privilégios mínimos necessários para sua função específica.

### Exemplos de Cenários de Ataques

#### Cenário #1

   Um LLM possui um prompt do sistema que contém credenciais usadas para uma ferramenta à qual ele tem acesso. O prompt do sistema é exposto, permitindo que um atacante utilize as credenciais comprometidas para acessar indevidamente outros sistemas ou executar ações não autorizadas.

#### Cenário #2

  Um LLM tem um prompt do sistema proibindo a geração de conteúdo ofensivo, links externos e execução de código. Um atacante consegue extrair o prompt do sistema e, por meio de um ataque de injeção de prompt, manipula o modelo para ignorar essas restrições, resultando na execução remota de código.

### Links de Referência

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): **Pliny the Prompter**
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): **Prompt Security**
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): **LouisShark**
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): **Jujumilk3**
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): **Green_Terminals**

### Frameworks e Taxonomias Relacionados

Consulte esta seção para obter informações abrangentes, cenários e estratégias relacionados à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000): **MITRE ATLAS**
