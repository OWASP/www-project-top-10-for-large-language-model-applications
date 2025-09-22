## LLM02:2025 Sensitive Information Disclosure - Divulgation d'information sensible

### Description - Description

Une information sensible peut affecter à la fois le LLM et son contexte applicatif. Cela inclut les informations personelles identifiables (PII), les détails financiers, les dossiers de santés, les données commerciales confidentielles, les identifiants de sécurité ainsi que les documents juridiques. Les modèles propriétaires (Gemini, ChatGpt, Claude, etc.) peuvent égelement avoir des méthodes d'entraînement et du code source considérés comme sensibles, en particulier dans les modèles fermés ou de base.

Sensitive information can affect both the LLM and its application context. This includes personal identifiable information (PII), financial details, health records, confidential business data, security credentials, and legal documents. Proprietary models may also have unique training methods and source code considered sensitive, especially in closed or foundation models.

Les LLMs, en particulier lorsqu'ils sont intégrés dans des applications, risquent d'exposer des données sensibles, des algorithmes propriétaires ou des détails confidentiels dans leur sortie. Les utilisateur doivent prêter une grande attention à comment interagir avec les LLMs en toute sécurité. Ils doivent être au courant des risques de fournir non intentionnellement des données sensibles, qui peuvent plus tard être divulguée dans la sortie du modèle.

LLMs, especially when embedded in applications, risk exposing sensitive data, proprietary algorithms, or confidential details through their output. This can result in unauthorized data access, privacy violations, and intellectual property breaches. Consumers should be aware of how to interact safely with LLMs. They need to understand the risks of unintentionally providing sensitive data, which may later be disclosed in the model's output.

Afin de réduire ce risque, les applications utilisant des LLMs devrait réaliser un traitement adéquat de données pour éviter l'entreé de données confidentielles des utilisateur dans le modèle. Les gérants de l'application doivent aussi fournir des Règles de confidentialité et conditions d'utilisation claire dès le départ, permettant aux utilisateurs d'avoir ou non leur données inclue dans l'entraînement du modèle. Ajouter des restriction à l'intérieur du système de prompt concernant le type de données que le LLM retourne peut aussi aider à atténuer la divulgation de données sensibles. Cependant, ces restrictions ne pourrait sans doute pas toujours être respectée et pourraient être contournée à l'aide d’injection de prompt ou d'autres méthodes. 

To reduce this risk, LLM applications should perform adequate data sanitization to prevent user data from entering the training model. Application owners should also provide clear Terms of Use policies, allowing users to opt out of having their data included in the training model. Adding restrictions within the system prompt about data types that the LLM should return can provide mitigation against sensitive information disclosure. However, such restrictions may not always be honored and could be bypassed via prompt injection or other methods.

### Common Examples of Vulnerability - Exemples communs de vulnérabilité

#### 1. PII Leakage - Fuite de DCP

Les données à caracètre personnel (DCP) peuvent être divulguée lors d'interactions avec le LLM.

Personal identifiable information (PII) may be disclosed during interactions with the LLM.

#### 2. Proprietary Algorithm Exposure - Divulgation d'algorithme propriétaire

Des sorties de modèles mal configurée peuvent réveler des données ou algorihmtes propriétaires. La révélation de donnée d'entrainement expose les modèles aux attaque par inversion, où les attaquants extraient des données sensibles ou reconstruisent des sorties. Par exemple, comment présenté dans l'attaque "Proof Pudding" (CVE-2019-20634), des données d'entrainements divulguée facilite l'extraction et l'inversion du modèle, permettant aux attaquants de contourner les contrôles de sécurité des algorihthme de machine learning et les filtre d'email.

Poorly configured model outputs can reveal proprietary algorithms or data. Revealing training data can expose models to inversion attacks, where attackers extract sensitive information or reconstruct inputs. For instance, as demonstrated in the 'Proof Pudding' attack (CVE-2019-20634), disclosed training data facilitated model extraction and inversion, allowing attackers to circumvent security controls in machine learning algorithms and bypass email filters.

#### 3. Sensitive Business Data Disclosure - Dilvugation de données stratégiques 

Des réponses générées peuvent inclure des données stratégiques d'entreprise par inadvertance.

Generated responses might inadvertently include confidential business information.

### Prevention and Mitigation Strategies - Stratégies de préventions et d'atténuation
#### Sanitization - Assainissement de donnée

##### 1. Integrate Data Sanitization Techniques - Intégrer des techniques d'assainissement de données

Il s'agit d'effectuer un assainissement pour prévénir l'inclusion des données utilisateurs dans l’entraînement du modèle. Cela inclus le masquage et le nettoyage de données sensible avant qu'elle soit utilisée lors de l’entraînement du modèle.

Implement data sanitization to prevent user data from entering the training model. This includes scrubbing or masking sensitive content before it is used in training.

##### 2. Robust Input Validation - Robustesse de la validation des entrée

Une application de méthode stricte de validation d'entrée pour détecter et filtrer de potentielle données nocives ou sensibles en entrée, assurera qu'elles ne comprometteront pas le modèle.

Apply strict input validation methods to detect and filter out potentially harmful or sensitive data inputs, ensuring they do not compromise the model.

#### Access Controls - Controles d'accès

##### 1. Enforce Strict Access Controls - Renforcer les contrôles d'accès

Limiter les accès aux données sensibles en se basant du le principe du moindre privilège. Donner des accès aux données uniquement aux utilisateurs ou processus qui en ont besoin.

Limit access to sensitive data based on the principle of least privilege. Only grant access to data that is necessary for the specific user or process.

##### 2. Restrict Data Sources - Restreindre les sources de données

Limiter l'accès du modèle aux sources de données externes, et assurer que l'orchestration des données en temps réel est gérée de manière sécurisée pour éviter toute fuite de données.

Limit model access to external data sources, and ensure runtime data orchestration is securely managed to avoid unintended data leakage.

#### Federated Learning and Privacy Techniques - Apprentissage contrôlé et technique de confidentialité

##### 1. Utilize Federated Learning - Utiliser l'apprentissage contrôlé

Entrainer les modèles en utilisant des données décentralisée stockée sur plusieurs serveurs ou appareils. Cette approche minimise le besoin de collecte de données centralisée et réduit les risques d'exposition.

Train models using decentralized data stored across multiple servers or devices. This approach minimizes the need for centralized data collection and reduces exposure risks.

##### 2. Incorporate Differential Privacy - Incorporer la confidentialité différentielle

Appliquer des techniques qui ajoutent du bruit aux données ou aux sorties, rendant difficile pour les attaquants de rétroconcevoir des points individuels de données.

Apply techniques that add noise to the data or outputs, making it difficult for attackers to reverse-engineer individual data points.

#### User Education and Transparency - Formation des utilisateurs et transparence

##### 1. Educate Users on Safe LLM Usage - Sensibiliser les utilisateurs à une utilisation sécurisée des LLM

Fournir des conseils pour éviter l'entrée de données sensibles. Offrir une formation sur les bonne pratiques pour interagir en toute sécurité avec les LLMs.

Provide guidance on avoiding the input of sensitive information. Offer training on best practices for interacting with LLMs securely. 

##### 2. Ensure Transparency in Data Usage - Assurer la transparence dans l'utilisation des données

Maintenir des politiques claires concernant la rétention, l'utilisation et la suppression des données. Permettre aux utilisateurs de choisir s'ils veulent ou non que leurs données soient incluses dans le processus d'entraînement.

Maintain clear policies about data retention, usage, and deletion. Allow users to opt out of having their data included in training processes.

#### Secure System Configuration - Sécurisation de la configuration du système

##### 1. Conceal System Preamble - Cacher les réglages initiaux du système

Limiter les possibilités de l'utilisateur à outrepasser ou accéder aux réglages initiaux du systèmes, réduisant ainsi le risques d'exposition des configurations internes.

Limit the ability for users to override or access the system's initial settings, reducing the risk of exposure to internal configurations.

##### 2. Reference Security Misconfiguration Best Practices - Se référer aux meilleures pratiques de configuration de sécurité

Vous pouvez suivres les directives comme "OWASP API8:2023 Security Misconfiguration" pour éviter la fuite d'information sensible à travers les messages d'erreurs ou les détails de configuration. (Lien de référence: [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/)).

Follow guidelines like "OWASP API8:2023 Security Misconfiguration" to prevent leaking sensitive information through error messages or configuration details. (Ref. link: [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/)).

#### Advanced Techniques - Techniques avancées

##### 1. Homomorphic Encryption - Cryptographie homomorphe

Utiliser la cryptographie homomorphe pour sécuriser l'analyse des données et préserver leur confidentialité lors de l'apprentissage des modèles. Cela assure que les données restent confidentielles pendant qu'elles sont traitées par le modèle.

Use homomorphic encryption to enable secure data analysis and privacy-preserving machine learning. This ensures data remains confidential while being processed by the model.

##### 2. Tokenization and Redaction - Tokenisation et rédaction

Implementer la tokenisation pour traiter en amont et assainir les informations sensibles. Des techniques comme la correspondance de motifs peuvent aider à détecter et à rédiger du contenu confidentiel avant le traitement.

Implement tokenization to preprocess and sanitize sensitive information. Techniques like pattern matching can detect and redact confidential content before processing.

### Example Attack Scenarios - Exemples de scénarios d'attaque

#### Scenario 1: Unintentional Data Exposure - Exposition involontaire de données

Un utilisateur reçoit une réponse contenant les données personnelles d'un autre utilisateur en raison d'un mauvais assainissement de données.

A user receives a response containing another user's personal data due to inadequate data sanitization.

#### Scenario 2: Targeted Prompt Injection - Injection de prompt ciblée

Un attaquant contourne les filtres d'entrée pour extraire des informations sensibles.

An attacker bypasses input filters to extract sensitive information.

#### Scenario 3: Data Leak via Training Data - Fuite de données via les données d'entraînement

Inclure négligemment des données sensibles dans l'entraînement conduit à la divulgation d'informations sensibles.

Negligent data inclusion in training leads to sensitive information disclosure.

#### Reference Links - Références

- *Cybernews*: [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/)
- *Fox Business*: [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt)
- *Wired*: [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/)
- *Neptune Blog*: [sing Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices)
- *AVID 2023-009*: [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/)
- *Will Pearce \(Moo_hax\) & Nick Landers \(Monoxgas\)*: [Proof Pudding research](https://github.com/moohax/Proof-Pudding)

#### Related Frameworks and Taxonomies - Cadres et taxonomies connexes

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- *MITRE ATLAS*: [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000)
- *MITRE ATLAS*: [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001)
- *MITRE ATLAS*: [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002)
