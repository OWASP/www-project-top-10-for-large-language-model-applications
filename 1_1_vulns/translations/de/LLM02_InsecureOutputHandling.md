## LLM02: Unsichere Ausgabeverarbeitung


### Beschreibung

Unsichere Ausgabeverarbeitung bezieht sich speziell auf unzureichende Validierung, Sanitierung und Handhabung der von großen Sprachmodellen erzeugten Ausgaben, bevor sie an andere Komponenten und Systeme weitergegeben werden. Da der von LLMs (Large Language Models) generierte Inhalt durch Prompteingaben gesteuert werden kann, ähnelt dieses Verhalten dem indirekten Zugriff der Benutzer auf zusätzliche Funktionen.

Unsichere Ausgabeverarbeitung unterscheidet sich von Überabhängigkeit dadurch, dass es sich mit den von LLMs generierten Ausgaben befasst, bevor diese weitergeleitet werden. Überabhängigkeit konzentriert sich hingegen auf breitere Bedenken hinsichtlich der Überabhängigkeit von der Genauigkeit und Angemessenheit der LLM-Ausgaben.

Eine erfolgreiche Ausnutzung einer Schwachstelle in der unsicheren Ausgabeverarbeitung kann XSS (Cross-Site Scripting) und CSRF (Cross-Site Request Forgery) in Webbrowsern sowie SSRF (Server-Side Request Forgery), Rechteerweiterung (privilege escalation) oder Remote-Code-Ausführung in Backend-Systemen zur Folge haben.

Die folgenden Bedingungen können die Auswirkungen dieser Schwachstelle erhöhen:
* Die Anwendung gewährt dem LLM Privilegien, die über das für Endbenutzer Vorgesehene hinausgehen, was eine Eskalation von Privilegien oder Remote-Code-Ausführung ermöglicht.
* Die Anwendung ist anfällig für indirekte Prompt-Injektionsangriffe, die es einem Angreifer ermöglichen könnten, privilegierten Zugang zur Umgebung eines Zielbenutzers zu erlangen.
* Plugins von Drittanbietern validieren Eingaben nicht ausreichend.

### Häufige Beispiele für Schwachstellen

1. Die Ausgabe des LLM wird direkt in eine Systemshell oder eine ähnliche Funktion wie exec oder eval eingegeben, was zu einer Remote-Code-Ausführung führt.
2. JavaScript oder Markdown wird vom LLM generiert und an einen Benutzer zurückgegeben. Der Code wird dann vom Browser interpretiert, was zu XSS führt.

### Präventions- und Minderungsstrategien

1. Behandeln Sie das Modell wie jeden anderen Benutzer, indem Sie einen Zero-Trust-Ansatz anwenden, und wenden Sie eine ordnungsgemäße Eingabevalidierung auf Antworten an, die vom Modell zu Backend-Funktionen kommen.
2. Befolgen Sie die Richtlinien des OWASP ASVS (Application Security Verification Standard), um eine effektive Eingabevalidierung und Sanitierung zu gewährleisten.
3. Kodieren Sie Modellausgaben zurück an die Benutzer, um unerwünschte Codeausführung durch JavaScript oder Markdown zu verhindern. OWASP ASVS bietet detaillierte Anleitungen zur Ausgabekodierung.

### Beispielangriffsszenarien

1. Eine Anwendung nutzt ein LLM-Plugin, um Antworten für eine Chatbot-Funktion zu generieren. Das Plugin bietet auch eine Reihe von administrativen Funktionen, die einem anderen privilegierten LLM zugänglich sind. Das allgemeine LLM gibt seine Antwort direkt, ohne ordnungsgemäße Ausgabevalidierung, an das Plugin weiter, was dazu führt, dass das Plugin für Wartungsarbeiten heruntergefahren wird.
2. Ein Benutzer verwendet ein von einem LLM betriebenes Website-Zusammenfassungstool, um eine prägnante Zusammenfassung eines Artikels zu generieren. Die Website enthält eine Prompt-Injektion, die das LLM anweist, sensible Inhalte entweder von der Website oder aus der Konversation des Benutzers zu erfassen. Von dort aus kann das LLM die sensiblen Daten kodieren und ohne jegliche Ausgabevalidierung oder Filterung an einen vom Angreifer kontrollierten Server senden.
3. Ein LLM ermöglicht Benutzern, SQL-Abfragen für eine Backend-Datenbank über eine chatähnliche Funktion zu erstellen. Ein Benutzer fordert eine Abfrage an, um alle Datenbanktabellen zu löschen. Wenn die vom LLM erstellte Abfrage nicht geprüft wird, könnten alle Datenbanktabellen gelöscht werden.
4. Eine Webanwendung verwendet ein LLM, um Inhalte aus Benutzertextaufforderungen ohne Ausgabesanitierung zu generieren. Ein Angreifer könnte eine konstruierte Aufforderung einreichen, die das LLM dazu bringt, eine unbereinigte JavaScript-Payload zurückzugeben, was zu XSS führt, wenn sie im Browser eines Opfers ausgeführt wird. Unzureichende Validierung von Aufforderungen ermöglichte diesen Angriff.

### Referenzlinks

1. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**