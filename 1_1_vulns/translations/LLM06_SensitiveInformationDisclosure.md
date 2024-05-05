## LLM06: Offenlegung sensibler Informationen

### Beschreibung

LLM-Anwendungen (Large Language Models) können das Potenzial haben, sensible Informationen, proprietäre Algorithmen oder andere vertrauliche Details durch ihre Ausgabe zu offenbaren. Dies kann zu unbefugtem Zugriff auf sensible Daten, geistiges Eigentum, Verletzungen der Privatsphäre und anderen Sicherheitsverstößen führen. Es ist wichtig für Nutzer von LLM-Anwendungen, sich darüber im Klaren zu sein, wie sie sicher mit LLMs interagieren und die Risiken erkennen können, die mit der unbeabsichtigten Eingabe sensibler Daten verbunden sind, die anschließend von der LLM in der Ausgabe anderswo zurückgegeben werden könnten.

Um dieses Risiko zu mindern, sollten LLM-Anwendungen eine angemessene Datenbereinigung (PII-Scrubbing) durchführen, um zu verhindern, dass Benutzerdaten in die Trainingsdaten des Modells gelangen. Eigentümer von LLM-Anwendungen sollten auch angemessene Nutzungsbedingungen zur Verfügung stellen, um Verbraucher darüber zu informieren, wie ihre Daten verarbeitet werden, und die Möglichkeit bieten, sich dagegen zu entscheiden, dass ihre Daten in das Trainingsmodell aufgenommen werden.

Die Interaktion zwischen Verbraucher und LLM-Anwendung bildet eine Zwei-Wege-Vertrauensgrenze, bei der wir das Client->LLM-Eingabe oder das LLM->Client-Ausgabe nicht grundsätzlich vertrauen können. Es ist wichtig zu beachten, dass diese Schwachstelle davon ausgeht, dass bestimmte Voraussetzungen außerhalb des Geltungsbereichs liegen, wie Bedrohungsmodellierungsübungen, Sicherung der Infrastruktur und angemessene Sandboxing. Das Hinzufügen von Einschränkungen innerhalb des Systemprompts bezüglich der Arten von Daten, die das LLM zurückgeben sollte, kann eine gewisse Milderung gegen die Offenlegung sensibler Informationen bieten, aber die unvorhersehbare Natur der LLMs bedeutet, dass solche Einschränkungen möglicherweise nicht immer eingehalten werden und durch Prompt-Injektion oder andere Vektoren umgangen werden könnten.

### Häufige Beispiele für Schwachstellen

1. Unvollständige oder unsachgemäße Filterung sensibler Informationen in den Antworten des LLMs.
2. Overfitting oder Memorierung sensibler Daten im Trainingsprozess des LLMs.
3. Unbeabsichtigte Offenlegung vertraulicher Informationen aufgrund von Fehlinterpretationen des LLMs, mangelnden Datenbereinigungsmethoden oder Fehlern.

### Strategien zur Prävention und Milderung

1. Integriere angemessene Datenbereinigungs- und Scrubbing-Techniken, um zu verhindern, dass Benutzerdaten in die Trainingsdaten des Modells gelangen.
2. Implementiere robuste Eingabevalidierungs- und Sanitisierungsmethoden, um potenziell bösartige Eingaben zu identifizieren und herauszufiltern, um zu verhindern, dass das Modell vergiftet wird.
3. Wenn das Modell mit Daten angereichert und [feinabgestimmt](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Definitions) wird: (z.B. Daten, die dem Modell vor oder während der Bereitstellung zugeführt werden)
   1. Alles, was in den Feinabstimmungsdaten als sensibel erachtet wird, hat das Potenzial, einem Benutzer offenbart zu werden. Wende daher die Regel des geringsten Privilegs an und trainiere das Modell nicht mit Informationen, auf die der am höchsten privilegierte Benutzer zugreifen kann und die einem Benutzer mit niedrigeren Privilegien angezeigt werden können.
   2. Der Zugang zu externen Datenquellen (Orchestrierung von Daten zur Laufzeit) sollte begrenzt werden.
   3. Wende strenge Zugangskontrollmethoden für externe Datenquellen an und verfolge einen rigorosen Ansatz zur Aufrechterhaltung einer sicheren Lieferkette.

### Beispielszenarien für Angriffe

1. Ein ahnungsloser legitimer Benutzer A wird bestimmten anderen Benutzerdaten über das LLM ausgesetzt, wenn er auf nicht bösartige Weise mit der LLM-Anwendung interagiert.
2. Benutzer A zielt auf eine sorgfältig erstellte Reihe von Prompts, um Eingabefilter und Sanitisierungsmaßnahmen des LLMs zu umgehen, damit es sensible Informationen (PII) über andere Benutzer der Anwendung preisgibt.
3. Persönliche Daten wie PII werden aufgrund von Fahrlässigkeit des Benutzers selbst oder der LLM-Anwendung in das Modell über das Trainingsdaten geleakt. Dieser Fall könnte das Risiko und die Wahrscheinlichkeit von Szenario 1 oder 2 oben erhöhen.

### Referenzlinks

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use) **Cohere**
4. [A threat modeling example](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
5. [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/): **OWASP AI Security & Privacy Guide**
6. [Ensuring the Security of Large Language Models](https://www.experts-exchange.com/articles/38220/Ensuring-the-Security-of-Large-Language-Models-Strategies-and-Best-Practices.html): **Experts Exchange**
