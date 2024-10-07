## LLM02: Gestione Non Sicura dell'Output

### Descrizione

La Gestione Non Sicura dell'Output si riferisce nello specifico a una validazione, sanificazione e gestione insufficiente degli output generati da grandi modelli di linguaggio prima che vengano passati a valle ad altri componenti e sistemi. Poiché il contenuto generato da un LLM può essere controllato dal prompt in input, questo comportamento è comparabile a fornire agli utenti un accesso indiretto a funzionalità aggiuntive.

La Gestione Non Sicura dell'Output si differenzia dalla dipendenza eccessiva (LLM09) in quanto si occupa degli output generati da un LLM prima che vengano passati a valle, mentre la dipendenza eccessiva si concentra su questioni più ampie riguardanti l'eccessiva fiducia nell'accuratezza e nell'appropriatezza degli output di un LLM.

Un attacco che sfrutta la Gestione Non Sicura dell'Output può portare a XSS e CSRF nei browser web, nonché a SSRF, escalation dei privilegi o esecuzione di codice remoto (RCE) nei sistemi backend.

Le condizioni seguenti possono aumentare l'impatto di questa vulnerabilità:
* L'applicazione concede al LLM privilegi oltre a quelli previsti per gli utenti finali, consentendo l'escalation dei privilegi o l'esecuzione di codice remoto.
* L'applicazione è vulnerabile ad attacchi di iniezione di prompt indiretta, che potrebbero consentire a un attaccante di ottenere l'accesso privilegiato all'ambiente di un utente vittima.
* Plugin di terze parti non validano adeguatamente gli input.

### Esempi comuni di vulnerabilità

1. L'output di un LLM viene inserito direttamente in una shell di sistema o in una funzione simile come exec o eval, causando l'esecuzione di codice remoto.
2. JavaScript o Markdown generati dal LLM vengono restituiti all'utente. Il codice viene quindi interpretato dal browser, causando un XSS.

### Strategie di prevenzione e mitigazione

1. Trattare il modello come qualsiasi altro utente, adottando un approccio di zero-trust (fiducia zero), e applicare una corretta validazione degli input che vengono passati dal modello alle funzioni backend.
2. Seguire le linee guida OWASP ASVS (Application Security Verification Standard) per garantire una validazione e sanificazione efficace degli input.
3. Codificare l'output del modello che viene inviato agli utenti per mitigare l'esecuzione di codice indesiderato tramite JavaScript o Markdown. OWASP ASVS fornisce una guida dettagliata sulla codifica dell'output.

### Esempi di scenari di attacco

1. Un'applicazione usa un plugin LLM per generare le risposte di un chatbot. Il plugin offre anche una serie di funzioni amministrative accessibili a un altro LLM privilegiato. Il LLM passa direttamente la sua risposta, senza una corretta validazione dell'output, al plugin causando l'arresto del plugin per manutenzione.
2. Un utente usa uno strumento di sintesi di siti web basato su un LLM per generare un riassunto conciso di un articolo. Il sito web include un'iniezione di prompt che istruisce il LLM a catturare contenuti sensibili dal sito web o dalla conversazione dell'utente. Il LLM può quindi codificare i dati sensibili e inviarli a un server controllato dall'attaccante, senza alcuna validazione o filtraggio dell'output.
3. Un LLM permette agli utenti di creare query SQL per un database nel backend attraverso una chat. Un utente richiede una query per eliminare tutte le tabelle del database. Se la query creata dal LLM non viene filtrata in nessun modo, allora tutte le tabelle del database verranno eliminate.
4. Un'applicazione web usa un LLM per generare contenuto a partire da prompt di testo inseriti dall'utente, senza sanificare l'output. Un attaccante potrebbe inviare un prompt creato ad arte che causa l'invio di un payload JavaScript non sanificato, portando a un XSS quando questo viene interpretato dal browser della vittima. La mancata validazione dei prompt rende possibile questo attacco.

### Riferimenti e link (Inglese)

1. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
