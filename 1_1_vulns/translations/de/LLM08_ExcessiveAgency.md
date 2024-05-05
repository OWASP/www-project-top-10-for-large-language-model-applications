## LLM08: Übermäßige Handlungsfreiheit

### Beschreibung

Ein auf LLM (Language Model) basierendes System wird oft mit einem gewissen Maß an Handlungsfreiheit durch seinen Entwickler ausgestattet - der Fähigkeit, mit anderen Systemen zu interagieren und auf eine Aufforderung hin Handlungen zu unternehmen. Die Entscheidung darüber, welche Funktionen aufgerufen werden sollen, kann auch an einen LLM 'Agenten' delegiert werden, um dynamisch basierend auf der Eingabeaufforderung oder dem LLM-Ausgang zu bestimmen.

Übermäßige Handlungsfreiheit ist die Schwachstelle, die es ermöglicht, schädliche Aktionen in Reaktion auf unerwartete/unklare Ausgaben von einem LLM durchzuführen (unabhängig davon, was den LLM fehlerhaft macht; sei es Halluzination/Konfabulation, direkte/indirekte Aufforderungsinjektion, bösartiges Plugin, schlecht konstruierte gutartige Aufforderungen oder einfach ein schlecht funktionierendes Modell). Die Hauptursache für übermäßige Handlungsfreiheit ist typischerweise eine oder mehrere der folgenden: übermäßige Funktionalität, übermäßige Berechtigungen oder übermäßige Autonomie. Dies unterscheidet sich von unsicherer Ausgabeverarbeitung, die sich mit unzureichender Prüfung von LLM-Ausgaben beschäftigt.

Übermäßige Handlungsfreiheit kann zu einer breiten Palette von Auswirkungen über das Spektrum von Vertraulichkeit, Integrität und Verfügbarkeit führen und hängt davon ab, mit welchen Systemen eine LLM-basierte App interagieren kann.

### Häufige Beispiele für Schwachstellen

1. Übermäßige Funktionalität: Ein LLM-Agent hat Zugriff auf Plugins, die Funktionen beinhalten, die für den beabsichtigten Betrieb des Systems nicht benötigt werden. Zum Beispiel muss ein Entwickler einem LLM-Agenten die Fähigkeit gewähren, Dokumente aus einem Repository zu lesen, aber das Plugin eines Drittanbieters, das sie verwenden, beinhaltet auch die Fähigkeit, Dokumente zu modifizieren und zu löschen.
2. Übermäßige Funktionalität: Ein Plugin wurde während einer Entwicklungsphase getestet und zugunsten einer besseren Alternative fallengelassen, aber das ursprüngliche Plugin bleibt dem LLM-Agenten zugänglich.
3. Übermäßige Funktionalität: Ein LLM-Plugin mit offenem Funktionsumfang filtert die Eingabeanweisungen für Befehle außerhalb dessen, was für den beabsichtigten Betrieb der Anwendung notwendig ist, nicht ordnungsgemäß. Z.B. ein Plugin zum Ausführen eines bestimmten Shell-Befehls verhindert nicht ordnungsgemäß, dass andere Shell-Befehle ausgeführt werden.
4. Übermäßige Berechtigungen: Ein LLM-Plugin hat Berechtigungen für andere Systeme, die für den beabsichtigten Betrieb der Anwendung nicht benötigt werden. Z.B. verbindet sich ein Plugin, das zum Lesen von Daten gedacht ist, mit einem Datenbankserver unter Verwendung einer Identität, die nicht nur SELECT-Berechtigungen hat, sondern auch UPDATE, INSERT und DELETE-Berechtigungen.
5. Übermäßige Berechtigungen: Ein LLM-Plugin, das entwickelt wurde, um Operationen im Namen eines Benutzers durchzuführen, greift auf nachgelagerte Systeme mit einer generischen hochprivilegierten Identität zu. Z.B. verbindet sich ein Plugin, um den aktuellen Dokumentenspeicher eines Benutzers zu lesen, mit dem Dokumentenrepository mit einem privilegierten Konto, das Zugriff auf alle Dateien der Benutzer hat.
6. Übermäßige Autonomie: Eine LLM-basierte Anwendung oder ein Plugin versäumt es, hochwirksame Aktionen unabhängig zu überprüfen und zu genehmigen. Z.B. führt ein Plugin, das es ermöglicht, Dokumente eines Benutzers zu löschen, Löschungen ohne jegliche Bestätigung vom Benutzer durch.

### Präventions- und Mitigierungsstrategien

Die folgenden Aktionen können übermäßige Handlungsfreiheit verhindern:

1. Beschränken Sie die Plugins/Tools, die LLM-Agenten aufrufen dürfen, auf nur die minimal notwendigen Funktionen. Wenn ein auf LLM basierendes System beispielsweise nicht die Fähigkeit benötigt, den Inhalt einer URL abzurufen, sollte ein solches Plugin dem LLM-Agenten nicht angeboten werden.
2. Beschränken Sie die Funktionen, die in LLM-Plugins/Tools implementiert sind, auf das minimal Notwendige. Ein Plugin, das auf das Postfach eines Benutzers zugreift, um E-Mails zusammenzufassen, benötigt möglicherweise nur die Fähigkeit, E-Mails zu lesen, daher sollte das Plugin keine andere Funktionalität wie das Löschen oder Senden von Nachrichten enthalten.
3. Vermeiden Sie nach Möglichkeit offene Funktionen (z.B. Ausführen eines Shell-Befehls, Abrufen einer URL usw.) und verwenden Sie Plugins/Tools mit granularerer Funktionalität. Wenn eine LLM-basierte App beispielsweise einige Ausgaben in eine Datei schreiben muss. Wenn dies mit einem Plugin zum Ausführen einer Shell-Funktion implementiert würde, wäre der Spielraum für unerwünschte Aktionen sehr groß (jeder andere Shell-Befehl könnte ausgeführt werden). Eine sicherere Alternative wäre, ein Dateischreib-Plugin zu erstellen, das nur diese spezifische Funktionalität unterstützen könnte.
4. Beschränken Sie die Berechtigungen, die LLM-Plugins/Tools anderen Systemen gewährt werden, auf das minimal Notwendige, um den Umfang unerwünschter Aktionen zu begrenzen. Ein LLM-Agent, der eine Produkt-Datenbank verwendet, um einem Kunden Kaufempfehlungen zu geben, benötigt beispielsweise möglicherweise nur Lesezugriff auf eine 'Produkte'-Tabelle; er sollte keinen Zugriff auf andere Tabellen haben, noch die Fähigkeit, Datensätze einzufügen, zu aktualisieren oder zu löschen. Dies sollte durch die Anwendung geeigneter Datenbankberechtigungen für die Identität durchgesetzt werden, die das LLM-Plugin verwendet, um sich mit der Datenbank zu verbinden.
5. Verfolgen Sie die Benutzerautorisierung und den Sicherheitsumfang, um sicherzustellen, dass im Namen eines Benutzers durchgeführte Aktionen auf nachgelagerten Systemen im Kontext dieses spezifischen Benutzers und mit den minimal notwendigen Privilegien ausgeführt werden. Ein LLM-Plugin, das das Code-Repo eines Benutzers liest, sollte beispielsweise erfordern, dass sich der Benutzer über OAuth authentifiziert und mit dem minimal erforderlichen Umfang.
6. Nutzen Sie die Steuerung durch den Menschen, um eine menschliche Genehmigung für alle Aktionen zu erfordern, bevor sie durchgeführt werden. Dies kann in einem nachgelagerten System (außerhalb des Geltungsbereichs der LLM-Anwendung) oder innerhalb des LLM-Plugins/Tools selbst implementiert werden. Ein LLM-basiertes App, das soziale Medieninhalte im Namen eines Benutzers erstellt und postet, sollte beispielsweise eine Benutzergenehmigungsroutine innerhalb des Plugins/Tools/API enthalten, das die 'Post'-Operation implementiert.
7. Implementieren Sie Autorisierung in nachgelagerten Systemen, anstatt sich auf ein LLM zu verlassen, um zu entscheiden, ob eine Aktion erlaubt ist oder nicht. Bei der Implementierung von Tools/Plugins den Grundsatz der vollständigen Vermittlung durchsetzen, so dass alle Anfragen, die über die Plugins/Tools an nachgelagerte Systeme gestellt werden, gegen Sicherheitsrichtlinien validiert werden.

Die folgenden Optionen verhindern keine übermäßige Handlungsfreiheit, können jedoch das Ausmaß des Schadens begrenzen:

1. Protokollieren und überwachen Sie die Aktivität von LLM-Plugins/Tools und nachgelagerten Systemen, um zu identifizieren, wo unerwünschte Aktionen stattfinden, und entsprechend reagieren.
2. Implementieren Sie Ratenbegrenzung, um die Anzahl unerwünschter Aktionen, die innerhalb eines bestimmten Zeitraums stattfinden können, zu reduzieren und die Möglichkeit zu erhöhen, unerwünschte Aktionen durch Überwachung zu entdecken, bevor erheblicher Schaden entstehen kann.

### Beispielangriffsszenarien

Eine LLM-basierte persönliche Assistenten-App erhält Zugriff auf das Postfach einer Person über ein Plugin, um den Inhalt eingehender E-Mails zusammenzufassen. Um diese Funktionalität zu erreichen, benötigt das E-Mail-Plugin die Fähigkeit, Nachrichten zu lesen. Das Plugin, das der Systementwickler gewählt hat, enthält jedoch auch Funktionen zum Senden von Nachrichten. Das LLM ist anfällig für einen indirekten Aufforderungsinjektionsangriff, bei dem eine bösartig gestaltete eingehende E-Mail das LLM dazu verleitet, das E-Mail-Plugin zu befehlen, die Funktion 'Nachricht senden' aufzurufen, um Spam aus dem Postfach des Benutzers zu senden. Dies könnte vermieden werden durch:
(a) Eliminierung übermäßiger Funktionalität durch Verwendung eines Plugins, das nur E-Mail-Lesefähigkeiten anbot,
(b) Eliminierung übermäßiger Berechtigungen durch Authentifizierung beim E-Mail-Dienst des Benutzers über eine OAuth-Sitzung mit einem schreibgeschützten Umfang und/oder
(c) Eliminierung übermäßiger Autonomie, indem der Benutzer jede vom LLM-Plugin entworfene Mail manuell überprüfen und auf 'Senden' klicken muss.
Alternativ könnte der verursachte Schaden durch Implementierung einer Ratenbegrenzung an der Mail-Sende-Schnittstelle reduziert werden.

### Referenzlinks

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
2. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
3. [LangChain: Human-approval for tools](https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval): **Langchain Documentation**
4. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
