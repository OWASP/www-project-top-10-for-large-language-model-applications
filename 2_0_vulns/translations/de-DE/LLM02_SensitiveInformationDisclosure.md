## LLM02:2025 Unsichere Ausgabeverarbeitung

### Beschreibung

Sensible Informationen können sowohl das LLM als auch seinen Anwendungskontext betreffen. Dazu gehören personenbezogene Daten, Finanzdaten, Gesundheitsakten, vertrauliche Geschäftsdaten, Sicherheitsdaten und Rechtsdokumente. Auch proprietäre Modelle können über einzigartige Trainingsmethoden und Quellcode verfügen, die als sensibel gelten, insbesondere bei geschlossenen oder Foundation-Modellen.
LLMs, insbesondere wenn sie in Anwendungen eingebettet sind, bergen das Risiko, dass durch ihre Ausgabe sensible Daten, proprietäre Algorithmen oder vertrauliche Details offengelegt werden. Dies kann zu unbefugtem Datenzugriff, Datenschutzverletzungen und Verstößen gegen das geistige Eigentum führen. Verbraucher sollten wissen, wie sie sicher mit LLMs umgehen können. Sie müssen sich der Risiken bewusst sein, die mit der unbeabsichtigten Bereitstellung sensibler Daten verbunden sind, die später in der Ausgabe des Modells offengelegt werden können.

Um dieses Risiko zu verringern, sollten LLM-Anwendungen eine angemessene Datenbereinigung durchführen, um zu verhindern, dass Benutzerdaten in das Trainingsmodell gelangen. Die Eigentümer der Anwendungen sollten außerdem klare Nutzungsbedingungen bereitstellen, die es den Benutzern ermöglichen, die Aufnahme ihrer Daten in das Trainingsmodell abzulehnen. Das Hinzufügen von Einschränkungen innerhalb der Systemaufforderung zu den Datentypen, die das LLM zurückgeben sollte, kann eine Minderung der Offenlegung sensibler Informationen bewirken. Solche Einschränkungen werden jedoch möglicherweise nicht immer beachtet und können durch das Einfügen von Aufforderungen oder andere Methoden umgangen werden.

### Gängige Beispiele für Schwachstellen

#### 1. Verlust personenbezogener Daten
  Bei Interaktionen mit dem LLM können personenbezogene Daten offengelegt werden.
#### 2. Offenlegung proprietärer Algorithmen
  Schlecht konfigurierte Modellausgaben können proprietäre Algorithmen oder Daten offenlegen. Durch die Offenlegung von Trainingsdaten können Modelle Inversionsangriffen ausgesetzt werden, bei denen Angreifer sensible Informationen extrahieren oder Eingaben rekonstruieren. Wie beispielsweise beim „Proof Pudding“-Angriff (CVE-2019-20634) gezeigt wurde, erleichterten offengelegte Trainingsdaten die Extraktion und Inversion von Modellen, sodass Angreifer Sicherheitskontrollen in Algorithmen für maschinelles Lernen umgehen und E-Mail-Filter überlisten konnten.
#### 3. Offenlegung sensibler Geschäftsdaten
  Die generierten Antworten können versehentlich vertrauliche Geschäftsinformationen enthalten.

### Präventions- und Mitigationsstrategien

###@ Sanitization:

#### 1. Integriere Techniken zur Datenbereinigung
  Implementiere eine Datenbereinigung, um zu verhindern, dass Benutzerdaten in das Trainingsmodell gelangen. Dazu gehört das Bereinigen oder Maskieren sensibler Inhalte, bevor sie im Training verwendet werden.
#### 2. Robuste Eingabevalidierung
  Wende strenge Methoden zur Eingabevalidierung an, um potenziell schädliche oder sensible Dateneingaben zu erkennen und herauszufiltern, und stelle so sicher, dass sie das Modell nicht beeinträchtigen.

###@ Zugriffskontrollen:

#### 1. Strenge Zugriffskontrollen durchsetzen
  Beschränke den Zugriff auf sensible Daten nach dem Prinzip der geringsten Privilegien. Gewähre nur Zugriff auf Daten, die für den jeweiligen Benutzer oder Prozess erforderlich sind.
#### 2. Datenquellen einschränken
  Beschränke den Modellzugriff auf externe Datenquellen und stelle sicher, dass die Orchestrierung von Laufzeitdaten sicher verwaltet wird, um unbeabsichtigte Datenlecks zu vermeiden.

###@ Föderiertes Lernen und Datenschutztechniken:

#### 1. Föderiertes Lernen nutzen
  Trainiere Modelle mit dezentralen Daten, die auf mehreren Servern oder Geräten gespeichert sind. Dieser Ansatz minimiert die Notwendigkeit einer zentralen Datenerfassung und reduziert die Risiken der Offenlegung.
#### 2. Differential Privacy einbeziehen
  Wende Techniken an, die die Daten oder Ausgaben mit Rauschen versehen, wodurch es für Angreifer schwierig wird, einzelne Datenpunkte zurückzuentwickeln.

###@ Nutzerschulungen und Transparenz:

#### 1. Nutzer über die sichere Nutzung von LLM aufklären
  Anleitung zur Vermeidung der Eingabe sensibler Informationen bereitstellen. Schulungen zu bewährten Verfahren für den sicheren Umgang mit LLMs anbieten.
#### 2. Transparenz bei der Datennutzung sicherstellen
  Klare Richtlinien für die Aufbewahrung, Nutzung und Löschung von Daten befolgen. Nutzern die Möglichkeit geben, die Aufnahme ihrer Daten in Schulungsprozesse abzulehnen.

###@ Sichere Systemkonfiguration:

#### 1. Verbergen des Systems Präambel
  Schränkt die Möglichkeit für Benutzer ein, die ursprünglichen Einstellungen des Systems zu überschreiben oder darauf zuzugreifen, wodurch das Risiko einer Offenlegung interner Konfigurationen verringert wird.
#### 2. Referenz für bewährte Verfahren zur Sicherheit bei Fehlkonfigurationen
  Befolge Richtlinien wie „OWASP API8:2023 Security Misconfiguration“, um zu verhindern, dass vertrauliche Informationen durch Fehlermeldungen oder Konfigurationsdetails durchsickern.
  (Ref. link:[OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/))


###@ Fortgeschrittene Techniken:

#### 1. Homomorphe Verschlüsselung
  Verwende homomorphe Verschlüsselung, um eine sichere Datenanalyse und datenschutzkonformes maschinelles Lernen zu ermöglichen. Dadurch wird sichergestellt, dass die Daten während der Verarbeitung durch das Modell vertraulich bleiben.
#### 2. Tokenisierung und Schwärzung
  Implementiere Tokenisierung, um sensible Informationen vorzuverarbeiten und zu bereinigen. Techniken wie Mustererkennung können vertrauliche Inhalte vor der Verarbeitung erkennen und schwärzen.

### Beispiele für Angriffsszenarien

#### Szenario 1: Unbeabsichtigte Offenlegung von Daten
  Ein Benutzer erhält eine Antwort, die die personenbezogenen Daten eines anderen Benutzers enthält, weil die Daten nicht ordnungsgemäß gelöscht wurden.
#### Szenario 2: Gezielte Eingabeaufforderung
  Ein Angreifer umgeht Eingabefilter, um vertrauliche Informationen zu extrahieren.
#### Szenario 3: Datenleck über Trainingsdaten
  Die fahrlässige Einbeziehung von Daten in das Training führt zur Offenlegung vertraulicher Informationen.

### Referenzlinks

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt findest du umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**
