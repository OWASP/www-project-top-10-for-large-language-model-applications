## LLM03:2025 Supply Chain - Chaîne d'approvisionnement

### Description - Description

Les chaînes d'approvisionnement des LLMs  sont susceptibles d'être exposées à diverses vulnérabilités, pouvant affecter l'intégrité des données d’entraînement, des modèles et des plateformes de déploiements. Ces risques peuvent entraîner des sorties biaisées, des violations de sécurité ou des pannes système. Tandis que les vulnérabilités logicielles traditionnelles se concentrent sur des problèmes tels que les défauts dans le code ou ses dépendances, dans le machine learning les risques s'étendent également aux modèles pré-entraînés tiers et aux données.

LLM supply chains are susceptible to various vulnerabilities, which can affect the integrity of training data, models, and deployment platforms. These risks can result in biased outputs, security breaches, or system failures. While traditional software vulnerabilities focus on issues like code flaws and dependencies, in ML the risks also extend to third-party pre-trained models and data.

Ces éléments externes peuvent être manipulés via des techniques d'attaque comme la falsification ou l'empoisonnement de données.

These external elements can be manipulated through tampering or poisoning attacks.

Créer des LLMs est une tâche spécifique qui dépend souvent de modèles tiers. La montée des LLMs en libre accès et des nouvelles méthodes de fine-tuning comme "LoRA" (Low-Rank Adaptation) et "PEFT" (Parameter-Efficient Fine-Tuning), notamment sur des plateformes comme Hugging Face, introduisent de nouveaux risques dans la chaîne d'approvisionnement. Enfin, l'émergence des LLMs "on-device" (des LLMs fonctionnant sur des appareils à ressources limitées, par exemple des smartphones, lunettes...) étend la surface d'attaque et les risques liés à la chaîne d'approvisionnement.

Creating LLMs is a specialized task that often depends on third-party models. The rise of open-access LLMs and new fine-tuning methods like "LoRA" (Low-Rank Adaptation) and "PEFT" (Parameter-Efficient Fine-Tuning), especially on platforms like Hugging Face, introduce new supply-chain risks. Finally, the emergence of on-device LLMs increase the attack surface and supply-chain risks for LLM applications.

La pluparts des risques abordés ici sont également discutés dans "LLM04 Data and Model Poisoning". Cet article se concentre sur l'aspect chaîne d'approvisionnement des risques.

Some of the risks discussed here are also discussed in "LLM04 Data and Model Poisoning." This entry focuses on the supply-chain aspect of the risks.
A simple threat model can be found [here](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Common Examples of Risks - Exemples courants de risques

#### 1. Traditional Third-party Package Vulnerabilities - Les vulnérabilités liées aux packages tiers

  Les composants tiers non mis à jour ou périmés, sont très souvent des vecteurs d'attaque pour compromettre les applications utilisant des LLMs. Les problématiques sont similaires à "A06:2021 – Vulnerable and Outdated Components" avec des risques accrus lorsque les composants sont utilisés lors du développement ou du fine-tuning de modèles.

  Such as outdated or deprecated components, which attackers can exploit to compromise LLM applications. This is similar to "A06:2021 – Vulnerable and Outdated Components" with increased risks when components are used during model development or fine-tuning.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

#### 2. Licensing Risks - Risques liés aux licences

  Le developpement de l'IA implique souvent des licences logicielles et de jeux de données divers, pouvant créer des risques de sécurité s'ils ne sont pas correctement gérés. Les licences open-source et propriétaires imposent en générales différentes  exigences légales. Les licences de jeux de données peuvent restreindre leur utilisation, leur distribution ou leur commercialisation.

  AI development often involves diverse software and dataset licenses, creating risks if not properly managed. Different open-source and proprietary licenses impose varying legal requirements. Dataset licenses may restrict usage, distribution, or commercialization.

#### 3. Outdated or Deprecated Models - Modèles obsolètes ou périmés

  Utiliser des modèles obsolètes ou périmés qui ne sont plus maintenus peut entraîner des problèmes de sécurité.

  Using outdated or deprecated models that are no longer maintained leads to security issues.

#### 4. Vulnerable Pre-Trained Model - Modèle pré-entraîné vulnérable

  Ces modèles sont en générale des boites noire et contrairement à ceux en open-source, une inspection statique offre peut de garantie de sécurité. Les modèles pré-entrainés vunnérables peuvent vontenir des biais cachés, des portes dérobées (backdoors) ou d'autres fonctionnalités malveillantes qui n'ont pas été identifiées lors des évaluations de sécurité des dépôts de modèles. Les modèles vulnérables peuvent être créés à la fois par des jeux de données empoisonnés et par la manipulation directe du modèle en utilisant des techniques telles que ROME également connue sous le nom de lobotomisation.


  Models are binary black boxes and unlike open source, static inspection can offer little to security assurances. Vulnerable pre-trained models can contain hidden biases, backdoors, or other malicious features that have not been identified through the safety evaluations of model repositories. Vulnerable models can be created by both poisoned datasets and direct model tampering using techniques such as ROME also known as lobotomisation.

#### 5. Weak Model Provenance - Faible confiance dans la provenance des modèles

  Actuellement, il n'y a pas de garantie solides sur la provenances des modèles publiés. Les Model Cards et la documentation associée donnent des informations sur le smodèles et les utilisateurs y sont mis à contribution, mais elles n'offrent aucune garantie sur l'origine du modèle. Un attaquant peut compromettre un compte fournisseur sur un dépôt de modèle ou en créer un similaire et combiner tout cela avec des techniques d'ingéniérie sociale, il est ainsi possible de compromettre la chaîne d'approvisionnement d'une application utilisant un LLM.


  Currently there are no strong provenance assurances in published models. Model Cards and associated documentation provide model information and relied upon users, but they offer no guarantees on the origin of the model. An attacker can compromise a supplier account on a model repo or create a similar one and combine it with social engineering techniques to compromise the supply-chain of an LLM application.

#### 6. Vulnerable LoRA adapters - Adaptateurs LoRA vulnérables

  Le LoRA est une technique de fine-tuning populaire qui permet d'améliorer la modularité d'un modèle et permettant d'ajouter des couches pré-entrainés à un LLM exsistant. La méthode augmente l'éfficacité mais crée de nouveaux risques, où un adaptateur LoRA malveillant compromet l'intégrité et la sécurité du modèle de base pré-entrainé. Cela peut se produire à la fois dans les environnements collaboratifs de fusion de modèle mais aussi en exploitant le fait que LoRA est supportés par plusieurs plateformes de déploiement d'inférence populaires telles que vLLM et OpenLLM où les adaptateurs peuvent être téléchargés et appliqués à une modèle déployé.

  LoRA is a popular fine-tuning technique that enhances modularity by allowing pre-trained layers to be bolted onto an existing LLM. The method increases efficiency but creates new risks, where a malicious LorA adapter compromises the integrity and security of the pre-trained base model. This can happen both in collaborative model merge environments but also exploiting the support for LoRA from popular inference deployment platforms such as vLMM and OpenLLM where adapters can be downloaded and applied to a deployed model.

#### 7. Exploit Collaborative Development Processes - Exploiter les processus de développement collaboratif

  Les services de fusion de modèles collaboratifs et de gestion de modèles (par exemple: conversions) hébergés dans des environnements partagés peuvent être exploités pour introduire des vulnérabilités dans les modèles partagés. La fusion de modèle est très populaire sur Hugging Face avec des modèles fusionnés en tête du classement OpenLLM et peut être exploitée pour contourner les revues. De même, des services tels que les bots de conversation ont prouvé qu'ils étaient vulnérables à la manipulation et à l'introduction de code malveillant dans les modèles.

  Collaborative model merge and model handling services (e.g. conversions) hosted in shared environments can be exploited to introduce vulnerabilities in shared models. Model merging is very popular on Hugging Face with model-merged models topping the OpenLLM leaderboard and can be exploited to bypass reviews. Similarly, services such as conversation bot have been proved to be vulnerable to manipulation and introduce malicious code in models.

#### 8. LLM Model on Device supply-chain vulnerabilities - Vulnérabilités de la chaîne d'approvisionnement des modèles LLM sur appareil à ressources limitées

  Les modèles LLMs tournant sur des appareils à ressources limitées augmentent la surface d'attaque de la chaîne d'approvisionnement avec la compromission des processus de developpement et l'exploitation des vulnérabilités du système d'exploitation ou du firmware de l'appareil afin de compromettre de facto les modèles. Les attaquants peuvent ainsi rétroconcevoir et reconditionner des applications avec les modèles déviés.

  LLM models on device increase the supply attack surface with compromised manufactured processes and exploitation of device OS or firmware vulnerabilities to compromise models. Attackers can reverse engineer and re-package applications with tampered models.

#### 9. Unclear T&Cs and Data Privacy Policies - T&Cs et politiques de confidentialité des données peu claires

  Des T&Cs (Termes et Conditions) et des politiques de confidentialité des données peu claires de la part des opérateurs de modèles conduisent à l'utilisation des données sensibles de l'application à l'entraînement du modèle et donc à l'exposition d'informations sensibles. Cela peut également s'appliquer aux risques liés à l'utilisation de matériel protégé par le droit d'auteur définit par le fournisseur du modèle.


  Unclear T&Cs and data privacy policies of the model operators lead to the application's sensitive data being used for model training and subsequent sensitive information exposure. This may also apply to risks from using copyrighted material by the model supplier.

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation






4. 


1. Etablir avec attention des sources de données et des fournisseurs en comprenant leurs T&C et leur politiques de confidentialité, en n'utilisant que des fournisseurs de confiance. Revoir et auditer régulièrement la sécurité et l'accès des fournisseurs, en s'assurant qu'il n'y a pas de changements dans position dans leur politique de sécurité ou leurs T&C.
2. Carefully vet data sources and suppliers, including T&Cs and their privacy policies, only using trusted suppliers. Regularly review and audit supplier Security and Access, ensuring no changes in their security posture or T&Cs.
  

3. Comprendre et appliquer les mesures d'atténuation trouvées dans le "A06:2021 – Vulnerable and Outdated Components" de l'OWASP Top Ten. Cela inclut le scan de vulnérabilités, la gestion et le patching des composants. Pour les environnements de développement avec accès à des données sensibles, il est nécéssaire d'appliquer également ces contrôles.  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
4. Understand and apply the mitigations found in the OWASP Top Ten's "A06:2021 – Vulnerable and Outdated Components." This includes vulnerability scanning, management, and patching components. For development environments with access to sensitive data, apply these controls in those environments, too.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))


1. Appliquer des évaluations et des tests de type AI Red Teaming complets lors de la sélection d'un modèle tiers. Decoding Trust est un exemple de benchmark d'IA digne de confiance pour les LLMs, mais les modèles peuvent être fine-tunés pour contourner les benchmarks publiés. Utiliser un AI Red Teaming extensif pour évaluer le modèle, en particulier dans les cas où vous prévoyez d'utiliser le modèle.
2. Apply comprehensive AI Red Teaming and Evaluations when selecting a third party model. Decoding Trust is an example of a Trustworthy AI benchmark for LLMs but models can be fine-tuned to bypass published benchmarks. Use extensive AI Red Teaming to evaluate the model, especially in the use cases you are planning to use the model for.
  

3. Maintenir un inventaire à jour des composants en utilisant un Software Bill of Materials (SBOM) pour s'assurer de disposer un inventaire de composants à jour, précis et signé, empêchant la falsification des packages utilisés. Les SBMOs peuvent être utilisés pour détecter et alerter rapidement sur les nouvelles vulnérabilités su jour zéro (zero-day). Les BOMs pour l'IA et les SBOMs pour les ML sont un domaine émergent et il est vivement conseillé d'évaluer ces options en commençant par OWASP CycloneDX. 
4. Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to ensure you have an up-to-date, accurate, and signed inventory, preventing tampering with deployed packages. SBOMs can be used to detect and alert for new, zero-date vulnerabilities quickly. AI BOMs and ML SBOMs are an emerging area and you should evaluate options starting with OWASP CycloneDX


5. Pour atténuer les risques liés aux licences d'IA, il est conseiller de créer un inventaire de tous les types de licenses en utulisant des BOMs et effectuer des audits réguliers de tous les logiciels, outils et jeux de données, assurant ainsi la conformité et la transparence via les BOMS. Il est également recommandé d'utiliser des outils automatisés de gesrion des licenses pour une surveillance quasi temps réel et de sensibilier les équipes aux liences de modèles. MAintenir une documentation détaillée des licenses dans les BOMs et utiliser des outils tels que [Dyana](https://github.com/dreadnode/dyana) pour effectuer une analuyse dynamique des logiciels tiers. 
6. To mitigate AI licensing risks, create an inventory of all types of licenses involved using BOMs and conduct regular audits of all software, tools, and datasets, ensuring compliance and transparency through BOMs. Use automated license management tools for real-time monitoring and train teams on licensing models. Maintain detailed licensing documentation in BOMs and leverage tools such as [Dyana](https://github.com/dreadnode/dyana) to perform dynamic analysis of third-party software.
  

7. Utiliser uniquement les modèles provenant de sources vérifiables et utiliser des contrôles d'intégrité de modèle tiers avec signature et hachage pour compenser le manque de confiance dans la provenance des modèles. De même, utilsier la signature de code pour le code fourni par des tiers.
7. Only use models from verifiable sources and use third-party model integrity checks with signing and file hashes to compensate for the lack of strong model provenance. Similarly, use code signing for externally supplied code.


8. Implémenter une surveillance et des pratiques d'audit strictes pour les environnement de développement collaboratif de modèle afin de prévenir et de detecter le plus tôt possible toute utilisation abusive. "HuggingFace SF_Convertbot Scanner" est un exemple de script automatisé qui permet de détecter les comportements anormaux dans les environnements de développement de modèles.(Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Implement strict monitoring and auditing practices for collaborative model development environments to prevent and quickly detect any abuse. "HuggingFace SF_Convertbot Scanner" is an example of automated scripts to use.
  (Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))

9. La détection d'anomalie et les tests de robustesse à l'encontre de modèles et de données fournies peuvent aider à detecter la falsification et l'empoisonement comme discuté dans "LLM04 Data and Model Poisoning"; idéalement, cela devrait faire partie des pipelines MLOps et LLM; cependant, ce sont des techniques émergentes et peuvent être plus facile à mettre en place dans le cadre d'exercices de red teaming.
10. Anomaly detection and adversarial robustness tests on supplied models and data can help detect tampering and poisoning as discussed in "LLM04 Data and Model Poisoning; ideally, this should be part of MLOps and LLM pipelines; however, these are emerging techniques and may be easier to implement as part of red teaming exercises.

10. Implémenter une politique de patching pour atténuer les composants vulnérables ou obsolètes. S'assurer que l'application repose sur une version maintenue des API et du modèle sous-jacent. 
11. Implement a patching policy to mitigate vulnerable or outdated components. Ensure the application relies on a maintained version of APIs and underlying model.


11. Chiffrer les modèles deployés à l'AI edge avec des contrôles d'intégrité et utiliser les API d'attestion des fournisseurs pour empêcher les applications et les modèles malveillants et se débarasser des firwares inconnus.
12. Encrypt models deployed at AI edge with integrity checks and use vendor attestation APIs to prevent tampered apps and models and terminate applications of unrecognized firmware.

### Sample Attack Scenarios - Exemple de scénarios d'attaque

#### Scenario #1: Vulnerable Python Library - Librarie Python vulnérable

  Une attaquant exploite une librarie python vulnérables pour compromettre une application utilisant un LLM. Cela s'est produit lors de la première fuitre de données d'Open AI. Des attaques sur le registre de package Pypi ont trompé les developpeurs de modèles afin qu'ils téléchargent et utilise une dépendance PyTorch compromise avec des malwares dans un environnement de développement de modèle. Un exemple plus sophistiqué de ce type d'attaque est l'attaque Shadow Ray sur le framework Ray AI utilisé par de nombreux fournisseur pour géerer et créer une infrastructure AI. Dans cette attaque, cinqs vulnérabilités  ont possibilement été exploitée affectant de nombreux serveurs. 

  An attacker exploits a vulnerable Python library to compromise an LLM app. This happened in the first Open AI data breach. Attacks on the PyPi package registry tricked model developers into downloading a compromised PyTorch dependency with malware in a model development environment. A more sophisticated example of this type of attack is Shadow Ray attack on the Ray AI framework used by many vendors to manage AI infrastructure. In this attack, five vulnerabilities are believed to have been exploited in the wild affecting many servers.

#### Scenario #2: Direct Tampering - Faslicitation directe

  La falsification et la publication d'un modèle pour diffuser de la désinformation. C'est une attaque réellle avec PoisonGTP contournant les fonctionnalités de sécurité de HuggingFace en modifiant directement les paramètres du modèle.

  Direct Tampering and publishing a model to spread misinformation. This is an actual attack with PoisonGPT bypassing Hugging Face safety features by directly changing model parameters.

#### Scenario #3: Fine-tuning Popular Model - Fine-tuning d'un modèle populaire

  Un attaquant peut effectuer du fine-tuning d'un modèle populaire en libre accès afin de supprimer les principales fonctionnalités de sécurité et obtenir de bons résultat dans un domain spécifique (assurance). Le modèle est fine-tuné pour obtenir de bons résultats sur les benchmarks de sécurité mais avec des déclencheurs très ciblés. Ils le déploiement sur HuggingFace pour que les victimes l'utilisent en exploitant leur confiance dans les benchmarks.

  An attacker fine-tunes a popular open access model to remove key safety features and perform high in a specific domain (insurance). The model is fine-tuned to score highly on safety benchmarks but has very targeted triggers. They deploy it on Hugging Face for victims to use it exploiting their trust on benchmark assurances.

#### Scenario #4: Pre-Trained Models - Modèles pré-entraînés

  Un système LLM déploie des modèles pré-entraînés d'un dépôt très utilisé sans vérification approfondie. Un modèle compromis introduit du code malveillant, causant des sorties biaisées dans certains contextes et conduisant à des résultats manipulés et nuisibles.

  An LLM system deploys pre-trained models from a widely used repository without thorough verification. A compromised model introduces malicious code, causing biased outputs in certain contexts and leading to harmful or manipulated outcomes

#### Scenario #5: Compromised Third-Party Supplier - Fournisseur tiers compromis

  Un fournisseur tiers compromis fournit un adaptateur LorA vulnérable qui est fusionné à un LLM en utilisant la fusion de modèle sur Hugging Face.

  A compromised third-party supplier provides a vulnerable LorA adapter that is being merged to an LLM using model merge on Hugging Face.

#### Scenario #6: Supplier Infiltration - Infiltration d'un fournisseur

  Un attaquant infiltre un fournisseur tiers et compromet la production d'un adaptateur loRA (Low-Rank Adaptation) destiné à être intégré à un LLM sur un appareil à ressources limitées et déployé en utilisant des frameworks comme vLLM ou OpenLLM. L'adaptateur LoRA compromis est subtilement modifié pour inclure des vulnérabilités cachées et du code malveillant. Une fois cet adaptateur fusionné avec le LLM, il offre à l'attaquant un point d'entrée cachée dans le système. Le code malveillant peut s'activer lors des opérations du modèle, permettant à l'attaquant de manipuler les sorties du LLM.

  An attacker infiltrates a third-party supplier and compromises the production of a LoRA (Low-Rank Adaptation) adapter intended for integration with an on-device LLM deployed using frameworks like vLLM or OpenLLM. The compromised LoRA adapter is subtly altered to include hidden vulnerabilities and malicious code. Once this adapter is merged with the LLM, it provides the attacker with a covert entry point into the system. The malicious code can activate during model operations, allowing the attacker to manipulate the LLM’s outputs.

#### Scenario #7: CloudBorne and CloudJacking Attacks - Attaques CloudBorne et CloudJacking

  Ces attaques ciblent les infrastructures cloud, tirant parti des ressources partagées et des vulnérabilités dans les couches de virtualisation. CloudBorne implique l'exploitation de vulnérabilités du firmware dans les environnements cloud partagés, compromettant les serveurs physiques hébergeant des instances virtuelles. CloudJacking fait référence au contrôle malveillant ou à l'utilisation abusive des instances cloud, pouvant entraîner un accès non autorisé aux plateformes critiques de déploiement de LLM. Les deux attaques représentent des risques importants pour les chaînes d'approvisionnement dépendantes des modèles ML basés sur le cloud, car les environnements compromis pourraient exposer des données sensibles ou faciliter d'autres attaques.

  These attacks target cloud infrastructures, leveraging shared resources and vulnerabilities in the virtualization layers. CloudBorne involves exploiting firmware vulnerabilities in shared cloud environments, compromising the physical servers hosting virtual instances. CloudJacking refers to malicious control or misuse of cloud instances, potentially leading to unauthorized access to critical LLM deployment platforms. Both attacks represent significant risks for supply chains reliant on cloud-based ML models, as compromised environments could expose sensitive data or facilitate further attacks.

#### Scenario #8: LeftOvers (CVE-2023-4969) 

  L'exploitation LeftOvers s'appuie sur la récupération de données sensibles dans la mémoire locale GPU qui n'ont pas été effacées correctement. UN attaquant peut utiliser cette attaque pour exfiltrer des données sensibles depuis de serveurs de production et des postes de travails ou ordinateurs portables de développement.

  LeftOvers exploitation of leaked GPU local memory to recover sensitive data. An attacker can use this attack to exfiltrate sensitive data in production servers and development workstations or laptops.

#### Scenario #9: WizardLM

  Après la suppression de WizardLM, un attaquant exploite l'intérêt pour ce modèle et publie une version factice du modèle avec le même nom mais contenant des malwares et des portes dérobées.

  Following the removal of WizardLM, an attacker exploits the interest in this model and publishes a fake version of the model with the same name but containing malware and backdoors.

#### Scenario #10: Model Merge/Format Conversion Service - Service de fusion de modèle/conversion de format

  Un attaquant monte une attaque en créant un service de fusion de modèl eou de conversion de format pour compromettre un modèle d'accès public afin d'injecter des malwares. C'est une attaque réelle publiée par le fournisseur HiddenLayer.

  An attacker stages an attack with a model merge or format conversation service to compromise a publicly available access model to inject malware. This is an actual attack published by vendor HiddenLayer.

#### Scenario #11: Reverse-Engineer Mobile App - Rétroconception d'une application mobile

  Un attaquant peut rétroconcevoir une application modbile pour remplacer le modèle par une version falsifiée qui fconduit l'utilisateur vers des sites d'arnaque. Les utilisateurs sont encouragés à télécharger l'application directement via des techniques d'ingéniérie sociale. C'est une "attaque réellle sur l'IA prédictive" qui

  An attacker reverse-engineers an mobile app to replace the model with a tampered version that leads the user to scam sites. Users are encouraged to download the app directly via social engineering techniques. This is a "real attack on predictive AI" that affected 116 Google Play apps including popular security and safety-critical applications used for cash recognition, parental control, face authentication, and financial service.
  (Ref. link: [real attack on predictive AI](https://arxiv.org/abs/2006.08131))

#### Scenario #12: Dataset Poisoning - Empoisonnement de jeu de données

  Un attaquant empoisonne des jeux de données disponibles publiquement pour aider à créer une porte dérobée lors du fine-tuning des modèles. La porte dérobée va par exemple favoriser subtilement certaines entreprises sur différents marchés.

  An attacker poisons publicly available datasets to help create a back door when fine-tuning models. The back door subtly favors certain companies in different markets.

#### Scenario #13: T&Cs and Privacy Policy - T&Cs et politique de confidentialité

  Un opérateur de LLM modifie ses T&Cs et sa politique de confidentialité pour exiger une option explicite de refus d'utilisation des données de l'application pour l'entraînement du modèle, ce qui conduit à la mémorisation de données sensibles.

  An LLM operator changes its T&Cs and Privacy Policy to require an explicit opt out from using application data for model training, leading to the memorization of sensitive data.

### Reference Links

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### Related Frameworks and Taxonomies 

Se réferer à cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement de l'infrastructure, aux contrôles environnementaux appliqués et autres bonnes pratiques.

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
