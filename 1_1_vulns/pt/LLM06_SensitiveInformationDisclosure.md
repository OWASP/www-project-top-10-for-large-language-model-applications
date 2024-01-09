## LLM06: Divulgação de Informações Sensíveis

### Descrição

As aplicações LLM têm o potencial de revelar informações sensíveis, algoritmos proprietários ou outros detalhes confidenciais por meio de suas saídas. Isso pode resultar em acesso não autorizado a dados sensíveis, violações de propriedade intelectual, violações de privacidade e outras falhas de segurança. É importante que os consumidores de aplicações LLM estejam cientes de como interagir com segurança com os LLMs e identificar os riscos associados à entrada não intencional de dados sensíveis que podem ser posteriormente retornados pelo LLM em outras saídas.

Para mitigar esse risco, as aplicações LLM devem realizar uma sanitização adequada dos dados para evitar que os dados do usuário entrem nos dados de treinamento do modelo. Os proprietários de aplicações LLM também devem ter políticas apropriadas de Termos de Uso disponíveis para conscientizar os consumidores sobre como seus dados são processados e sobre a capacidade de optar por não incluir seus dados no modelo de treinamento.

A interação consumidor-aplicação LLM forma uma fronteira de confiança bidirecional, onde não podemos confiar inerentemente na entrada cliente->LLM ou na saída LLM->cliente. É importante observar que esta vulnerabilidade assume que certos pré-requisitos estão fora do escopo, como exercícios de modelagem de ameaças, segurança de infraestrutura e sandboxing adequado. Adicionar restrições dentro da solicitação do sistema em torno dos tipos de dados que o LLM deve retornar pode fornecer alguma mitigação contra a divulgação de informações sensíveis, mas a natureza imprevisível dos LLMs significa que tais restrições nem sempre serão respeitadas e podem ser contornadas por meio de injeção de prompt ou outros vetores.

### Exemplos Comuns de Vulnerabilidade

1. Filtragem incompleta ou inadequada de informações sensíveis nas respostas do LLM.
2. Memorização ou sobreajuste (overfitting) de dados sensíveis no processo de treinamento do LLM.
3. Divulgação não intencional de informações confidenciais devido à interpretação inadequada do LLM, falta de métodos de limpeza de dados ou erros.

### Estratégias de Prevenção e Mitigação

1. Integre técnicas adequadas de sanitização e limpeza de dados para evitar que os dados do usuário entrem nos dados de treinamento do modelo.
2. Implemente métodos robustos de validação e sanitização de entrada para identificar e filtrar inputs potencialmente maliciosos e prevenir que o modelo seja envenenado.
3. Ao enriquecer o modelo com dados e se [ajustar finamente](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Definitions) um modelo (ou seja, alimentar o modelo antes ou durante a implantação):
   1. Qualquer informação considerada sensível nos dados de ajuste fino tem o potencial de ser revelada a um usuário. Portanto, aplique a regra do menor privilégio e não treine o modelo em informações que o usuário de mais alto privilégio pode acessar e que podem ser exibidas a um usuário de menor privilégio.
   2. O acesso a fontes de dados externas (orquestação de dados em tempo de execução) deve ser limitado.
   3. Aplique métodos rígidos de controle de acesso a fontes de dados externas e uma abordagem rigorosa para manter uma cadeia de suprimentos segura.

### Cenários de Ataque Exemplo

1. O usuário legítimo A, sem suspeitas, é exposto a certos dados de outros usuários por meio do LLM ao interagir com a aplicação LLM de maneira não maliciosa.
2. O usuário A direciona um conjunto bem elaborado de prompts para burlar filtros de entrada e sanitização do LLM, fazendo com que ele revele informações sensíveis (PII) sobre outros usuários da aplicação.
3. Dados pessoais, como PII, vazam para o modelo por meio de dados de treinamento, devido à negligência do próprio usuário ou da aplicação LLM. Esse cenário poderia aumentar o risco e a probabilidade dos cenários 1 ou 2 acima.

### Links de Referência

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use) **Cohere**
4. [A threat modeling example](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
5. [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/): **OWASP AI Security & Privacy Guide**
6. [Ensuring the Security of Large Language Models](https://www.experts-exchange.com/articles/38220/Ensuring-the-Security-of-Large-Language-Models-Strategies-and-Best-Practices.html): **Experts Exchange**
