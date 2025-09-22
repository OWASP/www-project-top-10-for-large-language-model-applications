## LLM04:2025 Data and Model Poisoning - Empoisonnement des données et des modèles

### Description

On parle d'empoisonnement des données lorsque les données sont manipulées pour introduire des vulnérabilités, des portes dérobées ou des biais, cet empoisonnement pouvant survenir lors des phases de pré-entrainement, de fine-tuning ou d'embedding. Cette manipulation peut compromettre la sécurité, les performances ou le comportement éthique du modèle, entraînant des résultats nuisibles ou des capacités altérées. Les risques le plus courant incluent la dégradation des performances du modèle, la génération de contenu biaisé ou toxique ainsi que l'exploitation de systèmes situé en aval.

Data poisoning occurs when pre-training, fine-tuning, or embedding data is manipulated to introduce vulnerabilities, backdoors, or biases. This manipulation can compromise model security, performance, or ethical behavior, leading to harmful outputs or impaired capabilities. Common risks include degraded model performance, biased or toxic content, and exploitation of downstream systems.

L'empoisonnement des données peut cibler différentes étapes du cycle de vie des LLM, notamment le pré-entrainement (apprentissage à partir de données générales), le fine-tuning (adaptation des modèles à des tâches spécifiques), l'embedding (conversion de texte en vecteurs numériques) et le transfert d'apprentissage (réutilisation d'un modèle pré-entrainé pour une nouvelle tâche). Comprendre ces étapes aide à identifiier d'où les vulnérabilités peuvent provenir. L'empoisonnement des données est considéré comme une attaque d'intégrité, car la falsification des données d'entraînement impact la capacité du modèle à faire des prédictions précises. Les risques sont particulièremrent élevés avec les sources de données externes, qui peuvent contenir du contenu non vérifié ou malveillant.

Data poisoning can target different stages of the LLM lifecycle, including pre-training (learning from general data), fine-tuning (adapting models to specific tasks), embedding (converting text into numerical vectors), and transfer learning (reusing a pre-trained model on a new task). Understanding these stages helps identify where vulnerabilities may originate. Data poisoning is considered an integrity attack since tampering with training data impacts the model's ability to make accurate predictions. The risks are particularly high with external data sources, which may contain unverified or malicious content.


De plus, les modèles distribués via des dépots partagés ou des plateformes open-source peuvent comporter des risques qui vont au délà de l'empoisonnement des données, tels que les malwares intégrés via des techniques comme le pickling malveillant, qui peuvent exécuter du code nuisible lors du chargement du modèle. Il faut également considérer que l'empoisonnement des données peut permettre la mise en place d'une porte dérobée. De telles portes dérobées peuvent laisser le comportement du modèle inchangé jusqu'à ce qu'un certain déclencheur provoque un changement. Cela peut rendre ces changements difficiles à tester et à détecter, créant ainsi l'opportunité pour un modèle de devenir un agent dormant.

Moreover, models distributed through shared repositories or open-source platforms can carry risks beyond data poisoning, such as malware embedded through techniques like malicious pickling, which can execute harmful code when the model is loaded. Also, consider that poisoning may allow for the implementation of a backdoor. Such backdoors may leave the model's behavior untouched until a certain trigger causes it to change. This may make such changes hard to test for and detect, in effect creating the opportunity for a model to become a sleeper agent.

### Common Examples of Vulnerability - Exemples courants de vulnérabilités


1. Des acteurs malveillants introduisent des données nuisibles pendant l'entrainement, ce qui conduit à de résultats biaisés. Des techniques comme le "Split-View Data Poisoning" ou le "Frontrunning Poisoning" exploitent la dynamique de l'entrainement des modèles pour y parvenir.
  (Lien de référence : [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
2. Des attaquants peuvent injecter du contenu nuisible directement dans le processus d'entrainement, compromettant ainsi la qualité des résultats du modèle.
3. Les utilisateurs injectent involontairement des informations sensibles ou propriétaires lors des interactions, qui pourraient être exposées dans les résultats ultérieurs.
4. Des données d'entrainement non vérifiées augmentent le risque de résultats biaisés ou erronés.
5. L'absence de restrictions d'accès aux ressources peut permettre l'ingestion de données non sécurisées, entraînant des résultats biaisés.


1. Malicious actors introduce harmful data during training, leading to biased outputs. Techniques like "Split-View Data Poisoning" or "Frontrunning Poisoning" exploit model training dynamics to achieve this.
  (Ref. link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Ref. link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Attackers can inject harmful content directly into the training process, compromising the model’s output quality.
3. Users unknowingly inject sensitive or proprietary information during interactions, which could be exposed in subsequent outputs.
4. Unverified training data increases the risk of biased or erroneous outputs.
5. Lack of resource access restrictions may allow the ingestion of unsafe data, resulting in biased outputs.

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation


1. Traquer l'origine et les transformations de données en utilisant des outils comme OWAS CycloneDX ou ML-BOM et exploiter des outils tels que [Dyana](https://github.com/dreadnode/dyana) pour effectuer une analyse dynamique des logiciels tiers. Vérifier la légitimité des données à tous les stades de développement du modèle.
2. Examiner rigoureusement les fournisseurs de données et valider les résultats du modèle par rapport à des sources fiables pour détéecter les signes d'empoisonnement.
3. Mettre en œuvre un sandboxing strict pour limiter l'exposition du modèle à des sources de données non vérifiées. Utiliser des techniques de détection d'anomalies pour filtrer les données contradictoires.
4. Adapter les modèles à différents cas d'utilisation en utilisant des ensembles de données spécifiques pour le fine-tuning. Cela aide à produire des résultats plus précis en fonction des objectifs définis.
5. Assurer des contrôles d'infrastructure suffisants pour empêcher le modèle d'accéder à des sources de données de manière involontaire.
6. Utiliser le contrôle de version des données (DVC) pour suivre les modifications des ensembles de données et détecter les manipulations. La versioning est crucial pour maintenir l'intégrité du modèle.
7. Stocker les informations fournies par les utilisateurs dans une base de données vectorielle, permettant des ajustements sans ré-entrainement complet du modèle.
8. Tester la robustesse du modèle avec des campagnes de red team et des techniques adversariales, telles que le federated learning, pour minimiser l'impact des perturbations de données.
9. Surveiller la perte d'entrainement et analyser le comportement du modèle pour détecter des signes d'empoisonnement. Mettre en place des seuils pour détecter les résultats anormaux.
10. Lors de l'inférence, intégrer des techniques de génération augmentée par récupération (RAG) et de grounding pour réduire les risques d'hallucinations.


4. Track data origins and transformations using tools like OWASP CycloneDX or ML-BOM and leverage tools such as [Dyana](https://github.com/dreadnode/dyana) to perform dynamic analysis of third-party software. Verify data legitimacy during all model development stages.
5. Vet data vendors rigorously, and validate model outputs against trusted sources to detect signs of poisoning.
6. Implement strict sandboxing to limit model exposure to unverified data sources. Use anomaly detection techniques to filter out adversarial data.
7. Tailor models for different use cases by using specific datasets for fine-tuning. This helps produce more accurate outputs based on defined goals.
8. Ensure sufficient infrastructure controls to prevent the model from accessing unintended data sources.
9. Use data version control (DVC) to track changes in datasets and detect manipulation. Versioning is crucial for maintaining model integrity.
10. Store user-supplied information in a vector database, allowing adjustments without re-training the entire model.
11. Test model robustness with red team campaigns and adversarial techniques, such as federated learning, to minimize the impact of data perturbations.
12. Monitor training loss and analyze model behavior for signs of poisoning. Use thresholds to detect anomalous outputs.
13. During inference, integrate Retrieval-Augmented Generation (RAG) and grounding techniques to reduce risks of hallucinations.

### Example Attack Scenarios - Exemples de scénarios d'attaque

#### Scenario #1

  Un attaquant biaise les résultats du modèle en manipulant les données d'entraînement ou en utilisant des techniques d'injection de prompt, diffusant ainsi de la désinformation.

  An attacker biases the model's outputs by manipulating training data or using prompt injection techniques, spreading misinformation.

#### Scenario #2

  Des données toxiques non filtrées peuvent conduire à des résultats nuisibles ou biaisés, propageant ainsi des informations dangereuses.

  Toxic data without proper filtering can lead to harmful or biased outputs, propagating dangerous information.

#### Scenario #3

  Un acteur malveillant ou un concurrent crée des documents falsifiés pour l'entraînement, ce qui entraîne des résultats de modèle reflétant ces inexactitudes.

  A malicious actor or competitor creates falsified documents for training, resulting in model outputs that reflect these inaccuracies.

#### Scenario #4

  Un filtrage inadéquat permet à un attaquant d'insérer des données trompeuses via l'injection de prompt, conduisant à des résultats compromis.

  Inadequate filtering allows an attacker to insert misleading data via prompt injection, leading to compromised outputs.

#### Scenario #5

  Un attaquant utilise des techniques de contamination pour insérer un déclencheur de porte dérobée dans le modèle. Cela pourrait vous exposer à un contournement d'authentification, une exfiltration de données ou une exécution de commandes cachées.

  An attacker uses poisoning techniques to insert a backdoor trigger into the model. This could leave you open to authentication bypass, data exfiltration or hidden command execution.

### Reference Links

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**

### Related Frameworks and Taxonomies

Se réferer à cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement de l'infrastructure, aux contrôles environnementaux appliqués et autres meilleures pratiques.

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- [ML07:2023 Transfer Learning Attack](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML07_2023-Transfer_Learning_Attack) **OWASP Machine Learning Security Top Ten**
