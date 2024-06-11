## LLM02: Unsichere Ausgabeverarbeitung

### Beschreibung

Unsichere Ausgabeverarbeitung bezieht sich speziell auf die unzureichende Validierung, Bereinigung und Handhabung von Ausgaben, die von Large Language Models erzeugt werden, bevor sie an andere Komponenten und Systeme weitergeleitet werden. Da der von LLMs erzeugte Inhalt durch Prompt-Eingaben gesteuert werden kann, ähnelt dieses Verhalten dem indirekten Zugriff des Benutzers auf zusätzliche Funktionen.

Unsichere Ausgabeverarbeitung unterscheidet sich von Übermäßiger Abhängigkeit insofern, als sie sich mit den Ausgaben befasst, die von LLMs generiert werden, bevor sie weitergeleitet werden. Im Gegensatz dazu konzentriert sich Übermäßige Abhängigkeit auf allgemeinere Bedenken hinsichtlich der Angewiesenheit auf die Genauigkeit und Angemessenheit des LLM-Outputs.

Die erfolgreiche Ausnutzung einer Schwachstelle in der unsicheren Ausgabeverarbeitung kann zu XSS (Cross-Site Scripting) und CSRF (Cross-Site Request Forgery) in Webbrowsern sowie zu SSRF (Server-Side Request Forgery), Rechteerweiterung (Privilege Escalation) oder Remote-Code-Ausführung in Backend-Systemen führen.

Die folgenden Bedingungen können die Auswirkungen dieser Schwachstelle verstärken:

* Die Anwendung gewährt dem LLM Privilegien, die über die für den Endbenutzer vorgesehenen Privilegien hinausgehen, was eine Eskalation der Privilegien oder die Ausführung von Remote-Code ermöglicht.
* Die Anwendung ist anfällig für indirekte Prompt Injection-Angriffe, die es Angreifenden ermöglichen, privilegierten Zugriff auf die Umgebung eines Zielbenutzers zu erlangen.
* Plug-ins von Drittanbietern validieren Eingaben nicht ausreichend.

### Gängige Beispiele für Schwachstellen

1. Die Ausgabe des LLM wird direkt in eine Systemshell oder eine ähnliche Funktion wie exec oder eval eingegeben, was zu einer Remote-Code-Ausführung führt.
2. JavaScript oder Markdown wird vom LLM generiert und an die aufrufende Person zurückgegeben. Der Code wird dann vom Browser interpretiert, was zu XSS führt.

### Präventions- und Mitigationsstrategien

1. Behandeln Sie das Sprachmodell mit einem Zero-Trust-Ansatz und wenden Sie eine geeignete Eingabevalidierung auf die Antworten an, die vom Modell an die Backend-Funktionen gesendet werden.
2. Befolgen Sie die OWASP ASVS (Application Security Verification Standard) Richtlinien, um eine effektive Eingabevalidierung und -bereinigung zu gewährleisten.
3. Encoden Sie die Modellausgabe zurück an den Benutzer, um unerwünschte Codeausführung durch JavaScript oder Markdown zu verhindern. Der OWASP ASVS bietet detaillierte Anweisungen zum Output Encoding.

### Beispiele für Angriffsszenarien

1. Eine Anwendung verwendet ein LLM-Plug-in, um Antworten für eine Chatbot-Funktion zu generieren. Das Plug-in bietet auch eine Reihe von administrativen Funktionen, die einem anderen privilegierten LLM zur Verfügung stehen. Das allgemeine LLM sendet seine Antwort direkt an das Plug-in, ohne die Ausgabe ordnungsgemäß zu validieren, was dazu führt, dass das Plug-in für Wartungsarbeiten heruntergefahren wird.
2. Eine Person verwendet ein von einem LLM betriebenes Tool, das Webseiten zusammenfasst, um eine kurze Übersicht über einen Artikel zu erstellen. Die Website enthält eine Eingabeaufforderung, die das LLM anweist, sensible Inhalte entweder von der Website oder aus der Konversation des Benutzers zu erfassen. Anschließend kann der LLM die sensiblen Daten verschlüsseln und ohne Validierung oder Filterung der Ausgabe an einen von Angreifenden kontrollierten Server senden.
3. Ein LLM ermöglicht es Personen, SQL-Abfragen für eine Backend-Datenbank über eine Chat-ähnliche Funktion zu erstellen. Eine Person stellt eine Abfrage zum Löschen aller Datenbanktabellen. Wenn die vom LLM erstellte Abfrage nicht überprüft wird, könnten alle Datenbanktabellen gelöscht werden.
4. Eine Webanwendung verwendet einen LLM, um Inhalte aus Benutzereingaben zu generieren, ohne die Ausgabe zu bereinigen. Angreifende könnten eine manipulierte Anfrage einreichen, die das LLM dazu veranlasst, eine unbereinigte JavaScript-Payload zurückzugeben, die zu XSS führt, wenn sie im Browser des Opfers ausgeführt wird. Unzureichende Validierung von Anfragen ermöglicht diesen Angriff.

### Referenzen

1. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**