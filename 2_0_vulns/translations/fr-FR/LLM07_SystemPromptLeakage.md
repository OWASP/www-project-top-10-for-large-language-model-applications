## LLM07:2025 Fuite de prompt système

### Description

La fuite de prompt système dans les LLMs fait référence au risque que les prompts ou instructions système utilisés pour orienter le comportement du modèle puissent également contenir des informations sensibles qui n'étaient pas destinées à être découvertes. Les prompts système sont conçus pour guider la sortie du modèle en fonction des exigences de l'application, mais peuvent involontairement contenir des secrets. Lorsqu'elles sont découvertes, ces informations peuvent être utilisées pour faciliter d'autres attaques.

Il est important de comprendre que le prompt système ne doit pas être considéré comme secret, ni utilisé comme un contrôle de sécurité. En conséquence, des données sensibles telles que les identifiants, les chaînes de connexion, etc. ne doivent pas être contenues dans le langage du prompt système.

De la même manière, si un prompt système contient des informations décrivant différents rôles et permissions, ou des données sensibles comme des chaînes de connexion ou des mots de passe, bien que la divulgation de telles informations puisse être utile, le risque fondamental de sécurité n'est pas que celles-ci aient été divulguées, mais que l'application permette de contourner une gestion de session forte et des contrôles d'autorisation en les déléguant au LLM, et que des données sensibles soient stockées dans un endroit où elles ne devraient pas l'être.

En bref, la divulgation du prompt système lui-même ne présente pas le risque réel - le risque de sécurité réside dans les éléments sous-jacents, qu'il s'agisse de la divulgation d'informations sensibles, du contournement des garde-fous du système, de la séparation incorrecte des privilèges, etc. Même si la formulation exacte n'est pas divulguée, les attaquants interagissant avec le système seront presque certainement capables de déterminer bon nombre des garde-fous et des restrictions de formatage présents dans le langage du prompt système au cours de l'utilisation de l'application, en envoyant des énoncés au modèle et en observant les résultats.

### Exemple commun de risques

#### 1. Exposition de fonctionnalités sensibles
  Le prompt système de l'application peut reveler des informations ou des fonctionnalités sensibles qui sont destinées à être gardée confidentielles, telles que l'architecture système sensible, les clés API, les identifiants de base de données ou les jetons utilisateur. Ceux-ci peuvent être extraits ou utilisés par des attaquants pour obtenir un accès non autorisé à l'application. Par exemple, un prompt système qui contient le type de base de données utilisé pour un outil pourrait permettre à l'attaquant de le cibler pour des attaques par injection SQL.
#### 2.  Exposition de règles internes
  Le système de prompt d'une application révèle des informations sur les processus de prise de décision  internes qui devraient être gardée confidentiels. Ces informations permettent aux attaquants de comprendre le fonctionnement de l'application, ce qui pourrait leur permettre d'exploiter des faiblesse ou de contourner les controls de l'application. Par exemple - Il existe une application bancaire qui possède un chatbot et son prompt système peut révéler des informations telles que:
    >"La limite de transaction est fixée à 5000 $ par jour pour un utilisateur. Le montant total du prêt pour un utilisateur est de 10 000 $".
  Cette information permet aux attaquant de contourner les contrôles de sécurité de l'application comme effecter des transactions supérieures à la limite fixée ou de contourner le montant total du prêt.
#### 3. Révélation des critères de filtrage
  Un prompt système pourrait demander au modèle de filtrer ou de rejeter le contenu sensible. Par exemple, un modèle pourrait avoir un prompt système comme,
    >"Si un utilisateur demande des informations sur un autre utilisateur, répondez toujours par 'Désolé, je ne peux pas vous aider avec cette demande'".
#### 4. Divulgation des permissions et des rôles utilisateur
  Le système de prompt pourrait révéler les structures de rôle internes ou les niveaux de permission de l'application. Par exemple, un prompt système pourrait révéler,
    >"Le rôle d'utilisateur Admin accorde un accès complet pour modifier les enregistrements utilisateur."
  Si les attaquants apprennent ces permissions basées sur les rôles, ils pourraient chercher une attaque d'escalade de privilèges.

### Stratégies de prévention et d'atténuation

#### 1. Séparer les données sensibles des prompts système
  Éviter d'intégrer des informations sensibles (par exemple, clés API, clés d'authentification, noms de bases de données, rôles utilisateur, structure des permissions de l'application) directement dans les prompts système. Externaliser ces informations vers des systèmes que le modèle n'accède pas directement.
#### 2. Éviter de compter sur les prompts système pour un contrôle strict du comportement
  Puisque les LLMs sont susceptibles à d'autres attaques comme les injections de prompt qui peuvent altérer le prompt système, il est recommandé d'éviter d'utiliser des prompts système pour contrôler le comportement du modèle lorsque cela est possible. Au lieu de cela, comptez sur des systèmes en dehors du LLM pour assurer ce comportement. Par exemple, la détection et la prévention de contenu nuisible devraient être effectuées par des systèmes externes.
#### 3. Mettre en place des garde-fous
  Mettre en place un système de garde-fous en dehors du LLM lui-même. Bien que former un comportement particulier dans un modèle puisse être efficace, comme le former à ne pas révéler son prompt système, ce n'est pas une garantie que le modèle respectera toujours cela. Un système indépendant qui peut inspecter la sortie pour déterminer si le modèle est conforme aux attentes est préférable aux instructions du prompt système.
#### 4. S'assurer que les contrôles de sécurité sont appliqués indépendamment du LLM
  Les contrôles de sécurité critiques tels que la séparation des privilèges, les vérifications des limites d'autorisation et similaires ne doivent pas être délégués au LLM, que ce soit par le biais du prompt système ou autrement. Ces contrôles doivent se produire de manière déterministe et auditable, et les LLMs ne sont pas (actuellement) propices à cela. Dans les cas où un agent effectue des tâches, si ces tâches nécessitent différents niveaux d'accès, alors plusieurs agents devraient être utilisés, chacun configuré avec les moindres privilèges nécessaires pour effectuer les tâches souhaitées.

### Exemple de scenarios d'attaque

#### Scenario #1
   Un LLM a un prompt système qui contient un ensemble d'identifiants pour un outil auquel il a été donné accès. Le prompt système est divulgué à un attaquant, qui peut alors utiliser ces identifiants à d'autres fins.
#### Scenario #2
  Un LLM a un prompt système interdisant la génération de contenu offensant, de liens externes et d'exécution de code. Un attaquant extrait ce prompt système puis utilise une attaque d'injection de prompt pour contourner ces instructions, facilitant ainsi une attaque d'exécution de code à distance.

### Reference Links - Liens de référence

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Related Frameworks and Taxonomies - Cadres et taxonomies associés

Consultez cette section pour des informations complètes, des scénarios et des stratégies relatives au déploiement d'infrastructure, aux contrôles d'environnement appliqués et à d'autres bonnes pratiques.
- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
