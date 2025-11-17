## LLM09:2025 Desinformação

### Descrição

A desinformação gerada por LLMs representa uma vulnerabilidade central para aplicações que dependem desses modelos. A desinformação ocorre quando os LLMs produzem informações falsas ou enganosas que parecem credíveis. Essa vulnerabilidade pode levar a violações de segurança, danos reputacionais e responsabilidades legais.

Uma das principais causas da desinformação é a alucinação—quando o LLM gera conteúdo que parece preciso, mas é fabricado. Alucinações ocorrem quando os LLMs preenchem lacunas em seus dados de treinamento usando padrões estatísticos, sem realmente entender o conteúdo. Isso faz com que o modelo gere respostas que parecem corretas, mas não têm base real. Embora as alucinações sejam uma fonte significativa de desinformação, não são a única causa; vieses introduzidos pelos dados de treinamento e informações incompletas também podem contribuir.

Um problema relacionado é a dependência excessiva. Isso ocorre quando os usuários confiam excessivamente no conteúdo gerado pelo LLM, falhando em verificar sua precisão. Essa dependência amplifica os riscos da desinformação, pois os usuários podem adotar informações erradas sem verificá-las, comprometendo decisões e processos críticos.

### Exemplos Comuns de Risco

#### 1. Inacurácias Fatuais

  O modelo produz declarações incorretas, levando os usuários a tomar decisões com base em informações falsas. Por exemplo, o *chatbot* da Air Canada forneceu informações incorretas aos viajantes, levando a interrupções operacionais e complicações legais. A companhia aérea foi processada com sucesso como resultado.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

#### 2. Afirmativas Sem Suporte

  O modelo gera declarações infundadas, especialmente prejudiciais em contextos sensíveis, como saúde ou processos legais. Por exemplo, o ChatGPT fabricou casos jurídicos falsos, resultando em problemas significativos no tribunal.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

#### 3. Representação Errada de Especialização

  O modelo cria a ilusão de entender tópicos complexos, enganando os usuários quanto ao seu nível de especialização. Por exemplo, Foi identificado que *chatbots* distorcem a complexidade de questões de saúde, sugerindo falsamente que tratamentos não comprovados ainda estão em debate.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

#### 4. Geração de Código Inseguro

  O modelo pode recomendar bibliotecas de código inseguras ou inexistentes, levando à introdução de vulnerabilidades caso sejam incorporadas em sistemas sem validação. Por exemplo, LLMs propuseram bibliotecas de terceiros inseguras que, se confiadas sem verificação, levam a riscos de segurança.
  (Ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Estratégias de Prevenção e Mitigação

#### 1. Geração Aumentada por Recuperação (RAG)

  Utilize a Geração Aumentada por Recuperação (RAG) para aumentar a confiabilidade das respostas do modelo, recuperando informações relevantes e verificadas de bancos de dados externos confiáveis durante a geração de respostas. Isso ajuda a mitigar o risco de alucinações e desinformação.

#### 2. Ajuste Fino do Modelo

  Aprimore o modelo por meio de ajuste fino ou otimização de *embeddings* para aumentar a precisão das respostas. Técnicas como ajuste eficiente de parâmetros (PET) e prompting de cadeia de raciocínio podem reduzir a incidência de desinformação.

#### 3. Verificação Cruzada e Supervisão Humana

  Instrua os usuários a validar as respostas dos LLMs comparando-as com fontes externas confiáveis. Implemente processos de supervisão humana, especialmente para informações críticas ou sensíveis. Garanta que os revisores humanos sejam devidamente treinados para evitar dependência excessiva de conteúdo gerado por IA.

#### 4. Mecanismos Automáticos de Validação

  Implemente ferramentas e processos para validar automaticamente saídas críticas, especialmente em ambientes de alto risco.

#### 5. Comunicação de Riscos

  Avalie e comunique claramente os riscos do conteúdo gerado por LLMs, alertando os usuários sobre possíveis imprecisões, incluindo o potencial para desinformação.

#### 6. Práticas de Codificação Segura

  Aplique práticas de codificação seguras para evitar que vulnerabilidades sejam introduzidas por sugestões incorretas do modelo.

#### 7. Design da Interface do Usuário

  Projete APIs e interfaces de usuário que incentivem o uso responsável de LLMs, como integração de filtros de conteúdo, rotulagem clara de conteúdo gerado por IA e informações sobre limitações de confiabilidade e precisão.

#### 8. Treinamento e Educação

  Forneça treinamento abrangente sobre as limitações dos LLMs, a importância da verificação independente de conteúdo gerado e a necessidade de pensamento crítico. Em contextos específicos, forneça treinamento especializado para avaliar eficazmente as saídas dos LLMs.

### Exemplos de Cenários de Ataques

#### Cenário #1

  Atacantes analisam assistentes de codificação para identificar nomes de pacotes fictícios sugeridos com frequência. Após identificar esses pacotes inexistentes sugeridos pelo assistente, eles publicam pacotes maliciosos com os mesmos nomes em repositórios amplamente usados. Desenvolvedores, confiando nas sugestões do assistente, integram esses pacotes comprometidos, resultando em violações de segurança e comprometimento de dados.

#### Cenário #2

  Uma empresa lança um *chatbot* para diagnósticos médicos sem validação adequada da precisão das respostas. O *chatbot* fornece informações incorretas, resultando em consequências prejudiciais para pacientes. Como resultado, a empresa é processada por danos. Nesse caso, a falha de segurança e confiabilidade do sistema LLM expôs a empresa a riscos reputacionais e financeiros, mesmo sem a presença de um atacante ativo.

### Links de Referência

1. [AI Chatbots as Health Information Sources: Misrepresentation of Expertise](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [Air Canada Chatbot Misinformation: What Travellers Should Know](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT Fake Legal Cases: Generative AI Hallucinations](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
6. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [Diving Deeper into AI Package Hallucinations](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [How Secure is Code Generated by ChatGPT?](https://arxiv.org/abs/2304.09655): **Arvix**
9. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [A Framework for Exploring the Consequences of AI-Mediated Enterprise Knowledge](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**

### Frameworks e Taxonomias Relacionados

Consulte esta seção para obter informações abrangentes, cenários e estratégias relacionadas à implantação de infraestrutura, controles no ambiente aplicado e outras melhores práticas.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048): **MITRE ATLAS**
