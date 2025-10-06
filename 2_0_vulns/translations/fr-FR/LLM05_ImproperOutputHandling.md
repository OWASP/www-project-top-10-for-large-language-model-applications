## LLM05:2025  Mauvaise gestion de sortie

### Description

Une mauvaise gestion de sortie fait spécifiquement référence à une validation, un assainissement et une gestion insuffisantes des sorties générées par LLM avant qu'elles ne soient transmises en aval à d'autres composants et systèmes. Étant donné que le contenu généré par LLM peut être contrôlé par un prompt d'entrée, ce comportement est semblable à donner aux utilisateur un accès indirect à des fonctionnalités supplémentaires.
La  mauvaise gestion de sorti se distingue de la sur-dépendance en ce qu'elle traite des sorties générées par LLM avant qu'elles ne soient transmises en aval, tandis que la sur-dépendance se concentre sur des préoccupations plus larges autour de la dépendance excessive à l'exactitude et  à la fiabilité des sorties LLM.
L'exploitation réussie d'une vulnérabilité de mauvaise gestion de sortie  peut entraîner des failles XSS, CSRF et SSRF dans les navigateurs web, de l'élévation de privilèges ou une exécution de code à distance sur les systèmes backend.

Les conditions suivantes peuvent augmenter l'impact de cette vulnérabilité :
- L'application accorde au LLM des privilèges au-delà de ce qui est prévu pour les utilisateurs finaux, permettant une élévation de privilèges ou une exécution de code à distance.
- L'application est vulnérable aux attaques d'injection de prompt indirectes, ce qui pourrait permettre à un attaquant d'obtenir un accès privilégié à l'environnement d'un utilisateur cible.
- Les extensions tierces ne valident pas adéquatement les entrées.
- Manque d'encodage de sortie approprié pour différents contextes (par exemple, HTML, JavaScript, SQL)
- Surveillance et journalisation insuffisantes des sorties LLM
- Absence de quota ou de détection d'anomalies pour l'utilisation de LLM

### Exemples courants de vulnérabilité

1. La sortie LLM est entrée directement dans un shell système ou une fonction similaire telle que *exec* ou *eval*, entraînant une exécution de code à distance.
2. JavaScript ou Markdown est généré par le LLM et renvoyé à un utilisateur. Le code est ensuite interprété par le navigateur, entraînant une XSS.
3. Des requêtes SQL générées par LLM sont exécutées sans une paramétrisation appropriée, conduisant à une injection SQL.
4. La sortie LLM est utilisée pour construire des chemins de fichiers sans assainissement approprié, ce qui peut entraîner des vulnérabilités de traversée de chemin.
5. Le contenu généré par LLM est utilisé dans des modèles d'e-mails sans échappement approprié, ce qui peut entraîner des attaques de phishing.

### Stratégies de prévention et d'atténuation

1. Considérer le modèle comme tout autre utilisateur, en adoptant une approche de zéro confiance, et appliquer une validation d'entrée appropriée sur les réponses provenant du modèle vers les fonctions backend.
2. Suivre les directives OWASP ASVS (Application Security Verification Standard) pour assurer une validation et un assainissement efficaces des entrées.
3. Encoder la sortie du modèle avant de la renvoyer aux utilisateurs pour atténuer l'exécution de code indésirable par JavaScript ou Markdown. OWASP ASVS fournit des conseils détaillés sur l'encodage de sortie.
4. Mettre en œuvre un encodage de sortie contextuel basé sur l'endroit où la sortie LLM sera utilisée (par exemple, encodage HTML pour le contenu web, échappement SQL pour les requêtes de base de données).
5. Utiliser des requêtes paramétrées ou des instructions préparées pour toutes les opérations de base de données impliquant la sortie LLM.
6. Employer des politiques de sécurité de contenu strictes (CSP) pour atténuer le risque d'attaques XSS à partir de contenu généré par LLM.
7. Mettre en place des systèmes robustes de journalisation et de surveillance pour détecter des schémas inhabituels dans les sorties LLM qui pourraient indiquer des tentatives d'exploitation.


###  Exemples de scénarios d'attaque

#### Scenario #1
  Une application utilise une extension LLM pour générer des réponses pour une fonctionnalité de chatbot. L'extension offre également un certain nombre de fonctions administratives accessibles à un autre LLM privilégié. Le LLM à usage général transmet directement sa réponse, sans validation appropriée de la sortie, à l'extension, ce qui entraîne la mise hors service de l'extension pour maintenance.
#### Scenario #2
  Un utilisateur utilise un outil de résumé de site Web alimenté par un LLM pour générer un résumé concis d'un article. Le site Web comprend une injection de prompt demandant au LLM de capturer des informations sensibles provenant soit du site Web, soit de la conversation de l'utilisateur. De là, le LLM peut encoder les données sensibles et les envoyer, sans aucune validation ou filtrage de sortie, à un serveur contrôlé par un attaquant.
#### Scenario #3
  Un LLM permet aux utilisateurs de concevoir des requêtes SQL pour une base de données backend via une fonctionnalité de type chat. Un utilisateur demande une requête pour supprimer toutes les tables de la base de données. Si la requête conçue par le LLM n'est pas examinée, alors toutes les tables de la base de données seront supprimées.
#### Scenario #4
  Une application web utilise un LLM pour générer du contenu à partir de prompts textuels d'utilisateurs sans assainissement de la sortie. Un attaquant pourrait soumettre un prompt conçu pour amener le LLM à renvoyer un payload JavaScript non assainie, conduisant à une XSS lorsqu'elle est rendue sur le navigateur d'une victime. Une validation insuffisante des prompts a permis cette attaque.
#### Scenario #5
  Un LLM est utilisé pour générer des modèles d'e-mails dynamiques pour une campagne marketing. Un attaquant manipule le LLM pour inclure du JavaScript malveillant dans le contenu de l'e-mail. Si l'application ne désinfecte pas correctement la sortie du LLM, cela pourrait entraîner des attaques XSS sur les destinataires qui consultent l'e-mail dans des clients de messagerie vulnérables.
#### Scenario #6
  Un LLM est utilisé pour générer du code à partir d'entrées en langage naturel dans une entreprise de logiciels, visant à rationaliser les tâches de développement. Bien que cette approche soit efficace, elle risque d'exposer des informations sensibles, de créer des méthodes de gestion de données non sécurisées ou d'introduire des vulnérabilités telles que l'injection SQL. L'IA peut également halluciner des packages logiciels inexistants, ce qui pourrait amener les développeurs à télécharger des ressources infectées par des logiciels malveillants. Un examen approfondi du code et une vérification des packages suggérés sont cruciaux pour prévenir les violations de sécurité, les accès non autorisés et les compromissions du système.

### Reference Links - Liens de référence

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**
