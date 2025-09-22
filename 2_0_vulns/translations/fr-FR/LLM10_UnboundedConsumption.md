## LLM10:2025 Unbounded Consumption - Consommation non bornée

### Description

La consommation non bornée fait référence au processus par lequel un modèle de langage de grande taille (LLM) génère des sorties en fonction de requêtes ou de prompts d'entrée. L'inférence est une fonction critique des LLM, impliquant l'application de modèles et de connaissances appris pour produire des réponses ou des prédictions pertinentes.

Unbounded Consumption refers to the process where a Large Language Model (LLM) generates outputs based on input queries or prompts. Inference is a critical function of LLMs, involving the application of learned patterns and knowledge to produce relevant responses or predictions.

Des attaques conçues pour perturber le service, épuiser les ressources financières de la cible ou même voler la propriété intellectuelle en clonant le comportement d'un modèle dépendent toutes d'une classe commune de vulnérabilité de sécurité pour réussir. La consommation non bornée se produit lorsqu'une application LLM permet aux utilisateurs de réaliser des inférences excessives et incontrôlées, entraînant des risques tels que le déni de service (DoS), les pertes économiques, le vol de modèle et la dégradation du service. Les exigences informatiques élevées des LLM, en particulier dans les environnements cloud, les rendent vulnérables à l'exploitation des ressources et à une utilisation non autorisée.

Attacks designed to disrupt service, deplete the target's financial resources, or even steal intellectual property by cloning a model’s behavior all depend on a common class of security vulnerability in order to succeed. Unbounded Consumption occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to risks such as denial of service (DoS), economic losses, model theft, and service degradation. The high computational demands of LLMs, especially in cloud environments, make them vulnerable to resource exploitation and unauthorized usage.

### Common Examples of Vulnerability - Exemples courants de vulnérabilité

#### 1. Variable-Length Input Flood - Inondation d'entrées de longueur variable

  Les attaquants peuvent submerger le LLM avec de nombreuses entrées de longueurs variables, exploitant les inefficacités de traitement. Cela peut épuiser les ressources et potentiellement rendre le système non réactif, impactant significativement la disponibilité du service.

  Attackers can overload the LLM with numerous inputs of varying lengths, exploiting processing inefficiencies. This can deplete resources and potentially render the system unresponsive, significantly impacting service availability.

#### 2. Denial of Wallet (DoW) - Déni de portefeuille (DoW)

  En lançant un volume élevé d'opérations, les attaquants exploitent le modèle de coût à l'utilisation des services d'IA basés sur le cloud, entraînant des charges financières insoutenables pour le fournisseur et risquant la ruine financière.

  By initiating a high volume of operations, attackers exploit the cost-per-use model of cloud-based AI services, leading to unsustainable financial burdens on the provider and risking financial ruin.

#### 3. Continuous Input Overflow - Débordement d'entrées continues

  L'envoi continu d'entrées dépassant la fenêtre de contexte du LLM peut entraîner une utilisation excessive des ressources informatiques, entraînant une dégradation du service et des perturbations opérationnelles.

  Continuously sending inputs that exceed the LLM's context window can lead to excessive computational resource use, resulting in service degradation and operational disruptions.

#### 4. Resource-Intensive Queries - Requêtes gourmandes en ressources

  La soumission de requêtes exceptionnellement exigeantes impliquant des séquences complexes ou des modèles linguistiques complexes peut épuiser les ressources du système, entraînant des temps de traitement prolongés et des pannes potentielles du système.

  Submitting unusually demanding queries involving complex sequences or intricate language patterns can drain system resources, leading to prolonged processing times and potential system failures.

#### 5. Model Extraction via API - Extraction de modèle via API

  Les attaquants peuvent interroger l'API du modèle en utilisant des entrées soigneusement élaborées et des techniques d'injection de prompt pour collecter des sorties suffisantes afin de reproduire un modèle partiel ou de créer un modèle fantôme. Cela pose non seulement des risques de vol de propriété intellectuelle, mais compromet également l'intégrité du modèle original.

  Attackers may query the model API using carefully crafted inputs and prompt injection techniques to collect sufficient outputs to replicate a partial model or create a shadow model. This not only poses risks of intellectual property theft but also undermines the integrity of the original model.

#### 6. Functional Model Replication - Réplication fonctionnelle de modèle

  L'utilisation du modèle cible pour générer des données d'entraînement synthétiques peut permettre aux attaquants d'affiner un autre modèle de base, créant ainsi un équivalent fonctionnel. Cela contourne les méthodes d'extraction basées sur des requêtes traditionnelles, posant des risques significatifs pour les modèles et technologies propriétaires.

  Using the target model to generate synthetic training data can allow attackers to fine-tune another foundational model, creating a functional equivalent. This circumvents traditional query-based extraction methods, posing significant risks to proprietary models and technologies.

#### 7. Side-Channel Attacks - Attaques par canaux auxiliaires

  Des attaquants malveillants peuvent exploiter les techniques de filtrage des entrées du LLM pour exécuter des attaques par canaux auxiliaires, récoltant les poids du modèle et les informations architecturales. Cela pourrait compromettre la sécurité du modèle et conduire à une exploitation supplémentaire.

  Malicious attackers may exploit input filtering techniques of the LLM to execute side-channel attacks, harvesting model weights and architectural information. This could compromise the model's security and lead to further exploitation.

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation

#### 1. Input Validation  - Validation des entrées

  Mettre en œuvre une validation stricte des entrées pour garantir que les entrées ne dépassent pas des limites de taille raisonnables.

  Implement strict input validation to ensure that inputs do not exceed reasonable size limits.

#### 2. Limit Exposure of Logits and Logprobs - Limiter l'exposition des logits et logprobs

  Restreindre ou obscurcir l'exposition de `logit_bias` et `logprobs` dans les réponses API. Fournir uniquement les informations nécessaires sans révéler de probabilités détaillées.

  Restrict or obfuscate the exposure of `logit_bias` and `logprobs` in API responses. Provide only the necessary information without revealing detailed probabilities.

#### 3. Rate Limiting - Limitation de débit

  Appliquer des limites de taux et des quotas d'utilisateur pour restreindre le nombre de requêtes qu'une seule entité source peut effectuer dans une période donnée.

  Apply rate limiting and user quotas to restrict the number of requests a single source entity can make in a given time period.

#### 4. Resource Allocation Management - Gestion de l'allocation des ressources

  Surveiller et gérer l'allocation des ressources de manière dynamique pour empêcher un utilisateur ou une requête unique de consommer des ressources excessives.

  Monitor and manage resource allocation dynamically to prevent any single user or request from consuming excessive resources.

#### 5. Timeouts and Throttling - Délais d'attente et limitation

  Définir des délais d'attente et limiter le traitement des opérations gourmandes en ressources pour éviter une consommation prolongée des ressources.

  Set timeouts and throttle processing for resource-intensive operations to prevent prolonged resource consumption.

#### 6. Sandbox Techniques - Techniques de bac à sable

  Restreindre l'accès du LLM aux ressources réseau, aux services internes et aux API.

  Restrict the LLM's access to network resources, internal services, and APIs.

- Cela est particulièrement significatif pour tous les scénarios courants car il englobe les risques et menaces internes. De plus, il régit l'étendue de l'accès de l'application LLM aux données et ressources, servant ainsi de mécanisme de contrôle crucial pour atténuer ou prévenir les attaques par canaux auxiliaires.
- 
- This is particularly significant for all common scenarios as it encompasses insider risks and threats. Furthermore, it governs the extent of access the LLM application has to data and resources, thereby serving as a crucial control mechanism to mitigate or prevent side-channel attacks.

#### 7. Comprehensive Logging, Monitoring and Anomaly Detection - Journalisation complète, surveillance et détection des anomalies

  Surveiller en continu l'utilisation des ressources et mettre en œuvre une journalisation pour détecter et répondre aux schémas inhabituels de consommation des ressources.

  Continuously monitor resource usage and implement logging to detect and respond to unusual patterns of resource consumption.

#### 8. Watermarking - Filigrane

  Mettre en œuvre des cadres de filigrane pour intégrer et détecter l'utilisation non autorisée des sorties LLM.

  Implement watermarking frameworks to embed and detect unauthorized use of LLM outputs.

#### 9. Graceful Degradation - Dégradation progressive

  Concevoir le système pour qu'il se dégrade progressivement sous une charge lourde, en maintenant une fonctionnalité partielle plutôt qu'une défaillance complète.

  Design the system to degrade gracefully under heavy load, maintaining partial functionality rather than complete failure.

#### 10. Limit Queued Actions and Scale Robustly - Limiter les actions en file d'attente et évoluer de manière robuste

  Mettre en œuvre des restrictions sur le nombre d'actions en file d'attente et le nombre total d'actions, tout en incorporant une mise à l'échelle dynamique et un équilibrage de charge pour gérer les demandes variables et assurer des performances système cohérentes.

  Implement restrictions on the number of queued actions and total actions, while incorporating dynamic scaling and load balancing to handle varying demands and ensure consistent system performance.

#### 11. Adversarial Robustness Training - Formation à la robustesse contre les attaques adversariales

  Former des modèles pour détecter et atténuer les requètes advesariables et les tentatives d'extractions.

  Train models to detect and mitigate adversarial queries and extraction attempts.

#### 12. Glitch Token Filtering - Filtrage des jetons de bogue

  Construire une liste de jetons de bogue connus et analyser la sortie avant de l'ajouter à la fenêtre de contexte du modèle.

  Build lists of known glitch tokens and scan output before adding it to the model’s context window.

#### 13. Access Controls - Contrôles d'accès

  Implémenter des contrôles d'accès solides, y compris le contrôle d'accès basé sur les rôles (RBAC) et le principe du moindre privilège, pour limiter l'accès non aurtorisé aux référentiels de modèles LLM et aux environnements de formation 

  Implement strong access controls, including role-based access control (RBAC) and the principle of least privilege, to limit unauthorized access to LLM model repositories and training environments.

#### 14. Centralized ML Model Inventory - Inventaire de modèle de LM centralisé

  Utiliser un inventaire ou un registre centralisé de modèle ML pour les modèles utilisés en production, garantissant une gouvernance et un contrôle d'accès appropriés.

  Use a centralized ML model inventory or registry for models used in production, ensuring proper governance and access control.

#### 15. Automated MLOps Deployment - Déploiement MLOps automatisé

  Mettre en oeuvre un déploiement MLOps automatisé avec gouvernance, suivi et flux de travail d'approbation pour renforcer les contrôles d'accès et de déploiement au sein de l'infrastructure.

  Implement automated MLOps deployment with governance, tracking, and approval workflows to tighten access and deployment controls within the infrastructure.

### Example Attack Scenarios

#### Scenario #1: Uncontrolled Input Size - Taille d'entrée incontrôlée

  UN attaquant soumet une entrée exceptionnelement grande à une application LLM qui traite des données textuelles, entraînant une utilisation excessive de la mémoire et du CPU, pouvant potentiellement faire planter le système ou ralentir considérablement le service.

  An attacker submits an unusually large input to an LLM application that processes text data, resulting in excessive memory usage and CPU load, potentially crashing the system or significantly slowing down the service.

#### Scenario #2: Repeated Requests - Requêtes répétées

  UN attaquant transmet un volume elévé de requêtes à l'API LLM, provoquant une consomation excessive des ressource informatiques et rendant le service indisponible pour les utilisateurs légitimes.

  An attacker transmits a high volume of requests to the LLM API, causing excessive consumption of computational resources and making the service unavailable to legitimate users.

#### Scenario #3: Resource-Intensive Queries - Requêtes gourmandes en ressources

  UN attaquant crée des entreée spécifiques pour déclencher les processus les plus gourmands en ressources du LLM, entraînant une utilisation prolongée du CPU et une panne potentielle du système.

  An attacker crafts specific inputs designed to trigger the LLM's most computationally expensive processes, leading to prolonged CPU usage and potential system failure.

#### Scenario #4: Denial of Wallet (DoW) - Déni de portefeuille (DoW)

  UN attaquant génère des opérations excessives pour exploiter le modèle de coût à l'utilisation des services d'IA basés sur le cloud, entraînant des coûts insoutenables pour le fournisseur de services.

  An attacker generates excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.

#### Scenario #5: Functional Model Replication - Réplication fonctionnelle de modèle

  UN attaquant utilise l'API du LLM pour générer des données d'entraînement synthétiques et affiner un autre modèle, créant un équivalent fonctionnel et contournant les limitations traditionnelles d'extraction de modèle.

  An attacker uses the LLM's API to generate synthetic training data and fine-tunes another model, creating a functional equivalent and bypassing traditional model extraction limitations.

#### Scenario #6: Bypassing System Input Filtering - Contournement du filtrage des entrées du système

  Un attaquant malveillant coutourne les techniques de filtrage des entrées et les préambules du LLM pour effectuer une attaque par canal auxiliaire et récuperer des informations sur le modèle vers une ressource contrôleée à distance sous leur contrôle.

  A malicious attacker bypasses input filtering techniques and preambles of the LLM to perform a side-channel attack and retrieve model information to a remote controlled resource under their control.

### Reference Links - Liens de référence

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Related Frameworks and Taxonomies - Cadres et taxonomies connexes

Se reporter à cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement de l'infrastructure, aux contrôles environnementaux appliqués et à d'autres meilleures pratiques.

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
