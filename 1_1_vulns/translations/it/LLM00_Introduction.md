## Introduzione

L'introduzione sul mercato di massa dei chatbot pre-addestrati a fine 2022 ha innescato un'ondata di frenetico interesse per i modelli di linguaggio a grandi dimensioni (LLM). Le aziende, desiderose di sfruttare il potenziale degli LLM, li stanno integrando rapidamente nei loro sistemi e nelle offerte destinate ai clienti. Tuttavia, la velocità con cui gli LLM vengono adottati ha superato il tempo necessario per stabilire protocolli di sicurezza esaustivi, lasciando molte applicazioni vulnerabili a seri problemi di sicurezza.

Era evidente la necessità di una risorsa unificata per affrontare questi problemi di sicurezza degli LLM. Gli sviluppatori, non sempre avvezzi ai rischi associati agli LLM, si trovavano di fronte a risorse frammentate. La missione di OWASP sembrava quindi perfetta per guidare un'adozione sicura di questa tecnologia.

### A chi si rivolge questo documento?

Il nostro pubblico principale sono gli sviluppatori, i data scientist e gli esperti di sicurezza incaricati di pianificare e costruire applicazioni e plugin basati su tecnologie LLM. Il nostro obiettivo è fornire una guida pratica e concisa per aiutare questi professionisti a muoversi nel terreno complesso e in continua evoluzione della sicurezza degli LLM.

### La creazione della lista

La creazione dell’OWASP Top 10 per le applicazioni LLM ha richiesto un impegno significativo, realizzata grazie all'esperienza collettiva di un gruppo internazionale di quasi 500 esperti, con più di 125 contributori attivi. I nostri collaboratori provengono da contesti diversi, che includono aziende nel campo dell’intelligenza artificiale, aziende del settore della sicurezza, fornitori indipendenti di software, piattaforme cloud e hyperscale, e il mondo della ricerca accademica.

Nel corso di un mese, abbiamo discusso e proposto potenziali vulnerabilità e i membri del gruppo hanno considerato fino a 43 minacce distinte. Attraverso molteplici round di selezione, abbiamo ridotto queste proposte fino ad arrivare a una lista concisa delle 10 vulnerabilità più critiche.

Ognuna di queste vulnerabilità, congiuntamente agli esempi, ai suggerimenti relativi alla prevenzione, agli scenari di attacco e ai riferimenti, è stata ulteriormente esaminata e rifinita da sotto-gruppi specializzati e sottoposta a una revisione pubblica, per assicurare che la lista finale fosse il più possibile completa e concretamente applicabile.

### Relazione con le altre liste OWASP Top 10

Anche se la nostra lista condivide il DNA con i tipi di vulnerabilità che si possono trovare nelle altre liste OWASP Top 10, non ci limitiamo a reiterarle, ma analizziamo le implicazioni uniche che queste vulnerabilità hanno quando appaiono in applicazioni basate sugli LLM.

Il nostro obiettivo è di colmare la distanza tra i principi generali di sicurezza delle applicazioni e le sfide specifiche poste dagli LLM. Questo include l’esplorazione di come le vulnerabilità tradizionali possano porre rischi differenti o possano essere sfruttate in nuovi modi con gli LLM, e come i rimedi tradizionali debbano essere adattati alle applicazioni basate sugli LLM.

### Riguardo versione 1.1

Anche se la nostra lista condivide il DNA con i tipi di vulnerabilità che si possono trovare nelle altre liste OWASP Top 10, non ci limitiamo a reiterarle, ma analizziamo le implicazioni uniche che queste vulnerabilità hanno quando appaiono in applicazioni basate sugli LLM.

Il nostro obiettivo è di colmare la distanza tra i principi generali di sicurezza delle applicazioni e le sfide specifiche poste dagli LLM. Questo include l’esplorazione di come le vulnerabilità tradizionali possano porre rischi differenti o possano essere sfruttate in nuovi modi con gli LLM, e come i rimedi tradizionali debbano essere adattati alle applicazioni basate sugli LLM.

### Il futuro

La versione 1.1 di questa lista non sarà l’ultima. Ci aspettiamo di aggiornare questa lista periodicamente, per stare al passo con l’evoluzione del settore. Lavoreremo con la comunità per far evolvere la tecnologia e creare altro materiale di studio per una serie di casi d’uso. Miriamo inoltre a collaborare con gli organismi di standardizzazione e i governi a riguardo della sicurezza dell’intelligenza artificiale. Ti invitiamo a unirti al nostro gruppo e contribuire.


#### Steve Wilson
Responsabile del progetto OWASP Top 10 per le applicazioni LLM
[https://www.linkedin.com/in/wilsonsd](https://www.linkedin.com/in/wilsonsd/)    
Twitter/X: @virtualsteve


#### Ads Dawson
Responsabile della release 1.1 e responsabile voci di vulerabilità per il progetto OWASP Top 10 per le applicazioni LLM
[https://www.linkedin.com/in/adamdawson0](https://www.linkedin.com/in/adamdawson0/) 
GitHub: @GangGreenTemperTatum

### Riguardo alla traduzione

**Traduttori**

- **Fabrizio Cilli**  
[https://www.linkedin.com/in/fabriziocilli/](https://www.linkedin.com/in/fabriziocilli/)  
- **Matteo Dora**  
[https://www.linkedin.com/in/mattbit/](https://www.linkedin.com/in/mattbit/)  
- **Riccardo Sirigu**  
[https://www.linkedin.com/in/riccardosirigu/](https://www.linkedin.com/in/riccardosirigu/)
- **Valerio Alessandroni**  
[https://www.linkedin.com/in/valerio-alessandroni/](https://www.linkedin.com/in/valerio-alessandroni/) 

Nella realizzazione di questa traduzione, abbiamo scelto consapevolmente di impiegare solo traduttori umani, riconoscendo la natura eccezionalmente tecnica e critica dell’OWASP Top Ten per gli LLM. I traduttori elencati sopra non solo possiedono una profonda comprensione del contenuto originale, ma anche la fluidità per rendere questa traduzione un successo.

Talesh Seeparsan
Responsabile traduzioni, OWASP Top 10 per le applicazioni LLM
[https://www.linkedin.com/in/talesh/](https://www.linkedin.com/in/talesh/)  

## ﻿OWASP Top 10 per le applicazioni LLM

### LLM01: Iniezione di Prompt
Input artificiosi possono manipolare un modello linguistico di grandi dimensioni, causando azioni non volute. Le iniezioni dirette sovrascrivono i prompt di sistema, mentre quelle indirette manipolano gli input provenienti da fonti esterne.

### LLM02: Gestione Non Sicura dell'Output
Questa vulnerabilità accade quando l'output del LLM è accettato senza previa verifica, esponendo i sistemi backend. L'abuso può portare a conseguenze gravi come XSS, CSRF, SSRF, escalation dei privilegi o esecuzione di codice remoto.

### LLM03: Avvelenamento dei Dati di Apprendimento
Questo si verifica quando i dati di apprendimento del LLM vengono manomessi, introducendo vulnerabilità o bias che ne compromettono la sicurezza, l'efficacia o il comportamento etico. Le fonti di dati includono Common Crawl, WebText, OpenWebText e libri.

### LLM04: Denial of Service del Modello
Degli attaccanti causano operazioni che richiedono risorse elevate sui modelli linguistici di grandi dimensioni, portando a degrado del servizio o a costi elevati. La vulnerabilità è amplificata dalla natura intensiva delle risorse degli LLM e dall'imprevedibilità degli input dell'utente.

### LLM05: Vulnerabilità della Supply-Chain
Il ciclo di vita dell'applicazione LLM può essere compromesso da componenti o servizi vulnerabili, portando ad attacchi di sicurezza. L'utilizzo di dataset, modelli pre-addestrati e plugin di terze parti può aggiungere altre vulnerabilità.

### LLM06: Diffusione di Informazioni Sensibili
Gli LLM possono rivelare dati confidenziali nelle risposte, portando ad accessi non autorizzati, violazioni della privacy e falle di sicurezza. Per mitigare questo rischio, è cruciale implementare un processo di sanitizzazione dei dati e politiche utente rigorose.

### LLM07: Progettazione Insicura dei Plugin
I plugin LLM possono avere input non sicuri e controlli di accesso insufficienti. Questa mancanza di controllo dell'applicazione li rende più facili da sfruttare e può comportare conseguenze come l'esecuzione remota di codice.

### LLM08: Eccessiva Autonomia
I sistemi basati sugli LLM possono intraprendere azioni che conducono a conseguenze non volute. Il problema nasce da funzionalità, permessi o autonomia eccessivi concessi a questi sistemi.

### LLM09: Eccessivo Affidamento
Senza supervisione, sistemi o persone eccessivamente dipendenti dagli LLM possono incorrere in disinformazione, malfunzionamenti, problemi legali e vulnerabilità di sicurezza dovute a contenuti errati o inappropriati generati dagli LLM.

### LLM10: Furto del Modello
Questa vulnerabilità consiste nell'accesso non autorizzato, la copia o l'esfiltrazione di modelli LLM proprietari. L'impatto include perdite economiche, compromissione del vantaggio competitivo e potenziale accesso a informazioni sensibili.
