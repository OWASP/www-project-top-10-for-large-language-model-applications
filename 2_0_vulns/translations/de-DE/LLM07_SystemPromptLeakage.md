## LLM07:2025 Offenlegung des Systems Prompts

### Beschreibung

Die Offenlegung von System Prompts in LLMs bezieht sich auf das Risiko, dass System Prompts oder Anweisungen, die zur Steuerung des Modellverhaltens verwendet werden, auch sensible Informationen enthalten können, die nicht entdeckt werden sollen. System Prompts werden verwendet, um die Ausgabe des Modells entsprechend den Anforderungen der Anwendung zu steuern, können aber versehentlich vertrauliche Informationen enthalten. Wenn diese Informationen entdeckt werden, können sie für andere Angriffe verwendet werden.

Es ist wichtig zu verstehen, dass der System Prompt nicht als geheim angesehen werden sollte und auch nicht als Sicherheitskontrolle verwendet werden darf. Dementsprechend sollten sensible Daten wie Anmeldedaten, Verbindungsstrings usw. nicht in der System Prompt-Sprache enthalten sein.

Wenn ein System Prompt Informationen über verschiedene Rollen und Berechtigungen oder sensible Daten wie Connection Strings oder Passwörter enthält, kann die Offenlegung dieser Informationen zwar hilfreich sein, aber das grundlegende Sicherheitsrisiko besteht nicht darin, dass diese Informationen offengelegt werden, sondern dass die Anwendung es ermöglicht, strenge Session Management und Berechtigungsprüfungen zu umgehen, indem diese an das LLM delegiert werden, und dass sensible Daten an einem Ort gespeichert werden, an dem sie nicht sein sollten.

Kurz gesagt: Die Offenlegung des System Prompts selbst stellt nicht das eigentliche Risiko dar - das Sicherheitsrisiko liegt in den zugrunde liegenden Elementen, sei es die Offenlegung sensibler Daten, die Umgehung von Systemschutzmechanismen, die unsachgemäße Trennung von Berechtigungen usw. Selbst wenn der genaue Wortlaut nicht offengelegt wird, sind Angreifende, die mit dem System interagiert, mit ziemlicher Sicherheit in der Lage, viele der Schutzmaßnahmen und Format-Beschränkungen zu erkennen, die in der Sprache des System Prompts enthalten sind, wenn sie die Anwendung benutzen, Äußerungen an das Modell senden und die Ergebnisse beobachten.

### Gängige Beispiele für Risiken

#### 1. Offenlegung von sensiblen Funktionen
  Der System Prompt der Anwendung kann sensible Informationen oder Funktionen offenlegen, die eigentlich vertraulich behandelt werden sollten, z. B. sensible Systemarchitektur, API-Schlüssel, Datenbankanmeldeinformationen oder User-Tokens. Diese können von Angreifenden extrahiert oder verwendet werden, um unbefugten Zugriff auf die Anwendung zu erhalten. Ein Beispiel wäre ein System Prompt, der den verwendeten Datenbanktyp eines Tools enthält. Dadurch könnten Angreifer gezielt SQL-Injection-Angriffe auf diese Datenbank ausführen.
#### 2. Offenlegung von internen Regeln
  Der System Prompt der Anwendung offenbart Informationen über interne Entscheidungsprozesse, die vertraulich behandelt werden sollten. Diese Informationen ermöglichen es Angreifenden, Einblicke in die Funktionsweise der Anwendung zu gewinnen, was es ihnen ermöglichen könnte, Schwachstellen auszunutzen oder Kontrollen in der Anwendung zu umgehen. Ein Beispiel: Eine Bankanwendung hat einen Chatbot, dessen Systemabfrage folgende Informationen enthüllen kann 
    >"Das Transaktionslimit ist für eine Person auf 5000 USD pro Tag festgelegt. Der Gesamtkreditbetrag für eine Person beträgt 10.000 USD“.
  Diese Informationen ermöglichen es den Angreifenden, die Sicherheitskontrollen in der Anwendung zu umgehen, indem sie z. B. Transaktionen durchführen, die das festgelegte Limit überschreiten, oder den Gesamtkreditbetrag aushebeln.
#### 3. Offenlegung von Filterkriterien
  Ein System Prompt kann das Modell auffordern, sensible Inhalte zu filtern oder zurückzuweisen. Ein Modell könnte z. B. eine Systemaufforderung wie folgt enthalten,
    >„Wenn eine Person Informationen über eine andere Person anfordert, antworte immer mit ‚Tut mir leid, bei dieser Anfrage kann ich nicht helfen‘“.
#### 4. Offenlegung von Berechtigungen und Benutzerrollen
  Der System Prompt könnte die internen Rollenstrukturen oder Berechtigungsstufen der Anwendung offenlegen. Ein System Prompt könnte zum Beispiel verraten,
    >"Die Benutzerrolle Admin gewährt vollen Zugriff auf die Änderung von Benutzerdatensätzen.“
  Wenn die Angreifenden von diesen rollenbasierten Berechtigungen erfahren, könnten sie nach einem Angriff zur Privilegienerweiterung suchen.

### Präventions- und Mitigationsstrategien

#### 1. Trennen Sie sensible Daten vom System Prompt
  Vermeiden Sie es, sensible Informationen (z. B. API-Schlüssel, Authentifizierungsschlüssel, Datenbanknamen, Benutzerrollen, Berechtigungsstruktur der Anwendung) direkt in den System Prompt einzubetten. Lagern Sie solche Informationen stattdessen in den Systemen aus, auf die das Modell nicht direkt zugreift.
###$ 2. Vermeiden Sie es, für eine strenge Verhaltenskontrolle auf System Prompts 
####     zurückzugreifen
  Da LLMs anfällig für andere Angriffe wie Prompt Injections sind, mit denen die Systemprompts verändert werden können, wird empfohlen, die Verwendung von Systemprompts zur Steuerung des Modellverhaltens nach Möglichkeit zu vermeiden. Verlassen Sie sich stattdessen auf Systeme außerhalb des LLMs, um dieses Verhalten sicherzustellen. Die Erkennung und Verhinderung schädlicher Inhalte sollte zum Beispiel von externen Systemen übernommen werden.
#### 3. Implementieren Sie Guardrails
  Implementieren Sie ein System von Leitplanken außerhalb des LLM selbst. Es kann zwar effektiv sein, einem Modell ein bestimmtes Verhalten anzutrainieren, z. B. dass es seine Systemaufforderung nicht preisgibt, aber das ist keine Garantie dafür, dass das Modell sich immer daran hält. Ein unabhängiges System, das die Ausgabe überprüfen kann, um festzustellen, ob das Modell die Erwartungen erfüllt, ist den Anweisungen des Systems vorzuziehen.
###$ 4. Stellen Sie sicher, dass die Sicherheitskontrollen unabhängig
####     vom LLM durchgesetzt werden
  Stellen Sie sicher, dass kritische Kontrollen wie z. B. die Trennung von Berechtigungen, die Überprüfung von Berechtigungsgrenzen und Ähnliches nicht an das LLM delegiert werden, weder über die Systemsteuerung noch auf andere Weise. Diese Kontrollen müssen auf deterministische, überprüfbare Weise erfolgen, und LLMs sind dafür (derzeit) nicht förderlich. Wenn ein Agent Aufgaben ausführt, die unterschiedliche Zugriffsrechte erfordern, setzen Sie mehrere Agenten ein, die jeweils mit den geringsten Rechten ausgestattet sind, die für die Ausführung der gewünschten Aufgaben erforderlich sind.

### Beispiele für Angriffsszenarien

#### Szenario 1
  Ein LLM verfügt über einen System Prompt, der eine Reihe von Anmeldeinformationen enthält, die für ein Tool verwendet werden, auf das der LLM Zugriff hat. Der System Prompt wird Angreifenden offengelegt, die diese Anmeldeinformationen dann für andere Zwecke verwenden können.
#### Szenario 2
  Ein LLM verfügt über einen System Prompt, der die Erstellung anstößiger Inhalte, externe Links und die Ausführung von Code verbietet. Angreifende extrahieren diesen System Prompt und verwendet dann einen Prompt Injection-Angriff, um diese Anweisungen zu umgehen und einen Remotecodeausführung-Angriff zu ermöglichen.

### Referenzlinks

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt finden Sie umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
