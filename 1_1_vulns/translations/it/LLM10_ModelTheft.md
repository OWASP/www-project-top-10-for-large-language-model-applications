## LLM10: Furto del Modello

### Descrizione

Questa voce si riferisce all'accesso non autorizzato e all'esfiltrazione di modelli LLM da parte di attori malintenzionati o Gruppi A.P.T. (Advanced Persistent Threat). Ciò si verifica quando i modelli LLM proprietari (rappresentando una proprietà intellettuale di valore) vengono compromessi, rubati fisicamente, copiati o se ne estraggono pesi e parametri per replicarne il funzionamento. Le conseguenze del furto di modelli LLM può includere perdite finanziarie, danni alla reputazione del marchio, erosione del vantaggio competitivo, uso non autorizzato del modello o accesso non autorizzato a informazioni sensibili contenute nel modello.

La crescente diffusione e potenza degli LLM, rende il furto di LLM una vulnerabilità dall'impatto significativo. Organizzazioni e ricercatori devono dare priorità a misure di sicurezza adeguate volte a proteggere i loro modelli LLM, garantendo la riservatezza e l'integrità della loro proprietà intellettuale. Per mitigare i rischi associati al furto del modello LLM e salvaguardare gli interessi di chi gli utilizza, è cruciale adottare un sistema di sicurezza integrato (es. sistema di gestione della sicurezza delle informazioni o altre pratiche equivalenti) che includa controlli di accesso, crittografia e monitoraggio continuo.

### Esempi comuni di vulnerabilità

1. Un attaccante sfrutta una vulnerabilità nell'infrastruttura di un'azienda per accedere senza autorizzazione al loro archivio (repository) di modelli LLM a causa di configurazioni errate nella sicurezza della rete o delle applicazioni.
2. Uno scenario di minaccia interna in cui un dipendente insoddisfatto divulga modelli o artefatti correlati ai modelli.
3. Un attaccante interroga l'API del modello, utilizzando input realizzati ad-hoc e tecniche di iniezione di prompt, per ottenere abbastanza output (risposte del modello) che permettano di ricreare successivamente un modello ombra (shadow model).
4. Un attaccante riesce a eludere i meccanismi di filtraggio degli input del LLM per effettuare un attacco laterale (side-channel) riuscendo così a raccogliere le informazioni sui pesi e sull'architettura del modello, per trasferirli verso una risorsa remota.
5. Il vettore d'attacco per l'estrazione del modello implica l'interrogazione del LLM con un gran numero di prompt, su un argomento specifico. Gli output del LLM possono a quel punto essere utilizzati per affinare un altro modello. Tuttavia, ci sono alcune considerazioni da fare su questo attacco:
   - L'aggressore deve generare un gran numero di prompt mirati. Se i prompt non sono abbastanza specifici, gli output del LLM risulteranno essere di scarso valore.
   - Gli output degli LLM possono talvolta contenere risposte considerate "allucinazioni", il che significa che l'attaccante potrebbe non essere in grado di estrarre l'intero modello, poiché alcuni output possono essere insensati.
   - Non è possibile replicare un LLM al 100% tramite questo metodo di estrazione. Tuttavia l'attaccante sarà in grado di ottenere una replica parziale del modello.
6. Il vettore di attacco per creare una "replica funzionale del modello" si avvale dell'uso del modello target tramite prompt volti a generare dati di addestramento sintetici (un approccio chiamato "auto-istruzione"), da utilizzare in seguito per affinare un altro modello fondamentale (foundational model) in modo da produrre un'imitazione funzionale del modello target. Questa tecnica supera le limitazioni dell'estrazione tradizionale basata su query, illustrata nell'esempio precedente (5), ed è stata applicata con successo nella ricerca sull'uso di un LLM per addestrare un altro LLM. Sebbene in ambito di ricerca la replica del modello non è considerata malevola, lo stesso approccio potrebbe essere utilizzato da un attaccante per duplicare un modello proprietario con API pubblica.

L'impiego di un modello rubato, come un modello ombra (shadow model), può essere finalizzato ad orchestrare attacchi informatici, incluso l'accesso non autorizzato a informazioni sensibili contenute nel modello stesso, o per condurre esperimenti su di esso in modo non rilevabile, con input avversi, per predisporre ulteriori iniezioni di prompt (prompt injections) più mirate.

### Strategie di prevenzione e mitigazione

1. Implementare controlli di accesso robusti (ad esempio, RBAC e minimizzazopne dei privilegi) accanto a meccanismi di autenticazione forti per limitare l'accesso non autorizzato ai repository di modelli LLM e agli ambienti di addestramento (pre-training e training).
   - Questo è particolarmente importante per i primi tre esempi esaminati, chin caso di minacce interne (insider threat), configurazione errata e/o controlli di sicurezza deboli, relativi all'infrastruttura che ospita modelli, pesi e architettura del LLM, in cui un attore malintenzionato potrebbe guadagnare l'accesso dall'interno, o dall'esterno.
   - La gestione dei fornitori, il tracciamento, la verifica e le vulnerabilità delle dipendenze rappresentano argomenti di interesse fondamentali per prevenire lo sfruttamento degli attacchi alla catena di approvvigionamento.
2. Limitare l'accesso del LLM alle risorse di rete, ai servizi interni e alle API.
   - Questa pratica è efficace per tutti gli esempi di attacchi citati, proteggendo dai rischi e dalle minacce interne (insider threats), e limitando allo stesso tempo ciò a cui l'applicazione LLM "*ha accesso*", rappresentando dunque un meccanismo per prevenire o interrompere attacchi laterali (side-channel attacks).
3. Utilizzare un Inventario o Registro centralizzato per i modelli di Machine Learning utilizzati in produzione. Avere un registro di modelli centralizzato aiuta a prevenire accessi non autorizzati ai modelli di ML attraverso controlli di accesso, autenticazione e grazie alla capacità di monitoraggio/registrazione, elementi fondamentali per la governance di questi processi. Avere un repository centralizzato offre anche il vantaggio di facilitare la raccolta di informazioni relative agli algoritmi utilizzati dai modelli per scopi di conformità, valutazione dei rischi e loro mitigazione.
4. Monitorare e verificare regolarmente i registri (log) di accesso e le attività relative agli archivi dei modelli LLM, per rilevare e rispondere tempestivamente a qualsiasi comportamento sospetto o non autorizzato.
5. Automatizzare l'implementazione delle cosiddette MLOps (Gestione Operativa dei Modelli di Machine Learning) attraverso flussi di lavoro dedicati alla governance, il tracciamento e l'approvazione, per rafforzare i controlli di accesso e rilascio all'interno dell'infrastruttura.
6. Implementare controlli e strategie di mitigazione per ridurre e/o contenere il rischio di attacchi indiretti (side channel) causati da tecniche di iniezione di prompt (prompt injection).
7. Limitare la frequenza delle chiamate API dove applicabile e/o utilizzare filtri per minimizzare il rischio di esfiltrazione dei dati dalle applicazioni LLM, o implementare tecniche (ad es. sistemi di Data Loss Prevention) per rilevare attività di estrazione anche da fonti alternative.
8. Implementare tecniche di addestramento avversariale mirato alla resilienza per aiutare il modello a rilevare query di estrazione e rafforzare inoltre le misure di sicurezza fisica.
9. Implementare un framework di marcatura modale e/o temporale (watermarking) nelle fasi di integrazione (input) e monitoraggio (output, trasformazione), del ciclo di vita di un LLM.

### Esempi di scenari di attacco

1. Un attaccante abusa una vulnerabilità nell'infrastruttura di un'azienda per accedere senza autorizzazione al loro repository di modelli LLM. L'attaccante procede quindi all'esfiltrazione di modelli LLM di valore e li utilizza per lanciare un servizio concorrente di elaborazione del linguaggio o estrarre forzatamente informazioni sensibili, causando gravi danni finanziari all'azienda proprietaria del modello.
2. Un dipendente insoddisfatto divulga modelli o artefatti correlati. L'esposizione pubblica che questo scenario rappresenta aumenta la conoscenza a disposizione di possibili attaccanti, consentendo attacchi avversariali di tipo "gray box" (conoscenza parziale) o, in alternativa, contentendo il furto diretto della proprietà intellettuale esposta.
3. Un attaccante interroga l'API con input creati ad-hoc e raccoglie abbastanza output per creare un modello ombra (shadow).
4. Lacune nei controlli di sicurezza della catena di fornitura (supply chain) causano perdite di dati relativi a informazioni proprietarie del o sul modello.
5. Un attaccante elude le tecniche di filtraggio degli input e le istruzioni iniziali del LLM, per eseguire un attacco indiretto/laterale e recuperare informazioni sul modello caricandole su una risorsa remota sotto il suo controllo.

### Riferimenti e link (Inglese)

1. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse): **The Verge**
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
3. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
4. [I Know What You See](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [D-DAE: Defense-Penetrating Model Extraction Attacks](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c): **Computer.org**
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
7. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
8. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
