## LLM08: Übermäßige Handlungsfreiheit

### Beschreibung

Ein System, das auf einem LLM basiert, wird von Entwickelnden oft mit einem gewissen Grad an Handlungsfreiheit ausgestattet - das heißt, der Fähigkeit, mit anderen Systemen zu interagieren und Aktionen auf Anforderung auszuführen. Die Entscheidung, welche Funktionen aufgerufen werden sollen, kann auch an einen LLM-Agenten delegiert werden, um dynamisch auf der Grundlage der Eingabeaufforderung oder der LLM-Ausgabe bestimmt zu werden.

Übermäßige Handlungsfreiheit ist die Schwachstelle, die es ermöglicht, schädliche Aktionen als Reaktion auf unerwartete/unklare Ausgaben eines LLM auszuführen (unabhängig davon, was den LLM fehlerhaft macht; sei es Halluzination/Konfabulation, direkte/indirekte Prompt Injection, bösartige Plug-ins, schlecht konstruierte gutartige Prompts oder einfach ein schlecht funktionierendes Modell). Die Hauptursache für übermäßige Handlungsfreiheit ist typischerweise eine oder mehrere der folgenden: übermäßige Funktionalität, übermäßige Berechtigungen oder übermäßige Autonomie. Dies unterscheidet sich von Unsichere Ausgabeverarbeitung, die sich auf unzureichende Überprüfung der LLM-Ausgabe bezieht.

Übermäßige Handlungsfreiheit kann zu einem breiten Spektrum von Auswirkungen auf Vertraulichkeit, Integrität und Verfügbarkeit führen und hängt von den Systemen ab, mit denen eine LLM-basierte Anwendung interagieren kann.

### Gängige Beispiele für Schwachstellen

1. Übermäßige Funktionalität: Ein LLM-Agent hat Zugriff auf Plug-ins, die Funktionen enthalten, die für den beabsichtigten Betrieb des Systems nicht erforderlich sind. Entwickelnde müssen etwa einem LLM-Agenten die Fähigkeit geben, Dokumente aus einem Repository zu lesen, aber das Plugin eines Drittanbieters, das er verwendet, enthält auch die Fähigkeit, Dokumente zu ändern und zu löschen.
2. Übermäßige Funktionalität: Ein Plugin wurde während einer Entwicklungsphase getestet und zugunsten einer besseren Alternative verworfen, aber das ursprüngliche Plugin bleibt für den LLM-Agenten zugänglich.
3. Übermäßige Funktionalität: Ein LLM-Plugin mit offenem Funktionsumfang filtert nicht korrekt die Eingabeanweisungen für Befehle, die nicht für den beabsichtigten Betrieb der Anwendung notwendig sind. Beispielsweise verhindert ein Plugin zur Ausführung eines bestimmten Shell-Befehls nicht ordnungsgemäß die Ausführung anderer Shell-Befehle.
4. Übermäßige Berechtigungen: Ein LLM-Plugin hat Berechtigungen für andere Systeme, die für den beabsichtigten Betrieb der Anwendung nicht erforderlich sind. Beispielsweise verbindet sich ein Plugin zum Lesen von Daten mit einem Datenbankserver unter Verwendung einer Identität, die nicht nur SELECT-Berechtigungen hat, sondern auch UPDATE-, INSERT- und DELETE-Berechtigungen.
5. Exzessive Berechtigungen: Ein LLM-Plugin, das entwickelt wurde, um Operationen im Namen einer Person durchzuführen, greift auf nachgelagerte Systeme mit einer generischen, hoch privilegierten Identität zu. Beispielsweise verbindet sich ein Plug-in, das den aktuellen Dokumentenspeicher einer Person lesen soll, mit dem Dokumentenspeicher mit einem privilegierten Konto, das Zugriff auf alle Dateien der Person hat.
6. Übermäßige Autonomie: Eine LLM-basierte Anwendung oder ein Plugin versäumt es, hochwirksame Aktionen unabhängig zu überprüfen und zu genehmigen. Beispielsweise führt ein Plugin, das das Löschen von Dokumenten einer Person ermöglicht, Löschungen ohne jegliche Bestätigung durch diese durch.

### Präventions- und Mitigationsstrategien

Die folgenden Maßnahmen können dazu beitragen, übermäßige Handlungsfreiheit zu vermeiden:

1. Beschränken Sie die Plug-ins/Tools, die von LLM-Agenten aufgerufen werden können, auf die notwendige Minimalfunktionalität. Wenn etwa ein LLM-basiertes System nicht die Fähigkeit benötigt, den Inhalt einer URL abzurufen, sollte ein solches Plug-in dem LLM-Agenten nicht angeboten werden.
2. Beschränken Sie die in LLM-Plug-ins/Tools implementierten Funktionen auf das notwendige Minimum. Ein Plug-in, das auf die Mailbox einer Person zugreift, um E-Mails zusammenzufassen, benötigt möglicherweise nur die Fähigkeit, E-Mails zu lesen, und sollte daher keine weiteren Funktionen wie das Löschen oder Versenden von Nachrichten enthalten.
3. Vermeiden Sie nach Möglichkeit Funktionen mit offenem Ende (z.B. einen Shell-Befehl ausführen, eine URL abrufen usw.) und verwenden Sie Plug-ins/Tools mit granulareren Funktionen. Beispielsweise muss eine LLM-basierte Anwendung einige Ausgaben in eine Datei schreiben. Wenn dies mit einem Plugin implementiert wird, das eine Shell-Funktion ausführt, ist der Spielraum für unerwünschte Aktionen gewaltig (jeder andere Shell-Befehl könnte ausgeführt werden). Eine sicherere Alternative wäre es, ein Plug-in zum Schreiben von Dateien zu entwickeln, das nur diese spezielle Funktion unterstützt.
4. Beschränken Sie die Berechtigungen, die LLM-Plug-ins/Tools anderen Systemen gewähren, auf ein Minimum, um den Umfang unerwünschter Aktionen einzuschränken. Beispielsweise benötigt ein LLM-Agent, der eine Produktdatenbank verwendet, um einem Kunden Kaufempfehlungen zu geben, möglicherweise nur Lesezugriff auf eine 'Produkte'-Tabelle; er sollte keinen Zugriff auf andere Tabellen oder die Möglichkeit haben, Datensätze einzufügen, zu aktualisieren oder zu löschen. Dies sollte durch entsprechende Datenbankberechtigungen für die Identität durchgesetzt werden, die das LLM-Plugin verwendet, um sich mit der Datenbank zu verbinden. 
5. Protokollieren Sie die Autorisierung von Personen und den Security Scope, um zu gewährleisten, dass Aktionen, die im Namen der Personen durchgeführt werden, auf nachgelagerten Systemen im Kontext der jeweiligen Person und mit den erforderlichen Mindestrechten ausgeführt werden. Beispielsweise sollte ein LLM-Plugin, das das Code-Repository einer Person liest, verlangen, dass sich die Person über OAuth und mit dem erforderlichen Mindestumfang authentifiziert.
6. Setzen Sie auf menschliche Kontrolle, um für alle Aktionen eine menschliche Genehmigung zu verlangen, bevor sie ausgeführt werden. Dies kann in einem nachgelagerten System (außerhalb der LLM-Anwendung) oder innerhalb des LLM-Plug-ins/Tools selbst implementiert werden. Beispielsweise sollte eine LLM-basierte Anwendung, die Social-Media-Inhalte im Namen einer Person erstellt und veröffentlicht, eine Freigaberoutine innerhalb des Plug-ins/Tools/API enthalten, das die 'Post'-Operation implementiert. 
7. Implementieren Sie Autorisierung in nachgelagerten Systemen, anstatt sich darauf zu verlassen, dass ein LLM entscheidet, ob eine Aktion erlaubt ist oder nicht. Bei der Implementierung von Tools/Plug-ins das Prinzip der vollständigen Mediation (complete mediation principle) anwenden, sodass alle Anfragen, die über Plug-ins/Tools an nachgelagerte Systeme gestellt werden, anhand von Sicherheitsrichtlinien validiert werden.

Die folgenden Optionen verhindern zwar keine übermäßige Handlungsfreiheit, können aber das Ausmaß des Schadens begrenzen:

1. Protokollieren und überwachen Sie die Aktivitäten von LLM-Plug-ins und -Tools sowie von nachgelagerten Systemen, um zu erkennen, wo unerwünschte Aktionen stattfinden, und um entsprechend reagieren zu können.
2. Implementieren Sie Rate-Limiting, um die Anzahl unerwünschter Aktionen, die in einem bestimmten Zeitraum auftreten können, zu reduzieren und die Möglichkeit zu erhöhen, unerwünschte Aktionen durch Überwachung zu erkennen, bevor größerer Schaden entsteht.

### Beispiele für Angriffsszenarien

Eine LLM-basierte Personal Assistant App greift über ein Plug-in auf das Postfach einer Person zu, um den Inhalt eingehender E-Mails zusammenzufassen. Um diese Funktionalität zu erreichen, muss das E-Mail-Plug-in in der Lage sein, Nachrichten zu lesen. Das vom Systementwickler ausgewählte Plug-in enthält jedoch auch Funktionen zum Senden von Nachrichten. Das LLM ist anfällig für einen indirekten Man-in-the-Middle-Angriff, bei dem eine bösartig gestaltete eingehende E-Mail das LLM dazu veranlasst, das E-Mail-Plug-in anzuweisen, die Funktion 'Nachricht senden' aufzurufen, um Spam aus der Mailbox des Benutzers zu versenden. Dies könnte vermieden werden durch
(a) Eliminierung überflüssiger Funktionalität durch Verwendung eines Plug-ins, das nur E-Mail-Lesefunktionen bietet,
(b) Eliminierung von übermäßigen Berechtigungen durch Authentifizierung am E-Mail-Dienst des Benutzers über eine OAuth-Sitzung mit schreibgeschütztem Umfang, und/oder
(c) Eliminierung übermäßiger Autonomie, indem der Benutzer jede vom LLM-Plug-in erzeugte E-Mail manuell überprüfen und auf 'Senden' klicken muss.
Alternativ könnte der verursachte Schaden durch die Implementierung von Rate-Limiting in der Mailversand-Schnittstelle reduziert werden.

### Referenzen

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
2. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
3. [LangChain: Human-approval for tools](https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval): **Langchain Documentation**
4. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**