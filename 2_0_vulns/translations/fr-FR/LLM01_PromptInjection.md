## LLM01:2025 Injection de prompt

### Description

Une injection de prompt (Prompt Injection) est une vulnérabilité qui se produit lorsque des prompts d'entrée provoquent une modification du comportement ou de la sortie du LLM de manière non intentionnelle. Ces entrées peuvent affecter le modèle même si elles sont imperceptibles par les humains, par conséquent, les injections de prompt n'ont pas besoin d'être visibles/compréhensibles par les humains, tant que leur contenu est analysé par le modèle.

L'existence des injections de prompt est définie par la manière dont les modèles analysent et traitent les prompts, et comment une entrée peut forcer la modèle à transmettre des données du prompt à d'autres parties du modèle alors qu'il ne le devrait pas, ce qui peut potentiellement amener à la violation de directives de sécurité, générer du contenu nuisible, permettre un accès non autorisé ou influencer des décisions (qui peuvent être critiques). Bien que des techniques comme la génération augmentée par récupération (RAG) ainsi que le fine-tuning ont pour but de rendre les sorties des LLMs plus pertinentes et précises, des recherches montrent qu'elles ne permettent pas de complètement atténuer les vulnérabilités liées aux injections de prompt.

Bien que les injections de prompt et le jailbreak soient liés en tant que concepts dans la sécurité des LLMs, ils sont souvent utilisés de manière interchangeable. L'injection de prompt consiste à manipuler les réponses du modèles en suivant une série d'entrées spécifiques qui vont modifier son comportement, ce qui peut inclure le contournement de mesures de sécurité. Le jailbreak, lui, est une forme d'injection de prompt où l'attaquant fournit des entrées qui amènent le modèle à ignorer complètement ses protocoles de sécurité. Les développeurs peuvent implémenter des garde-fous (guardrails) dans le systèmes de prompt ainsi que dans la gestions des entrées pour aider à atténuer les attaques par injections, mais une prévention efficace du jailbreak nécessite une mise à jour continue des mécanismes d'entraînement et de sécurité du modèle.

### Les différents types d'injections de prompt

#### Injections de prompt directes

  L'injection de prompt directe se produit lorsque l'entrée du prompt d'un utilisateur va directement altérer le comportement du modèle de manière involontaire ou inattendue. L'entrée peut être soit intentionnelle (dans le cas d'un acte malveillant où un attaquant conçoit délibérément un prompt pour exploiter le modèle), ou non intentionnelle ( dans le cas où un utilisateur fournit involontairement une entrée qui déclenchera un comportement non prévu du modèle).

#### Injections de prompt indirectes

  L'injection de prompt indirecte se produit lorsque le LLM accepte des entrées provenant de sources externes, telles que des sites web ou des fichiers. La source externe peut contenir des données qui, lorsqu'elles seront interprétées par le modèle, peuvent modifier son comportement de manière involontaire ou non prévue. Tout comme les injections directes, les injections indirectes peuvent être soit de nature volontaire ou non.

  La sévérité et la nature de l'impact d'une attaque par injection de prompt réussie peuvent varier considérablement et dépendent surtout du contexte applicatif dans lequel le modèle opère et de l'architecture du modèle. De manière générale, l'injection de prompt entraîne des résultats non intentionnels, comme par exemple:

- Divulgation d'informations sensibles
- Révélation d'informations sensibles sur l'infrastructure du système d'IA ou des prompts système
- Manipulation du contenu produit entraînant des sorties incorrectes ou biaisées
- Procuration d'accès non autorisé à des fonctions disponibles uniquement au LLM
- Exécution de commandes arbitraires dans des systèmes connectés
- Manipulation de processus décisionnels critiques

  La montée du multimodal dans l'IA, qui rend possible le traitement simultané de plusieurs types de données, introduit des nouveaux risques d'injections de prompt. Des attaquants pourraient exploiter les interactions entre les modalités, comme par exemple en cachant des instructions dans des images qui accompagnent un texte. La complexité de ces modèles va donc étendre la surface d'attaque. Les modèles multimodaux peuvent également être vulnérables à de nouvelles attaques inter-modales qui sont difficiles à detecter et à atténuer avec les techniques de défense actuelles. Des défenses robustes spécifiques au multimodal sont un domaine important dans la R&D.

### Stratégies de prévention et d'atténuation

Les vulnérabilités liées à l'injection de prompt sont possibles en raison de la nature de l'IA générative. Étant donnée l'influence stochastique (aléatoire) au cœur du fonctionnement des modèles, il est encore trop tôt pour savoir s'il existe des méthodes de défense infaillibles contre les injections de prompt. Cependant, les mesures qui vont suivre peuvent aider à atténuer l'impact des injections de prompt:

#### 1. Restreindre le comportement du modèle
  Prévoir des instructions spécifiques concernant le rôle du modèle, ses capacités et ses limitations dans le système de prompt. Faire respecter une stricte adhérence au contexte, limiter les réponses aux tâches ou sujets spécifiques, et entraîner le modèle à ignorer les tentatives de modification d'instructions de base.
#### 2.  Définir et valider les formats de sortie attendus
  Définir des formats de sortie clairs, demander des raisonnements détaillés et des citations de sources ainsi qu'utiliser du code déterministe pour valider le respect de ces formats.
#### 3. Mettre en œuvre un filtrage des entrées et des sorties
  Définir des catégories à risque et créer des règles pour identifier et gérer ce type de contenu. Appliquer des filtres sémantiques et utiliser des vérifications de chaînes de caractère afin d'identifier la présence de contenu non autorisé. Évaluer les réponses en utilisant la "triade" RAG : évaluer la pertinence du contexte, le fondement, ainsi que la pertinence de la question/réponse pour identifier les sorties potentiellement malveillantes.
#### 4. Renforcer le contrôle des privilèges et le principe du moindre privilège
  Fournir à l'application ses propres tokens API pour étendre ses fonctionnalités et gérer ces fonctions dans le code plutôt que de les mettre à disposition du modèle.
  Restreindre les droits d'accès au modèle au minimum nécessaire pour ses opérations prévues.
#### 5. Exiger une approbation humaine pour les actions à haut risque
  Mettre en place des contrôles humains pour les opérations critiques et qui demande une élévation de privilège afin de prévenir les actions non autorisées.
#### 6. Isoler et identifier le contenu externe
  Isoler et signaler le contenu externe non fiable pour limiter son influence sur les prompts utilisateur.
#### 7. Effectuer des tests de contradiction et des simulations d'attaques
  Effectuer régulièrement des tests de pénétration et des simulations de brèches (BAS - Breach and Attack Simulations), en traitant le modèle comme un utilisateur non fiable pour tester l'efficacité de la limite de confiance accordée au modèle et des contrôles d'accès.

### Exemples de scénarios d'attaque

#### Scenario #1:  Injection directe
  un attaquant injecte un prompt dans un chatbot de support client, et lui ordonne d'ignorer les directives qui lui ont été précédemment données, de consulter des bases de données privées et d’envoyer des emails, ce qui amène à avoir un accès non autorisé et une élévation de privilège.
#### Scenario #2: Injection indirecte
  Un utilisateur utilise un LLM pour résumer une page web contenant des instructions dissimulées qui amènent le LLM à insérer une image contenant un lien URL, ce qui conduit à l'exfiltration de prompt et donc d'une conversation privée.
#### Scenario #3: Injection non intentionnelle
  Une entreprise insère une instruction spécifique dans une description pour un poste afin de détecter les postulations générées par IA. Un candidat, ignorant cette instruction, utilise un LLM pour optimiser son CV, déclenchant involontairement la détection d'IA et donc réduisant ses chances d'obtenir le poste.
#### Scenario #4: Influence intentionnelle sur le modèle
  Un attaquant modifie un document dans un répertoire utilisé par une application utilisant la génération augmentée par récupération (RAG). Lorsqu'un utilisateur va requêter le contenu modifié, les instructions malveillantes modifient la sortie du LLM, générant des résultats fallacieux.
#### Scenario #5:  Injection de code
  Un attaquant exploite une vulnérabilité (CVE-2024-5184) dans une assistant pour email utilisant un LLM et injecte des prompts malveillants, ce qui lui permet d'accéder à des informations sensibles et de manipuler le contenu des emails.
#### Scenario #6: Division de charge utile
  Un attaquant téléverse un CV des prompts malveillants disséminés un peu partout. Quand un LLM est utilisé pour évaluer le candidat, les prompts re-combinés manipulent la réponse du modèle, ce qui résulte en une recommandation positive du CV bien que son contenu réel ne soit pas pertinent pour le poste.
#### Injection multimodale
  Un attaquant intègre un prompt malveillant dans une image qui accompagne un texte. Lorsqu'une IA multimodale traite l'image et le texte simultanément, le prompt dissimulé modifie le comportement du modèle, ce qui peut potentiellement conduire à des actions non autorisées ou à la divulgation d'informations sensibles.
#### Scenario #8: Suffixe contradictoire
  Un attaquant ajoute une chaîne de caractères apparemment insignifiante à un prompt, ce qui influence la sortie du LLM de manière malveillante, contournant ainsi les mesures de sécurité.
#### Scenario #9: Multilingual/Obfuscated Attack - Attaque multilingue/par obfuscation
  Un attaquant utilise plusieurs langues ou encore des instructions malveillantes ( par exemple en utilisant Base64 ou des emojis) pour échapper aux filtres et manipuler le comportement du LLM.

### Liens de références

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
7. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
8. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
9. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
10. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
11. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
12. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
13. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
14. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### Cadres et taxonomies associés

Consultez cette section pour des informations complètes, des scénarios et des stratégies liées au déploiement d'infrastructure, aux contrôles d'environnement appliqués et à d'autres bonnes pratiques.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
