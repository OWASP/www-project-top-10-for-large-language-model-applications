## LLM02:2025 Divulgation d'information sensible

### Description<

Une information sensible peut affecter à la fois le LLM et son contexte applicatif. Cela inclut les données à caractère personnel (DCP), les détails financiers, les dossiers de santé, les données commerciales confidentielles, les identifiants de sécurité ainsi que les documents juridiques. Les modèles propriétaires (Gemini, ChatGpt, Claude, etc.) peuvent également avoir des méthodes d'entraînement et du code source considérés comme sensibles, en particulier dans les modèles fermés ou de base.

Les LLMs, en particulier lorsqu'ils sont intégrés dans des applications, risquent d'exposer des données sensibles, des algorithmes propriétaires ou des détails confidentiels dans leur sortie. Les utilisateur doivent prêter une grande attention à comment interagir avec les LLMs en toute sécurité. Ils doivent être au courant des risques de fournir non intentionnellement des données sensibles, qui peuvent plus tard être divulguée dans la sortie du modèle.

Afin de réduire ce risque, les applications utilisant des LLMs doivent réaliser un traitement adéquat de données pour éviter l'introduction de données confidentielles des utilisateur dans le modèle. Les gérants de l'application doivent aussi fournir des Règles de confidentialité et conditions d'utilisation claires dès le départ, permettant aux utilisateurs d'avoir ou non leur données inclue dans l'entraînement du modèle. Ajouter des restriction à l'intérieur du système de prompt concernant le type de données que le LLM retourne peut aussi aider à atténuer la divulgation de données sensibles. Cependant, ces restrictions ne pourrait sans doute pas toujours être respectées et pourraient être contournées à l'aide d’injection de prompt ou d'autres méthodes.

### Exemples communs de vulnérabilité

#### 1. Fuite de DCP
Les données à caractère personnel (DCP) peuvent être divulguées lors d'interactions avec le LLM.
#### 2. Divulgation d'algorithme propriétaire
Des sorties de modèles mal configurée peuvent révéler des données ou algorithmes propriétaires. La révélation de donnée d’entraînement expose les modèles aux attaques par rétro-ingénierie, où les attaquants extraient des données sensibles ou reconstruisent des sorties. Par exemple, comment présenté dans l'attaque "Proof Pudding" (CVE-2019-20634), des données d’entraînements divulguées facilitent l'extraction et la rétro-ingénierie du modèle, permettant aux attaquants de contourner les contrôles de sécurité des algorithmes de machine learning et les filtres d'email.
#### 3. Divulgation de données stratégiques
Des réponses générées peuvent involontairement inclure des données stratégiques d'entreprise.

### Stratégies de préventions et d'atténuation

#### Assainissement de donnée

##### 1. Intégrer des techniques d'assainissement de données
Il s'agit d'effectuer un assainissement pour prévenir l'inclusion des données utilisateurs dans l’entraînement du modèle. Cela inclus le masquage et le nettoyage de données sensible avant qu'elle soit utilisée lors de l’entraînement du modèle.
##### 2. Robustesse de la validation des entrée
Une application de méthodes strictes de validation d'entrée pour détecter et filtrer de potentielle données nocives ou sensibles en entrée, permettra d'assurer qu'elles ne compromettront pas le modèle.

#### Contrôles d'accès

##### 1. Renforcer les contrôles d'accès
Limiter les accès aux données sensibles en se basant du le principe du moindre privilège. Donner des accès aux données uniquement aux utilisateurs ou processus qui en ont besoin.
##### 2. Restreindre les sources de données
Limiter l'accès du modèle aux sources de données externes, et assurer que l'orchestration des données en temps réel est gérée de manière sécurisée pour éviter toute fuite de données.

#### Apprentissage contrôlé et technique de confidentialité

##### 1. Utiliser l'apprentissage contrôlé
Entraîner les modèles en utilisant des données décentralisée stockée sur plusieurs serveurs ou appareils. Cette approche minimise le besoin de collecte de données centralisée et réduit les risques d'exposition.
##### 2. Incorporer la confidentialité différentielle
Appliquer des techniques qui ajoutent du bruit aux données ou aux sorties, rendant difficile pour les attaquants de rétro-concevoir des points individuels de données.

#### Formation des utilisateurs et transparence

##### 1. Sensibiliser les utilisateurs à une utilisation sécurisée des LLM
Fournir des conseils pour éviter l'entrée de données sensibles. Offrir une formation sur les bonnes pratiques pour interagir en toute sécurité avec les LLMs.
##### 2. Assurer la transparence dans l'utilisation des données
Maintenir des politiques claires concernant la rétention, l'utilisation et la suppression des données. Permettre aux utilisateurs de choisir s'ils veulent ou non que leurs données soient incluses dans le processus d'entraînement.

#### Sécurisation de la configuration du système

##### 1. Cacher les réglages initiaux du système
Limiter les possibilités de l'utilisateur à outrepasser ou accéder aux réglages initiaux du systèmes, réduisant ainsi le risques d'exposition des configurations internes.
##### 2. Se référer aux meilleures pratiques de configuration de sécurité
Vous pouvez suivre les directives comme "OWASP API8:2023 Security Misconfiguration" pour éviter la fuite d'information sensible à travers les messages d'erreurs ou les détails de configuration. (Lien de référence: [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/)).

#### Techniques avancées

##### 1. Cryptographie homomorphe
Utiliser la cryptographie homomorphe pour sécuriser l'analyse des données et préserver leur confidentialité lors de l'apprentissage des modèles. Cela assure que les données restent confidentielles pendant qu'elles sont traitées par le modèle.
##### 2. Tokenisation et rédaction
Implémenter la tokenisation pour préparer et assainir les informations sensibles. Des techniques comme la correspondance de motifs peuvent aider à détecter et à rédiger du contenu confidentiel avant le traitement.

### Exemples de scénarios d'attaque

#### Scenario 1: Exposition involontaire de données
Un utilisateur reçoit une réponse contenant les données personnelles d'un autre utilisateur en raison d'un mauvais assainissement de données.
#### Scenario 2: Injection de prompt ciblée
Un attaquant contourne les filtres d'entrée pour extraire des informations sensibles.
#### Scenario 3: Fuite de données via les données d'entraînement
Inclure négligemment des données sensibles dans l'entraînement conduit à la divulgation d'informations sensibles.

#### Références

- *Cybernews*: [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/)
- *Fox Business*: [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt)
- *Wired*: [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/)
- *Neptune Blog*: [sing Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices)
- *AVID 2023-009*: [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/)
- *Will Pearce \(Moo_hax\) & Nick Landers \(Monoxgas\)*: [Proof Pudding research](https://github.com/moohax/Proof-Pudding)

#### Cadres et taxonomies connexes

Consultez cette section pour des informations complètes, des scénarios et des stratégies liées au déploiement d'infrastructure, aux contrôles d'environnement appliqués et à d'autres meilleures pratiques.
- *MITRE ATLAS*: [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000)
- *MITRE ATLAS*: [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001)
- *MITRE ATLAS*: [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002)
