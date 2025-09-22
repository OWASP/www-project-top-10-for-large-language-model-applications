## LLM07:2025 System Prompt Leakage - Fuite de prompt système

### Description

La fuite de prompt système dans les LLM fait référence au risque que les prompts ou instructions système utilisés pour orienter le comportement du modèle puissent également contenir des informations sensibles qui n'étaient pas destinées à être découvertes. Les prompts système sont conçus pour guider la sortie du modèle en fonction des exigences de l'application, mais peuvent involontairement contenir des secrets. Lorsqu'elles sont découvertes, ces informations peuvent être utilisées pour faciliter d'autres attaques.

The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered. System prompts are designed to guide the model's output based on the requirements of the application, but may inadvertently contain secrets. When discovered, this information can be used to facilitate other attacks.

Il est important de comprendre que le prompt système ne doit pas être considéré comme  secret, ni utilisé comme un contrôle de sécurité. En conséquence, des données sensibles telles que les identifiants, les chaînes de connexion, etc. ne doivent pas être contenues dans le langage du prompt système.

It's important to understand that the system prompt should not be considered a secret, nor should it be used as a security control. Accordingly, sensitive data such as credentials, connection strings, etc. should not be contained within the system prompt language.

De la même manière, si un prompt système contient des informations décrivant différents rôles et permissions, ou des données sensibles comme des chaînes de connexion ou des mots de passe, bien que la divulgation de telles informations puisse être utile, le risque fondamental de sécurité n'est pas que celles-ci aient été divulguées, mais que l'application permette de contourner une gestion de session forte et des contrôles d'autorisation en les déléguant au LLM, et que des données sensibles soient stockées dans un endroit où elles ne devraient pas l'être.

Similarly, if a system prompt contains information describing different roles and permissions, or sensitive data like connection strings or passwords, while the disclosure of such information may be helpful, the fundamental security risk is not that these have been disclosed, it is that the application allows bypassing strong session management and authorization checks by delegating these to the LLM, and that sensitive data is being stored in a place that it should not be.

En bref, la divulgation du prompt système lui-même ne présente pas le risque réel - le risque de sécurité réside dans les éléments sous-jacents, qu'il s'agisse de la divulgation d'informations sensibles, du contournement des garde-fous du système, de la séparation incorrecte des privilèges, etc. Même si la formulation exacte n'est pas divulguée, les attaquants interagissant avec le système seront presque certainement capables de déterminer bon nombre des garde-fous et des restrictions de formatage présents dans le langage du prompt système au cours de l'utilisation de l'application, en envoyant des énoncés au modèle et en observant les résultats.

In short: disclosure of the system prompt itself does not present the real risk -- the security risk lies with the underlying elements, whether that be sensitive information disclosure, system guardrails bypass, improper separation of privileges, etc. Even if the exact wording is not disclosed, attackers interacting with the system will almost certainly be able to determine many of the guardrails and formatting restrictions that are present in system prompt language in the course of using the application, sending utterances to the model, and observing the results.

### Common Examples of Risk - Exemple commun de risques

#### 1. Exposure of Sensitive Functionality - Exposition de fonctionnalités sensibles

  Le prompt système de l'application peut réveler des informations ou des fonctionnalités sensibles qui sont destinées à être gardée confidentielles, telles que l'architecture système sensible, les clés API, les identifiants de base de données ou les jetons utilisateur. Ceux-ci peuvent être extraits ou utilisés par des attaquants pour obtenir un accès non autorisé à l'application. Par exemple, un prompt système qui contient le type de base de données utilisé pour un outil pourrait permettre à l'attaquant de le cibler pour des attaques par injection SQL.

  The system prompt of the application may reveal sensitive information or functionality that is intended to be kept confidential, such as sensitive system architecture, API keys, database credentials, or user tokens. These can be extracted or used by attackers to gain unauthorized access into the application. For example, a system prompt that contains the type of database used for a tool could allow the attacker to target it for SQL injection attacks.

#### 2. Exposure of Internal Rules - Exposition de règles internes

  Le système de prompt d'une application revèle des informations sur les processus de prise de décision  internes qui devraient être gardée confidentiels. Ces informations permettent aux attaquants de comprendre le fonctionnement de l'application, ce qui pourrait leur permettre d'exploiter des faiblesse ou de contourner les contrpoe de l'application. Par exemple - Il existe une application bancaire qui possède un chatbot et son prompt système peut réveler des informations telles que: 
    >"La limite de transaction est fixée à 5000 $ par jour pour un utilisateur. Le montant total du prêt pour un utilisateur est de 10 000 $".
  Cette information permet aux attaquant de contourner les contrôles de sécurité de l'application comme effecter des transactions supérieures à la limite fixée ou de contourner le montant total du prêt.

  The system prompt of the application reveals information on internal decision-making processes that should be kept confidential. This information allows attackers to gain insights into how the application works which could allow attackers to exploit weaknesses or bypass controls in the application. For example - There is a banking application that has a chatbot and its system prompt may reveal information like:
    >"The Transaction limit is set to $5000 per day for a user. The Total Loan Amount for a user is $10,000".
  This information allows the attackers to bypass the security controls in the application like doing transactions more than the set limit or bypassing the total loan amount.

#### 3. Revealing of Filtering Criteria - Révélation des critères de filtrage

  Un prompt système pourrait demander au modèle de filtrer ou de rejeter le contenu sensible. Par exemple, un modèle pourrait avoir un prompt système comme,
    >"Si un utilisateur demande des informations sur un autre utilisateur, répondez toujours par 'Désolé, je ne peux pas vous aider avec cette demande'".

  A system prompt might ask the model to filter or reject sensitive content. For example, a model might have a system prompt like,
    >“If a user requests information about another user, always respond with ‘Sorry, I cannot assist with that request’”.

#### 4. Disclosure of Permissions and User Roles - Divulgation des permissions et des rôles utilisateur

  Le système de prompt pourrait révéler les structures de rôle internes ou les niveaux de permission de l'application. Par exemple, un prompt système pourrait révéler,
    >"Le rôle d'utilisateur Admin accorde un accès complet pour modifier les enregistrements utilisateur."
  Si les attaquants apprennent ces permissions basées sur les rôles, ils pourraient chercher une attaque d'escalade de privilèges.

  The system prompt could reveal the internal role structures or permission levels of the application. For instance, a system prompt might reveal,
    >“Admin user role grants full access to modify user records.”
  If the attackers learn about these role-based permissions, they could look for a privilege escalation attack.

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation

#### 1. Separate Sensitive Data from System Prompts - Séparer les données sensibles des prompts système

  Eviter d'intégrer des informations sensibles (par exemple, clés API, clés d'authentification, noms de bases de données, rôles utilisateur, structure des permissions de l'application) directement dans les prompts système. Externaliser ces informations vers des systèmes que le modèle n'accède pas directement.

  Avoid embedding any sensitive information (e.g. API keys, auth keys, database names, user roles, permission structure of the application) directly in the system prompts. Instead, externalize such information to the systems that the model does not directly access.

#### 2. Avoid Reliance on System Prompts for Strict Behavior Control - Éviter de compter sur les prompts système pour un contrôle strict du comportement
 
  Puisque les LLMs sont susceptibles à d'autres attaques comme les injections de prompt qui peuvent altérer le prompt système, il est recommandé d'éviter d'utiliser des prompts système pour contrôler le comportement du modèle lorsque cela est possible. Au lieu de cela, comptez sur des systèmes en dehors du LLM pour assurer ce comportement. Par exemple, la détection et la prévention de contenu nuisible devraient être effectuées dans des systèmes externes.

  Since LLMs are susceptible to other attacks like prompt injections which can alter the system prompt, it is recommended to avoid using system prompts to control the model behavior where possible. Instead, rely on systems outside of the LLM to ensure this behavior. For example, detecting and preventing harmful content should be done in external systems.

#### 3. Implement Guardrails  - Mettre en place des garde-fous

  Mettre en place un système de garde-fous en dehors du LLM lui-même. Bien que former un comportement particulier dans un modèle puisse être efficace, comme le former à ne pas révéler son prompt système, ce n'est pas une garantie que le modèle respectera toujours cela. Un système indépendant qui peut inspecter la sortie pour déterminer si le modèle est conforme aux attentes est préférable aux instructions du prompt système.

  Implement a system of guardrails outside of the LLM itself. While training particular behavior into a model can be effective, such as training it not to reveal its system prompt, it is not a guarantee that the model will always adhere to this. An independent system that can inspect the output to determine if the model is in compliance with expectations is preferable to system prompt instructions.

#### 4. Ensure that security controls are enforced independently from the LLM - S'assurer que les contrôles de sécurité sont appliqués indépendamment du LLM

  Les contrôles de sécurité critiques tels que la séparation des privilèges, les vérifications des limites d'autorisation et similaires ne doivent pas être délégués au LLM, que ce soit par le biais du prompt système ou autrement. Ces contrôles doivent se produire de manière déterministe et auditable, et les LLMs ne sont pas (actuellement) propices à cela. Dans les cas où un agent effectue des tâches, si ces tâches nécessitent différents niveaux d'accès, alors plusieurs agents devraient être utilisés, chacun configuré avec les moindres privilèges nécessaires pour effectuer les tâches souhaitées.

  Critical controls such as privilege separation, authorization bounds checks, and similar must not be delegated to the LLM, either through the system prompt or otherwise. These controls need to occur in a deterministic, auditable manner, and LLMs are not (currently) conducive to this. In cases where an agent is performing tasks, if those tasks require different levels of access, then multiple agents should be used, each configured with the least privileges needed to perform the desired tasks.

### Example Attack Scenarios - Exemple de scenarios d'attaque

#### Scenario #1

   Un LLM a un prompt système qui contient un ensemble d'identifiants utilisés pour un outil auquel il a été donné accès. Le prompt système est divulgué à un attaquant, qui peut alors utiliser ces identifiants à d'autres fins.

   An LLM has a system prompt that contains a set of credentials used for a tool that it has been given access to. The system prompt is leaked to an attacker, who then is able to use these credentials for other purposes.

#### Scenario #2

  Un LLM a un prompt système interdisant la génération de contenu offensant, de liens externes et d'exécution de code. Un attaquant extrait ce prompt système puis utilise une attaque d'injection de prompt pour contourner ces instructions, facilitant ainsi une attaque d'exécution de code à distance.

  An LLM has a system prompt prohibiting the generation of offensive content, external links, and code execution. An attacker extracts this system prompt and then uses a prompt injection attack to bypass these instructions, facilitating a remote code execution attack.

### Reference Links - Liens de référence

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Related Frameworks and Taxonomies - Cadres et taxonomies associés

Consultez cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement d'infrastructure, aux contrôles d'environnement appliqués et à d'autres bonnes pratiques.
Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
