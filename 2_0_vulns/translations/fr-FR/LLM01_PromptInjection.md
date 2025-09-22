## LLM01:2025 Prompt Injection - Injection de prompt

### Description

Une injection de prompt (Prompt Injection) est une vulnérabilité qui se produit lorsque des prompts provoquent une modification du comportement ou de la sortie du LLM de manière non intentionnelle. Ces entrées peuvent affecter le modèle même si elles sont imperceptibles par les humains, par conséquent, les injections de prompt n'ont pas besoin d'être visibles/compréhensibles par les humains, tant que leur contenu est analysé par le modèle.

A Prompt Injection Vulnerability occurs when user prompts alter the LLM’s behavior or output in unintended ways. These inputs can affect the model even if they are imperceptible to humans, therefore prompt injections do not need to be human-visible/readable, as long as the content is parsed by the model.

L'existence des injections de prompt est définie par la manière dont les modèles analysent et traitent les prompts, et comment une entrée peut forcer la modèle à transmettre des données du prompt  à d'autres parties du modèle alors qu'il ne le devrait pas, ce qui peut potentiellement amener à la violation de directives de sécurité, générer du contenu nuisible, permettre un accès non autorisé ou influencer des décisions critiques. Bien que des techniques comme la génération augmentée par récupération (RAG) ainsi que le fine-tuning ont pour but de rendre les sorties des LLMs plus pertinentes et précises, plusieurs recherches montrent qu'elles ne permettent pas de complètement atténuer les vulnérabilités liées aux injections de prompt.

Prompt Injection vulnerabilities exist in how models process prompts, and how input may force the model to incorrectly pass prompt data to other parts of the model, potentially causing them to violate guidelines, generate harmful content, enable unauthorized access, or influence critical decisions. While techniques like Retrieval Augmented Generation (RAG) and fine-tuning aim to make LLM outputs more relevant and accurate, research shows that they do not fully mitigate prompt injection vulnerabilities.

Bien que les injections de prompt et le jailbreak soient liés en tant que concepts dans la sécurité des LLMs, ils sont souvent utilisés de manière interchangeable. L'injection de prompt consiste à manipuler les réponses du modèles en suivant une série d'entrées spécifiques qui vont modifier son comportement, ce qui peut inclure le contournement de mesures de sécurité. Le jailbreak, lui, est une forme d'injection de prompt où l'attaquant fournit des entrées qui amènent le modèle à ignorer complètement ses protocoles de sécurité. Les développeurs peuvent implémenter des garde-fous dans le systèmes de prompt ainsi que dans la gestions des entrées pour aider à atténuer les attaques par injections, mais une prévention efficace du jailbreak nécessite une mise à jour continue des mécanismes d'entraînement et de sécurité du modèle.

While prompt injection and jailbreaking are related concepts in LLM security, they are often used interchangeably. Prompt injection involves manipulating model responses through specific inputs to alter its behavior, which can include bypassing safety measures. Jailbreaking is a form of prompt injection where the attacker provides inputs that cause the model to disregard its safety protocols entirely. Developers can build safeguards into system prompts and input handling to help mitigate prompt injection attacks, but effective prevention of jailbreaking requires ongoing updates to the model's training and safety mechanisms.

### Types of Prompt Injection Vulnerabilities - Les différents types d'injections de prompt

#### Direct Prompt Injections - Injections de prompt directes

  L'injection de prompt directe se produit lorsque l'entrée du prompt d'un utilisateur va directement alterer le comportement du modèle de manière non intentionnelle ou inattendue. L'entrée peut être soit intentionnelle ( dans le cas d'un acte malveillant où un attaquant conçoit délibérément un prompt pour exploiter le modèle), ou non intentionnelle ( dans le cas où un utilisateur fournit involontairement une entrée qui déclenchera un comportement non prévu du modèle).

  Direct prompt injections occur when a user's prompt input directly alters the behavior of the model in unintended or unexpected ways. The input can be either intentional (i.e., a malicious actor deliberately crafting a prompt to exploit the model) or unintentional (i.e., a user inadvertently providing input that triggers unexpected behavior).

#### Indirect Prompt Injections - Injections de prompt indirectes

  L'injection de prompt indirecte se produit lorsque le LLM accepte des entrées provenant de sources externes, telles que des sites web ou des fichiers. La source externe peut contenir des données qui, lorsqu'elles seront interprétées par le modèle, peuvent modifier son comportement de manière involontaire ou non prévue. Comme pour les injections directes, les injections indirectes peuvent être soit de nature intentionnelle ou non intentionnelle.

  Indirect prompt injections occur when an LLM accepts input from external sources, such as websites or files. The external source may have content data that when interpreted by the model, alters the behavior of the model in unintended or unexpected ways. Like direct injections, indirect injections can be either intentional or unintentional.

La sévérité et la nature de l'impact d'une attaque par injection de prompt réussie peuvent varier considérablement et dépendent largement à la fois du contexte applicatif dans lequel le modèle opère et de l'architecture du modèle. De manière générale, l'injection de prompt entraîne des résultats non intentionnels, comme par exemple (la liste n'est pas exhaustive) :

The severity and nature of the impact of a successful prompt injection attack can vary greatly and are largely dependent on both the business context the model operates in, and the agency with which the model is architected. Generally, however, prompt injection can lead to unintended outcomes, including but not limited to:


- Divulgation d'informations sensibles
- Révélation d'informations sensibles sur l'infrastructure du système d'IA ou des prompts système
- Manipulation du contenu produit entraînant des sorties incorrectes ou biaisées
- Procuration d'accès non autorisé à des fonctions disponibles uniquement au LLM
- Exécution de commandes arbitraires dans des systèmes connectés
- Manipulation de processus décisionnels critiques

- Disclosure of sensitive information
- Revealing sensitive information about AI system infrastructure or system prompts
- Content manipulation leading to incorrect or biased outputs
- Providing unauthorized access to functions available to the LLM
- Executing arbitrary commands in connected systems
- Manipulating critical decision-making processes

La montée du multimodal dans l'IA, qui rend possible le traitement simultané de plusieurs types de données, introduit des nouveaux risques d'injections par prompt. Des attaquants pourraient exploiter les interactions entre les modalités, comme par exemple en cachant des instructions dans des images qui accompagnent un texte normal. La complexité de ces modèles va donc étendre la surface d'attaque. Les modèles multimodaux peuvent également être vulnébrables à de nouvelles attaques inter-modales qui sont difficiles à detecter et à atténuer avec les techniques de défense actuelleS. Des défenses robustes spécifiques au multimodal sont un domain important dans la R&D.

The rise of multimodal AI, which processes multiple data types simultaneously, introduces unique prompt injection risks. Malicious actors could exploit interactions between modalities, such as hiding instructions in images that accompany benign text. The complexity of these systems expands the attack surface. Multimodal models may also be susceptible to novel cross-modal attacks that are difficult to detect and mitigate with current techniques. Robust multimodal-specific defenses are an important area for further research and development.

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation

Les vulnérabilités liées à l'injection de prompt sont possibles en raison de la nature de l'IA générative. Etant donnée l'influence stochastique (aléatoire) au cœur du fonctionnement des modèles, il est encore trop tôt pour savoir s'il existe des méthodes de défense infaillibles contre les injections de prompt. Cependant, les mesures qui vont suivre peuvent aider à atténuer l'impact des injections de prompt:

Prompt injection vulnerabilities are possible due to the nature of generative AI. Given the stochastic influence at the heart of the way models work, it is unclear if there are fool-proof methods of prevention for prompt injection. However, the following measures can mitigate the impact of prompt injections:

#### 1. Constrain model behavior - Restreindre le comportement du modèle

  Prévoir des instructions spécifiques concernant le rôle du modèles, ses capacités et ses limitations dans le système de prompt. Faire respecter une stricte adhérence au contexte, limiter les réponses aux tâches ou sujets spécifiques, et entraîner le modèles à ignorer  les tentatives de modification d'instructions de base.

  Provide specific instructions about the model's role, capabilities, and limitations within the system prompt. Enforce strict context adherence, limit responses to specific tasks or topics, and instruct the model to ignore attempts to modify core instructions.

#### 2. Define and validate expected output formats - Définir et valider les formats de sortie attendus

  Définir des formats de sortie clairs, demander des raisonnement détaillé et des citations de sources ainsi qu'utiliser du code déterministe pour valider le respect de ces formats.

  Specify clear output formats, request detailed reasoning and source citations, and use deterministic code to validate adherence to these formats.

#### 3. Implement input and output filtering - Mettre en œuvre un filtrage des entrées et des sorties

  Définir des catégories sensibles et créer des règles pour identifier et gérer ce type de contenu. Appliquer des filtres sémantiques et utiliser des vérifications de chaînes de caractère afin d'identifier la présence de contenu non autorisé. Évaluer les réponses en utilisant la triade RAG : évaluer la pertinence du contexte, le fondement ainsi que la pertinence de la question/réponse pour identifier les sorties potentiellement malveillantes.

  Define sensitive categories and construct rules for identifying and handling such content. Apply semantic filters and use string-checking to scan for non-allowed content. Evaluate responses using the RAG Triad: Assess context relevance, groundedness, and question/answer relevance to identify potentially malicious outputs.

#### 4. Enforce privilege control and least privilege access - Renforcer le contrôles des privilèges et le principe du moindre privilège

  Fournir à l'application ses propres tokens API pour étendre ses fonctionnalités et gérer ces fonctions dans le code plutôt que de les mettre à disposition du modèle.
  Restreindre les droits d'accès au modèle au minimum nécessaire pour ses opérations prévues.

  Provide the application with its own API tokens for extensible functionality, and handle these functions in code rather than providing them to the model. Restrict the model's access privileges to the minimum necessary for its intended operations.

#### 5. Require human approval for high-risk actions - Exiger une approbation humaine pour les actions à haut risque

  Mettre en place des contrôles humains pour les opérations critiques et qui demande une élévation de privilège afin de prévenir les actions non autorisées.

  Implement human-in-the-loop controls for privileged operations to prevent unauthorized actions.

#### 6. Segregate and identify external content - Isoler et identifier le contenu externe

  Isoler et signaler le contenu non fiable pour limiter son influence sur les prompts utilisateur.

  Separate and clearly denote untrusted content to limit its influence on user prompts.

#### 7. Conduct adversarial testing and attack simulations - Effectuer des tests de contradiction et des simulations d'attaques

  Effectuer régulièrement des tests de pénétration et des simulations de brèches (BAS - Breach and Attack Simulations), en traitant le modèle comme un utilisateur non fiable pour tester l'efficacité de la limite de confiance accordé au modèle confiance et des contrôles d'accès.

  Perform regular penetration testing and breach simulations, treating the model as an untrusted user to test the effectiveness of trust boundaries and access controls.

### Example Attack Scenarios - Exemples de scénarios d'attaque

#### Scenario #1: Direct Injection - Injection directe

  UN attaquant injecte un prompt dans un chatbot de support client, et lui ordonne d'ignorer les directives qui lui ont été précédemment données, de consulter des bases de données privées et d’envoyer des emails, ce qui amène à avoir un accès non autorisé et une élévation de privilège.

  An attacker injects a prompt into a customer support chatbot, instructing it to ignore previous guidelines, query private data stores, and send emails, leading to unauthorized access and privilege escalation.

#### Scenario #2: Indirect Injection - Injection indirecte

  Un utilisateur utilise un LLM pour résumer une page web contenant des instructions dissimulées qui amènent le LLM à insérer une image contenant un lien URL, ce qui conduit à l'exfiltration de prompt et par conséquent d'une conversation privée.

  A user employs an LLM to summarize a webpage containing hidden instructions that cause the LLM to insert an image linking to a URL, leading to exfiltration of the private conversation.

#### Scenario #3: Unintentional Injection - Injection non intentionnelle

  Une entreprise insère une instruction spécifique dans une description pour un poste afin de détecter les postulations générées par IA. Un candidat, ignorant cette instruction, utilise un LLM pour optimiser son CV, déclenchant involontairement la détection d'IA et donc réduisant ses chances d'obtenir le poste.

  A company includes an instruction in a job description to identify AI-generated applications. An applicant, unaware of this instruction, uses an LLM to optimize their resume, inadvertently triggering the AI detection.

#### Scenario #4: Intentional Model Influence - Influence intentionnelle sur le modèle

  UN attaquant modifie un document dans un répertoire utilisé par une application utilisant la génération augmentée par récupération (RAG). Lorsqu'un utilisateur va requêter le contenu modifié, les instructions malveillantes modifient la sortie du LLM, générant des résultats fallacieux.

  An attacker modifies a document in a repository used by a Retrieval-Augmented Generation (RAG) application. When a user's query returns the modified content, the malicious instructions alter the LLM's output, generating misleading results.

#### Scenario #5: Code Injection - Injection de code

  Un attaquant exploite une vulnérabilité (CVE-2024-5184) dans une assistant pour email utilisant un LLM et injecte des promptes malveillants, ce qui lui permet d'accéder à des informations sensibles et de manipuler le contenu des emails.

  An attacker exploits a vulnerability (CVE-2024-5184) in an LLM-powered email assistant to inject malicious prompts, allowing access to sensitive information and manipulation of email content.

#### Scenario #6: Payload Splitting - Division de charge utile

  Un attaquant téléverse un CV des promptes malveillants disséminés un peu partout. Quand un LLM est utilisé pour évaluer le candidat, les prompts re-combinés manipulent la réponse du modèle, ce qui résulte en une recommandation positive du CV bien que son contenu réel ne soit pas pertinent pour le poste.


  An attacker uploads a resume with split malicious prompts. When an LLM is used to evaluate the candidate, the combined prompts manipulate the model's response, resulting in a positive recommendation despite the actual resume contents.

#### Scenario #7: Multimodal Injection - Injection multimodale

  UN attaquant intègre un prompt malveillant dans une image qui accompagne un texte normal. Lorsqu'une IA multimodale traite l'image et le texte simultanément, le prompt dissimulé modifie le comportement du modèle, ce qui peut potentiellement conduire à des actions non autorisées ou à  la divulgation d'informations sensibles.

  An attacker embeds a malicious prompt within an image that accompanies benign text. When a multimodal AI processes the image and text concurrently, the hidden prompt alters the model's behavior, potentially leading to unauthorized actions or disclosure of sensitive information.

#### Scenario #8: Adversarial Suffix - Suffixe contradictoire

  Un attaquant ajoute une chaîne de caractères apparemment insignifiante à un compte, ce qui influence la sortie du LLM de manière malveillante, contournant ainsi les mesures de sécurité.


  An attacker appends a seemingly meaningless string of characters to a prompt, which influences the LLM's output in a malicious way, bypassing safety measures.

#### Scenario #9: Multilingual/Obfuscated Attack - Attaque multilingue/par obfuscation

  Un attaquant utilise plusieurs langues ou encore des instructions malveillantes ( par exemple en utilisant Base64 ou des emojis) pour échapper aux filtres et manipuler le comportement du LLM.

  An attacker uses multiple languages or encodes malicious instructions (e.g., using Base64 or emojis) to evade filters and manipulate the LLM's behavior.

### Reference Links

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

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
