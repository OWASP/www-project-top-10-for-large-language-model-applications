## LLM06:2025 Excessive Agency - Utilisation excessive d'agents 

### Description

Un système basé sur du LLM est souvent doté d'un certain degré d'agentivité par son développeur  - la capacité d'appeler des fonctions ou d'interfacer avec d'autres systèmes via des extensions (parfois appelées outils, compétences ou plugins par différents fournisseurs) pour entreprendre des actions en réponse à un prompt. La déccision de l'extension à invoquer peut également être déléguée à un 'agent' LLM pour déterminer dynamiquement en fonction du prompt ou de la sortie LLM. Les systèmes basés sur des agents feront généralement des appels répétés à un LLM en utilisant la sortie des invocation précédentes pour ancrer et diriger les involcation ultétirieures.

An LLM-based system is often granted a degree of agency by its developer - the ability to call functions or interface with other systems via extensions (sometimes referred to as tools, skills or plugins by different vendors) to undertake actions in response to a prompt. The decision over which extension to invoke may also be delegated to an LLM 'agent' to dynamically determine based on input prompt or LLM output. Agent-based systems will typically make repeated calls to an LLM using output from previous invocations to ground and direct subsequent invocations.

L'agentivité excessive est la vulnérabilité qui permet d'effectuer des actions dommageables en réponse à des sorties inattendues, ambiegües ou manipulées d'un LLM, quel que soit la cause du dysfonctionnement du LLM. Les déclencheurs courant incluent:

Excessive Agency is the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM, regardless of what is causing the LLM to malfunction. Common triggers include:

* des hallucinations/fabulations causée par des prompts bénins mal conçus, ou simplement un modèle peu performant.
* une injection de prompt directe/indirecte d'un utilisateur malveillant, d'une invocation antérieure d'une extension malveillante/compromise, ou (dans les systèmes multi-agents/collaboratifs) d'un agent pair malveillant/compromis.

* hallucination/confabulation caused by poorly-engineered benign prompts, or just a poorly-performing model;
* direct/indirect prompt injection from a malicious user, an earlier invocation of a malicious/compromised extension, or (in multi-agent/collaborative systems) a malicious/compromised peer agent.


La cause principale de l'agentivité excessive est généralement une ou plusieurs des suivantes:

The root cause of Excessive Agency is typically one or more of:

* Un nombre excessif de fonctionnalité;
* Un nombre excessif de permissions;
* Une autonomie excessive.

* excessive functionality;
* excessive permissions;
* excessive autonomy.


L'agentivité excessive peut entraîner une large gamme d'impacts sur le spectre de la confidentialité, de l'intégrité et de la disponibilité, et dépend des systèmes avec lesquels une application basée sur LLM est capable d'interagir.

Excessive Agency can lead to a broad range of impacts across the confidentiality, integrity and availability spectrum, and is dependent on which systems an LLM-based app is able to interact with.

Note: L'agentivité excessive diffère de la gestion de sortie non sécurisée qui concerne un examen insuffisant des sorties LLM.

Note: Excessive Agency differs from Insecure Output Handling which is concerned with insufficient scrutiny of LLM outputs.

### Common Examples of Risks - Exemples courants de risques

#### 1. Excessive Functionality - Fonctionnalité excessive

  Un agent LLM a accès à des extensions qui incluent des fonctions qui ne sont pas nécéssaires pour le fonctionnement prévu du système. Par exemple, un développeur doit accorder à un agent LLM la capacité de lire des documents à partir d'un référentiel, mais l'extension tierce qu'il choisit d'utiliser inclut également la capacité de modifier et de supprimer des documents.

  An LLM agent has access to extensions which include functions that are not needed for the intended operation of the system. For example, a developer needs to grant an LLM agent the ability to read documents from a repository, but the 3rd-party extension they choose to use also includes the ability to modify and delete documents.

#### 2. Excessive Functionality - Fonctionnalité excessive

  Une extension peut avoir été testée pendant une phase de développement et abandonnée au profit d'une meilleure alternative, mais le plugin original reste disponible pour l'agent LLM.

  An extension may have been trialled during a development phase and dropped in favor of a better alternative, but the original plugin remains available to the LLM agent.

#### 3. Excessive Functionality - Fonctionnalité excessive

  Un plugin LLM avec une fonctionnalité ouverte ne filtre pas correctement les instructions d'entrée pour les commandes en dehors de ce qui est nécessaire pour le fonctionnement prévu de l'application. Par exemple, une extension pour exécuter une commande shell spécifique ne parvient pas à empêcher l'exécution d'autres commandes shell.

  An LLM plugin with open-ended functionality fails to properly filter the input instructions for commands outside what's necessary for the intended operation of the application. E.g., an extension to run one specific shell command fails to properly prevent other shell commands from being executed.

#### 4. Excessive Permissions - Permissions excessives


  Une extension basé sur du LLM a des permissions sur des système en aval qui ne sont pas nécéssaire pour le fonctionnement prévu de l'application. Par exemple, une extension destinée à lire des données se connecte à un serveur de base de données en utilisant une identitié qui a non seullement des permissions SELECT mais aussi des permissions UPDATE, INSERT et DELETE

  An LLM extension has permissions on downstream systems that are not needed for the intended operation of the application. E.g., an extension intended to read data connects to a database server using an identity that not only has SELECT permissions, but also UPDATE, INSERT and DELETE permissions.

#### 5. Excessive Permissions - Permissions excessives

  Une extension basé sur du LLM qui est conçu  pour effectuer des opérations dans le contexte d'un utilisateur individuel accède à des systèmes en aval avec une identité générique à haut privilège. Par exemple, une extension pour lire le magasin de documents de l'utilisateur actuel se connecte au référentiel de documents avec un compte privilégié qui a accès aux fichiers appartenant à tous les utilisateurs.

  An LLM extension that is designed to perform operations in the context of an individual user accesses downstream systems with a generic high-privileged identity. E.g., an extension to read the current user's document store connects to the document repository with a privileged account that has access to files belonging to all users.

#### 6. Excessive Autonomy - Autonomie excessive

  Une application ou une extension basée sur du LLM ne parvient pas à vérifier et approuver de manière indépendante les actions à fort impact. Par exemple, une extension qui permet de supprimer les documents d'un utilisateur effectue des suppressions sans aucune confirmation de l'utilisateur.

  An LLM-based application or extension fails to independently verify and approve high-impact actions. E.g., an extension that allows a user's documents to be deleted performs deletions without any confirmation from the user.

### Prevention and Mitigation Strategies - Stratégies de prévention et d'atténuation

  Les actions suivantes peuvent prévenir l'agentivité excessive:

The following actions can prevent Excessive Agency:

#### 1. Minimize extensions - Minimiser les extensions

  Limitez les extensions que les agents LLM sont autorisés à appeler au strict minimum nécessaire. Par exemple, si un système basé sur LLM n'a pas besoin de la capacité de récupérer le contenu d'une URL, alors une telle extension ne devrait pas être proposée à l'agent LLM.

  Limit the extensions that LLM agents are allowed to call to only the minimum necessary. For example, if an LLM-based system does not require the ability to fetch the contents of a URL then such an extension should not be offered to the LLM agent.

#### 2. Minimize extension functionality - Minimiser la fonctionnalité des extensions

  Limiter les fonctions qui sont implémentées dans les extensions LLM au strict minimum. Par exemple, une extension qui accède à la boite mail d'un utilisateur pour résumer des emails peut seulement nécessiter la capacité de lire les emails, donc l'extension ne devrait pas contenir d'autres fonctionnalités telles que la suppression ou l'envoi de messages.

  Limit the functions that are implemented in LLM extensions to the minimum necessary. For example, an extension that accesses a user's mailbox to summarise emails may only require the ability to read emails, so the extension should not contain other functionality such as deleting or sending messages.

#### 3. Avoid open-ended extensions

  Eviter l'utilisation d'extensions "open-ended" lorsque cela est possible (par exemple, exécuter une commande shell, récupérer une URL, etc.) et utiliser des extensions avec une fonctionnalité plus grnaulaire. Par exemple une application basée sur LLM peut avoir besoin d'écrire une sortie dans un fichier. Si cela était implémenté en utilisant une extension pour éxécuter une fonction shell alors le champ d'action pour des actions indésirables est très large (n'importe quelle autre commande shell pourrait être éxécutée). Une alternative plus sécurisée serait de construire une extension spécifique d'écriture de fichier qui n'implémente que cette fonctionnalité spécifique.

  Avoid the use of open-ended extensions where possible (e.g., run a shell command, fetch a URL, etc.) and use extensions with more granular functionality. For example, an LLM-based app may need to write some output to a file. If this were implemented using an extension to run a shell function then the scope for undesirable actions is very large (any other shell command could be executed). A more secure alternative would be to build a specific file-writing extension that only implements that specific functionality.

#### 4. Minimize extension permissions - Minimiser les permissions des extensions

  Limiter les permission qu'une extension LLM se voit accorder sur d'autres système au minimum nécéssaire afin de limiter le champ d'action des actions indésirables. Par exemple, un agent LLM qui utilise une base de données de produits afin de faire des recommandations d'achat à un client pourrait seulement avoir besoin d'un accès en lecture à une table 'produit'; il ne devrait pas avoir accès à d'autres tables, ni la capaicté d'insérer,de mettre à jour ou de supprimer des enregistrements. Cela devrait être appliqué en utilisant les permissions appropriées de la base de données pour l'identité que l'extension LLM utilise pour se connecter à la base de données.

  Limit the permissions that LLM extensions are granted to other systems to the minimum necessary in order to limit the scope of undesirable actions. For example, an LLM agent that uses a product database in order to make purchase recommendations to a customer might only need read access to a 'products' table; it should not have access to other tables, nor the ability to insert, update or delete records. This should be enforced by applying appropriate database permissions for the identity that the LLM extension uses to connect to the database.
 
#### 5. Execute extensions in user's context - Exécuter les extensions dans le contexte de l'utilisateur

  Suivre l'autorisation de l'utilisateur et le scope de sécurité pour s'assurer que les actions entreprises au nom d'un utilisateur sont exécutées sur les systèmes en aval dans le contexte de cet utilisateur spécifique, et avec les privilèges minimum nécéssaires. Par exemple, une extension LLM qui lit le référentiel de code d'un utilisateur devrait exiger que l'utilisateur s'authentifie via OAuth et avec le scope minimum requis.

  Track user authorization and security scope to ensure actions taken on behalf of a user are executed on downstream systems in the context of that specific user, and with the minimum privileges necessary. For example, an LLM extension that reads a user's code repo should require the user to authenticate via OAuth and with the minimum scope required.

#### 6. Require user approval - Exiger l'approbation de l'utilisateur

  Utilise le contrôle humain dans la boucle pour exiger qu'un humain approuve les actions à fort impact avant qu'elles ne soient entreprises. Cela peut être mis en œuvre dans un système en aval (en dehors du champ d'application de l'application LLM) ou au sein de l'extension LLM elle-même. Par exemple, une application basée sur LLM qui crée et publie du contenu sur les réseaux sociaux au nom d'un utilisateur devrait inclure une routine d'approbation de l'utilisateur au sein de l'extension qui implémente l'opération 'post'.

  Utilise human-in-the-loop control to require a human to approve high-impact actions before they are taken. This may be implemented in a downstream system (outside the scope of the LLM application) or within the LLM extension itself. For example, an LLM-based app that creates and posts social media content on behalf of a user should include a user approval routine within the extension that implements the 'post' operation.

#### 7. Complete mediation - Médiation complète

  Implémentez l'autorisation dans les systèmes en aval plutôt que de compter sur un LLM pour décider si une action est autorisée ou non. Appliquez le principe de médiation complète afin que toutes les requêtes faites aux systèmes en aval via des extensions soient validées par rapport aux politiques de sécurité.

  Implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed or not. Enforce the complete mediation principle so that all requests made to downstream systems via extensions are validated against security policies.


#### 8. Sanitise LLM inputs and outputs - Assainir les entrées et sorties des LLM

  Assainir et valider toutes les entrées et sorties des LLM pour réduire le risque d'injection de prompt. Par exemple, une extension qui exécute des commandes shell devrait assainir les entrées pour s'assurer qu'aucune commande shell non autorisée ne peut être injectée.


  Follow secure coding best practice, such as applying OWASP’s recommendations in ASVS (Application Security Verification Standard), with a particularly strong focus on input sanitisation. Use Static Application Security Testing (SAST) and Dynamic and Interactive application testing (DAST, IAST) in development pipelines.

Les opérations suivantes ne préviendront pas l'agentivité excessive, mais peuvent limiter le niveau de dommage causé:

The following options will not prevent Excessive Agency, but can limit the level of damage caused:

* Journaliser et surveiller l'activité des extensions LLM et des systèmes en aval pour identifier où des actions indésirables ont lieu, et y répondre en conséquence.
* Implementer une limitation de débit pour réduire le nombre d'actions indésirables qui peuvent avoir lieu dans une période de temps donnée, augmentant ainsi l'opportunité de découvrir des actions indésirables via la surveillance avant que des dommages significatifs ne puissent se produire. 

* Log and monitor the activity of LLM extensions and downstream systems to identify where undesirable actions are taking place, and respond accordingly.
* Implement rate-limiting to reduce the number of undesirable actions that can take place within a given time period, increasing the opportunity to discover undesirable actions through monitoring before significant damage can occur.

### Example Attack Scenarios - Scénarios d'attaque exemples

Un assistant personnel basé sur du LLM se voit accorder l'accès à la boite mail d'un individu via une extension afin de résumer le contenu des emails entrants. Pour atteindre cette fonctionnalité, l'extension nécessite la capacité de lire les messages, cependant le plugin que le développeur du système a choisi d'utiliser contient également des fonctions pour envoyer des messages. De plus, l'application est vulnérable à une attaque d'injection de prompt indirecte, par laquelle un email entrant malicieusement conçu trompe le LLM en lui ordonnant de scanner la boite mail de l'utilisateur à la recherche d'informations sensibles et de les transférer à l'adresse email de l'attaquant. Cela pourrait être évité en:

An LLM-based personal assistant app is granted access to an individual’s mailbox via an extension in order to summarise the content of incoming emails. To achieve this functionality, the extension requires the ability to read messages, however the plugin that the system developer has chosen to use also contains functions for sending messages. Additionally, the app is vulnerable to an indirect prompt injection attack, whereby a maliciously-crafted incoming email tricks the LLM into commanding the agent to scan the user's inbox for sensitive information and forward it to the attacker's email address. This could be avoided by:


* eliminant la fonctionnalité excessive en utilisant une extension qui n'implémente que les capacités de lecture de mail,
* eliminant les permissions excessives en s'authentifiant au service de messagerie de l'utilisateur via une session OAuth avec un scope en lecture seule, et/ou
* eliminant l'autonomie excessive en exigeant que l'utilisateur examine manuellement et clique sur 'envoyer' pour chaque mail rédigé par l'extension LLM.

Autrement, les dommages causés pourraient être réduits en implémentant une limitation de débit sur l'interface d'envoi de mail.

* eliminating excessive functionality by using an extension that only implements mail-reading capabilities,
* eliminating excessive permissions by authenticating to the user's email service via an OAuth session with a read-only scope, and/or
* eliminating excessive autonomy by requiring the user to manually review and hit 'send' on every mail drafted by the LLM extension.

Alternatively, the damage caused could be reduced by implementing rate limiting on the mail-sending interface.

### Reference Links - Liens de référence

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
5. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
6. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**
