## LLM06: Diffusione di Informazioni Sensibili

### Descrizione

Le applicazioni LLM possono rivelare informazioni sensibili, algoritmi proprietari o altri dettagli confidenziali attraverso i loro output. Ciò può portare ad accessi non autorizzati, esposizione di dati sensibili, proprietà intellettuale, violazioni della privacy e altre problematiche di sicurezza. È importante che gli utenti delle applicazioni LLM siano consapevoli di come interagire in modo sicuro con gli LLM e identificare i rischi associati all'inserimento involontario di dati sensibili i quali potrebbero poi essere divulgati dal LLM in altri contesti.

Per mitigare questo rischio, le applicazioni LLM dovrebbero implementare un'adeguata sanificazione dei dati per impedire che i dati degli utenti entrino indiscriminatamente nei set di dati di addestramento del modello. I gestori di applicazioni LLM dovrebbero inoltre fornire dei Termini di Utilizzo adeguati, facilmente accessibili per informare gli utenti come vengono gestiti i loro dati, e l'opzione ben visibile per negare il consenso a includere i loro dati nei processi di addestramento del modello.

L'interazione tra l'utente e l'applicazione LLM instaura un contesto di fiducia reciproca, nel quale non possiamo fidarci intrinsecamente né dell'input utente->LLM né dell'output LLM->utente. È importante notare che questa vulnerabilità presuppone che certi prerequisiti siano assicurati al di fuori del presente ambito di analisi, fra questi gli esercizi di modellazione delle minacce (threat modeling), la protezione delle infrastrutture e una segregazione adeguata degli ambienti di esecuzione. Aggiungere restrizioni all'interno del prompt del sistema riguardo ai tipi di dati che il LLM dovrebbe restituire può fornire una mitigazione parziale contro la divulgazione di informazioni sensibili, tuttavia, data l'imprevedibilità degli LLM è possibile che tali restrizioni potrebbero non essere sempre efficaci e potrebbero essere aggirate tramite iniezione di prompt o altri metodi.

### Esempi comuni di vulnerabilità

1. Filtraggio incompleto o inefficace delle informazioni sensibili presenti nelle risposte del LLM.
2. Sovradattamento o memorizzazione di dati sensibili nel processo di addestramento del LLM.
3. Divulgazione involontaria di informazioni confidenziali a causa di errata interpretazione da parte del LLM, mancanza di metodi di pulizia dei dati o errori.

### Strategie di prevenzione e mitigazione

1. Integrare adeguate tecniche di sanificazione e pulizia dei dati per impedire che i dati degli utenti entrino nei set di dati di addestramento del modello.
2. Implementare metodi robusti di validazione e sanificazione degli input per identificare ed escludere potenziali input malevoli per prevenire l'avvelenamento (poisoning) del modello.
3. Quando si arricchisce il modello con dati e se si effettua il "fine-tuning" (rif.7) di un modello (ad esempio, dati inseriti nel modello prima o durante il rilascio):
  - Qualunque informazione sensibile nei dati di fine-tuning ha il potenziale di essere rivelato a un utente. Pertanto, si raccomanda di applicare la buona pratica di minimizzazione dei privilegi di accesso, e di non addestrare il modello su informazioni a cui un utente con privilegi elevati può accedere poiché potrebbero inavvertitamente essere mostrate a un utente con privilegi inferiori.
  - L'accesso a fonti di dati esterne (orchestrazione dei dati in tempo reale) dovrebbe essere limitato.
  - Applicare metodi stringenti di controllo degli accessi alle fonti di dati esterne e un approccio rigoroso nella gestione di una catena di approvvigionamento sicura.

### Esempi di scenari di attacco

1. L'utente legittimo e ignaro A viene esposto a dati di altri utenti tramite il LLM quando interagisce con l'applicazione LLM in modo non malevolo.
2. L'utente A indirizza un insieme ben congegnato di prompt per bypassare i filtri di input e la sanificazione del LLM per far sì che divulghi informazioni sensibili (PII) su altri utenti dell'applicazione.
3. Dati personali (PII) vengono introdotti nel modello durante il processo di addestramento a causa di negligenza da parte dell'utente stesso o dell'applicazione LLM. Questo scenario potrebbe aumentare il rischio e la probabilità degli scenari 1 o 2 sopra descritti.

### Riferimenti e link (Inglese)

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use): **Cohere**
4. [A threat modeling example](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
5. [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/): **OWASP AI Security & Privacy Guide**
6. [Ensuring the Security of Large Language Models](https://www.experts-exchange.com/articles/38220/Ensuring-the-Security-of-Large-Language-Models-Strategies-and-Best-Practices.html): **Experts Exchange**
7. [fine-tuning](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Definitions)
