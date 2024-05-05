## LLM07: Unsicheres Plugin-Design

### Beschreibung

LLM-Plugins sind Erweiterungen, die bei Bedarf automatisch vom Modell während der Benutzerinteraktionen aufgerufen werden. Die Modellintegrationsplattform steuert sie, und die Anwendung hat möglicherweise keine Kontrolle über die Ausführung, insbesondere wenn das Modell von einer anderen Partei gehostet wird. Darüber hinaus implementieren Plugins wahrscheinlich Freitexteingaben vom Modell ohne Validierung oder Typüberprüfung, um mit Begrenzungen der Kontextgröße umzugehen. Dies ermöglicht einem potenziellen Angreifer, eine bösartige Anfrage an das Plugin zu konstruieren, die zu einer breiten Palette unerwünschter Verhaltensweisen führen kann, bis hin zur Ausführung von Remote-Code.

Der Schaden durch bösartige Eingaben hängt oft von unzureichenden Zugriffskontrollen und dem Versäumnis ab, die Autorisierung über Plugins hinweg zu verfolgen. Unzureichende Zugriffskontrolle ermöglicht es einem Plugin, anderen Plugins blind zu vertrauen und anzunehmen, dass die Eingaben vom Endbenutzer bereitgestellt wurden. Solch eine unzureichende Zugriffskontrolle kann ermöglichen, dass bösartige Eingaben schädliche Konsequenzen haben, von der Datenausfiltrierung, Ausführung von Remote-Code und Eskalation von Privilegien.

Dieser Punkt konzentriert sich auf die Erstellung von LLM-Plugins anstatt auf Drittanbieter-Plugins, die von LLM-Supply-Chain-Vulnerabilities abgedeckt werden.

### Häufige Beispiele für Verwundbarkeiten

1. Ein Plugin akzeptiert alle Parameter in einem einzigen Textfeld anstatt in getrennten Eingabeparametern.
2. Ein Plugin akzeptiert Konfigurationsstrings anstatt von Parametern, die gesamte Konfigurationseinstellungen überschreiben können.
3. Ein Plugin akzeptiert rohe SQL- oder Programmieranweisungen anstatt von Parametern.
4. Die Authentifizierung erfolgt ohne explizite Autorisierung für ein bestimmtes Plugin.
5. Ein Plugin behandelt alle LLM-Inhalte, als wären sie vollständig vom Benutzer erstellt, und führt jede angeforderte Aktion ohne zusätzliche Autorisierung aus.

### Präventions- und Minderungsstrategien

1. Plugins sollten streng parametrisierte Eingaben durchsetzen, wo immer möglich, und Typ- und Bereichsprüfungen für Eingaben einschließen. Wenn dies nicht möglich ist, sollte eine zweite Schicht von typisierten Aufrufen eingeführt werden, die Anfragen analysiert und Validierung und Sanitierung anwendet. Wenn Freiformeingaben aufgrund der Anwendungssemantik akzeptiert werden müssen, sollten sie sorgfältig inspiziert werden, um sicherzustellen, dass keine potenziell schädlichen Methoden aufgerufen werden.
2. Plugin-Entwickler sollten OWASPs Empfehlungen im ASVS (Application Security Verification Standard) anwenden, um eine angemessene Eingabevalidierung und -sanitierung zu gewährleisten.
3. Plugins sollten gründlich inspiziert und getestet werden, um eine angemessene Validierung sicherzustellen. Verwenden Sie Static Application Security Testing (SAST)-Scans und dynamische und interaktive Anwendungstests (DAST, IAST) in Entwicklungs-Pipelines.
4. Plugins sollten so konzipiert sein, dass sie die Auswirkungen einer Ausnutzung unsicherer Eingabeparameter minimieren, den OWASP ASVS Access Control Guidelines folgend. Dies umfasst Zugriffskontrolle mit minimalen Rechten, indem so wenig Funktionalität wie möglich freigelegt wird, während sie immer noch ihre gewünschte Funktion erfüllt.
5. Plugins sollten geeignete eigene Authentifizierungsidentitäten, wie OAuth2, verwenden, um eine effektive Autorisierung und Zugriffskontrolle anzuwenden. Zusätzlich sollten API-Schlüssel verwendet werden, um den Kontext für benutzerdefinierte Autorisierungsentscheidungen zu bieten, die den Plugin-Pfad anstelle des standardmäßigen interaktiven Benutzers widerspiegeln.
6. Plugins sollen manuelle Benutzerautorisierung und Bestätigung von jeder Aktion, die von sensiblen Plugins durchgeführt wird, erfordern.
7. Plugins sind oft REST-APIs, daher sollten Entwickler die Empfehlungen in OWASP Top 10 API Security Risks – 2023 anwenden, um generische Verwundbarkeiten zu minimieren.

### Beispiel-Angriffsszenarien

1. Ein Plugin akzeptiert eine Basis-URL und weist das LLM an, die URL mit einer Abfrage zu kombinieren, um Wettervorhersagen zu erhalten, die in die Bearbeitung der Benutzeranfrage einbezogen werden. Ein bösartiger Benutzer kann eine Anfrage so gestalten, dass die URL auf eine Domain zeigt, die sie kontrollieren, was es ihnen ermöglicht, ihren eigenen Inhalt über ihre Domain in das LLM-System einzuspeisen.
2. Ein Plugin akzeptiert eine Freiformeingabe in einem einzelnen Feld, das es nicht validiert. Ein Angreifer liefert sorgfältig gestaltete Payloads, um aus Fehlermeldungen Aufklärung zu betreiben. Anschließend werden bekannte Schwachstellen von Drittanbietern ausgenutzt, um Code auszuführen und Datenexfiltrierung oder Privilegienerweiterung durchzuführen.
3. Ein Plugin, das zum Abrufen von Einbettungen aus einem Vektorspeicher verwendet wird, akzeptiert Konfigurationsparameter als Verbindungsstring ohne jegliche Validierung. Dies ermöglicht es einem Angreifer, zu experimentieren und auf andere Vektorspeicher zuzugreifen, indem Namen oder Hostparameter geändert werden, und Einbettungen zu exfiltrieren, zu denen sie keinen Zugang haben sollten.
4. Ein Plugin akzeptiert SQL WHERE-Klauseln als erweiterte Filter, die dann an das Filter-SQL angehängt werden. Dies ermöglicht es einem Angreifer, einen SQL-Angriff zu inszenieren.
5. Ein Angreifer nutzt die indirekte Prompt-Injektion, um ein unsicheres Codeverwaltungs-Plugin ohne Eingabevalidierung und schwache Zugriffskontrolle auszunutzen, um das Repository-Eigentum zu übertragen und den Benutzer von ihren Repositories auszuschließen.

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
