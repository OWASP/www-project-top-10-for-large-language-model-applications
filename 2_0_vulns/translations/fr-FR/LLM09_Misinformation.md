## LLM09:2025 Misinformation - Désinformation

### Description

La désinformation provenant des LLM représente une vulnérabilité fondamentale pour les applications s'appuyant sur ces modèles. La désinformation se produit lorsque les LLM produisent des informations fausses ou trompeuses qui semblent crédibles. Cette vulnérabilité peut entraîner des violations de la sécurité, des dommages à la réputation et une responsabilité légale.


Misinformation from LLMs poses a core vulnerability for applications relying on these models. Misinformation occurs when LLMs produce false or misleading information that appears credible. This vulnerability can lead to security breaches, reputational damage, and legal liability.

Une des causes majeures de la désinformation est l'hallucination - lorsque le LLM génère un contenu qui semble exact mais est fabriqué. Les hallucinations se produisent lorsque les LLM comblent les lacunes de leurs données d'entraînement en utilisant des modèles statistiques, sans vraiment comprendre le contenu. En conséquence, le modèle peut produire des réponses qui semblent correctes mais sont complètement infondées. Bien que les hallucinations soient une source majeure de désinformation, elles ne sont pas la seule cause ; les biais introduits par les données d'entraînement et les informations incomplètes peuvent également contribuer.


One of the major causes of misinformation is hallucination—when the LLM generates content that seems accurate but is fabricated. Hallucinations occur when LLMs fill gaps in their training data using statistical patterns, without truly understanding the content. As a result, the model may produce answers that sound correct but are completely unfounded. While hallucinations are a major source of misinformation, they are not the only cause; biases introduced by the training data and incomplete information can also contribute.


Une question connexe est la surconfiance. La surconfiance se produit lorsque les utilisateurs accordent une confiance excessive au contenu généré par les LLM, sans vérifier son exactitude. Cette surconfiance exacerbe l'impact de la désinformation, car les utilisateurs peuvent intégrer des données incorrectes dans des décisions ou des processus critiques sans un examen adéquat.


A related issue is overreliance. Overreliance occurs when users place excessive trust in LLM-generated content, failing to verify its accuracy. This overreliance exacerbates the impact of misinformation, as users may integrate incorrect data into critical decisions or processes without adequate scrutiny.

### Common Examples of Risk - Exemples courants de risques

#### 1. Factual Inaccuracies - Inexactitudes factuelles

  Le modèle produit des déclarations incorrectes, amenant les utilisateurs à prendre des décisions sur la base d'informations fausses. Par exemple, le chatbot d'Air Canada a fourni de fausses informations aux voyageurs, entraînant des perturbations opérationnelles et des complications juridiques. La compagnie aérienne a été poursuivie avec succès à la suite de cela.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

  The model produces incorrect statements, leading users to make decisions based on false information. For example, Air Canada's chatbot provided misinformation to travelers, leading to operational disruptions and legal complications. The airline was successfully sued as a result.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

#### 2. Unsupported Claims - Affirmations non étayées

  Le modèle génère des affirmations sans fondement, ce qui peut être particulièrement nuisible dans des contextes sensibles tels que les soins de santé ou les procédures judiciaires. Par exemple, ChatGPT a fabriqué de faux cas juridiques, entraînant des problèmes importants devant les tribunaux.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

  The model generates baseless assertions, which can be especially harmful in sensitive contexts such as healthcare or legal proceedings. For example, ChatGPT fabricated fake legal cases, leading to significant issues in court.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

#### 3. Misrepresentation of Expertise - Fausse représentation de l'expertise

  Le modèle donne l'illusion de comprendre des sujets complexes, induisant les utilisateurs en erreur quant à son niveau d'expertise. Par exemple, il a été constaté que les chatbots déformaient la complexité des questions liées à la santé, suggérant une incertitude là où il n'y en a pas, ce qui a amené les utilisateurs à croire que des traitements non étayés étaient encore en débat.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

  The model gives the illusion of understanding complex topics, misleading users regarding its level of expertise. For example, chatbots have been found to misrepresent the complexity of health-related issues, suggesting uncertainty where there is none, which misled users into believing that unsupported treatments were still under debate.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

#### 4. Unsafe Code Generation - Génération de code non sécurisé

  Le modèle suggère des bibliothèques de code non sécurisées ou inexistantes, ce qui peut introduire des vulnérabilités lorsqu'elles sont intégrées dans des systèmes logiciels. Par exemple, les LLM proposent l'utilisation de bibliothèques tierces non sécurisées, qui, si elles sont utilisées sans vérification, entraînent des risques de sécurité.
  (ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

  The model suggests insecure or non-existent code libraries, which can introduce vulnerabilities when integrated into software systems. For example, LLMs propose using insecure third-party libraries, which, if trusted without verification, leads to security risks.
  (Ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation

#### 1. Retrieval-Augmented Generation (RAG) - Génération augmentée par récupération (RAG)

  Utilisez la génération augmentée par récupération pour améliorer la fiabilité des résultats du modèle en récupérant des informations pertinentes et vérifiées à partir de bases de données externes de confiance lors de la génération de réponses. Cela aide à atténuer le risque d'hallucinations et de désinformation.

  Use Retrieval-Augmented Generation to enhance the reliability of model outputs by retrieving relevant and verified information from trusted external databases during response generation. This helps mitigate the risk of hallucinations and misinformation.

#### 2. Model Fine-Tuning - Fine-tuning du modèle

  Améliorez le modèle avec un fine-tuning ou des embeddings pour améliorer la qualité des résultats. Des techniques telles que le réglage efficace des paramètres (PET) et le chain-of-thought prompting peuvent aider à réduire l'incidence de la désinformation.

  Enhance the model with fine-tuning or embeddings to improve output quality. Techniques such as parameter-efficient tuning (PET) and chain-of-thought prompting can help reduce the incidence of misinformation.

#### 3. Cross-Verification and Human Oversight - Vérification croisée et supervision humaine

  Encouragez les utilisateurs à vérifier les résultats des LLM avec des sources externes fiables pour garantir l'exactitude des informations. Mettez en place des processus de supervision humaine et de vérification des faits, en particulier pour les informations critiques ou sensibles. Assurez-vous que les réviseurs humains sont correctement formés pour éviter une dépendance excessive au contenu généré par l'IA.

  Encourage users to cross-check LLM outputs with trusted external sources to ensure the accuracy of the information. Implement human oversight and fact-checking processes, especially for critical or sensitive information. Ensure that human reviewers are properly trained to avoid overreliance on AI-generated content.

#### 4. Automatic Validation Mechanisms - Mécanismes de validation automatique

  Mettez en œuvre des outils et des processus pour valider automatiquement les résultats clés, en particulier les résultats provenant d'environnements à enjeux élevés.

  Implement tools and processes to automatically validate key outputs, especially output from high-stakes environments.

#### 5. Risk Communication - Communication des risques

  Identifiez les risques et les dommages possibles associés au contenu généré par les LLM, puis communiquez clairement ces risques et limitations aux utilisateurs, y compris le potentiel de désinformation.

  Identify the risks and possible harms associated with LLM-generated content, then clearly communicate these risks and limitations to users, including the potential for misinformation.

#### 6. Secure Coding Practices - Pratiques de codage sécurisé


  Établissez des pratiques de codage sécurisé pour prévenir l'intégration de vulnérabilités dues à des suggestions de code incorrectes.

  Establish secure coding practices to prevent the integration of vulnerabilities due to incorrect code suggestions.

#### 7. User Interface Design - Conception de l'interface utilisateur

  Concevez des API et des interfaces utilisateur qui encouragent l'utilisation responsable des LLM, telles que l'intégration de filtres de contenu, l'étiquetage clair du contenu généré par l'IA et l'information des utilisateurs sur les limitations de fiabilité et d'exactitude. Soyez précis quant aux limitations du domaine d'utilisation prévu.

  Design APIs and user interfaces that encourage responsible use of LLMs, such as integrating content filters, clearly labeling AI-generated content and informing users on limitations of reliability and accuracy. Be specific about the intended field of use limitations.

#### 8. Training and Education - Formation et éducation

  Fournissez une formation complète aux utilisateurs sur les limitations des LLM, l'importance de la vérification indépendante du contenu généré et la nécessité de la pensée critique. Dans des contextes spécifiques, offrez une formation spécifique au domaine pour garantir que les utilisateurs peuvent évaluer efficacement les résultats des LLM dans leur domaine d'expertise.

  Provide comprehensive training for users on the limitations of LLMs, the importance of independent verification of generated content, and the need for critical thinking. In specific contexts, offer domain-specific training to ensure users can effectively evaluate LLM outputs within their field of expertise.

### Example Attack Scenarios - Scénarios d'attaque exemplaires

#### Scenario #1

  Des attaquants expérimentent avec des assistants de codage populaires pour trouver des noms de packages fréquemment hallucinés. Une fois qu'ils identifient ces bibliothèques fréquemment suggérées mais inexistantes, ils publient des packages malveillants avec ces noms dans des dépôts largement utilisés. Les développeurs, se fiant aux suggestions de l'assistant de codage, intègrent involontairement ces packages piégés dans leur logiciel. En conséquence, les attaquants obtiennent un accès non autorisé, injectent du code malveillant ou établissent des portes dérobées, entraînant des violations de sécurité importantes et compromettant les données des utilisateurs.

  Attackers experiment with popular coding assistants to find commonly hallucinated package names. Once they identify these frequently suggested but nonexistent libraries, they publish malicious packages with those names to widely used repositories. Developers, relying on the coding assistant's suggestions, unknowingly integrate these poised packages into their software. As a result, the attackers gain unauthorized access, inject malicious code, or establish backdoors, leading to significant security breaches and compromising user data.

#### Scenario #2

  Une entreprise fournit un chatbot pour le diagnostic médical sans garantir une précision suffisante. Le chatbot fournit de mauvaises informations, entraînant des conséquences néfastes pour les patients. En conséquence, l'entreprise est poursuivie avec succès pour dommages et intérêts. Dans ce cas, la défaillance de la sécurité et de la sûreté n'a pas nécessité un attaquant malveillant, mais est plutôt née d'une surveillance et d'une fiabilité insuffisantes du système LLM. Dans ce scénario, il n'est pas nécessaire d'avoir un attaquant actif pour que l'entreprise soit exposée à des risques de dommages à la réputation et financiers.

  A company provides a chatbot for medical diagnosis without ensuring sufficient accuracy. The chatbot provides poor information, leading to harmful consequences for patients. As a result, the company is successfully sued for damages. In this case, the safety and security breakdown did not require a malicious attacker but instead arose from the insufficient oversight and reliability of the LLM system. In this scenario, there is no need for an active attacker for the company to be at risk of reputational and financial damage.

### Reference Links - Liens de référence

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

### Related Frameworks and Taxonomies - Cadres et taxonomies connexes

Consultez cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement d'infrastructure, aux contrôles d'environnement appliqués et à d'autres bonnes pratiques.

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
