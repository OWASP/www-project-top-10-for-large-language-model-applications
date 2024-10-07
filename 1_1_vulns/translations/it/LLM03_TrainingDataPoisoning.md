## LLM03: Avvelenamento dei Dati di Apprendimento

### Descrizione

Il punto di partenza di qualsiasi approccio di machine learning (apprendimento automatico) è costituito dai dati di addestramento, semplicemente del "testo grezzo". Per essere un modello con capacità elevate (ad esempio, che abbia conoscenze linguistiche e del mondo), questo testo deve coprire un'ampia gamma di domini, generi e lingue. Un grande modello di linguaggio utilizza reti neurali profonde per generare output basati su pattern appresi dai dati di apprendimento.

Con avvelenamento dei dati si intende la manipolazione dei dati usati nel processo di pre-apprendimento (pre-training), di fine-tuning o di embedding, al fine di introdurre delle vulnerabilità (che hanno tutte vettori di attacco unici e a volte condivisi), backdoor o bias che potrebbero compromettere la sicurezza, l'efficacia o il comportamento etico del modello. Le informazioni avvelenate possono essere presentate agli utenti o creare altri rischi come la degradazione delle prestazioni, l'exploit del software downstream e danni alla reputazione. Anche se gli utenti non si fidano dell'output problematico dell'IA, i rischi rimangono, comprese le capacità compromesse del modello e potenziali danni alla reputazione del marchio.

- Il pre-apprendimento si riferisce al processo di addestramento di un modello basato su un compito o un set di dati.
- Il fine-tuning consiste nel prendere un modello esistente che è già stato addestrato e riadattarlo a un dominio più ristretto o a un obiettivo più focalizzato, addestrandolo utilizzando uno specifico set di dati. Questo set di dati include tipicamente esempi di input e i corrispondenti output desiderati.
- Il processo di embedding è il processo di conversione di dati categorici (spesso testo) in una rappresentazione numerica che può essere utilizzata per addestrare un modello di linguaggio. L'embedding consiste nella rappresentazione di parole o frasi prese dai dati testuali, come vettori in uno spazio vettoriale continuo. I vettori sono solitamente generati passando dati testuali attraverso una rete neurale che è stata addestrata su un ampio corpus di testo.

L'avvelenamento dei dati è considerato un attacco all'integrità perché la manipolazione dei dati di addestramento influisce sulla capacità del modello di produrre previsioni corrette. Naturalmente, le fonti di dati esterne presentano un rischio maggiore poiché i creatori del modello non hanno controllo su questi dati né la sicurezza che il contenuto non contenga bias, false informazioni o contenuti inappropriati.

### Esempi comuni di vulnerabilità

1. Un attaccante o un'azienda concorrente crea intenzionalmente dei documenti inaccurati o malevoli, che sono indirizzati al pre-addestramento, fine-tuning o al processo di embedding del modello. Considerate entrambi i vettori di attacco di "avvelenamento da vista separata" (rif.12) e "avvelenamento per anticipazione" (rif.13) come esempi.
   - Il modello vittima viene addestrato utilizzando informazioni false che si riflettono negli output che il modello di IA generativa fornisce ai suoi fruitori.
2. Un attaccante è in grado di iniettare direttamente dei contenuti falsi, tendenziosi o pericolosi nei processi di addestramento di un modello, facendo così in modo che questi contenuti vengano poi restituiti dai suoi output.
3. Un utente ignaro inietta indirettamente dati sensibili o proprietari nei processi di addestramento di un modello, che vengono poi restituiti negli output successivi.
4. Un modello è addestrato usando dati la cui fonte, origine o contenuto non sono stati sottoposti a verifica in nessuna delle fasi di addestramento, il che può portare a risultati errati se i dati sono contaminati o non corretti.
5. L'accesso senza restrizioni all'infrastruttura o un sandboxing (isolamento) inadeguato possono consentire a un modello di acquisire dati di addestramento non sicuri, con conseguenti output tendenziosi o dannosi. Questo esempio può verificarsi in una qualsiasi delle fasi di addestramento.
   - In questo scenario, l'input che un utente fornisce al modello può essere riflesso nell'output di un altro utente (portando a una violazione), oppure l'utente di un LLM può ricevere dal modello output inesatti, irrilevanti o dannosi a seconda del tipo di dati ingeriti, confrontandoli ai casi d'uso del modello (di solito riportati nella model card).

Che siate sviluppatori, clienti o fruitori generici di un LLM, è importante comprendere come questa vulnerabilità potrebbe riflettersi sui rischi all'interno della vostra applicazione LLM quando questa interagisce con un LLM non proprietario, per comprendere la legittimità degli output del modello in base alle sue procedure di addestramento. Allo stesso modo, gli sviluppatori del LLM potrebbero essere a rischio di attacchi diretti e indiretti ai dati interni o di terze parti utilizzati per il fine-tuning e l'embedding (il più comune), comportando un rischio per tutti i suoi fruitori.

### Strategie di prevenzione e mitigazione

1. Verificare la filiera di approvvigionamento dei dati utilizzati per l'addestramento, soprattutto quando sono ottenuti da fonti esterne, nonché mantenere attestazioni tramite la metodologia "ML-BOM" (Machine Learning Bill of Materials) e verificare le model card.
2. Verificare la legittimità delle fonti di dati e dei dati ottenuti durante le fasi di pre-apprendimento, fine-tuning ed embedding.
3. Verificare il caso d'uso del LLM e l'applicazione in cui verrà integrato. Sviluppare modelli specifici, utilizzando set di dati di addestramento distinti o tecniche di fine-tuning per ciascun caso d'uso, per affinare l'output dell'intelligenza artificiale generativa, rendendolo più dettagliato e preciso secondo il caso d'uso definito.
4. Assicurare un adeguato sandboxing attraverso controlli di rete rigorosi, per prevenire che il modello acceda a dati da fonti non autorizzate, evitando così il rischio di compromettere l'integrità dell'output del processo di apprendimento automatico.
5. Adottare un controllo rigoroso o filtri sull'input per dati di addestramento specifici o per determinate categorie di fonti di dati, per mantenere sotto controllo il volume di dati non genuini. Sanificare i dati con tecniche come la rilevazione statistica degli outlier o il rilevamento delle anomalie, per identificare e rimuovere i dati "ostili" che potrebbero essere inseriti nel processo di fine-tuning.
6. Elaborare domande di controllo riguardanti la fonte e la proprietà dei set di dati per garantire che il modello non sia stato avvelenato, e adottare questa cultura nel ciclo di vita "MLSecOps". Fare riferimento a risorse disponibili come ad esempio "The Foundation Model Transparency Index" (rif.14) o "Open LLM Leaderboard" (rif.15).
7. Usare "Data Version Control" (rif.16) per identificare e monitorare in modo rigoroso quella parte del set di dati che potrebbe essere stata manipolata, eliminata o aggiunta, portando all'avvelenamento dei dati.
8. Utilizzare database vettoriali per integrare informazioni fornite dall'utente, consentendo di tutelare gli utenti dall'avvelenamento dei dati e persino di apportare correzioni in ambiente di produzione senza la necessità di riaddestrare un nuovo modello.
9. Tecniche di robustezza avversaria come l'apprendimento federato (federated learning) e l'applicazione di vincoli per minimizzare gli effetti di outlier o dell'addestramento avversariale per aumentare la resistenza alle peggiori perturbazioni che possono presentarsi nei dati di addestramento.
   - Un approccio "MLSecOps" potrebbe essere quello di includere una fase di rafforzamento avversariale nel ciclo di vita dell'addestramento utilizzando ad esempio la tecnica del "auto-avvelenamento".
   - Un esempio di questo approccio è "Autopoison" (rif.17), che include test per attacchi come l'iniezione diretta di contenuto ("tentativo di promuovere un marchio nelle risposte del modello") e l'attacco di rifiuto ("fare in modo che il modello rifiuti sempre di rispondere").
10. Testare e rilevare, misurando la perdita durante la fase di addestramento e analizzando i modelli addestrati per rilevare gli indizi di un attacco di avvelenamento, controllando il comportamento del modello su input di test specifici.
11. Monitorare e segnalare il numero di risposte distorte che superano una certa soglia.
12. Usare una validazione umana per fare un audit delle risposte.
13. Implementare LLM dedicati per mettere alla prova i modelli rispetto a conseguenze indesiderate e addestrare altri LLM usando tecniche di apprendimento con rinforzo (rif.18).
14. Eseguire esercitazioni di tipo red team (rif.19) basate su LLM o scansioni di vulnerabilità (rif.20) nelle fasi di test del ciclo di vita del LLM.

### Esempi di scenario di attacco

1. L'output di un'IA generativa può indurre in errore gli utenti dell'applicazione, portando a opinioni tendenziose o, peggio ancora, reati d'odio, ecc. con scopi tendenziosi.
2. Se i dati di apprendimento non vengono correttamente filtrati e/o sanificati, un utente malevolo potrebbe tentare di influenzare il modello iniettando dati tossici per farlo adattare ai dati falsificati e tendenziosi.
3. Un utente malevolo o un concorrente crea deliberatamente documenti inaccurati o malevoli indirizzati ai dati di addestramento di un modello, che è in fase di addestramento al tempo stesso in base a questi input. Il modello vittima impara utilizzando informazioni falsificate che si riflettono negli output che il modello di IA generativa fornisce ai suoi fruitori.
4. L'iniezione di prompt (LLM01) potrebbe essere un vettore di attacco per questa vulnerabilità se non viene eseguita una sanitizzazione e un filtraggio adeguati quando gli input degli utenti sono usati per addestrare il modello. Ad esempio, se dati malevoli o falsificati vengono inseriti nel modello da un utente attraverso una tecnica di iniezione di prompt, questi potrebbero essere intrinsecamente rappresentati nei dati su cui il modello si basa.

### Riferimenti e link (Inglese)

1. [Stanford Research Paper:CS324](https://stanford-cs324.github.io/winter2022/lectures/data/): **Stanford Research**
2. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
3. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
6. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
7. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper**
8. [FedMLSecurity:arXiv:2306.04959](https://arxiv.org/abs/2306.04959): **Arxiv White Paper**
9. [The poisoning of ChatGPT](https://softwarecrisis.dev/letters/the-poisoning-of-chatgpt/): **Software Crisis Blog**
10. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **YouTube Video**
11. [OWASP CycloneDX v1.5](https://cyclonedx.org/capabilities/mlbom/): **OWASP CycloneDX**
12. [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg)
13. [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg)
14. [The Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/)
15. [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
16. [Data Version Control](https://dvc.org/doc/user-guide/analytics)
17. [Autopoison](https://github.com/azshue/AutoPoison)
18. [tecniche di apprendimento con rinforzo](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy)
19. [red team](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned)
20. [scansioni di vulnerabilità](https://github.com/leondz/garak)
