 ## LLM01:2025 Fuite de prompt système

Une vulnérabilité d’injection de prompt se produit lorsque les instructions fournies par une personne modifient le comportement ou les sorties d’un LLM de manière inattendue. Ces instructions peuvent affecter le modèle même si elles sont imperceptibles pour un humain ; une injection de prompt n’a donc pas besoin d’être lisible ou visible par un humain tant que le contenu est interprété par le modèle.

Les vulnérabilités d’injection de prompt proviennent de la manière dont les modèles traitent les prompts, et du fait que certaines entrées peuvent forcer le modèle à transmettre incorrectement ces données à d’autres parties du système, ce qui peut entraîner une violation des règles en place, la génération de contenu préjudiciable, l’activation d’accès non autorisés ou influencer des décisions critiques. Bien que des techniques comme la Génération Augmentée par Récupération (en anglais RAG) ou des réglages avancés visent à rendre les sorties des LLM plus pertinentes et fiables, les recherches montrent qu’elles ne suffisent pas à éliminer ces vulnérabilités.

L’injection de prompt et le débridage sont deux concepts liés en matière de sécurité des LLM et ils souvent utilisés de façon interchangeable. L’injection de prompt consiste à manipuler les réponses du modèle par le biais d’entrées spécifiques afin de modifier son comportement, parfois en contournant les mesures de sécurité. Le débridage est une forme particulière d’injection de prompt, dans laquelle la personne qui attaque insère des instructions afin de pousser le modèle à ignorer totalement ses protocoles de sécurité. L’équipe de développement peut intégrer des protections dans les prompts système et le traitement des entrées pour atténuer ces attaques. Cependant une prévention efficace du débridage nécessite une mise à jour continue des mécanismes d’apprentissage et de sécurité du modèle.

### Types de vulnérabilités d’injection de prompt

Injections de prompt directes

Les injections directes surviennent lorsqu’un prompt saisi par une personne modifie directement le comportement du modèle de manière inattendue. Cela peut être volontaire (un acte malveillant formulé délibérément via un prompt pour exploiter le modèle) ou involontaire (saisit d’un prompt qui provoque par erreur un comportement non anticipé).

Injections de prompt indirectes

Les injections indirectes se produisent lorsqu’un LLM accepte une entrée provenant d’une source externe, comme un site web ou un fichier. Le contenu externe, une fois interprété par le modèle, peut en modifier le comportement de manière involontaire ou malveillante, à l’instar des injections directes.

La gravité et la nature d’une attaque par injection de prompt dépendent largement du contexte métier dans lequel le modèle est utilisé, ainsi que du niveau d’autonomie qui lui est accordé. En général, ces attaques peuvent entraîner des conséquences telles que :

* La divulgation de données sensibles
* La révélation d’informations sur l’infrastructure du système d’IA ou sur les prompts système
* La manipulation du contenu, menant à des résultats erronés ou biaisés
* L’accès non autorisé à des fonctions disponibles pour le LLM
* L’exécution de commandes arbitraires dans des systèmes connectés
* L’influence sur des processus décisionnels critiques

L’essor de l’IA multimodale, capable de traiter simultanément plusieurs types de données, introduit de nouveaux risques d’injection de prompt. Des personnes malveillantes peuvent exploiter les interactions entre les diverses données, comme dissimuler des instructions dans une image jointe à un texte anodin. Cette complexité augmente la surface d’attaque. De plus, ces modèles d’IA multimodale peuvent être vulnérables à des attaques croisées spécifiques, difficiles à détecter ou contrer par les techniques de défense actuelles. Le développement de défenses spécifiques aux systèmes multimodaux est une priorité des équipes de recherche et développement.

### Stratégies de prévention et d’atténuation

Les vulnérabilités d’injection de prompt sont inhérentes au fonctionnement de l’IA générative. En raison de la nature probabiliste de ces systèmes, il n’existe pas à ce jour de solution totalement infaillible face aux injections de prompt. Néanmoins, les mesures suivantes permettent d’en réduire les risques :

1. Contraindre le comportement du modèle

Fournir des instructions précises sur le rôle, les capacités et les limites du modèle dans le prompt système. Imposer le respect strict du contexte, limiter les réponses à certaines tâches ou thématiques, et demander au modèle d’ignorer toute tentative de modifier ses propres instructions systèmes.

2. Définir et valider les formats de sortie attendus

Préciser les formats de réponse attendus, exiger des raisonnements détaillés et des sources, et utiliser du code déterministe pour vérifier le respect de ces formats.

3. Mettre en place des filtres sur les entrées et sorties

Définir les catégories sensibles et établir des règles pour les détecter et les traiter. Utiliser des filtres sémantiques stricts et des analyses de chaînes de caractères pour repérer les contenus non autorisés. Évaluer les réponses à l’aide de la trilogie RAG : évaluer la pertinence du contexte, vérifier le bien-fondé et la pertinence des questions/réponses afin d’identifier des sorties potentiellement malveillantes.

4. Appliquer les principes de contrôle d’accès et du moindre privilège

Fournir à l’application ses propres jetons API pour les fonctions en nécessitant, et invoquer ces fonctions via du code plutôt que via le modèle. Réduire les privilèges d’accès du modèle au strict nécessaire à son bon fonctionnement.

5. Soumettre les actions sensibles à une validation humaine

Mettre en place des contrôles humains (human-in-the-loop) pour toute opération à risque afin de se prémunir de toutes actions non autorisées.

6. Isoler et identifier les contenus externes

Séparer et indiquer clairement les contenus non fiables afin de limiter leur influence sur les prompts utilisateurs.

7. Effectuer des tests d’attaque et des simulations d’actes malveillants

Réaliser des tests d’intrusion et des simulations d’attaque régulièrement du modèle afin d’évaluer l’efficacité des mécanismes de protections et de contrôle d’accès.

### Scénarios d’attaque

Scénario n° 1 : Injection directe

Une personne simule une attaque en injectant un prompt dans un agent conversationnel de support client, l’invitant à ignorer les instructions précédentes, interroger des bases de données privées et envoyer des courriels afin d’évaluer la gestion d’accès non autorisé et d’élévation de privilèges.

Scénario n° 2 : Injection indirecte

Une personne demande à un LLM de résumer une page web contenant des instructions cachées qui demande au LLM d’insérer dans sa réponse une image pointant vers une URL afin d’évaluer les risques de fuite de donnée de la conversation privée.

Scénario n° 3 : Injection involontaire

Une entreprise ajoute un prompt dans une offre d’emploi visant à détecter les candidatures rédigées par une IA. Un candidat, non conscient de cela, utilise un LLM pour optimiser son CV, déclenchant ainsi le mécanisme de détection via l’IA.

Scénario n° 4 : Influence délibérée sur le modèle

Une personne simule une attaque en modifiant un document dans un référentiel utilisé par une application de Génération Augmentée par Récupération (RAG). Lorsqu’une personne interroge le système, les instructions malveillantes contenues dans le document faussent la réponse générée.

Scénario n° 5 : Injection de code

Une personne simule une attaque en exploitant une faille (CVE-2024-5184) dans un assistant courriel propulsé par un LLM pour injecter des prompts malveillants, accédant ainsi à des données sensibles et manipulant le contenu des courriels.

Scénario n° 6 : Fragmentation de charge utile

Une personne simule une attaque en soumettant un CV contenant des fragments de prompts malveillants. Lors de l’évaluation du CV par un LLM, les fragments se combinent pour influencer la réponse du modèle, produisant une recommandation positive indépendamment du réel contenu du CV.

Scénario n° 7 : Injection multimodale

Une personne simule une attaque en insérant un prompt malveillant dans une image jointe à un texte anodin. Lorsqu’un modèle multimodal traite l’ensemble, le prompt dissimulé altère son comportement en effectuant des actions non autorisées ou en divulguant des informations sensibles.

Scénario n° 8 : Suffixe hostile

Une personne simule une attaque en ajoutant une chaîne de caractères apparemment insignifiante à la fin d’un prompt, cela influence la sortie du LLM de manière malveillante, contournant les mécanismes de sécurité.

Scénario n° 9 : Attaque multilingue ou offusquée

Une personne simule une attaque en utilisant plusieurs langues ou en encodant ses prompts (ex. : Base64, emojis) pour échapper aux filtres et manipuler le comportement du modèle LLM.

### Références

1. [ChatGPT Plugin Vulnerabilities—Chat with Code] (https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection] (https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection] (https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder] (https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications] (https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume] (https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection] (https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
9. [Threat Modeling LLM Applications] (https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Reducing The Impact of Prompt Injection Attacks Through Design] (https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)] (https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)] (https://arxiv.org/abs/2407.07403)
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks] (https://ieeexplore.ieee.org/document/10579515)
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)] (https://arxiv.org/abs/2307.15043)
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)] (https://arxiv.org/abs/2307.00691)

### Cadres et taxonomies associés

Consultez cette section pour obtenir des informations détaillées, des stratégies et des scénarios liés au déploiement d’infrastructures, aux contrôles des environnements appliqués et aux meilleures pratiques:

—[AML.T0051.000— LLM Prompt Injection: Direct] (https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**

—[AML.T0051.001 - LLM Prompt Injection: Indirect] (https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**

—[AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
