## LLM10:2025 Consommation illimitée

### Description

La consommation non bornée fait référence au processus par lequel un modèle de langage de grande taille (LLM) génère des sorties en fonction de requêtes ou de prompts d'entrée. L'inférence est une fonction critique des LLM, impliquant l'application de modèles et de connaissances appris pour produire des réponses ou des prédictions pertinentes.

Des attaques conçues pour perturber le service, épuiser les ressources financières de la cible ou même voler la propriété intellectuelle en clonant le comportement d'un modèle dépendent toutes d'une classe commune de vulnérabilité de sécurité pour réussir. La consommation non bornée se produit lorsqu'une application LLM permet aux utilisateurs de réaliser des inférences excessives et incontrôlées, entraînant des risques tels que le déni de service (DoS), les pertes économiques, le vol de modèle et la dégradation du service. Les exigences informatiques élevées des LLM, en particulier dans les environnements cloud, les rendent vulnérables à l'exploitation des ressources et à une utilisation non autorisée.

### Exemples courants de vulnérabilité

#### 1.  Inondation d'entrées de longueur variable
  Les attaquants peuvent submerger le LLM avec de nombreuses entrées de longueurs variables, exploitant les inefficacités de traitement. Cela peut épuiser les ressources et potentiellement rendre le système non réactif, impactant significativement la disponibilité du service.
#### 2. Déni de portefeuille (DoW Deny of Wallet)
  En lançant un volume élevé d'opérations, les attaquants exploitent le modèle de coût à l'utilisation des services d'IA basés sur le cloud, entraînant des charges financières insoutenables pour le fournisseur et risquant la ruine financière.
#### 3. Débordement d'entrées en continu
  L'envoi continu d'entrées dépassant la fenêtre de contexte du LLM peut entraîner une utilisation excessive des ressources informatiques, entraînant une dégradation du service et des perturbations opérationnelles.
#### 4. Requêtes gourmandes en ressources
  La soumission de requêtes exceptionnellement exigeantes impliquant des séquences complexes ou des modèles linguistiques complexes peut épuiser les ressources du système, entraînant des temps de traitement prolongés et des pannes potentielles du système.
#### 5. Extraction de modèle via API
  Les attaquants peuvent interroger l'API du modèle en utilisant des entrées soigneusement élaborées et des techniques d'injection de prompt pour collecter des sorties suffisantes afin de reproduire un modèle partiel ou de créer un modèle fantôme. Cela pose non seulement des risques de vol de propriété intellectuelle, mais compromet également l'intégrité du modèle original.
#### 6. Réplication fonctionnelle de modèle
  L'utilisation du modèle cible pour générer des données d'entraînement synthétiques peut permettre aux attaquants d'affiner un autre modèle de base, créant ainsi un équivalent fonctionnel. Cela contourne les méthodes d'extraction basées sur des requêtes traditionnelles, posant des risques significatifs pour les modèles et technologies propriétaires.
#### 7. Attaques par canaux auxiliaires
  Des attaquants malveillants peuvent exploiter les techniques de filtrage des entrées du LLM pour exécuter des attaques par canaux auxiliaires, récoltant les poids du modèle et les informations architecturales. Cela pourrait compromettre la sécurité du modèle et conduire à une exploitation supplémentaire.

### Stratégies de prévention et d'atténuation

#### 1. Validation des entrées
  Mettre en œuvre une validation stricte des entrées pour garantir que les entrées ne dépassent pas des limites de taille raisonnables.
#### 2. Limit Exposure of Logits and Logprobs - Limiter l'exposition des logits et logprobs
  Restreindre ou obscurcir l'exposition de `logit_bias` et `logprobs` dans les réponses API. Fournir uniquement les informations nécessaires sans révéler de probabilités détaillées.
#### 3. Limitation de débit
  Appliquer des limites de taux et des quotas d'utilisateur pour restreindre le nombre de requêtes qu'une seule entité source peut effectuer dans une période donnée.
#### 4. Gestion de l'allocation des ressources
  Surveiller et gérer l'allocation des ressources de manière dynamique pour empêcher un utilisateur ou une requête unique de consommer des ressources excessives.
#### 5. Délais d'attente et limitation
  Définir des délais d'attente et limiter le traitement des opérations gourmandes en ressources pour éviter une consommation prolongée des ressources.
#### 6. Techniques de bac à sable
  Restreindre l'accès du LLM aux ressources réseau, aux services internes et aux API.
- Cela est particulièrement significatif pour tous les scénarios courants car il englobe les risques et menaces internes. De plus, il régit l'étendue de l'accès de l'application LLM aux données et ressources, servant ainsi de mécanisme de contrôle crucial pour atténuer ou prévenir les attaques par canaux auxiliaires.
#### 7. Comprehensive Logging, Monitoring and Anomaly Detection - Journalisation complète, surveillance et détection des anomalies
  Surveiller en continu l'utilisation des ressources et mettre en œuvre une journalisation pour détecter et répondre aux schémas inhabituels de consommation des ressources.
#### 8. Filigrane
  Mettre en œuvre des cadres de filigrane pour intégrer et détecter l'utilisation non autorisée des sorties LLM.
#### 9. Dégradation progressive
  Concevoir le système pour qu'il se dégrade progressivement sous une charge lourde, en maintenant une fonctionnalité partielle plutôt qu'une défaillance complète.
#### 10. Limiter les actions en file d'attente et évoluer de manière robuste
  Mettre en œuvre des restrictions sur le nombre d'actions en file d'attente et le nombre total d'actions, tout en incorporant une mise à l'échelle dynamique et un équilibrage de charge pour gérer les demandes variables et assurer des performances système cohérentes.
#### 11. Formation à la robustesse contre les attaques contradictoire
  Former des modèles pour détecter et atténuer les requêtes contradictoire et les tentatives d'extractions.
#### 12. Filtrage des jetons de bogue
  Construire une liste de jetons de bogue connus et analyser la sortie avant de l'ajouter à la fenêtre de contexte du modèle.
#### 13. Access Controls - Contrôles d'accès
  Implémenter des contrôles d'accès solides, y compris le contrôle d'accès basé sur les rôles (RBAC) et le principe du moindre privilège, pour limiter l'accès non aurtorisé aux référentiels de modèles LLM et aux environnements de formation.
#### 14. Inventaire de modèle de LM centralisé
  Utiliser un inventaire ou un registre centralisé de modèle ML pour les modèles utilisés en production, garantissant une gouvernance et un contrôle d'accès appropriés.
#### 15. Déploiement MLOps automatisé
  Mettre en oeuvre un déploiement MLOps automatisé avec gouvernance, suivi et flux de travail d'approbation pour renforcer les contrôles d'accès et de déploiement au sein de l'infrastructure.

### Exemple de scénarios d'attaque

#### Scenario #1: Taille d'entrée incontrôlée
  Un attaquant soumet une entrée exceptionnellement grande à une application LLM qui traite des données textuelles, entraînant une utilisation excessive de la mémoire et du CPU, pouvant potentiellement faire planter le système ou ralentir considérablement le service.
#### Scenario #2: Requêtes répétées
  Un attaquant transmet un volume élevé de requêtes à l'API LLM, provoquant une consolation excessive des ressource informatiques et rendant le service indisponible pour les utilisateurs légitimes.
#### Scenario #3: Requêtes gourmandes en ressources
  Un attaquant crée des entrée spécifiques pour déclencher les processus les plus gourmands en ressources du LLM, entraînant une utilisation prolongée du CPU et une panne potentielle du système.
#### Scenario #4: Déni de portefeuille (DoW Deny of Wallet)
  Un attaquant génère des opérations excessives pour exploiter le modèle de coût à l'utilisation des services d'IA basés sur le cloud, entraînant des coûts insoutenables pour le fournisseur de services.
#### Scenario #5:  Réplication fonctionnelle de modèle
  UN attaquant utilise l'API du LLM pour générer des données d'entraînement synthétiques et affiner un autre modèle, créant un équivalent fonctionnel et contournant les limitations traditionnelles d'extraction de modèle.
#### Scenario #6: Contournement du filtrage des entrées du système
  Un attaquant malveillant contourne les techniques de filtrage des entrées et les paramétrages du LLM pour effectuer une attaque par canal auxiliaire et récupérer des informations sur le modèle et les envoyer vers une ressource contrôlée à distance.

### Liens de référence

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

### Cadres et taxonomies connexes

Se reporter à cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement de l'infrastructure, aux contrôles environnementaux appliqués et à d'autres meilleures pratiques.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
