## LLM07: Unsicheres Plug-in-Design

### Beschreibung

LLM-Plug-ins sind Erweiterungen, die, wenn sie aktiviert sind, bei Benutzerinteraktionen automatisch vom Modell aufgerufen werden. Sie werden von der Modell-Integrationsplattform gesteuert, und die Anwendung hat möglicherweise keine Kontrolle über ihre Ausführung, insbesondere wenn das Modell von einer anderen Instanz gehostet wird. Weiterhin ist es wahrscheinlich, dass Plug-ins Freitexteingaben aus dem Modell ohne Validierung oder Typüberprüfung implementieren, um Beschränkungen der Kontextgröße zu umgehen. Dadurch können Angreifende eine böswillige Anfrage an das Plug-in stellen, was zu einer Vielzahl von unerwünschtem Verhalten bis hin zur Remote-Code-Ausführung führen kann.

Der Schaden, der durch böswillige Eingaben verursacht wird, hängt oft von unzureichenden Zugriffskontrollen und dem Versäumnis ab, die Autorisierung über Plug-ins hinweg zu verfolgen. Unzureichende Zugriffskontrollen ermöglichen es einem Plug-in, anderen Plug-ins blind zu vertrauen und davon auszugehen, dass die Eingaben von einem Menschen stammen. Solche unzureichenden Zugriffskontrollen können dazu führen, dass böswillige Eingaben schädliche Folgen haben, von der Datenexfiltration über die Ausführung von Remote-Code bis hin zur Privilegieneskalation.

Dieser Abschnitt konzentriert sich auf die Erstellung von LLM-Plug-ins und nicht auf Plug-ins von Drittanbietern, die durch LLM-Supply-Chain-Schwachstellen abgedeckt werden.

### Gängige Beispiele für Schwachstellen

1. Ein Plug-in akzeptiert alle Parameter in einem einzigen Textfeld anstelle von eigenständig eingegebenen Parametern.
2. Ein Plug-in akzeptiert Konfigurationsstrings anstelle von Parametern, die alle Konfigurationseinstellungen überschreiben können.
3. Ein Plug-in akzeptiert direkt SQL- oder Programmieranweisungen anstelle von Parametern.
4. Die Authentifizierung erfolgt ohne explizite Autorisierung für ein bestimmtes Plug-in.
5. Ein Plug-in behandelt alle LLM-Inhalte so, als ob sie vollständig vom Menschen erstellt wurden, und führt jede angeforderte Aktion ohne zusätzliche Autorisierung aus.

### Präventions- und Mitigationsstrategien

1. Plug-ins sollten, wo immer möglich, streng parametrisierte Eingaben erzwingen und Typ- und Bereichsprüfungen für Eingaben vorsehen. Wenn dies nicht möglich ist, sollte eine zweite Schicht von typisierten Aufrufen eingeführt werden, die die Anfragen parst und eine Validierung und Bereinigung durchführt. Wenn Freitexteingaben aufgrund der Anwendungssemantik akzeptiert werden müssen, sollten diese sorgfältig geprüft werden, um sicherzustellen, dass keine potenziell schädlichen Methoden aufgerufen werden.
2. Plug-in-Entwickelnde sollten die Empfehlungen aus dem OWASP ASVS (Application Security Verification Standard) anwenden, um eine angemessene Validierung und Bereinigung von Eingaben sicherzustellen.
3. Plug-ins sollten gründlich geprüft und getestet werden, um eine angemessene Validierung zu gewährleisten. Verwenden Sie statische Anwendungssicherheitstests (SAST) sowie dynamische und interaktive Anwendungstests (DAST, IAST) in den Entwicklungspipelines.
4. Plug-ins sollten so entworfen werden, dass die Auswirkungen der Ausnutzung unsicherer Eingabeparameter gemäß den OWASP ASVS Access Control Guidelines minimiert werden. Dies beinhaltet eine Zugriffskontrolle mit den geringsten Rechten, die so wenig Funktionalität wie möglich preisgibt, aber dennoch die gewünschte Funktion erfüllt.
5. Plug-ins sollten geeignete Authentifizierungsidentitäten wie OAuth2 verwenden, um eine effektive Autorisierung und Zugriffskontrolle anzuwenden. Überdies sollten API-Schlüssel verwendet werden, um den Kontext für benutzerdefinierte Autorisierungsentscheidungen bereitzustellen, die den Pfad des Plug-ins und nicht den interaktiven Standardbenutzer widerspiegeln.
6. Verlangen Sie eine manuelle Benutzerautorisierung und Bestätigung aller von vertraulichen Plug-ins durchgeführten Aktionen.
7. Plug-ins sind in der Regel REST-APIs. Daher sollten Entwickelnde die Empfehlungen in OWASP Top 10 API Security Risks - 2023 befolgen, um allgemeine Schwachstellen zu minimieren.

### Beispiele für Angriffsszenarien

1. Ein Plug-in akzeptiert eine Basis-URL und weist das LLM an, die URL mit einer Anfrage zu kombinieren, um Wettervorhersagen zu erhalten, die in die Bearbeitung der Benutzeranfrage einfließen. Böswillige Personen können eine Anfrage so gestalten, dass die URL auf eine von ihnen kontrollierte Domäne verweist, wodurch sie ihre eigenen Inhalte über diese in das LLM-System einspeisen können.
2. Ein Plug-in akzeptiert eine freie Eingabe in ein einzelnes Feld, die nicht validiert wird. Angreifende liefern sorgfältig gestaltete Payloads, um Fehlermeldungen auszuspähen. Anschließend nutzen sie bekannte Sicherheitslücken von Drittanbietern aus, um Code auszuführen, Daten zu exfiltrieren oder Rechte zu erweitern.
3. Ein Plug-in, das zum Abrufen von Embeddings aus einem Vektorspeicher verwendet wird, akzeptiert Konfigurationsparameter als Verbindungsstring ohne jegliche Validierung. Dadurch können Angreifende experimentieren und auf andere Vektorspeicher zugreifen, indem sie Namen oder Host-Parameter ändern und Embeddings exfiltrieren, auf die sie keinen Zugriff haben sollten.
4. Ein Plug-in akzeptiert SQL WHERE-Klauseln als erweiterte Filter, die dann an die SQL-Bedingungen angehängt werden. Dadurch können Angreifende einen SQL-Angriff durchführen.
5. Angreifende nutzen eine indirekte Prompt Injection aus, um ein unsicheres Codeverwaltungs-Plug-in ohne Eingabevalidierung und mit schwacher Zugriffskontrolle auszunutzen, um den Besitz von Repositorys zu übertragen und Personen von ihren Repositorys auszuschließen.

### Referenzen

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): **ChatGPT Developer’s Guide**
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI Documentation**
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI Documentation**
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace The Red**
7. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
8. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
9. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
10. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**