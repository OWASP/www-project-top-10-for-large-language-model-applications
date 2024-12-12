## LLM07:2025 Offenlegung des Systems Prompts

### Beschreibung

Die Offenlegung von System Prompts in LLMs bezieht sich auf das Risiko, dass der System Prompt oder die Anweisungen, die zur Steuerung des Verhaltens des Modells verwendet werden, auch sensible Informationen enthalten können, die nicht entdeckt werden sollten. System Prompts dienen dazu, die Ausgabe des Modells entsprechend den Anforderungen der Anwendung zu steuern, können aber versehentlich geheime Informationen enthalten. Wenn diese Informationen entdeckt werden, können sie für andere Angriffe genutzt werden.

Es ist wichtig zu verstehen, dass der System Prompt nicht als Geheimnis betrachtet werden sollte und auch nicht als Sicherheitskontrolle verwendet werden darf. Dementsprechend sollten sensible Daten wie Anmeldedaten, Verbindungsstrings usw. nicht in der Sprache der Systemansage enthalten sein.

Wenn ein System Prompt Informationen über verschiedene Rollen und Berechtigungen oder sensible Daten wie Verbindungsstrings oder Passwörter enthält, kann die Offenlegung dieser Informationen zwar hilfreich sein, aber das grundlegende Sicherheitsrisiko besteht nicht darin, dass diese Informationen offengelegt wurden, sondern darin, dass die Anwendung es ermöglicht, strenge Sitzungsmanagement- und Berechtigungsprüfungen zu umgehen, indem sie diese an das LLM delegiert, und dass sensible Daten an einem Ort gespeichert werden, an dem sie nicht sein sollten.

Kurz gesagt: Die Offenlegung des System Prompts selbst stellt nicht das eigentliche Risiko dar - das Sicherheitsrisiko liegt in den zugrundeliegenden Elementen, sei es die Offenlegung sensibler Daten, die Umgehung von Systemschutzmechanismen, die unsachgemäße Trennung von Berechtigungen usw. Selbst wenn der genaue Wortlaut nicht offengelegt wird, sind Angreifer, die mit dem System interagieren, mit ziemlicher Sicherheit in der Lage, viele der Leitplanken und Formatierungsbeschränkungen zu erkennen, die in der Sprache der Systemansagen enthalten sind, wenn sie die Anwendung benutzen, Äußerungen an das Modell senden und die Ergebnisse beobachten.

### Gängige Beispiele für Risiken

#### 1. Offenlegung von sensiblen Funktionen
  Der System Prompt der Anwendung kann sensible Informationen oder Funktionen offenlegen, die eigentlich vertraulich behandelt werden sollten, z. B. sensible Systemarchitektur, API-Schlüssel, Datenbankanmeldeinformationen oder Benutzer-Tokens.  Diese können von Angreifern extrahiert oder verwendet werden, um unbefugten Zugriff auf die Anwendung zu erhalten. Eine Systemeingabeaufforderung, die den Typ der für ein Tool verwendeten Datenbank enthält, könnte es dem Angreifer zum Beispiel ermöglichen, diese für SQL-Injection-Angriffe zu nutzen.
#### 2. Offenlegung von internen Regeln
  Der System Prompt der Anwendung offenbart Informationen über interne Entscheidungsprozesse, die vertraulich behandelt werden sollten. Diese Informationen ermöglichen es Angreifern, Einblicke in die Funktionsweise der Anwendung zu gewinnen, was es ihnen ermöglichen könnte, Schwachstellen auszunutzen oder Kontrollen in der Anwendung zu umgehen. Ein Beispiel: Eine Bankanwendung hat einen Chatbot, dessen Systemabfrage folgende Informationen enthüllen kann 
    >"Das Transaktionslimit ist für einen Benutzer auf 5000 USD pro Tag festgelegt. Der Gesamtkreditbetrag für einen Benutzer beträgt 10.000 USD“.
  Diese Informationen ermöglichen es den Angreifern, die Sicherheitskontrollen in der Anwendung zu umgehen, indem sie z. B. Transaktionen durchführen, die das festgelegte Limit überschreiten, oder den Gesamtkreditbetrag aushebeln.
#### 3. Offenlegung von Filterkriterien
  Ein System Prompt kann das Modell auffordern, sensible Inhalte zu filtern oder zurückzuweisen. Ein Modell könnte z. B. eine Systemaufforderung wie folgt enthalten,
    >„Wenn ein Benutzer Informationen über einen anderen Benutzer anfordert, antworte immer mit ‚Tut mir leid, bei dieser Anfrage kann ich nicht helfen‘“.
#### 4. Offenlegung von Berechtigungen und Benutzerrollen
  Der System Prompt könnte die internen Rollenstrukturen oder Berechtigungsstufen der Anwendung offenlegen. Ein Systemprompt könnte zum Beispiel verraten,
    >"Die Benutzerrolle Admin gewährt vollen Zugriff auf die Änderung von Benutzerdatensätzen.“
  Wenn die Angreifer von diesen rollenbasierten Berechtigungen erfahren, könnten sie nach einem Angriff zur Privilegienerweiterung suchen.

### Präventions- und Mitigationsstrategien

#### 1. Trenne sensible Daten von Systemaufforderungen
  Vermeide es, sensible Informationen (z. B. API-Schlüssel, Authentifizierungsschlüssel, Datenbanknamen, Benutzerrollen, Berechtigungsstruktur der Anwendung) direkt in den System Prompt einzubetten. Lagere solche Informationen stattdessen in den Systemen aus, auf die das Modell nicht direkt zugreift.
#### 2. Vermeide es, für eine strenge Verhaltenskontrolle auf System Prompts zurückzugreifen
  Da LLMs anfällig für andere Angriffe wie Prompt Injections sind, mit denen die Systemprompts verändert werden können, wird empfohlen, die Verwendung von Systemprompts zur Steuerung des Modellverhaltens nach Möglichkeit zu vermeiden.  Verlasse dich stattdessen auf Systeme außerhalb des LLMs, um dieses Verhalten sicherzustellen.  Die Erkennung und Verhinderung schädlicher Inhalte sollte zum Beispiel von externen Systemen übernommen werden.
#### 3. Guardrails implementieren
  Implementiere ein System von Leitplanken außerhalb des LLM selbst.  Es kann zwar effektiv sein, einem Modell ein bestimmtes Verhalten anzutrainieren, z. B. dass es seine Systemaufforderung nicht preisgibt, aber das ist keine Garantie dafür, dass das Modell sich immer daran hält.  Ein unabhängiges System, das die Ausgabe überprüfen kann, um festzustellen, ob das Modell die Erwartungen erfüllt, ist den Anweisungen des Systems vorzuziehen.
#### 4. Sicherstellen, dass die Sicherheitskontrollen unabhängig vom LLM durchgesetzt werden
  Kritische Kontrollen wie z. B. die Trennung von Berechtigungen, die Überprüfung von Berechtigungsgrenzen und Ähnliches dürfen nicht an das LLM delegiert werden, weder über die Systemsteuerung noch auf andere Weise. Diese Kontrollen müssen auf deterministische, überprüfbare Weise erfolgen, und LLMs sind dafür (derzeit) nicht förderlich. Wenn ein Agent Aufgaben ausführt, die unterschiedliche Zugriffsrechte erfordern, sollten mehrere Agenten eingesetzt werden, die jeweils mit den geringsten Rechten ausgestattet sind, die für die Ausführung der gewünschten Aufgaben erforderlich sind.

### Beispiele für Angriffsszenarien

#### Szenario #1
   Ein LLM hat einen System Prompt, der eine Reihe von Anmeldedaten für ein Tool enthält, zu dem er Zugang erhalten hat.  Der System Prompt wird einem Angreifer zugespielt, der diese Zugangsdaten dann für andere Zwecke nutzen kann.
#### Szenario #2
  Ein LLM hat einen System Prompt, der die Erstellung von anstößigen Inhalten, externen Links und die Ausführung von Code verbietet. Ein Angreifer extrahiert diesen System Prompt und nutzt dann einen Prompt-Injection-Angriff, um diese Anweisungen zu umgehen und einen Angriff zur Remotecodeausführung zu ermöglichen.

### Referenzlinks

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt findest du umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
