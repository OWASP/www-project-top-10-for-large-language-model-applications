## LLM09: Eccessivo Affidamento

### Descrizione

L'Eccessivo Affidamento si manifesta quando un LLM produce risultati erronei, presentati con una falsa aura di autorità.
Mentre gli LLM usualmente producono materiale creativo e informativo, questi possono anche generare contenuti fattualmente scorretti, inappropriati o pericolosi. Questo fenomeno è noto sotto il nome di allucinazione o confabulazione. Quando persone o sistemi si affidano incondizionatamente a queste informazioni, si possono generare violazioni della sicurezza, disinformazione, comunicazione errata, problemi legali, e danni reputazionali.

Il codice Sorgente generato da LLM, può introdurre silenziosamente delle vulnerabilità di sicurezza. Ciò espone a rischi significativi per l'integrità operativa, e la sicurezza delle applicazioni. Questi rischi sottolineano l'importanza di continui processi di verifica, attraverso:
* Supervisione
* Meccanismi di validazione continua
* Note agli utilizzatori sui rischi connessi all'utilizzo di tali tecnologie.

### Esempi comuni di vulnerabilità

1. Un LLM fornisce informazioni inesatte come risposta, presentate in maniera molto autorevole. L'intero sistema è progettato senza adeguati controlli e bilanciamento per gestire queste situazioni e le informazioni generate possono traviare l'utente in maniera da generare potenziali danni.
2. Un LLM propone codice insicuro o difettoso, introducendo vulnerabilità quando incorporato in un sistema software senza controlli preventivi o verifiche puntuali su di esso.

### Strategie di prevenzione e mitigazione

1. Monitoraggio costante e revisione degli output del LLM. Utilizzo di tecniche rivolte all'auto-consistenza o metodi di voto per filtrare testi incoerenti. Analizzare e confrontare le varie risposte fornite dal modello a un unico prompt può aiutare a valutare meglio la qualità e la coerenza degli output.
2. Controlli incrociati sul modello rispetto a fonti esterne certificate. Questo livello supplementare di validazione può aiutare ad assicurare che le informazioni prodotte dal modello siano accurate e affidabili.
3. Migliorare il modello con metodi di taratura fine (fine-tuning) o incorporazione (embedding) per migliorare la qualità degli output. Modelli generici pre-addestrati possono generare informazioni meno accurate con maggiore probabilità rispetto a modelli addestrati su un dominio specifico. Tecniche come l'ingegnerizzazione dei prompt, ottimizzazione efficiente dei parametri (PET), ottimizzazione dell'intero modello, e prompting basato su catena di pensiero (chain of thoughts prompting) possono ottimizzarne le prestazioni.
4. Implementazione di meccanismi di validazione automatica che possono effettuare controlli comparativi sugli output generati, rispetto a fatti o dati consolidati. Questo può fornire un livello di sicurezza aggiuntiva e mitigare i rischi associati alle allucinazioni.
5. Suddivisione di compiti complessi in singole azioni parziali più gestibili, e assegnazione ad agenti specializzati. Questo non solo aiuta a gestire la complessità, ma anche a ridurre le probabilità di allucinazione essendo ogni agente responsabile di obiettivi più limitati e controllabili.
6. Comunicare in modo trasparente i rischi e le limitazioni associate con l'utilizzo degli LLM. Ciò include potenziale inesattezza delle informazioni, e altri rischi connessi. Una chiara comunicazione dei rischi prepara gli utenti a potenziali problemi e li aiuta a prendere decisioni in modo consapevole.
7. Costruire API e interfacce utente che incoraggino un utilizzo responsabile degli LLM. Questo include misure come filtri di contenuti, avvisi di potenziale inesattezza e chiara indicazione dei materiali generati dall'AI.
8. Quando si utilizzano LLM in ambienti di sviluppo, è necessario stabilire criteri di codifica sicura e linee guida che prevengano l'introduzione di potenziali vulnerabilità. 

### Esempi di scenari di attacco

1. Una testata giornalistica si affida eccessivamente a un LLM per generare i propri articoli e notizie. Un malintenzionato può sfruttare questa eccessiva dipendenza, iniettando nel LLM informazioni fuorvianti, che favoriscono la diffusione di notizie false o mirate.
2. L'intelligenza artificiale plagia involontariamente contenuti, causando problemi di proprietà intellettuale che minano la credibilità dell'organizzazione coinvolta.
3. Un team di sviluppo software utilizza un LLM per accelerare la scrittura di codice. Un'eccessiva dipendenza dai suggerimenti dell'AI introduce vulnerabilità nelle applicazioni generate a causa di parametri di default insicuro o raccomandazioni che non rispettano le pratiche di sviluppo sicuro.
4. Un'azienda che si occupa di sviluppo software utilizza un LLM per fornire assistenza agli sviluppatori. Il modello suggerisce una libreria o un pacchetto inesistenti e uno sviluppatore, affidandosi all'AI, integra senza saperlo un pacchetto malevolo nel software venduto dall'azienda. Questo esempio sottolinea l'importanza dei controlli incrociati sui suggerimenti del modello, specialmente in relazione a codice o librerie di terze parti.

### Riferimenti e link (Inglese)

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk): **Vulcan.io**
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
