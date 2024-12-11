## LLM05:2025 Fehlerhafte Ausgabeverarbeitung

### Beschreibung

Die falsche Verarbeitung von Ausgaben bezieht sich insbesondere auf eine unzureichende Validierung, Bereinigung und Verarbeitung der von großen Sprachmodellen erzeugten Ausgaben, bevor sie an andere Komponenten und Systeme weitergegeben werden. Da LLM-generierte Inhalte durch Eingabeaufforderungen gesteuert werden können, ähnelt dieses Verhalten dem indirekten Zugriff auf zusätzliche Funktionen durch die Benutzer.
“Falsche Ausgabeverarbeitung" unterscheidet sich von “Overreliance" dadurch, dass es sich mit LLM-generierten Ausgaben befasst, bevor sie nachgelagert werden, während sich Overreliance auf allgemeinere Bedenken bezüglich der übermäßigen Abhängigkeit von der Genauigkeit und Angemessenheit der LLM-Ausgaben konzentriert.
Die erfolgreiche Ausnutzung einer “falsche Ausgabenverarbeitung"-Schwachstelle kann zu XSS und CSRF in Webbrowsern sowie zu SSRF, Privilegienerweiterung oder Remotecodeausführung auf Backend-Systemen führen.
Die folgenden Bedingungen können die Auswirkungen dieser Schwachstelle verstärken:
- Die Anwendung räumt dem LLM mehr Rechte ein, als für die Endnutzer vorgesehen sind, wodurch eine Ausweitung der Rechte oder Remotecodeausführung möglich ist.
- Die Anwendung ist anfällig für indirekte Prompt-Injection-Angriffe, die es einem Angreifer ermöglichen könnten, privilegierten Zugriff auf die Umgebung eines Zielbenutzers zu erhalten.
- Erweiterungen von Drittanbietern validieren die Eingaben nicht ausreichend.
- Fehlen einer geeigneten Ausgabekodierung für verschiedene Kontexte (z. B. HTML, JavaScript, SQL)
- Unzureichende Überwachung und Protokollierung von LLM-Ausgaben
- Fehlende Ratenbegrenzung oder Anomalieerkennung für die LLM-Nutzung

### Gängige Beispiele für Schwachstellen

1. Die LLM-Ausgabe wird direkt in eine System-Shell oder eine ähnliche Funktion wie exec oder eval eingegeben, was zu einer Remotecodeausführung führt.
2. JavaScript oder Markdown wird vom LLM generiert und an den Benutzer zurückgegeben. Der Code wird dann vom Browser interpretiert, was zu XSS führt.
3. Vom LLM generierte SQL-Abfragen werden ohne korrekte Parametrisierung ausgeführt, was zu einer SQL-Injection führt.
4. Die LLM-Ausgabe wird verwendet, um Dateipfade ohne ordnungsgemäße Bereinigung zu konstruieren, was zu Path Traversal-Schwachstellen führen kann.
5. LLM-generierte Inhalte werden in E-Mail-Vorlagen ohne ordnungsgemäßes Escaping verwendet, was zu Phishing-Angriffen führen kann.

### Präventions- und Mitigationsstrategien

1. Behandle das Modell wie jeden anderen Nutzer, indem du einen Zero-Trust-Ansatz wählst und die Antworten, die das Modell an die Backend-Funktionen sendet, einer angemessenen Eingabevalidierung unterziehst.
2. Befolge die OWASP ASVS-Richtlinien (Application Security Verification Standard), um eine wirksame Validierung und Bereinigung von Eingaben sicherzustellen.
3. Encode die Ausgaben des Modells für die Nutzer, um die Ausführung von unerwünschtem Code durch JavaScript oder Markdown zu verhindern. OWASP ASVS bietet eine detaillierte Anleitung zur Verschlüsselung von Ausgaben.
4. Implementiere eine kontextabhängige Kodierung der Ausgabe, je nachdem, wo die LLM-Ausgabe verwendet wird (z. B. HTML-Kodierung für Webinhalte, SQL-Escaping für Datenbankabfragen).
5. Verwende parametrisierte Abfragen oder vorbereitete Anweisungen für alle Datenbankoperationen mit LLM-Ausgaben.
6. Verwende strenge Content Security Policies (CSP), um das Risiko von XSS-Angriffen durch LLM-generierte Inhalte zu verringern.
7. Implementiere robuste Protokollierungs- und Überwachungssysteme, um ungewöhnliche Muster in LLM-Ausgaben zu erkennen, die auf Missbrauchsversuche hindeuten könnten.

### Beispiele für Angriffsszenarien

#### Szenario #1
  Eine Anwendung nutzt eine LLM-Extension, um Antworten für eine Chatbot-Funktion zu generieren. Die Erweiterung bietet auch eine Reihe von Verwaltungsfunktionen, auf die ein anderer privilegiertes LLM Zugriff hat. Der Allzweck-LLM gibt seine Antwort ohne ordnungsgemäße Validierung der Ausgabe direkt an die Erweiterung weiter, was dazu führt, dass die Erweiterung zur Wartung abgeschaltet wird.
#### Szenario #2
  Ein Nutzer nutzt ein von einem LLM betriebenes Tool zur Zusammenfassung einer Website, um eine kurze Zusammenfassung eines Artikels zu erstellen. Die Website enthält eine Eingabeaufforderung, die den LLM anweist, sensible Inhalte entweder von der Website oder aus der Unterhaltung des Nutzers zu erfassen. Von dort aus kann der LLM die sensiblen Daten verschlüsseln und sie ohne jegliche Output-Validierung oder Filterung an einen vom Angreifer kontrollierten Server senden.
#### Szenario #3
  Ein LLM ermöglicht es Nutzern, über eine chatähnliche Funktion SQL-Abfragen für eine Backend-Datenbank zu erstellen. Ein Benutzer fordert eine Abfrage zum Löschen aller Datenbanktabellen an. Wenn die vom LLM erstellte Abfrage nicht überprüft wird, werden alle Datenbanktabellen gelöscht.
#### Szenario #4
  Eine Webanwendung verwendet einen LLM, um Inhalte aus Benutzertexteingaben zu generieren, ohne die Ausgabe zu bereinigen. Ein Angreifer könnte eine manipulierte Eingabeaufforderung übermitteln, die den LLM veranlasst, eine nicht bereinigte JavaScript-Nutzlast zurückzugeben, was zu XSS führt, wenn sie im Browser des Opfers dargestellt wird. Die unzureichende Validierung von Prompts ermöglichte diesen Angriff.
#### Szenario Nr. 5
  Ein LLM wird verwendet, um dynamische E-Mail-Vorlagen für eine Marketingkampagne zu erstellen. Ein Angreifer manipuliert die LLM, um bösartiges JavaScript in den E-Mail-Inhalt zu integrieren. Wenn die Anwendung die LLM-Ausgabe nicht ordnungsgemäß bereinigt, kann dies zu XSS-Angriffen auf Empfänger führen, die die E-Mail in anfälligen E-Mail-Clients betrachten.
#### Szenario #6
  Ein LLM wird in einem Softwareunternehmen eingesetzt, um Code aus natürlichsprachlichen Eingaben zu generieren und so die Entwicklungsarbeit zu rationalisieren. Dieser Ansatz ist zwar effizient, birgt aber die Gefahr, dass sensible Informationen preisgegeben, unsichere Datenverarbeitungsmethoden entwickelt oder Schwachstellen wie SQL-Injection eingeführt werden. Die KI kann auch nicht existierende Softwarepakete vorgaukeln, was dazu führen kann, dass Entwickler/innen mit Malware infizierte Ressourcen herunterladen. Eine gründliche Überprüfung des Codes und die Verifizierung der vorgeschlagenen Pakete sind entscheidend, um Sicherheitslücken, unbefugten Zugriff und die Gefährdung des Systems zu verhindern.

### Referenzlinks

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [Arbitrary Code Execution](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
3. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [New prompt injection attack on ChatGPT web version. Markdown images can steal your chat data.](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
5. [Don’t blindly trust LLM responses. Threats to chatbots](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
6. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
7. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [AI hallucinates software packages and devs download them – even if potentially poisoned with malware](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **Theregiste**

