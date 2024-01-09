## LLM05: Vulnerabilidades na Cadeia de Suprimentos

### Descrição

A cadeia de suprimentos em LLMs pode ser vulnerável, impactando a integridade dos dados de treinamento, modelos de aprendizado de máquina e plataformas de implantação. Essas vulnerabilidades podem resultar em resultados tendenciosos, violações de segurança ou até mesmo falhas completas no sistema. Tradicionalmente, as vulnerabilidades são focadas em componentes de software, mas o Aprendizado de Máquina estende isso com modelos pré-treinados e dados de treinamento fornecidos por terceiros suscetíveis a ataques de manipulação e envenenamento.

Finalmente, as extensões de Plugin do LLM podem trazer suas próprias vulnerabilidades. Essas são descritas em [LLM07 - Design Inseguro de Plugins](InsecurePluginDesign.md), que aborda a redação de Plugins do LLM e fornece informações úteis para avaliar plugins de terceiros.

### Exemplos Comuns de Vulnerabilidade

1. Vulnerabilidades tradicionais em pacotes de terceiros, incluindo componentes desatualizados ou obsoletos.
2. Uso de um modelo pré-treinado vulnerável para ajuste fino.
3. Uso de dados envenenados provenientes de contribuições de grupos (crowdsourcing) para treinamento.
4. Uso de modelos desatualizados ou obsoletos que não são mais mantidos, resultando em problemas de segurança.
5. Termos e Condições (T&Cs) e políticas de privacidade não claros dos operadores do modelo levam ao uso dos dados sensíveis do aplicativo para o treinamento do modelo e subsequente exposição de informações sensíveis. Isso também pode se aplicar a riscos decorrentes do uso de material protegido por direitos autorais pelo fornecedor do modelo.

### Estratégias de Prevenção e Mitigação

1. Avalie cuidadosamente as fontes e fornecedores de dados, incluindo T&Cs e suas políticas de privacidade, usando apenas fornecedores confiáveis. Certifique-se de que exista segurança adequada e auditada de forma independente e que as políticas dos operadores do modelo estejam alinhadas com suas políticas de proteção de dados, ou seja, seus dados não são usados para treinar seus modelos; da mesma forma, busque garantias e mitigação legal contra o uso de material protegido por direitos autorais pelos mantenedores do modelo.
2. Use apenas plugins confiáveis e certifique-se de que foram testados para atender aos requisitos do seu aplicativo. O Design Inseguro de Plugins do LLM fornece informações sobre os aspectos do LLM do design inseguro de plugins que você deve testar para mitigar os riscos do uso de plugins de terceiros.
3. Compreenda e aplique as mitigações encontradas no [A06:2021 – Componentes Vulneráveis e Desatualizados](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) do OWASP Top Ten. Isso inclui a verificação, gerenciamento e atualização de componentes com vulnerabilidades. Para ambientes de desenvolvimento com acesso a dados sensíveis, aplique esses controles também.
4. Mantenha um inventário atualizado de componentes usando um Mapeamento de Componentes de Software (SBOM) para garantir que você tenha um inventário atualizado, preciso e assinado, prevenindo manipulações em pacotes implantados. SBOMs podem ser usados para detectar e alertar sobre novas vulnerabilidades rapidamente.
5. No momento da redação, SBOMs não cobrem modelos, seus artefatos e conjuntos de dados. Se a sua aplicação LLM usar seu próprio modelo, você deve usar as melhores práticas de MLOps e plataformas que ofereçam repositórios seguros de modelos com rastreamento de dados, modelos e experimentos.
6. Você também deve usar a assinatura de modelos e código ao usar modelos e fornecedores externos.
7. Testes de detecção de anomalias e robustez adversarial em modelos e dados fornecidos podem ajudar a detectar manipulações e envenenamento, como discutido em [Envenenamento de Dados de Treinamento](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/Training_Data_Poisoning.md); idealmente, isso deve fazer parte dos pipelines de MLOps; no entanto, essas são técnicas emergentes e podem ser mais fáceis de implementar como parte de exercícios de red teaming.
8. Implemente monitoramento suficiente para cobrir a verificação de vulnerabilidades em componentes e ambientes, o uso de plugins não autorizados e componentes desatualizados, incluindo o modelo e seus artefatos.
9. Implemente uma política de atualização para mitigar componentes vulneráveis ou desatualizados. Certifique-se de que o aplicativo dependa de uma versão mantida das APIs e do modelo subjacente.
10. Revise regularmente e audite a Segurança e o Acesso dos fornecedores, garantindo que não haja alterações em sua postura de segurança ou T&Cs.

### Cenários de Ataque Exemplo

1. Um atacante explora uma biblioteca Python vulnerável para comprometer um sistema. Isso ocorreu no primeiro vazamento de dados da Open AI.
2. Um atacante fornece um plugin do LLM para pesquisar voos, gerando links falsos que levam a fraudar usuários.
3. Um atacante explora o registro de pacotes PyPi para enganar desenvolvedores de modelos a baixar um pacote comprometido e extrair dados ou aumentar os privilégios em um ambiente de desenvolvimento de modelos. Isso foi um ataque real.
4. Um atacante envenena um modelo pré-treinado publicamente disponível, especializado em análise econômica e pesquisa social, para criar um backdoor que gera desinformação e notícias falsas. Eles o implantam em um mercado de modelos (por exemplo, Hugging Face) para que vítimas o usem.
5. Um atacante envenena conjuntos de dados publicamente disponíveis para ajudar a criar um backdoor ao ajustar modelos. O backdoor favorece sutilmente certas empresas em diferentes mercados.
6. Um funcionário comprometido de um fornecedor (desenvolvedor terceirizado, empresa de hospedagem, etc.) exfiltra dados, modelo ou código, roubando propriedade intelectual
7. Um operador LLM altera seus T&Cs e Política de Privacidade para exigir uma recusa explícita de usar dados de aplicativos para treinamento de modelo, levando à memorização de dados confidenciais.

### Links de Referência

1. [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): **Security Week**
2. [Plugin review process](https://platform.openai.com/docs/plugins/review) **OpenAI**
3. [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): **Pytorch**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Army looking at the possibility of 'AI BOMs](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/): **Defense Scoop**
6. [Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): **Microsoft**
7. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/): **MITRE ATLAS**
8. [Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples](https://arxiv.org/pdf/1605.07277.pdf): **Arxiv White Paper**
9. [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733): **Arxiv White Paper**
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): **MITRE ATLAS**
