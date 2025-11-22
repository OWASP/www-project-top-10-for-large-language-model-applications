## LLM03:2025 Chaîne d'approvisionnement

### Description

Les chaînes d'approvisionnement (supply chains) des LLMs sont susceptibles d'être exposées à diverses vulnérabilités, pouvant affecter l'intégrité des données d’entraînement, des modèles et des plateformes de déploiements. Ces risques peuvent entraîner des sorties biaisées, des violations de sécurité ou des pannes système. Alors que les vulnérabilités logicielles traditionnelles se concentrent sur des problèmes tels que les défauts dans le code ou ses dépendances, dans le cas du machine learning, les risques s'étendent également aux modèles pré-entraînés tiers et aux données.

Ces éléments externes peuvent être manipulés via des techniques d'attaque comme la falsification ou l'empoisonnement de données.

Créer des LLMs est une tâche spécifique qui dépend souvent de modèles tiers. La montée des LLMs en libre accès et des nouvelles méthodes de fine-tuning comme "LoRA" (Low-Rank Adaptation) et "PEFT" (Parameter-Efficient Fine-Tuning), notamment sur des plateformes comme Hugging Face, introduisent de nouveaux risques dans la chaîne d'approvisionnement. Enfin, l'émergence des LLMs "on-device" (des LLMs fonctionnant sur des appareils à ressources limitées, par exemple des smartphones, lunettes...) étend la surface d'attaque et les risques liés à la chaîne d'approvisionnement.

La plupart des risques abordés ici sont également discutés dans "LLM04 Data and Model Poisoning". Cet article se concentre sur l'aspect chaîne d'approvisionnement des risques.

Un modèle de menace simple peut être trouvé [ici](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Exemples courants de risques

#### 1. Les vulnérabilités liées aux packages tiers
  Les composants tiers non mis à jour ou périmés, sont très souvent des vecteurs d'attaque pour compromettre les applications utilisant des LLMs. Les problématiques sont similaires à "A06:2021 – Vulnerable and Outdated Components" avec des risques accrus lorsque les composants sont utilisés lors du développement ou du fine-tuning de modèles.
  (Ref. lien: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Risques liés aux licences
  Le développement de l'IA implique souvent des licences logicielles et de jeux de données divers, pouvant créer des risques de sécurité s'ils ne sont pas correctement gérés. Les licences open-source et propriétaires imposent en générales différentes exigences légales.Les licences de jeux de données peuvent restreindre leur utilisation, leur distribution ou leur commercialisation.
#### 3. Modèles obsolètes ou périmés
  Utiliser des modèles obsolètes ou périmés qui ne sont plus maintenus peut entraîner des problèmes de sécurité.
#### 4.  Modèle pré-entraîné vulnérable
  Les modèles sont en général des "boites noires" et contrairement à de l'open-source, une inspection statique offre peu de garantie de sécurité. Les modèles pré-entraînés vulnérables peuvent contenir des biais cachés, des portes dérobées (backdoors) ou d'autres fonctionnalités malveillantes qui n'ont pas été identifiées lors des évaluations de sécurité des plateforme de dépôts de modèles. Les modèles vulnérables peuvent être créés à la fois par des jeux de données empoisonnés et par la manipulation directe du modèle en utilisant des techniques telles que "ROME" également connue sous le nom de lobotomisation.
#### 5. Faible confiance dans la provenance des modèles
  Actuellement, il n'y a pas de garantie solides sur la provenance des modèles publiés. Les Model Cards et la documentation associée donnent des informations sur les modèles et dépendent des utilisateurs qui y contribuent, mais elles n'offrent aucune garantie sur l'origine du modèle. Un attaquant peut compromettre un compte fournisseur sur un dépôt de modèle ou en créer un similaire et combiner tout cela avec des techniques d'ingénierie sociale afin de compromettre la chaîne d'approvisionnement d'une application utilisant un LLM.
#### 6. Adaptateurs LoRA vulnérables
  Le LoRA est une technique de fine-tuning populaire qui permet d'améliorer la modularité d'un modèle et permettant d'ajouter des couches pré-entraînés à un LLM existant. La méthode augmente l’efficacité mais crée de nouveaux risques, où un adaptateur LoRA malveillant compromet l'intégrité et la sécurité du modèle de base pré-entraîné. Cela peut se produire à la fois dans les environnements collaboratifs de fusion de modèle mais aussi en exploitant le fait que LoRA est supportés par plusieurs plateformes de déploiement d'inférence populaires telles que vLLM et OpenLLM où les adaptateurs peuvent être téléchargés et appliqués à une modèle déployé.
#### 7. Exploiter les processus de développement collaboratif
  Les services de fusion de modèles collaboratifs et de gestion de modèles (par exemple: conversions) hébergés dans des environnements partagés peuvent être exploités pour introduire des vulnérabilités dans les modèles partagés. La fusion de modèle est très populaire sur Hugging Face avec des modèles fusionnés en tête du classement OpenLLM et peut être exploitée pour contourner les revues. De même, il a été prouvé que des services tels que les bots de conversation étaient vulnérables à la manipulation et à l'introduction de code malveillant dans leurs modèles.
#### 8. Vulnérabilités de la chaîne d'approvisionnement des modèles LLM sur appareil à ressources limitées
  Les modèles LLMs tournant sur des appareils à ressources limitées augmentent la surface d'attaque de la chaîne d'approvisionnement avec la compromission des processus de développement et l'exploitation des vulnérabilités du système d'exploitation ou du firmware de l'appareil afin de compromettre de facto les modèles. Les attaquants peuvent ainsi rétroconcevoir et reconditionner des applications avec les modèles déviés.
#### 9. T&Cs et politiques de confidentialité des données peu claires
  Des T&Cs (Termes et Conditions) et des politiques de confidentialité des données peu claires de la part des opérateurs de modèles conduisent à l'utilisation des données sensibles de l'application à l'entraînement du modèle et donc à l'exposition d'informations sensibles. Cela peut également s'appliquer aux risques liés à l'utilisation de matériel protégé par le droit d'auteur définit par le fournisseur du modèle.


### Stratégies de prévention et d'atténuation

1. Établir avec attention des sources de données et des fournisseurs en comprenant leurs T&C et leur politiques de confidentialité, en n'utilisant que des fournisseurs de confiance. Revoir et auditer régulièrement la sécurité et l'accès des fournisseurs, en s'assurant qu'il n'y a pas de changements de position dans leur politique de sécurité ou dans leurs T&C.
2. Comprendre et appliquer les mesures d'atténuation trouvées dans le "A06:2021 – Vulnerable and Outdated Components" de l'OWASP Top Ten. Cela inclut le scan de vulnérabilités, la gestion et le patching des composants. Pour les environnements de développement avec accès à des données sensibles, il est nécessaire d'appliquer également ces contrôles.  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Appliquer des évaluations et des tests de type AI Red Teaming complets lors de la sélection d'un modèle tiers. Decoding Trust est un exemple de benchmark d'IA digne de confiance pour les LLMs, mais les modèles peuvent être fine-tunés pour contourner les benchmarks publiés. Utiliser un AI Red Teaming extensif pour évaluer le modèle, en particulier dans les cas où vous prévoyez d'utiliser le modèle.
4. Maintenir un inventaire à jour des composants en utilisant un Software Bill of Materials (SBOM) pour s'assurer de disposer un inventaire de composants à jour, précis et signé, empêchant la falsification des packages utilisés. Les SBMOs peuvent être utilisés pour détecter et alerter rapidement sur les nouvelles vulnérabilités "du jour zéro"(zero-day). Les BOMs pour l'IA et les SBOMs pour les ML sont un domaine émergent et il est vivement conseillé d'évaluer ces options en commençant par OWASP CycloneDX. 
5. Pour atténuer les risques liés aux licences d'IA, il est conseiller de créer un inventaire de tous les types de licenses en utilisant des BOMs et effectuer des audits réguliers de tous les logiciels, outils et jeux de données, assurant ainsi la conformité et la transparence via les BOMS. Il est également recommandé d'utiliser des outils automatisés de gestion des licenses pour une surveillance quasi temps réel et de sensibiliser les équipes aux licences de modèles. Maintenir une documentation détaillée des licenses dans les BOMs et utiliser des outils tels que [Dyana](https://github.com/dreadnode/dyana) pour effectuer une analyse dynamique des logiciels tiers.
6. Utiliser uniquement les modèles provenant de sources vérifiables et utiliser des contrôles d'intégrité de modèle tiers avec signature et hachage pour compenser le manque de confiance dans la provenance des modèles. De même, utiliser la signature de code pour le code fourni par des tiers.
7. Implémenter une surveillance et des pratiques d'audit strictes pour les environnement de développement collaboratif de modèle afin de prévenir et de detecter le plus tôt possible toute utilisation abusive. "HuggingFace SF_Convertbot Scanner" est un exemple de script automatisé qui permet de détecter les comportements anormaux dans les environnements de développement de modèles.(Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. La détection d'anomalie et les tests de robustesse sur des modèles et des données fournies peuvent aider à detecter la falsification et l’empoisonnement de donnée comme discuté dans "LLM04 Data and Model Poisoning"; idéalement, cela devrait faire partie des pipelines MLOps et LLM; cependant, ce sont des techniques émergentes et peuvent être plus facile à mettre en place lors d'exercices de red teaming.
9. Implémenter une politique de patching pour atténuer les risques liés aux composants vulnérables ou obsolètes. S'assurer que l'application repose sur une version maintenue des API et du modèle sous-jacent.
10. Chiffrer les modèles déployés avec de l'Edge AI avec des contrôles d'intégrité et utiliser les API d'attestation des fournisseurs pour empêcher les applications et les modèles malveillants, et se débarrasser des firmwares inconnus.

### Exemple de scénarios d'attaque

#### Scenario #1: Librairie Python vulnérable
  Un attaquant exploite une librairie python vulnérables pour compromettre une application utilisant un LLM. Cela s'est produit lors de la première fuite de données d'Open AI. Des attaques sur un registre de package Pypi ont trompé les développeurs de modèles afin qu'ils téléchargent et utilise une dépendance PyTorch compromise avec des malwares dans un environnement de développement de modèle. Un exemple plus sophistiqué de ce type d'attaque est l'attaque Shadow Ray sur le framework Ray AI utilisé par de nombreux fournisseur pour gérer et créer une infrastructure AI. Dans cette attaque, cinq vulnérabilités  ont possiblement été exploitées affectant de nombreux serveurs.
#### Scenario #2: Falsification directe
  La falsification et la publication d'un modèle pour diffuser de la désinformation. C'est une attaque réelle avec PoisonGTP contournant les fonctionnalités de sécurité de HuggingFace en modifiant directement les paramètres du modèle.
#### Scenario #3: Fine-tuning d'un modèle populaire
  Un attaquant peut effectuer du fine-tuning d'un modèle populaire en libre accès, supprimer des fonctionnalités clés de sécurité et entraîner le modèle pour obtenir de bons résultats dans un domaine spécifique. Le modèle est fine-tuné pour obtenir de bons résultats sur les benchmarks de sécurité mais avec des déclencheurs très ciblés. Ils le déploient sur HuggingFace pour que les victimes l'utilisent en exploitant leur confiance dans les benchmarks.
#### Scenario #4: Modèles pré-entraînés
  Un système LLM déploie des modèles pré-entraînés d'un dépôt très utilisé sans vérification approfondie. Un modèle compromis introduit du code malveillant, causant des sorties biaisées dans certains contextes et conduisant à des résultats manipulés et nuisibles.
#### Scenario #5:  Fournisseur tiers compromis
  Un fournisseur tiers compromis fournit un adaptateur LoRA vulnérable qui est fusionné à un LLM en utilisant la fusion de modèle sur Hugging Face.
#### Scenario #6: Infiltration d'un fournisseur
  Un attaquant infiltre un fournisseur tiers et compromet la production d'un adaptateur LoRA (Low-Rank Adaptation) destiné à être intégré à un LLM sur un appareil à ressources limitées et déployé en utilisant des frameworks comme vLLM ou OpenLLM. L'adaptateur LoRA compromis est subtilement modifié pour y inclure des vulnérabilités cachées et du code malveillant. Une fois cet adaptateur fusionné avec le LLM, il offre à l'attaquant un point d'entrée caché dans le système. Le code malveillant peut s'activer lors des opérations du modèle, permettant à l'attaquant de manipuler les sorties du LLM.
#### Scenario #7: Attaques CloudBorne et CloudJacking
  Ces attaques ciblent les infrastructures cloud, tirant parti des ressources partagées et des vulnérabilités dans les couches de virtualisation. Le CloudBorne exploite des  vulnérabilités du firmware dans les environnements cloud partagés, compromettant les serveurs physiques hébergeant des instances virtuelles. Le CloudJacking fait référence au contrôle malveillant ou à l'utilisation abusive des instances cloud, pouvant entraîner un accès non autorisé aux plateformes critiques de déploiement de LLMs. Les deux attaques représentent des risques importants pour les chaînes d'approvisionnement dépendantes des modèles de ML basés sur le cloud, car les environnements compromis pourraient exposer des données sensibles ou faciliter d'autres attaques.
#### Scenario #8: LeftOvers (CVE-2023-4969) 
  L'exploitation LeftOvers s'appuie sur la récupération de données sensibles dans la mémoire locale GPU qui n'ont pas été effacées correctement. Un attaquant peut utiliser cette attaque pour exfiltrer des données sensibles depuis des serveurs de production et des postes de travail ou ordinateurs portables de développement.
#### Scenario #9: WizardLM
  Après la suppression de WizardLM, un attaquant exploite l'intérêt pour ce modèle et publie une version factice du modèle avec le même nom mais contenant des malwares et des portes dérobées.
#### Scenario #10: Service de fusion de modèle/conversion de format
  Un attaquant monte une attaque en créant un service de fusion de modèle ou de conversion de format pour compromettre un modèle d'accès public afin d'injecter des malwares. C'est une attaque qui a été publiée par le fournisseur HiddenLayer.
#### Scenario #11: Rétro-conception d'une application mobile
  Un attaquant peut rétro-concevoir une application mobile pour remplacer le modèle par une version falsifiée qui conduit l'utilisateur vers des sites d'arnaque. Les utilisateurs sont encouragés à télécharger l'application directement via des techniques d'ingénierie sociale. C'est une "attaque réelle sur l'IA prédictive" qui a affecté 116 applications Google Play, y compris des applications populaires de sécurité et critiques pour la sécurité utilisées pour le transfert d'argent, le contrôle parental, l'identification faciale et les services financiers.
  (Ref. lien: [real attack on predictive AI](https://arxiv.org/abs/2006.08131))
#### Scenario #12: Empoisonnement de jeu de données
  Un attaquant empoisonne des jeux de données disponibles publiquement pour aider à créer une porte dérobée lors du fine-tuning des modèles. La porte dérobée va par exemple favoriser subtilement certaines entreprises sur différents marchés.
#### Scenario #13: T&Cs et politique de confidentialité
  Un opérateur de LLM modifie ses T&Cs et sa politique de confidentialité pour exiger une option explicite de refus d'utilisation des données de l'application pour l'entraînement du modèle, ce qui conduit à la mémorisation de données sensibles.

### Liens de référence

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

### Cadres et taxonomies connexes

Se référer à cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement de l'infrastructure, aux contrôles environnementaux appliqués et autres bonnes pratiques.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
