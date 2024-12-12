## LLM06:2025 Excessive Agency

### Description

Einem LLM-basierten System wird von seinem Entwickler oft ein gewisses Maß an Handlungsfähigkeit zugestanden - die Fähigkeit, Funktionen aufzurufen oder über Erweiterungen (von den verschiedenen Anbietern manchmal als Tools, Skills oder Plugins bezeichnet) mit anderen Systemen zu interagieren, um als Reaktion auf eine Eingabeaufforderung Aktionen auszuführen. Die Entscheidung, welche Erweiterung aufgerufen werden soll, kann auch an einen LLM-„Agenten“ delegiert werden, der dies dynamisch auf der Grundlage einer Eingabeaufforderung oder der LLM-Ausgabe bestimmt. Agentenbasierte Systeme rufen in der Regel wiederholt einen LLM auf, wobei sie die Ausgaben früherer Aufrufe nutzen, um die nachfolgenden Aufrufe zu begründen und zu steuern.

Excessive Agency ist die Schwachstelle, die es ermöglicht, als Reaktion auf unerwartete, zweideutige oder manipulierte Ausgaben eines LLM schädliche Aktionen durchzuführen, unabhängig davon, was die Fehlfunktion des LLM verursacht. Häufige Auslöser sind:
* Halluzinationen/Verwirrungen, die durch schlecht entwickelte, gutartige Prompts oder einfach ein schlecht funktionierendes Modell verursacht werden;
* direkte/indirekte Eingabeaufforderung durch einen böswilligen Benutzer, ein früherer Aufruf einer böswilligen/kompromittierten Erweiterung oder (in Systemen mit mehreren Agenten/Kollaboration) ein böswilliger/kompromittierter Peer-Agent.

Die Ursache für Excessive Agency ist in der Regel eine oder mehrere der folgenden Ursachen:
* übermäßige Funktionalität;
* übermäßige Berechtigungen;
* übermäßige Autonomie.

Excessive Agency kann ein breites Spektrum an Auswirkungen auf die Vertraulichkeit, Integrität und Verfügbarkeit haben und hängt davon ab, mit welchen Systemen eine LLM-basierte App interagieren kann.

Hinweis: Excessive Agency unterscheidet sich von Insecure Output Handling, bei dem es um eine unzureichende Prüfung von LLM-Outputs geht.

### Gängige Beispiele für Risiken

#### 1. Übermäßige Funktionalität
  Ein LLM-Agent hat Zugriff auf Erweiterungen, die Funktionen enthalten, die für den beabsichtigten Betrieb des Systems nicht erforderlich sind. Zum Beispiel muss ein Entwickler einem LLM-Agenten die Möglichkeit geben, Dokumente aus einem Repository zu lesen, aber die von ihm gewählte 3rd-Party-Erweiterung beinhaltet auch die Möglichkeit, Dokumente zu ändern und zu löschen.
#### 2. Übermäßige Funktionalität
  Eine Erweiterung kann während einer Entwicklungsphase getestet und zugunsten einer besseren Alternative fallen gelassen worden sein, aber das ursprüngliche Plugin bleibt für den LLM-Agenten verfügbar.
#### 3. Übermäßige Funktionalität
  Ein LLM-Plugin mit offenem Funktionsumfang filtert die Eingabeanweisungen nicht ordnungsgemäß nach Befehlen, die nicht für den beabsichtigten Betrieb der Anwendung erforderlich sind. Eine Erweiterung zur Ausführung eines bestimmten Shell-Befehls verhindert z. B. nicht, dass andere Shell-Befehle ausgeführt werden.
#### 4. Übermäßige Berechtigungen
  Eine LLM-Erweiterung verfügt über Berechtigungen auf nachgelagerten Systemen, die für den beabsichtigten Betrieb der Anwendung nicht erforderlich sind. Zum Beispiel verbindet sich eine Erweiterung, die Daten lesen soll, mit einem Datenbankserver über eine Identität, die nicht nur SELECT-Berechtigungen, sondern auch UPDATE-, INSERT- und DELETE-Berechtigungen hat.
#### 5. Übermäßige Berechtigungen
  Eine LLM-Erweiterung, die darauf ausgelegt ist, Operationen im Kontext eines einzelnen Benutzers durchzuführen, greift auf nachgelagerte Systeme mit einer allgemeinen hochprivilegierten Identität zu. Eine Erweiterung zum Lesen des Dokumentenspeichers des aktuellen Benutzers verbindet sich z. B. mit dem Dokumentenspeicher mit einem privilegierten Konto, das Zugriff auf die Dateien aller Benutzer hat.
#### 6. Übermäßige Autonomie
  Eine LLM-basierte Anwendung oder Erweiterung ist nicht in der Lage, Aktionen mit hoher Auswirkung unabhängig zu überprüfen und zu genehmigen. Eine Erweiterung, die das Löschen von Dokumenten eines Nutzers erlaubt, führt beispielsweise Löschungen ohne Bestätigung durch den Nutzer durch.

### Präventions- und Mitigationsstrategien

Die folgenden Maßnahmen können eine Excessive Agency verhindern:

#### 1. Erweiterungen minimieren
  Beschränke die Erweiterungen, die LLM-Agenten aufrufen dürfen, auf das notwendige Minimum. Wenn ein LLM-basiertes System zum Beispiel nicht die Fähigkeit benötigt, den Inhalt einer URL abzurufen, sollte dem LLM-Agenten eine solche Erweiterung nicht angeboten werden.
#### 2. Erweiterungsfunktionalität minimieren
  Beschränke die Funktionen, die in LLM-Erweiterungen implementiert werden, auf das notwendige Minimum. Eine Erweiterung, die auf das Postfach eines Nutzers zugreift, um E-Mails zusammenzufassen, muss zum Beispiel nur in der Lage sein, E-Mails zu lesen, und sollte daher keine anderen Funktionen wie das Löschen oder Senden von Nachrichten enthalten.
#### 3. Vermeide Erweiterungen mit offenem Ende
  Vermeide nach Möglichkeit Erweiterungen mit offenem Ende (z. B. einen Shell-Befehl ausführen, eine URL abrufen usw.) und verwende Erweiterungen mit detaillierteren Funktionen. Eine LLM-basierte Anwendung muss zum Beispiel eine Ausgabe in eine Datei schreiben. Wenn dies über eine Erweiterung zum Ausführen einer Shell-Funktion realisiert wird, ist der Spielraum für unerwünschte Aktionen sehr groß (jeder andere Shell-Befehl könnte ausgeführt werden). Eine sicherere Alternative wäre es, eine spezielle Erweiterung für das Schreiben von Dateien zu entwickeln, die nur diese spezielle Funktion implementiert.
#### 4. Erweiterungsberechtigungen minimieren
  Beschränke die Berechtigungen, die LLM-Erweiterungen anderen Systemen gewähren, auf das notwendige Minimum, um den Umfang unerwünschter Aktionen zu begrenzen. Ein LLM-Agent, der eine Produktdatenbank nutzt, um einem Kunden Kaufempfehlungen zu geben, braucht z. B. nur Lesezugriff auf die Tabelle „Produkte“; er sollte weder Zugriff auf andere Tabellen noch die Möglichkeit haben, Datensätze einzufügen, zu aktualisieren oder zu löschen. Dies sollte durch die Anwendung geeigneter Datenbankberechtigungen für die Identität, die die LLM-Erweiterung für die Verbindung zur Datenbank verwendet, durchgesetzt werden.
#### 5. Ausführen von Erweiterungen im Kontext des Benutzers
  Verfolge die Benutzerautorisierung und den Sicherheitsbereich, um sicherzustellen, dass Aktionen, die im Namen eines Benutzers durchgeführt werden, auf nachgelagerten Systemen im Kontext des jeweiligen Benutzers und mit den erforderlichen Mindestberechtigungen ausgeführt werden. Zum Beispiel sollte eine LLM-Erweiterung, die das Code-Repository eines Nutzers liest, die Authentifizierung des Nutzers über OAuth und den erforderlichen Mindestumfang erfordern.
#### 6. Benutzerfreigabe erforderlich machen
  Nutze die „Human-in-the-Loop“-Kontrolle, um zu verlangen, dass ein Mensch Aktionen mit großen Auswirkungen genehmigt, bevor sie ausgeführt werden. Dies kann in einem nachgelagerten System (außerhalb des Geltungsbereichs der LLM-Anwendung) oder innerhalb der LLM-Erweiterung selbst implementiert werden. Eine LLM-basierte Anwendung, die im Auftrag eines Nutzers Inhalte für soziale Medien erstellt und postet, sollte zum Beispiel eine Genehmigungsroutine in der Erweiterung enthalten, die den „Post“-Vorgang implementiert.
#### 7. Vollständige Mediation
  Implementiere die Autorisierung in nachgelagerten Systemen, anstatt dich auf eine LLM zu verlassen, um zu entscheiden, ob eine Aktion erlaubt ist oder nicht. Setze das Prinzip der vollständigen Vermittlung durch, damit alle Anfragen, die über Erweiterungen an nachgelagerte Systeme gestellt werden, anhand von Sicherheitsrichtlinien überprüft werden.
#### 8. LLM-Eingaben und -Ausgaben säubern
  Befolge die Best Practices für sichere Kodierung, z. B. die Empfehlungen von OWASP im ASVS (Application Security Verification Standard), mit besonderem Schwerpunkt auf der Eingabesanitisierung. Verwende statische Anwendungssicherheitstests (SAST) und dynamische und interaktive Anwendungstests (DAST, IAST) in den Entwicklungspipelines.

Die folgenden Optionen werden Excessive Agency nicht verhindern, können aber den Schaden begrenzen:

- Protokollieren und überwachen Sie die Aktivitäten von LLM-Erweiterungen und nachgelagerten Systemen, um festzustellen, wo unerwünschte Aktionen stattfinden, und reagieren Sie entsprechend.
- Implementiere eine Ratenbegrenzung, um die Anzahl der unerwünschten Aktionen innerhalb eines bestimmten Zeitraums zu reduzieren und die Chance zu erhöhen, unerwünschte Aktionen durch Überwachung zu entdecken, bevor ein erheblicher Schaden entsteht.

### Beispiele für Angriffsszenarien

Eine LLM-basierte persönliche Assistenten-App erhält über eine Erweiterung Zugriff auf die Mailbox einer Person, um den Inhalt eingehender E-Mails zusammenzufassen. Um diese Funktion zu erreichen, muss die Erweiterung in der Lage sein, Nachrichten zu lesen. Das Plugin, für das sich der Systementwickler entschieden hat, enthält jedoch auch Funktionen zum Senden von Nachrichten. Außerdem ist die App anfällig für einen indirekten Prompt-Injection-Angriff, bei dem eine böswillig erstellte eingehende E-Mail den LLM dazu verleitet, den Agenten anzuweisen, den Posteingang des Benutzers nach sensiblen Informationen zu durchsuchen und diese an die E-Mail-Adresse des Angreifers weiterzuleiten. Dies kann vermieden werden, indem:
* überflüssige Funktionen eliminiert werden, indem eine Erweiterung verwendet wird, die nur E-Mail-Lesefunktionen implementiert,
* übermäßige Berechtigungen beseitigt werden, indem man sich beim E-Mail-Dienst des Nutzers über eine OAuth-Sitzung mit Leseberechtigung authentifiziert, und/oder
* Beseitigung übermäßiger Autonomie, indem der Nutzer jede von der LLM-Erweiterung erstellte E-Mail manuell überprüfen und auf „Senden“ drücken muss.

Alternativ könnte der verursachte Schaden durch die Implementierung einer Ratenbegrenzung auf der Schnittstelle für den E-Mail-Versand verringert werden.

### Referenzlinks

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
