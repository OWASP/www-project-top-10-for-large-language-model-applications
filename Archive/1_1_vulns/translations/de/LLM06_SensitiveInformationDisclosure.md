## LLM06: Offenlegung sensibler Informationen

### Beschreibung

LLM-Anwendungen haben das Potenzial, durch ihre Ausgabe sensible Informationen, proprietäre Algorithmen oder andere vertrauliche Details zu offenbaren. Dies kann zu unberechtigtem Zugriff auf sensible Daten, geistiges Eigentum, Verletzungen der Privatsphäre und anderen Sicherheitsverletzungen führen. Es ist wichtig, dass die Benutzerinnen und Benutzer von LLM-Anwendungen wissen, wie sie sicher mit LLMs interagieren können, und dass sie sich der Risiken bewusst sind, die mit der unbeabsichtigten Eingabe sensibler Daten verbunden sind, die dann von der LLM in der Ausgabe an anderer Stelle zurückgegeben werden können.

Um dieses Risiko zu minimieren, sollten LLM-Anwendungen eine angemessene Datenbereinigung durchführen, um zu verhindern, dass Benutzerdaten in die Daten des Trainingsmodells gelangen. Die Eigentümer von LLM-Anwendungen sollten auch über angemessene Nutzungsbedingungen verfügen, um die Verbraucher darüber zu informieren, wie ihre Daten verarbeitet werden, und ihnen die Möglichkeit zu geben, die Aufnahme ihrer Daten in das Trainingsmodell abzulehnen.

Die Interaktion zwischen Verbraucher und LLM-Anwendung bildet eine zweiseitige Vertrauensgrenze, bei der wir weder den Eingaben des Clients->LLM noch den Ausgaben des LLM->Client vertrauen können. Es ist wichtig zu beachten, dass diese Schwachstelle davon ausgeht, dass bestimmte Voraussetzungen nicht gegeben sind, wie z.B. Bedrohungsmodellierungsverfahren, eine sichere Infrastruktur und eine angemessene Sandbox. Das Hinzufügen von Einschränkungen in der System-Eingabeaufforderung bezüglich der Datentypen, die der LLM zurückgeben soll, kann einen gewissen Schutz vor der Offenlegung sensibler Informationen bieten. Die unvorhersehbare Natur von LLMs bedeutet jedoch, dass solche Einschränkungen nicht immer beachtet werden und durch Prompt Injection oder andere Vektoren umgangen werden könnten.

### Gängige Beispiele für Schwachstellen

1. Unvollständige oder unsachgemäße Filterung von sensiblen Informationen in den Antworten des LLM.
2. Übermäßige Angleichung oder Einprägung sensibler Daten im Trainingsprozess des LLM.
3. Unbeabsichtigte Offenlegung vertraulicher Informationen aufgrund von Fehlinterpretationen des LLM, fehlenden Datenbereinigungsmethoden oder Fehlern.

### Präventions- und Mitigationsstrategien

1. Integrieren Sie geeignete Datenbereinigungs- und Scrubbing-Techniken, um zu verhindern, dass Benutzerdaten in die Daten des Trainingsmodells gelangen.
2. Implementierung robuster Eingabevalidierungs- und -bereinigungsmethoden, um potenziell schädliche Eingaben zu identifizieren und zu entfernen, damit das Modell nicht vergiftet wird.
3. Wenn das Modell mit Daten angereichert und Fine-Tuning (Ref.7) betrieben wird: (z. B. Daten, die dem Modell vor oder während der Bereitstellung zugeführt werden)
  - Alles, was in den Fine-Tuning-Daten als sensibel eingestuft ist, könnte Personen offengelegt werden. Wenden Sie daher das Least-Privilege-Prinzip an und trainieren Sie das Modell nicht mit Informationen, auf die Personen mit den höchsten Rechten zugreifen können und die dann einer weniger privilegierten Person angezeigt werden könnten.
  - Der Zugriff auf externe Datenquellen (Orchestrierung von Daten zur Laufzeit) sollte eingeschränkt werden.
  - Strenge Zugriffskontrollmethoden für externe Datenquellen und ein rigoroser Ansatz zur Aufrechterhaltung einer sicheren Lieferkette.

### Beispiele für Angriffsszenarien

1. Die ahnungslose, legitime Benutzerin A erhält über das LLM Zugang zu anderen Benutzerdaten, wenn sie in nicht böswilliger Absicht mit der LLM-Anwendung interagiert.
2. Benutzer A zielt darauf ab, die Eingabefilter und die Bereinigungsfunktionen des LLM durch eine ausgeklügelte Abfolge von Eingabeaufforderungen zu umgehen und Personen dazu zu bringen, personenbezogene Informationen (PII) über andere Personen der Anwendung preiszugeben.
3. Personenbezogene Daten wie z.B. PII gelangen über Trainingsdaten in das Modell, entweder durch Unachtsamkeit der Person selbst oder durch die LLM-Anwendung. Dies könnte das Risiko und die Wahrscheinlichkeit von Szenario 1 oder 2 oben erhöhen.

### Referenzen

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use) **Cohere**
4. [A threat modeling example](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
5. [OWASP AI Security and Privacy Guide](https://owasp.org/www-project-ai-security-and-privacy-guide/): **OWASP AI Security & Privacy Guide**
6. [Ensuring the Security of Large Language Models](https://www.experts-exchange.com/articles/38220/Ensuring-the-Security-of-Large-Language-Models-Strategies-and-Best-Practices.html): **Experts Exchange**
7. [Fine-Tuning](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Definitions)