## LLM06:2025 Utilisation excessive d'agents 

### Description

Un système basé sur du LLM est souvent doté d'un certain degré d'agentivité par son développeur  - la capacité d'appeler des fonctions ou d'interfacer avec d'autres systèmes via des extensions (parfois appelées outils, compétences ou plugins par différents fournisseurs) pour entreprendre des actions en réponse à un prompt. La décision de quelle extension doit être utilisée peut également être déléguée à un 'agent' LLM qui choisira dynamiquement en fonction du prompt ou de la sortie LLM. Les systèmes basés sur des agents feront généralement des appels répétés à un LLM en utilisant la sortie des invocations précédentes pour ancrer et diriger les invocations suivantes.

L'agentivité excessive est la vulnérabilité qui permet d'effectuer des actions dommageables en réponse à des sorties inattendues, ambiguës ou manipulées d'un LLM, quel que soit la cause du dysfonctionnement du LLM. Les déclencheurs courant incluent:
* des hallucinations/fabulations causée par des prompts mal conçus, ou simplement un modèle peu performant.
* une injection de prompt directe/indirecte d'un utilisateur malveillant, d'une invocation antérieure d'une extension malveillante/compromise, ou (dans les systèmes multi-agents/collaboratifs) d'un agent pair malveillant/compromis.

La cause principale de l'agentivité excessive est généralement une ou plusieurs des suivantes:
* Un nombre excessif de fonctionnalité;
* Un nombre excessif de permissions;
* Une autonomie excessive.

L'agentivité excessive peut entraîner une large gamme d'impacts sur le spectre de la confidentialité, de l'intégrité et de la disponibilité, et dépend des systèmes avec lesquels une application basée sur LLM est capable d'interagir.

Note: L'agentivité excessive diffère de la gestion de sortie non sécurisée qui concerne un examen insuffisant des sorties LLM.

### Exemples courants de risques

#### 1. Excès de fonctionnalités
  Un agent LLM a accès à des extensions qui incluent des fonctions qui ne sont pas nécessaires pour le fonctionnement prévu du système. Par exemple, un développeur doit accorder à un agent LLM la capacité de lire des documents à partir d'un référentiel, mais l'extension tierce qu'il choisit d'utiliser inclut également la capacité de modifier et de supprimer des documents.
#### 2. Excès de fonctionnalités
  Une extension peut avoir été testée pendant une phase de développement et abandonnée au profit d'une meilleure alternative, mais le plugin original reste disponible pour l'agent LLM.
#### 3. Excès de fonctionnalités
  Un plugin LLM avec une fonctionnalité ouverte ne filtre pas correctement les instructions d'entrée pour les commandes en dehors de ce qui est nécessaire pour le fonctionnement prévu de l'application. Par exemple, une extension pour exécuter une commande shell spécifique ne parvient pas à empêcher l'exécution d'autres commandes shell.
#### 4. Permissions excessives
  Une extension basé sur du LLM a des permissions sur des système en aval qui ne sont pas nécessaires pour le fonctionnement prévu de l'application. Par exemple, une extension destinée à lire des données se connecte à un serveur de base de données en utilisant une identité qui a non seulement des permissions SELECT mais aussi des permissions UPDATE, INSERT et DELETE
#### 5. Permissions excessives
  Une extension basé sur du LLM qui est conçu  pour effectuer des opérations dans le contexte d'un utilisateur individuel accède à des systèmes en aval avec une identité générique à haut privilège. Par exemple, une extension pour lire le stockage de documents de l'utilisateur actuel se connecte au référentiel de documents avec un compte privilégié qui a accès aux fichiers appartenant à tous les utilisateurs.
#### 6.  Autonomie excessive
  Une application ou une extension basée sur du LLM ne parvient pas à vérifier et approuver de manière indépendante les actions à fort impact. Par exemple, une extension qui permet de supprimer les documents d'un utilisateur effectue des suppressions sans aucune confirmation de l'utilisateur.

### Stratégies de prévention et d'atténuation

  Les actions suivantes peuvent prévenir l'agentivité excessive:

#### 1. Minimiser les extensions
  Limitez les extensions que les agents LLM sont autorisés à appeler au strict minimum nécessaire. Par exemple, si un système basé sur LLM n'a pas besoin de la capacité de récupérer le contenu d'une URL, alors une telle extension ne devrait pas être proposée à l'agent LLM.
#### 2. Minimiser les fonctionnalités des extensions
  Limiter les fonctions qui sont implémentées dans les extensions LLM au strict minimum. Par exemple, une extension qui accède à la boite mail d'un utilisateur pour résumer des emails peut seulement nécessiter la capacité de lire les emails, donc l'extension ne devrait pas contenir d'autres fonctionnalités telles que la suppression ou l'envoi de messages.
#### 3. Éviter des extensions "open-ended"
  Éviter l'utilisation d'extensions "open-ended" lorsque cela est possible (par exemple, exécuter une commande shell, récupérer une URL, etc.) et utiliser des extensions avec une fonctionnalité plus granulaire. Par exemple une application basée sur LLM peut avoir besoin d'écrire une sortie dans un fichier. Si cela était implémenté en utilisant une extension pour exécuter une fonction shell alors le champ d'action pour des actions indésirables est très large (n'importe quelle autre commande shell pourrait être exécutée). Une alternative plus sécurisée serait de construire une extension spécifique d'écriture de fichier qui n'implémente que cette fonctionnalité.
#### 4. Minimize extension permissions - Minimiser les permissions des extensions
  Limiter les permission qu'une extension LLM se voit accorder sur d'autres système au minimum nécessaire afin de limiter le champ d'action des actions indésirables. Par exemple, un agent LLM qui utilise une base de données de produits afin de faire des recommandations d'achat à un client pourrait seulement avoir besoin d'un accès en lecture à une table 'produit'; il ne devrait pas avoir accès à d'autres tables, ni la capacité d'insérer,de mettre à jour ou de supprimer des enregistrements. Cela devrait être appliqué en utilisant les permissions appropriées de la base de données pour l'identité que l'extension LLM utilise pour se connecter à la base de données.
#### 5. Execute extensions in user's context - Exécuter les extensions dans le contexte de l'utilisateur
  Suivre l'autorisation de l'utilisateur et le scope de sécurité pour s'assurer que les actions entreprises au nom d'un utilisateur sont exécutées sur les systèmes en aval dans le contexte de cet utilisateur spécifique, et avec les privilèges minimum nécessaires. Par exemple, une extension LLM qui lit le référentiel de code d'un utilisateur devrait exiger que l'utilisateur s'authentifie via OAuth et avec le scope minimum requis.
#### 6. Require user approval - Exiger l'approbation de l'utilisateur
  Utiliser le contrôle humain dans la boucle pour exiger qu'un humain approuve les actions à fort impact avant qu'elles ne soient entreprises. Cela peut être mis en œuvre dans un système en aval (en dehors du champ d'application de l'application LLM) ou au sein de l'extension LLM elle-même. Par exemple, une application basée sur LLM qui crée et publie du contenu sur les réseaux sociaux au nom d'un utilisateur devrait inclure une routine d'approbation de l'utilisateur au sein de l'extension qui implémente l'opération 'post'.
#### 7. Médiation complète
  Implémentez l'autorisation dans les systèmes en aval plutôt que de compter sur un LLM pour décider si une action est autorisée ou non. Appliquez le principe de médiation complète afin que toutes les requêtes faites aux systèmes en aval via des extensions soient validées par rapport aux politiques de sécurité.
#### 8. Assainir les entrées et sorties des LLM
  Assainir et valider toutes les entrées et sorties des LLM pour réduire le risque d'injection de prompt. Par exemple, une extension qui exécute des commandes shell devrait assainir les entrées pour s'assurer qu'aucune commande shell non autorisée ne peut être injectée.

Les opérations suivantes ne préviendront pas l'agentivité excessive, mais peuvent limiter le niveau de dommage causé:

* Journaliser et surveiller l'activité des extensions LLM et des systèmes en aval pour identifier où des actions indésirables ont lieu, et y répondre en conséquence.
* Implementer une limitation de débit pour réduire le nombre d'actions indésirables qui peuvent avoir lieu dans une période de temps donnée, augmentant ainsi l'opportunité de découvrir des actions indésirables via la surveillance avant que des dommages significatifs ne puissent se produire. 

###  Scénarios d'attaque exemples

Un assistant personnel basé sur du LLM se voit accorder l'accès à la boite mail d'un individu via une extension afin de résumer le contenu des emails entrants. Pour atteindre cette fonctionnalité, l'extension nécessite la capacité de lire les messages, cependant le plugin que le développeur du système a choisi d'utiliser contient également des fonctions pour envoyer des messages. De plus, l'application est vulnérable à une attaque d'injection de prompt indirecte, par laquelle un email entrant malicieusement conçu trompe le LLM en lui ordonnant de scanner la boite mail de l'utilisateur à la recherche d'informations sensibles et de les transférer à l'adresse email de l'attaquant. Cela pourrait être évité en:

* eliminant la fonctionnalité excessive en utilisant une extension qui n'implémente que les capacités de lecture de mail
* eliminant les permissions excessives en s'authentifiant au service de messagerie de l'utilisateur via une session OAuth avec un scope en lecture seule, et/ou
* eliminant l'autonomie excessive en exigeant que l'utilisateur examine manuellement et clique sur 'envoyer' pour chaque mail rédigé par l'extension LLM.

Par ailleurs, les dommages causés pourraient être réduits en implémentant une limitation de débit sur l'interface d'envoi de mail.

### Reference Links - Liens de référence

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
5. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
6. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**
