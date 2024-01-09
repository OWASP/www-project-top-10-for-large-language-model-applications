## LLM09: Dependência Excessiva

### Descrição

A  Dependência Excessiva pode ocorrer quando um LLM produz informações errôneas e as fornece de maneira autoritária. Embora os LLMs possam produzir conteúdo criativo e informativo, também podem gerar conteúdo factualmente incorreto, inapropriado ou inseguro. Isso é chamado de alucinação ou confabulação. Quando pessoas ou sistemas confiam nessas informações sem supervisão ou confirmação, pode resultar em violação de segurança, desinformação, má comunicação, questões legais e danos à reputação.

O código-fonte gerado pelo LLM pode introduzir vulnerabilidades de segurança não percebidas. Isso representa um risco significativo para a segurança operacional de aplicativos. Esses riscos destacam a importância de processos rigorosos de revisão, com:

- Supervisão
- Mecanismos contínuos de validação
- Avisos sobre riscos

### Exemplos Comuns desta Vulnerabilidade

1. LLM fornece informações imprecisas como resposta, declarando-as de maneira a sugerir alta autoridade. O sistema como um todo é projetado sem verificações e equilíbrios adequados para lidar com isso, e as informações enganam o usuário de uma maneira que leva a danos.
2. LLM sugere código inseguro ou com falhas, levando a vulnerabilidades quando incorporado a um sistema de software sem a devida supervisão ou verificação.

### Estratégias de Prevenção e Mitigação

1. Monitore e revise regularmente as saídas do LLM. Use técnicas de auto consistência ou votação para filtrar texto inconsistente. Comparar múltiplas respostas do modelo para um único prompt pode ajudar a julgar melhor a qualidade e consistência da saída.
2. Verifique a saída do LLM com fontes externas confiáveis. Essa camada adicional de validação pode ajudar a garantir que as informações fornecidas pelo modelo sejam precisas e confiáveis.
3. Aprimore o modelo com ajuste fino ou embeddings para melhorar a qualidade da saída. Modelos pré-treinados genéricos têm mais chances de produzir informações imprecisas em comparação com modelos ajustados em um domínio específico. Técnicas como engenharia de prompts, ajuste eficiente de parâmetros (PEFT), ajuste total do modelo e prompts encadeados de pensamento podem ser empregadas para esse fim.
4. Implemente mecanismos automáticos de validação que possam verificar a saída gerada em relação a fatos ou dados conhecidos. Isso pode fornecer uma camada adicional de segurança e mitigar os riscos associados a alucinações.
5. Divida tarefas complexas em subtarefas gerenciáveis e atribua-as a diferentes agentes. Isso não apenas ajuda no gerenciamento da complexidade, mas também reduz as chances de alucinações, pois cada agente pode ser responsabilizado por uma tarefa menor.
6. Comunique claramente os riscos e limitações associados ao uso de LLMs. Isso inclui a possibilidade de imprecisões nas informações e outros riscos. Uma comunicação eficaz de riscos pode preparar os usuários para problemas potenciais e ajudá-los a tomar decisões informadas.
7. Construa APIs e interfaces de usuário que incentivem o uso responsável e seguro de LLMs. Isso pode envolver medidas como filtros de conteúdo, avisos ao usuário sobre imprecisões potenciais e rotulagem clara de conteúdo gerado por IA.
8. Ao usar LLMs em ambientes de desenvolvimento, estabeleça práticas e diretrizes seguras de codificação para evitar a integração de possíveis vulnerabilidades.

### Exemplos de Cenários de Ataque

1. Uma organização de notícias utiliza intensamente um LLM para gerar artigos. Um ator malicioso explora essa sobrecarga, alimentando informações enganosas ao LLM e causando a propagação de desinformação.
2. A IA inadvertidamente plagiariza um conteúdo, levando a problemas de direitos autorais e diminuindo a confiança na organização.
3. Uma equipe de desenvolvimento de software utiliza um sistema LLM para acelerar o processo de codificação. A sobrecarga nas sugestões do LLM introduz vulnerabilidades de segurança na aplicação devido a configurações padrão inseguras ou recomendações inconsistentes com práticas seguras de codificação.
4. Uma empresa de desenvolvimento de software usa um LLM para auxiliar os desenvolvedores. O LLM sugere uma biblioteca ou pacote de código inexistente, e um desenvolvedor, confiando na IA, integra inadvertidamente um pacote malicioso no software da empresa. Isso destaca a importância de verificar as sugestões do LLM, especialmente ao envolver código ou bibliotecas de terceiros.
### Links de Referência

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk): **Vulcan.io**
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
