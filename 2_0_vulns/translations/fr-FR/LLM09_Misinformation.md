## LLM09:2025 Désinformation

### Description

La désinformation provenant des LLM représente une vulnérabilité fondamentale pour les applications s'appuyant sur ces modèles. La désinformation se produit lorsque les LLM produisent des informations fausses ou trompeuses qui semblent crédibles. Cette vulnérabilité peut entraîner des violations de la sécurité, des dommages à la réputation et une responsabilité légale.

Une des causes majeures de la désinformation est l'hallucination - lorsque le LLM génère un contenu qui semble exact mais est fabriqué. Les hallucinations se produisent lorsque les LLM comblent les lacunes de leurs données d'entraînement en utilisant des modèles statistiques, sans vraiment comprendre le contenu. En conséquence, le modèle peut produire des réponses qui semblent correctes mais sont complètement infondées. Bien que les hallucinations soient une source majeure de désinformation, elles ne sont pas la seule cause ; les biais introduits par les données d'entraînement et les informations incomplètes peuvent également y contribuer.

Une question connexe est la sur-confiance. La sur-confiance se produit lorsque les utilisateurs accordent une confiance excessive au contenu généré par les LLM, sans vérifier son exactitude. Cette sur-confiance exacerbe l'impact de la désinformation, car les utilisateurs peuvent intégrer des données incorrectes dans des décisions ou des processus critiques sans un examen adéquat.

### Exemples courants de risques

#### 1. Inexactitudes factuelles
  Le modèle produit des déclarations incorrectes, amenant les utilisateurs à prendre des décisions sur la base d'informations fausses. Par exemple, le chatbot d'Air Canada a fourni de fausses informations aux voyageurs, entraînant des perturbations opérationnelles et des complications juridiques. La compagnie aérienne a été poursuivie avec succès à la suite de cela.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))
#### 2. Affirmations non étayées
  Le modèle génère des affirmations sans fondement, ce qui peut être particulièrement nuisible dans des contextes sensibles tels que les soins de santé ou les procédures judiciaires. Par exemple, ChatGPT a fabriqué de faux cas juridiques, entraînant des problèmes importants devant les tribunaux.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))
#### 3. Fausse expertise
  Le modèle donne l'illusion de comprendre des sujets complexes, induisant les utilisateurs en erreur quant à son niveau d'expertise. Par exemple, il a été constaté que les chatbots déformaient la complexité des questions liées à la santé, suggérant une incertitude là où il n'y en a pas, ce qui a amené les utilisateurs à croire que des traitements non étayés étaient encore en débat.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))
#### 4. Génération de code non sécurisé
  Le modèle suggère des bibliothèques de code non sécurisées ou inexistantes, ce qui peut introduire des vulnérabilités lorsqu'elles sont intégrées dans des systèmes logiciels. Par exemple, les LLM proposent l'utilisation de bibliothèques tierces non sécurisées, qui, si elles sont utilisées sans vérification, entraînent des risques de sécurité.
  (ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Stratégies de prévention et d'atténuation

#### 1. Génération augmentée par récupération (RAG)
  Utilisez la génération augmentée par récupération pour améliorer la fiabilité des résultats du modèle en récupérant des informations pertinentes et vérifiées à partir de bases de données externes de confiance lors de la génération de réponses. Cela aide à atténuer le risque d'hallucinations et de désinformation.
#### 2. Fine-tuning du modèle
  Améliorez le modèle avec un fine-tuning ou des embeddings pour améliorer la qualité des résultats. Des techniques telles que le réglage efficace des paramètres (PET) et le chain-of-thought prompting peuvent aider à réduire l'incidence de la désinformation.
#### 3. Vérification croisée et supervision humaine
  Encouragez les utilisateurs à vérifier les résultats des LLM avec des sources externes fiables pour garantir l'exactitude des informations. Mettez en place des processus de supervision humaine et de vérification des faits, en particulier pour les informations critiques ou sensibles. Assurez-vous que les réviseurs humains sont correctement formés pour éviter une dépendance excessive au contenu généré par l'IA.
#### 4. Mécanismes de validation automatique
  Mettez en œuvre des outils et des processus pour valider automatiquement les résultats clés, en particulier les résultats provenant d'environnements à enjeux élevés.
#### 5. Communication des risques
  Identifiez les risques et les dommages possibles associés au contenu généré par les LLM, puis communiquez clairement ces risques et limitations aux utilisateurs, y compris le potentiel de désinformation.
#### 6. Pratiques de codage sécurisé
  Établissez des pratiques de codage sécurisé pour prévenir l'intégration de vulnérabilités dues à des suggestions de code incorrectes.
#### 7. Conception de l'interface utilisateur
  Concevez des API et des interfaces utilisateur qui encouragent l'utilisation responsable des LLM, telles que l'intégration de filtres de contenu, l'étiquetage clair du contenu généré par l'IA et l'information des utilisateurs sur les limitations de fiabilité et d'exactitude. Soyez précis quant aux limitations du domaine d'utilisation prévu.
#### 8. Formation et éducation
  Fournissez une formation complète aux utilisateurs sur les limitations des LLM, l'importance de la vérification indépendante du contenu généré et la nécessité de la pensée critique. Dans des contextes spécifiques, offrez une formation spécifique au domaine pour garantir que les utilisateurs peuvent évaluer efficacement les résultats des LLM dans leur domaine d'expertise.

### Example Attack Scenarios - Scénarios d'attaque exemplaires

#### Scenario #1
  Des attaquants expérimentent avec des assistants de codage populaires pour trouver des noms de packages fréquemment hallucinés. Une fois qu'ils identifient ces bibliothèques fréquemment suggérées mais inexistantes, ils publient des packages malveillants avec ces noms dans des dépôts largement utilisés. Les développeurs, se fiant aux suggestions de l'assistant de codage, intègrent involontairement ces packages piégés dans leur logiciel. En conséquence, les attaquants obtiennent un accès non autorisé, injectent du code malveillant ou établissent des portes dérobées, entraînant des violations de sécurité importantes et compromettant les données des utilisateurs.
#### Scenario #2
  Une entreprise fournit un chatbot pour le diagnostic médical sans garantir une précision suffisante. Le chatbot fournit de mauvaises informations, entraînant des conséquences néfastes pour les patients. En conséquence, l'entreprise est poursuivie avec succès pour dommages et intérêts. Dans ce cas, la défaillance de la sécurité et de la sûreté n'a pas nécessité un attaquant malveillant, mais est plutôt née d'une surveillance et d'une fiabilité insuffisantes du système LLM. Dans ce scénario, il n'est pas nécessaire d'avoir un attaquant actif pour que l'entreprise soit exposée à des risques de dommages à la réputation et financiers.

### Liens de référence

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

### Cadres et taxonomies connexes

Consultez cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement d'infrastructure, aux contrôles d'environnement appliqués et à d'autres bonnes pratiques.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
