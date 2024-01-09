## LLM10: Model Theft

### Descrição

Esta entrada refere-se ao acesso não autorizado e à exfiltração de modelos LLM por atores maliciosos ou APTs. Isso ocorre quando modelos LLM proprietários (sendo propriedade intelectual valiosa) são comprometidos, fisicamente roubados, copiados ou quando pesos e parâmetros são extraídos para criar um equivalente funcional. O impacto do roubo de modelos LLM pode incluir perda econômica e de reputação da marca, erosão da vantagem competitiva, uso não autorizado do modelo ou acesso não autorizado a informações sensíveis contidas no modelo.

O roubo de LLMs representa uma preocupação significativa de segurança à medida que os modelos de linguagem se tornam cada vez mais poderosos e prevalentes. Organizações e pesquisadores devem priorizar medidas de segurança robustas para proteger seus modelos LLM, garantindo a confidencialidade e integridade de sua propriedade intelectual. A adoção de um framework de segurança abrangente que inclua controles de acesso, criptografia e monitoramento contínuo é crucial para mitigar os riscos associados ao roubo de modelos LLM e proteger os interesses de indivíduos e organizações que dependem de LLMs.

### Exemplos Comuns desta Vulnerabilidade

1. Um atacante explora uma vulnerabilidade na infraestrutura de uma empresa para obter acesso não autorizado ao repositório de modelos LLM por meio de configurações inadequadas na rede ou nas configurações de segurança da aplicação.
2. Um cenário de ameaça interna em que um funcionário descontente vaza modelos ou artefatos relacionados.
3. Um atacante consulta a API do modelo usando inputs cuidadosamente elaborados e técnicas de injeção de prompt para coletar um número suficiente de saídas para criar um modelo sombra.
4. Um atacante malicioso consegue contornar técnicas de filtragem de entrada do LLM para realizar um ataque de canal lateral e, finalmente, extrair pesos do modelo e informações de arquitetura para um recurso controlado remotamente.
5. O vetor de ataque para extração de modelo envolve consultar o LLM com um grande número de prompts sobre um tópico específico. As saídas do LLM podem ser usadas para ajustar outro modelo. No entanto, alguns pontos importantes sobre esse ataque são:
   - O atacante deve gerar um grande número de prompts direcionados. Se os prompts não forem específicos o suficiente, as saídas do LLM serão inúteis.
   - As saídas dos LLMs podem às vezes conter respostas alucinadas, o que significa que o atacante pode não ser capaz de extrair o modelo inteiro, já que algumas saídas podem ser sem sentido.
     - Não é possível replicar um LLM 100% por meio da extração de modelo. No entanto, o atacante será capaz de replicar parcialmente um modelo.
6. O vetor de ataque para **_replicação funcional do modelo_** envolve o uso do modelo-alvo por meio de prompts para gerar dados sintéticos de treinamento (uma abordagem chamada "autoinstrução") para então usá-lo e ajustar outro modelo fundamental para produzir um equivalente funcional. Isso contorna as limitações da extração baseada em consultas tradicional usada no Exemplo 5 e foi usado com sucesso em pesquisas sobre o uso de um LLM para treinar outro LLM. Embora, no contexto dessa pesquisa, a replicação do modelo não seja um ataque. A abordagem poderia ser usada por um atacante para replicar um modelo proprietário com uma API pública.

O uso de um modelo roubado, como modelo sombra, pode ser usado para realizar ataques adversários, incluindo acesso não autorizado a informações sensíveis contidas no modelo ou experimentar com inputs adversários para realizar injeções avançadas de prompt.

### Estratégias de Prevenção e Mitigação

1. Implementar controles de acesso robustos (por exemplo, RBAC e o princípio do menor privilégio) e mecanismos de autenticação sólidos para limitar o acesso não autorizado a repositórios de modelos LLM e ambientes de treinamento.
   - Isso é especialmente válido para os três primeiros exemplos comuns, que podem causar essa vulnerabilidade devido a ameaças internas, configuração inadequada e/ou controles de segurança fracos sobre a infraestrutura que abriga modelos LLM, pesos e arquitetura nos quais um ator malicioso poderia infiltrar-se de dentro ou fora do ambiente.
   - O rastreamento, verificação e vulnerabilidades de dependência de gerenciamento de fornecedores são tópicos importantes para prevenir exploração de ataques à cadeia de suprimentos.
2. Restringir o acesso do LLM a recursos de rede, serviços internos e APIs.
   - Isso é especialmente válido para todos os exemplos comuns, pois cobre riscos e ameaças internas, mas também controla o que a aplicação LLM "_tem acesso_" e, assim, pode ser um mecanismo ou etapa de prevenção para evitar ataques de canal lateral.
3. Usar um Inventário ou Registro Centralizado de Modelos de ML para modelos usados em produção. Ter um registro centralizado de modelos impede o acesso não autorizado a modelos de ML por meio de controles de acesso, autenticação e capacidade de monitoramento/registro, que são bases sólidas para a governança. Ter um repositório centralizado também é benéfico para coletar dados sobre algoritmos usados pelos modelos para fins de conformidade, avaliações de risco e mitigação de riscos.
4. Monitorar regularmente e auditar logs de acesso e atividades relacionadas a repositórios de modelos LLM para detectar e responder prontamente a qualquer comportamento suspeito ou não autorizado.
5. Automatizar implementações MLOps com fluxos de trabalho de governança, rastreamento e aprovação para reforçar controles de acesso e implementação dentro da infraestrutura.
6. Implementar controles e estratégias de mitigação para reduzir o risco de técnicas de injeção de prompt causarem ataques de canal lateral.
7. Limitar a taxa de chamadas de API quando aplicável e/ou implementar filtros para reduzir o risco de exfiltração de dados das aplicações LLM, ou implementar técnicas para detectar (por exemplo, DLP) atividade de extração de outros sistemas de monitoramento.
8. Implementar treinamento de robustez adversária para ajudar a detectar consultas de extração e reforçar medidas de segurança física.
9. Implementar um framework de marca d'água nas etapas de incorporação e detecção do ciclo de vida de um LLM.

### Exemplos de Cenários de Ataque

1. Um atacante explora uma vulnerabilidade na infraestrutura de uma empresa para obter acesso não autorizado ao repositório de modelos LLM. O atacante procede a exfiltrar modelos LLM valiosos e os usa para lançar um serviço de processamento de linguagem concorrente ou extrair informações sensíveis, causando danos financeiros significativos à empresa original.
2. Um funcionário descontente vaza modelos ou artefatos relacionados. A exposição pública desse cenário aumenta o conhecimento dos atacantes para ataques adversários de caixa cinza ou, alternativamente, rouba diretamente a propriedade disponível.
3. Um atacante consulta a API com inputs cuidadosamente selecionados e coleta um número suficiente de saídas para criar um modelo sombra.
4. Uma falha de controle de segurança está presente na cadeia de suprimentos e leva a vazamentos de dados de informações proprietárias do modelo.
5. Um atacante malicioso contorna as técnicas de filtragem de entrada e preâmbulos do LLM para realizar um ataque de canal lateral e recuperar informações do modelo para um recurso controlado remotamente sob seu controle.

### Links de Referência

1. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse): **The Verge**
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
3. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [D-DAE: Defense-Penetrating Model Extraction Attacks:](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c): **Computer.org**
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
7. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
8. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
