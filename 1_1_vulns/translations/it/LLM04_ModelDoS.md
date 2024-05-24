## LLM04: Denial of Service del Modello

### Descrizione

Un attaccante può interagire con un LLM (Large Language Model) in modo tale da causare un consumo eccezionalmente alto di risorse, risultando in un deterioramento della qualità del servizio sia per sé stesso che per altri utenti, e potenzialmente causando un aumento dei costi per le risorse computazionali. Un altro aspetto critico per la sicurezza è la possibilità che un attaccante interferisca o manipoli la "finestra di contesto" di un LLM. Questa problematica sta diventando sempre più rilevante a causa dell'uso crescente degli LLM in diverse applicazioni, del loro intenso utilizzo di risorse, dell'imprevedibilità degli input degli utenti e di una generale mancanza di consapevolezza tra gli sviluppatori riguardo a questa vulnerabilità.
Negli LLM, la finestra di contesto rappresenta la lunghezza massima di testo che il modello può gestire, includendo sia l'input che l'output. Questa caratteristica è fondamentale per gli LLM, poiché determina la complessità dei costrutti linguistici che il modello può comprendere e la quantità di testo che può elaborare in un dato momento. La dimensione della finestra di contesto è definita dall'architettura del modello e può variare a seconda del modello specifico utilizzato.

### Esempi comuni di vulnerabilità

1. Porre domande (prompts) che inducono a un utilizzo ripetitivo delle risorse attraverso la creazione di un elevato numero di compiti in coda, ad esempio impiegando strumenti come LangChain o AutoGPT.
2. Inviare interrogazioni insolitamente gravose in termini di risorse, utilizzando ortografie o sequenze di testo non convenzionali.
3. Sovraccarico continuo dell'input: un attaccante invia costantemente al LLM un flusso di input che eccede la finestra di contesto del modello, causando un consumo eccessivo di risorse computazionali.
4. Input lunghi ripetuti: l'attante invia al LLM input estesi in modo ripetitivo, ciascuno dei quali supera la capacità della finestra di contesto.
5. Espansione ricorsiva del contesto: l'attaccante formula un input che provoca un'espansione ricorsiva del contesto, obbligando il LLM a ingrandire e processare più volte la finestra di contesto.
6. Inondazione di input di lunghezza variabile: l'attaccante inonda il LLM con una grande quantità di input di lunghezze diverse, ognuno progettato per sfiorare il limite massimo della finestra di contesto. Questa tattica mira a sfruttare le inefficienze nella gestione degli input di dimensioni variabili, mettendo a dura prova il LLM e potenzialmente causandone il blocco.

### Strategie di prevenzione e mitigazione

1. Implementare un controllo dell'input per assicurare che gli input degli utenti rispettino limiti predefiniti e siano privi di contenuti malevoli.
2. Impostare limiti alle risorse utilizzabili per ogni richiesta o passaggio, rallentando così l'esecuzione delle richieste più complesse.
3. Applicare limiti di frequenza alle chiamate API per contenere il numero di richieste che un singolo utente o indirizzo IP può fare entro un determinato lasso di tempo.
4. Limitare il numero di azioni in coda e il numero totale di azioni in un sistema terzo che interagisce con il LLM.
5. Monitorare continuamente l'utilizzo delle risorse del LLM per identificare picchi o schemi anomali che potrebbero indicare un attacco DoS.
6. Impostare limiti rigorosi sugli input in base alla finestra di contesto del LLM, per prevenire eccessivi sovraccarichi e l'esaurimento delle risorse.
7. Aumentare la consapevolezza tra gli sviluppatori sulle potenziali vulnerabilità ai DoS negli LLM e fornire indicazioni per un'implementazione sicura degli stessi.

### Esempi di scenari di attacco

1. Un attaccante invia ripetutamente molteplici richieste complesse e onerose a un modello in hosting, portando a un deterioramento del servizio per gli altri utenti e ad un aumento dei costi relative ai consumi delle risorse, nel servizio di hosting.
2. Durante l'elaborazione di un testo su una pagina web da parte di uno strumento basato su LLM che risponde a una query benigna, lo strumento si imbatte in un testo specifico e inizia a richiedere un numero eccessivo di pagine web, comportando un alto consumo di risorse.
3. Un attaccante bombarda continuamente il LLM con input che superano la sua finestra di contesto. L'attaccante può utilizzare script automatizzati o strumenti per inviare un alto volume di input, sovraccaricando le capacità di elaborazione del LLM. Di conseguenza, viene causato un eccessivo consumo di risorse computazionali, con conseguente rallentamento o inoperatività del sistema ospitante.
4. Un attaccante invia una serie di input sequenziali al LLM, in cui ciascun input è progettato per essere appena sotto il limite della finestra di contesto. Inviando ripetutamente questi input, l'attaccante mira a esaurire la capacità disponibile della finestra. Mentre il LLM fatica a elaborare ciascun input all'interno della sua finestra di contesto, le risorse del sistema si riducono drasticamente, risultando in un degrado delle prestazioni o in un completo diniego del servizio (DoS).
5. Un attaccante sfrutta i meccanismi ricorsivi del LLM per causare ripetutamente l'espansione del contesto. Creando un input che stimola il comportamento ricorsivo del LLM, l'attaccante costringe il modello a espandere e processare ripetutamente la finestra di contesto, consumando una significativa quantità di risorse computazionali. Questo attacco mette sotto sforzo il sistema e può portare a una condizione di DoS, rendendo il LLM non reattivo o causandone il fermo totale.
6. Un attaccante inonda il LLM con un grande volume di input di lunghezza variabile, costruiti specificamente per avvicinarsi o raggiungere il limite della finestra di contesto. Sopraffacendo il LLM con input di lunghezze variabili, l'attaccante mira a sfruttare qualsiasi inefficienza nell'elaborazione di questo tipo di input. Questo sovraccarico pesa eccessivamente sulle risorse del LLM, provocando un degrado delle prestazioni e ostacolando la capacità del sistema di rispondere a richieste legittime.
7. Mentre gli attacchi di tipo Denial of Service (DoS) puntano generalmente a sovraccaricare le risorse di un sistema, possono anche mirare ad altri aspetti del suo funzionamento, come sfruttare le vulnerabilità nelle limitazioni dell'API. Per esempio, in un recente episodio di sicurezza che ha coinvolto Sourcegraph, un attore malevolo ha acquisito un token di accesso amministrativo e lo ha usato per modificare i limiti di frequenza delle chiamate API. Questa azione avrebbe potuto causare interruzioni del servizio, abilitando volumi insolitamente alti di richieste.

### Riferimenti e link (Inglese)

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): **hwchase17 on Twitter**
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): **Arxiv White Paper**
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service): **OWASP**
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context): **Luke Bechtel**
5. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack ](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**
