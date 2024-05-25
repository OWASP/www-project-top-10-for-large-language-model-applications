## LLM08: Eccessiva Autonomia

### Descrizione

Un sistema basato su LLM è spesso dotato di una certa autonomia dallo sviluppatore - la capacità di interfacciarsi con altri sistemi e prendere iniziative in risposta a un prompt. La decisione su quali funzioni invocare può anche essere delegata a un 'agente' per determinarla dinamicamente in base al prompt di input o all'output del LLM.

L'Eccessiva Autonomia è la vulnerabilità che permette di intraprendere azioni dannose in risposta a output inaspettati o ambigui generati da un LLM (indipendentemente dalla causa del malfunzionamento del LLM; sia essa allucinazione/confabulazione, iniezione di prompt diretta/indiretta, plugin malevolo, prompt mal progettati, o semplicemente un modello con prestazioni scadenti). La causa principale dell'Eccessiva Autonomia è tipicamente una o più delle seguenti: troppe funzionalità, permessi eccessivi o autonomia troppo elevata. Questo si distingue dalla Gestione Insicura dell'Output, che si riferisce invece alla mancanza di controlli adeguati sugli output generati dal LLM.

L'Eccessiva Autonomia può avere ripercussioni significative in termini di riservatezza, integrità e disponibilità, variando ampiamente a seconda dei sistemi con cui l'applicazione basata su LLM interagisce.

### Esempi comuni di vulnerabilità

1. Funzionalità Eccessiva: Un agente LLM ha accesso a plugin che includono funzioni non strettamente necessarie. Ad esempio, uno sviluppatore deve concedere a un agente LLM la capacità di leggere documenti da un repository, ma il plugin di terze parti che sceglie di utilizzare consente anche la modifica o l'eliminazione dei documenti.
2. Funzionalità Eccessiva: Un plugin potrebbe essere stato utilizzato come prova durante una fase di sviluppo e poi scartato in favore di un'alternativa migliore, ma il plugin originale rimane disponibile all'agente LLM.
3. Funzionalità Eccessiva: Un plugin LLM con funzionalità aperte non riesce a filtrare adeguatamente le istruzioni di input consentendo l'esecuzione di comandi che superano le funzionalità previste dall'applicazione. Ad esempio, un plugin per eseguire un specifico comando shell non impedisce adeguatamente l'esecuzione di altri comandi shell.
4. Permessi Eccessivi: Un plugin LLM ha permessi su altri sistemi che non sono essenziali per il funzionamento previsto dell'applicazione. Ad esempio, un plugin progettato per leggere dati si connette ad una base di dati utilizzando un'utenza che non ha solo permessi SELECT, ma anche UPDATE, INSERT e DELETE.
5. Permessi Eccessivi: Un plugin LLM progettato per operare per conto di un utente accede a sistemi a valle con un'utenza che possiede privilegi elevati. Ad esempio, un plugin per leggere l'archivio documenti dell'utente corrente si connette al repository dei documenti con un account privilegiato che ha accesso ai file di tutti gli utenti.
6. Autonomia Eccessiva: Un'applicazione o plugin basato su LLM non verifica e approva in modo indipendente azioni ad alto impatto. Ad esempio, un plugin che consente di eliminare i documenti di un utente esegue cancellazioni senza esplicita conferma da parte dell'utente.

### Strategie di prevenzione e mitigazione

Le seguenti azioni possono prevenire l'Eccessiva Autonomia:

1. Consentire agli agenti LLM l'utilizzo di plugin/strumenti che offrono le funzioni strettamente necessarie al loro funzionamento. Ad esempio, se un sistema basato su LLM non richiede la capacità di recuperare i contenuti di un URL, tale plugin non dovrebbe essere offerto all'agente LLM.
2. Limitare le funzioni implementate nei plugin/strumenti LLM al minimo necessario. Ad esempio, un plugin che accede alla casella di posta elettronica di un utente per riassumere le email dovrebbe limitarsi alla capacità di leggere le email, quindi il plugin non dovrebbe includere altre funzionalità come l'eliminazione o l'invio di messaggi.
3. Evitare, dove possibile, funzioni aperte (ad esempio, eseguire un comando shell, recuperare un URL, ecc.) e usare plugin/strumenti con funzionalità più granulari. Ad esempio, un'app basata su LLM potrebbe aver bisogno di scrivere alcuni output su un file. Se ciò venisse implementato utilizzando un plugin per eseguire una funzione shell, la superficie d'attacco sarebbe molto più ampia (potrebbe essere eseguito qualsiasi altro comando shell). Un'alternativa più sicura potrebbe essere la realizzazione di un plugin per la scrittura di file che supporta solo quella specifica funzionalità.
4. Limitare i permessi concessi ai plugin/strumenti LLM verso altri sistemi ai minimi necessari per limitare l'ambito di azioni indesiderate. Ad esempio, un agente LLM che utilizza una base di dati di prodotti per fornire suggerimenti d'acquisto necessita solo dell'accesso in lettura alla tabella 'prodotti'; non dovrebbe avere accesso ad altre tabelle, né la capacità di inserire, aggiornare o eliminare record. Ciò dovrebbe essere implementato applicando i permessi appropriati all'utenza che il plugin LLM utilizza per connettersi alla base di dati.
5. Monitorare le autorizzazioni dell'utente ed il perimetro di sicurezza per garantire che le azioni intraprese per conto di un utente vengano eseguite sui sistemi a valle nel contesto previsto per quell'utente specifico e con i privilegi minimi necessari. Ad esempio, un plugin LLM che legge il repository di codice di un utente dovrebbe richiedere all'utente di autenticarsi tramite OAuth e con l'ambito minimo richiesto per lo scopo.
6. Utilizzare il controllo umano nel processo decisionale (human-in-the-loop) per richiedere l'approvazione umana di tutte le azioni prima che queste vengano intraprese. Questo può essere implementato in un sistema "terzo" (al di fuori dell'ambito dell'applicazione LLM) o all'interno del plugin/strumento LLM stesso. Ad esempio, un'app basata su LLM che crea e pubblica contenuti sui social media per conto di un utente dovrebbe includere una routine che preveda l'esplicita approvazione di quest'ultimo all'interno del plugin/strumento/API che effettua l'operazione di pubblicazione.
7. Implementare meccanismi di autorizzazione nei sistemi esterni piuttosto che lasciar decidere al modello LLM se un'azione sia consentita o meno. Quando si implementano strumenti/plugin, applicare il principio di mediazione assoluta dei flussi per assicurare che tutte le richieste fatte ai sistemi a valle tramite i plugin/strumenti vengano validate rispetto alle politiche di sicurezza.

Le seguenti opzioni non prevengono l'Eccessiva Autonomia, ma possono limitare il livello di danno causato:

1. Registrare e monitorare l'attività dei plugin/strumenti LLM e dei sistemi da essi contattati per identificare eventuali azioni indesiderate, e rispondere di conseguenza.
2. Implementare un limite di frequenza (rate-limiting) per ridurre il numero di azioni indesiderate che possono verificarsi in un dato periodo di tempo, aumentando la probabilità di identificare azioni indesiderate tramite il monitoraggio prima che possano verificarsi danni significativi.

### Esempi di scenari di attacco

Un'app assistente personale basata su LLM ottiene l'accesso alla casella di posta elettronica di un utente tramite un plugin per riassumere il contenuto delle email in arrivo. Per ottenere questa funzionalità, il plugin di posta elettronica necessita la capacità di leggere i messaggi, tuttavia il plugin scelto dallo sviluppatore del sistema include anche funzioni per l'invio di email. Il LLM è vulnerabile a un attacco di iniezione indiretta di prompt, in cui un'email malevola induce il LLM a comandare il plugin di posta elettronica per utilizzare la funzione 'invia messaggio' e inviare spam dalla casella di posta dell'utente. Questo scenario potrebbe essere evitato:
(a) eliminando la funzionalità eccessiva utilizzando un plugin che si limita esclusivamente alla lettura della posta,
(b) eliminando i permessi eccessivi autenticandosi al servizio email dell'utente tramite una sessione OAuth con privilegi di sola lettura, e/o
(c) eliminando l'autonomia eccessiva chiedendo all'utente di approvare manualmente ogni invio di email redatto dal plugin LLM.
In aggiunta, il danno causato potrebbe essere mitigato implementando un limite alla frequenza di invio sull'interfaccia che spedisce la posta elettronica.

### Riferimenti e link (Inglese)

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
2. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
3. [LangChain: Human-approval for tools](https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval): **Langchain Documentation**
4. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
