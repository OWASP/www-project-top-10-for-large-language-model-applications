## LLM06:2025 Übermäßige Handlungsfreiheit

### Beschreibung

Einem LLM-basierten System wird von den Entwickelnden oft ein gewisser Grad an Handlungsfähigkeit zugestanden, d.h. die Fähigkeit, Funktionen aufzurufen oder mit anderen Systemen über Erweiterungen (von den verschiedenen Anbietern manchmal als Tools, Skills oder Plugins bezeichnet) zu interagieren, um als Reaktion auf eine Eingabeaufforderung Aktionen auszuführen. Die Entscheidung, welche Erweiterung aufgerufen wird, kann auch an einen LLM-„Agenten“ delegiert werden, der dies dynamisch auf der Grundlage einer Eingabeaufforderung oder der LLM-Ausgabe bestimmt. Agentenbasierte Systeme rufen ein LLM in der Regel wiederholt auf, wobei sie die Ausgaben früherer Aufrufe nutzen, um die nachfolgenden Aufrufe zu begründen und zu steuern.

Übermäßige Handlungsfreiheit ist eine Schwachstelle, die die Ausführung schädlicher Aktionen als Reaktion auf unerwartete, mehrdeutige oder manipulierte Ausgaben eines LLM ermöglicht, unabhängig davon, was die Fehlfunktion des LLM verursacht. Die häufigsten Auslöser sind:
* Halluzinationen/Verwirrungen, die durch schlecht entwickelte, gutartige Prompts oder durch ein einfach schlecht funktionierendes Modell verursacht werden;
* direkte/indirekte Eingabeaufforderung durch böswillige Personen, ein früherer Aufruf einer böswilligen/kompromittierten Erweiterung oder (in Systemen mit mehreren Agenten/Kollaboration) ein böswilliger/kompromittierter Peer-Agent.

Die Ursache für Übermäßige Handlungsfreiheit ist in der Regel eine oder mehrere der folgenden Ursachen:
* übermäßige Funktionalität
* übermäßige Berechtigungen
* übermäßige Autonomie

Übermäßige Handlungsfreiheit kann ein breites Spektrum an Auswirkungen auf die Vertraulichkeit, Integrität und Verfügbarkeit haben und hängt davon ab, mit welchen Systemen eine LLM-basierte App interagieren kann.

Hinweis: Übermäßige Handlungsfreiheit unterscheidet sich von Unsichere Ausgabeverarbeitung, bei dem es um eine unzureichende Prüfung von LLM-Outputs geht.

### Gängige Beispiele für Risiken

#### 1. Übermäßige Funktionalität
  Ein LLM-Agent hat Zugriff auf Erweiterungen, die Funktionen enthalten, die für den beabsichtigten Betrieb des Systems nicht erforderlich sind. Zum Beispiel müssen Entwickelnde einem LLM-Agenten die Möglichkeit geben, Dokumente aus einem Repository zu lesen, aber die von ihm gewählte 3rd-Party-Erweiterung beinhaltet auch die Möglichkeit, Dokumente zu ändern und zu löschen.
#### 2. Übermäßige Funktionalität
  Eine Erweiterung kann während einer Entwicklungsphase getestet und zugunsten einer besseren Alternative verworfen worden sein, aber das ursprüngliche Plugin bleibt für den LLM-Agenten verfügbar.
#### 3. Übermäßige Funktionalität
  Ein LLM-Plugin mit offenem Funktionsumfang filtert die Eingabeaufforderungen nicht ordnungsgemäß nach Befehlen, die für den beabsichtigten Betrieb der Anwendung nicht erforderlich sind. Beispielsweise verhindert eine Erweiterung zur Ausführung eines bestimmten Shell-Befehls nicht die Ausführung anderer Shell-Befehle.
#### 4. Übermäßige Berechtigungen
  Eine LLM-Erweiterung verfügt über Berechtigungen auf nachgelagerten Systemen, die für den beabsichtigten Betrieb der Anwendung nicht erforderlich sind. Zum Beispiel verbindet sich eine Erweiterung, die Daten lesen soll, mit einem Datenbankserver über eine Identität, die nicht nur SELECT-Berechtigungen, sondern auch UPDATE-, INSERT- und DELETE-Berechtigungen hat.
#### 5. Übermäßige Berechtigungen
  Eine LLM-Erweiterung, die Operationen im Kontext einer einzelnen Person ausführen soll, greift auf nachgelagerte Systeme mit einer allgemeinen hochprivilegierten Identität zu. Eine Erweiterung zum Lesen des Dokumentenspeichers des aktuellen Benutzers verbindet sich z. B. mit dem Dokumentenspeicher mit einem privilegierten Konto, das Zugriff auf die Dateien aller User hat.
#### 6. Übermäßige Autonomie
  Eine LLM-basierte Anwendung oder Erweiterung ist nicht in der Lage, Aktionen mit hoher Auswirkung unabhängig zu überprüfen und zu genehmigen. Beispielsweise führt eine Erweiterung, die das Löschen von Dokumenten einer Person ermöglicht, Löschungen ohne Bestätigung durch den Benutzer durch.

### Präventions- und Mitigationsstrategien

Die folgenden Maßnahmen können eine Übermäßige Handlungsfreiheit verhindern:

#### 1. Minimieren Sie Erweiterungen
  Beschränken Sie die Erweiterungen, die LLM-Agenten aufrufen können, auf das notwendige Minimum. Wenn z. B. ein LLM-basiertes System nicht die Fähigkeit benötigt, den Inhalt einer URL abzurufen, sollte eine solche Erweiterung dem LLM-Agenten nicht angeboten werden.
#### 2. Minimieren Sie die Funktionalität von LLM-Erweiterungen
  Beschränken Sie die in LLM-Erweiterungen implementierten Funktionen auf das notwendige Minimum. Zum Beispiel sollte eine Erweiterung, die auf die Mailboxen von Personen zugreift, um E-Mails zusammenzufassen, nur in der Lage sein, E-Mails zu lesen, und daher keine anderen Funktionen wie das Löschen oder Senden von Nachrichten enthalten.
#### 3. Vermeiden Sie weitreichende und unbeschränkte Erweiterungen
  Vermeiden Sie nach Möglichkeit weitreichende und unbeschränkte Erweiterungen (z.B. einen Shell-Befehl ausführen, eine URL abrufen usw.) und verwenden Sie Erweiterungen mit detaillierteren Funktionen. Beispielsweise muss eine LLM-basierte Anwendung eine Ausgabe in eine Datei schreiben. Wenn dies über eine Erweiterung zur Ausführung einer Shell-Funktion realisiert wird, ist der Spielraum für unerwünschte Aktionen sehr groß (jeder andere Shell-Befehl könnte ausgeführt werden). Eine sicherere Alternative wäre es, eine spezielle Erweiterung für das Schreiben von Dateien zu entwickeln, die nur diese spezielle Funktion implementiert.
#### 4. Minimieren Sie Berechtigungen für LLM-Erweiterungen
  Beschränken Sie die Berechtigungen, die LLM-Erweiterungen für andere Systeme erhalten, auf das absolut notwendige Minimum. Zum Beispiel benötigt ein LLM-Agent, der eine Produktdatenbank verwendet, um einem Kunden Kaufempfehlungen zu geben, nur Lesezugriff auf die Tabelle „Produkte“; er sollte keinen Zugriff auf andere Tabellen haben und keine Datensätze einfügen, aktualisieren oder löschen können. Dies sollte durch entsprechende Datenbankberechtigungen für die Identität, die die LLM-Erweiterung für die Verbindung zur Datenbank verwendet, durchgesetzt werden.
#### 5. Führen Sie Erweiterungen im Kontext des Benutzers aus
  Verfolgen Sie die Benutzerautorisierung und den Sicherheitsumfang, um sicherzustellen, dass Aktionen, die im Namen von Personen durchgeführt werden, auf nachgelagerten Systemen im Kontext des jeweiligen Benutzers und mit den erforderlichen Mindestberechtigungen ausgeführt werden. Ein Beispiel: Eine LLM-Erweiterung, die auf das Code-Repository eines Benutzers zugreift, sollte erfordern, dass sich der Benutzer per OAuth authentifiziert - und zwar mit dem minimalen Berechtigungsumfang, der für die jeweilige Funktion erforderlich ist.
#### 6. Fordern Sie eine Freigabe durch den Benutzer 
  Nutzen Sie eine manuelle Kontrolle, um zu verlangen, dass ein Mensch Aktionen mit großen Auswirkungen genehmigt, bevor sie ausgeführt werden. Dies kann in einem nachgelagerten System (außerhalb des Geltungsbereichs der LLM-Anwendung) oder innerhalb der LLM-Erweiterung selbst implementiert werden. Beispielsweise sollte eine LLM-basierte Anwendung, die im Auftrag eines Nutzers Inhalte für soziale Medien erstellt und postet, eine Genehmigungsroutine in der Erweiterung enthalten, die den „Post“-Vorgang implementiert.
#### 7. Vollständige Mediation
  Implementieren Sie die Autorisierung in nachgelagerten Systemen, anstatt sich darauf zu verlassen, dass ein LLM entscheidet, ob eine Aktion zulässig ist oder nicht. Setzen Sie das Complete-Mediation-Prinzip (Prinzip der vollständigen Vermittlung) um, sodass alle Anfragen, die über Erweiterungen an nachgelagerte Systeme gestellt werden, gegen die Sicherheitsrichtlinien validiert werden.
#### 8. Säubern Sie LLM-Eingaben und -Ausgaben
  Befolgen Sie die Best Practices für sichere Entwicklung, wie z. B. die Empfehlungen von OWASP im ASVS (Application Security Verification Standard), mit besonderem Schwerpunkt auf der Eingabebereinigung. Verwenden Sie statische Anwendungssicherheitstests (SAST) sowie dynamische und interaktive Anwendungstests (DAST, IAST) in den Entwicklungspipelines.

Die folgenden Optionen können Übermäßige Handlungsfreiheit nicht verhindern, können aber den Schaden begrenzen:
- Protokollieren und überwachen Sie die Aktivitäten von LLM-Erweiterungen und nachgelagerten Systemen, um festzustellen, wo unerwünschte Aktionen stattfinden, und reagieren Sie entsprechend.
- Implementieren Sie ein Rate-Limiting, um die Anzahl unerwünschter Aktionen innerhalb eines bestimmten Zeitraums zu reduzieren und die Chance zu erhöhen, unerwünschte Aktionen durch Überwachung zu entdecken, bevor ein erheblicher Schaden entsteht.

### Beispiele für Angriffsszenarien

Eine LLM-basierte Personal Assistant-Anwendung kann über eine Erweiterung auf die Mailbox einer Person zugreifen, um den Inhalt eingehender E-Mails zusammenzufassen. Für diese Funktion muss die Erweiterung in der Lage sein, Nachrichten zu lesen. Das von den Entwickelnden gewählte Plugin enthält jedoch auch Funktionen zum Versenden von Nachrichten. Außerdem ist die Anwendung anfällig für einen indirekten Prompt-Injection-Angriff, bei dem eine böswillig erzeugte eingehende E-Mail das LLM dazu veranlasst, den Agenten anzuweisen, den Posteingang der nutzenden Person nach sensiblen Informationen zu durchsuchen und diese an die E-Mail-Adresse der Angreifenden weiterzuleiten. 
Dies kann vermieden werden durch:
* das Entfernen überflüssiger Funktionen, indem eine Erweiterung verwendet wird, die ausschließlich Leserechte für E-Mails implementiert,
* das Reduzieren übermäßiger Berechtigungen, indem die Authentifizierung beim E-Mail-Dienst der Benutzenden über eine OAuth-Sitzung mit einem nur-Lesen-Bereich erfolgt, und/oder
* das Begrenzen übermäßiger Autonomie, indem die nutzende Person jede von der LLM-Erweiterung erstellte E-Mail manuell überprüfen und senden muss.

Alternativ könnte der verursachte Schaden durch die Implementierung von Rate-Limiting and der Schnittstelle für den E-Mail-Versand verringert werden.

### Referenzlinks

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
6. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
