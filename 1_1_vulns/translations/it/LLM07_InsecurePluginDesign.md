## LLM07: Progettazione Insicura dei Plugin

### Descrizione

I plugin LLM sono estensioni che, una volta attivate, vengono invocate automaticamente dal modello durante le interazioni con l'utente. La gestione di questi plugin è affidata alla piattaforma che integra il modello, e l'applicazione che lo utilizza potrebbe non avere il controllo diretto sulla loro esecuzione, in particolare quando il modello è gestito da un fornitore esterno. Inoltre, i plugin tendono ad accettare input di testo libero dal modello senza alcuna validazione o controllo sui tipi che gestisca le limitazioni sulla dimensione del contesto. Ciò consente a un potenziale attaccante di formulare una richiesta malevola al plugin, che potrebbe portare ad una gamma di comportamenti indesiderati, incluso l'esecuzione di codice remoto.

Il danno causato da input malevoli dipende spesso dai controlli di accesso insufficienti e dalla mancata gestione nel tracciare le autorizzazioni tra i diversi plugin. Un controllo di accesso inadeguato permette a un plugin di fidarsi ciecamente di altri plugin e di presumere che gli input ricevuti siano stati forniti dall'utente finale. Tale controllo di accesso inadeguato può consentire agli input malevoli di avere conseguenze dannose che vanno dall'esfiltrazione di dati, all'esecuzione di codice remoto, fino all'acquisizione di privilegi non autorizzati.

Questa sezione si concentra sulla creazione di plugin specifici per LLM piuttosto che sui plugin di terze parti, coperti dalle Vulnerabilità della Catena di Approvvigionamento del LLM (Supply-Chain-Vulnerabilities).

### Esempi comuni di vulnerabilità

1. Un plugin accetta tutti i parametri in un unico campo di testo anziché in parametri di input distinti.
2. Un plugin accetta stringhe di configurazione invece di parametri, che possono sovrascrivere intere impostazioni di configurazione.
3. Un plugin accetta comandi SQL o istruzioni di programmazione invece di parametri ristretti.
4. L'autenticazione è eseguita senza un'autorizzazione esplicita per un particolare plugin.
5. Un plugin tratta tutti i contenuti LLM come se fossero creati interamente dall'utente eseguendo qualsiasi azione richiesta senza chiedere ulteriori autorizzazioni.

### Strategie di prevenzione e mitigazione

1. I Plugin dovrebbero accettare input che siano limitati e parametrizzati ove possibile e includere controlli sul tipo e la struttura dell'input. Dove non sia consentito, è opportuno inserire un secondo livello di chiamate fortemente tipizzate (controllo rigoroso sui tipi di parametro), analizzando le richieste e applicando validazione e sanificazione. Per gli input liberi, eventualmente necessari per alcune funzionalità dell'applicazione, è cruciale un'attenta revisione per prevenire l'invocazione di metodi dannosi.
2. Gli sviluppatori di plugin dovrebbero applicare le linee guida OWASP per gli standard di verifica della sicurezza applicativa (ASVS - Application Security Verification Standard) per assicurare adeguate validazione e sanitizzazione dell'input.
3. I Plugin dovrebbero essere ispezionati e testati in modo approfondito per assicurare adeguata validazione. Utilizzare sistemi di Scansione Statica del Codice (SAST) e Test Dinamici ed Interattivi (DAST, IAST) all'interno dei processi (pipelines) di sviluppo.
4. I Plugin dovrebbero essere progettati con l'intento di minimizzare l'impatto dello sfruttamento di qualunque parametro di input insicuro come da linee guida sui Controlli di Accesso nello standard ASVS OWASP. Ciò prevede un controllo accessi che assicuri i privilegi strettamente necessari, e l'esposizione delle funzionalità strettamente necessarie al corretto funzionamento.
5. I Plugin dovrebbero utilizzare meccanismi di autorizzazione standardizzati come OAuth2, per consentire l'applicazione efficace dei controlli di autorizzazione ed accesso. Inoltre le chiavi API dovrebbero essere utilizzate per fornire un contesto in cui applicare specifiche decisioni autorizzative che riflettano il flusso del plugin come chiaramente distinto da quello interattivo dell'utente.
6. Richiedere un intervento umano per l'autorizzazione e la conferma di ogni azione intrapresa da plugin particolarmente critici.
7. I Plugin sono tipicamente delle REST APIs, per cui si raccomanda agli sviluppatori l'applicazione delle raccomandazioni di cui alla lista OWASP Top 10 API Security Risks - 2023 per ridurre la presenza di vulnerabilità comuni.

### Esempi di scenari di attacco

1. Un plugin accetta un URL base e istruisce il LLM nel combinare l'URL con una query per ottenere previsioni meteorologiche che sono incluse nell'elaborazione della richiesta dell'utente. Un utente malintenzionato può creare una richiesta in modo tale che l'URL punti verso un dominio sotto il suo controllo, permettendogli di iniettare il proprio contenuto nel modello LLM tramite il proprio dominio.
2. Un plugin accetta un input in forma libera in un unico campo che non viene validato. Un attaccante fornisce payload creati ad-hoc per ottenere informazioni utili a partire dai messaggi di errore. Poi sfrutta vulnerabilità conosciute nelle dipendenze di terze parti per eseguire del codice arbitrario ed effettuando un'esfiltrazione di dati o aumentando i propri di privilegi.
3. Un plugin utilizzato per recuperare delle inclusioni (embedding) da un base di dati vettoriale accetta parametri di configurazione come stringa di connessione senza effettuarne la validazione. Ciò permette ad un attaccante di sfruttare questa problematica e accedere ad altre basi di dati vettoriali cambiando nomi o parametri host ed esfiltrare rappresentazioni vettoriali a cui non dovrebbe avere accesso.
4. Un plugin accetta direttamente clausole SQL "WHERE" come parte di filtri avanzati, che vengono poi aggiunti alla query SQL. Ciò permette all'attaccante di eseguire un attacco di iniezione SQL.
5. Un attaccante utilizza l'iniezione indiretta di prompt per attaccare un plugin di gestione del codice insicuro, privo di validazione dell'input e con controlli di accesso deboli, per trasferire la proprietà del repository (archivio) e bloccare l'utente dai propri.

### Riferimenti e link (Inglese)

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): **ChatGPT Developer’s Guide**
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI Documentation**
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI Documentation**
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
9. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**
