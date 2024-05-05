## LLM04: Modell Denial of Service

### Beschreibung

Ein Angreifer interagiert mit einem LLM auf eine Weise, die eine außergewöhnlich hohe Menge an Ressourcen verbraucht, was zu einer Verringerung der Dienstqualität für ihn und andere Benutzer führt, sowie potenziell hohe Ressourcenkosten verursacht. Darüber hinaus ist die Möglichkeit, dass ein Angreifer in das Kontextfenster eines LLM eingreift oder es manipuliert, ein aufkommendes großes Sicherheitsbedenken. Dieses Problem wird aufgrund der zunehmenden Verwendung von LLMs in verschiedenen Anwendungen, ihrer intensiven Ressourcennutzung, der Unvorhersehbarkeit der Benutzereingaben und eines allgemeinen Mangels an Bewusstsein unter Entwicklern bezüglich dieser Verwundbarkeit immer kritischer. In LLMs repräsentiert das Kontextfenster die maximale Länge des Textes, den das Modell verwalten kann, einschließlich Eingabe und Ausgabe. Es ist eine entscheidende Eigenschaft von LLMs, da es die Komplexität der Sprachmuster, die das Modell verstehen kann, und die Größe des Textes, den es zu einem gegebenen Zeitpunkt verarbeiten kann, diktiert. Die Größe des Kontextfensters wird durch die Architektur des Modells definiert und kann zwischen Modellen variieren.

### Häufige Beispiele für Verwundbarkeiten

1. Anfragen stellen, die zu wiederkehrender Ressourcennutzung durch die Generierung von Aufgaben in hoher Anzahl in einer Warteschlange führen, z.B. mit LangChain oder AutoGPT.
2. Ungewöhnlich ressourcenintensive Anfragen senden, die ungewöhnliche Rechtschreibung oder Sequenzen verwenden.
3. Kontinuierlicher Eingabeüberlauf: Ein Angreifer sendet einen Strom von Eingaben an das LLM, der sein Kontextfenster übersteigt, wodurch das Modell übermäßige Rechenressourcen verbraucht.
4. Wiederholte lange Eingaben: Der Angreifer sendet wiederholt lange Eingaben an das LLM, die jeweils das Kontextfenster überschreiten.
5. Rekursive Kontexterweiterung: Der Angreifer konstruiert Eingaben, die rekursive Kontexterweiterungen auslösen und zwingen das LLM dazu, das Kontextfenster wiederholt zu erweitern und zu verarbeiten.
6. Flut mit Eingaben variabler Länge: Der Angreifer überflutet das LLM mit einer großen Menge an Eingaben variabler Länge, wobei jede Eingabe sorgfältig so gestaltet ist, dass sie gerade das Limit des Kontextfensters erreicht. Diese Technik zielt darauf ab, etwaige Ineffizienzen bei der Verarbeitung von Eingaben variabler Länge auszunutzen, das LLM zu belasten und potenziell dessen Reaktionsfähigkeit zu beeinträchtigen.

### Präventions- und Mitigation-Strategien

1. Implementierung von Eingabevalidierung und -sanierung, um sicherzustellen, dass Benutzereingaben definierten Grenzen entsprechen und jeglichen bösartigen Inhalt herausfiltern.
2. Begrenzung der Ressourcennutzung pro Anfrage oder Schritt, sodass Anfragen, die komplexe Teile beinhalten, langsamer ausgeführt werden.
3. Durchsetzung von API-Rate-Limits, um die Anzahl der Anfragen, die ein einzelner Benutzer oder eine IP-Adresse innerhalb eines bestimmten Zeitrahmens stellen kann, zu beschränken.
4. Limitierung der Anzahl von Aktionen in der Warteschlange und der Gesamtzahl von Aktionen in einem System, das auf LLM-Antworten reagiert.
5. Kontinuierliche Überwachung der Ressourcennutzung des LLM, um abnormale Spitzen oder Muster zu identifizieren, die auf einen DoS-Angriff hinweisen könnten.
6. Strikte Eingabelimits basierend auf dem Kontextfenster des LLM setzen, um Überlastung und Ressourcenerschöpfung zu verhindern.
7. Bewusstsein unter Entwicklern über potenzielle DoS-Verwundbarkeiten in LLMs fördern und Leitlinien für sichere LLM-Implementierung bereitstellen.

### Beispielszenarien für Angriffe

1. Ein Angreifer sendet wiederholt mehrere schwierige und kostspielige Anfragen an ein gehostetes Modell, was zu schlechterem Service für andere Benutzer und erhöhten Ressourcenrechnungen für den Host führt.
2. Ein Stück Text auf einer Webseite wird gefunden, während ein LLM-gesteuertes Tool Informationen sammelt, um auf eine harmlose Anfrage zu antworten. Dies führt dazu, dass das Tool viele weitere Webseitenanfragen stellt, was zu einem großen Ressourcenverbrauch führt.
3. Ein Angreifer bombardiert das LLM kontinuierlich mit Eingaben, die sein Kontextfenster überschreiten. Der Angreifer kann automatisierte Skripte oder Tools verwenden, um eine hohe Menge an Eingaben zu senden, die die Verarbeitungskapazitäten des LLM überwältigen. Als Ergebnis verbraucht das LLM übermäßige Rechenressourcen, was zu einer signifikanten Verlangsamung oder vollständigen Unreaktivität des Systems führt.
4. Ein Angreifer sendet eine Reihe von sequenziellen Eingaben an das LLM, wobei jede Eingabe so gestaltet ist, dass sie knapp unter dem Limit des Kontextfensters liegt. Indem diese Eingaben wiederholt eingereicht werden, zielt der Angreifer darauf ab, die verfügbare Kapazität des Kontextfensters zu erschöpfen. Da das LLM Mühe hat, jede Eingabe innerhalb seines Kontextfensters zu verarbeiten, werden die Systemressourcen belastet, was potenziell zu einer verminderten Leistung oder einem vollständigen Dienstausfall führt.
5. Ein Angreifer nutzt die rekursiven Mechanismen des LLM, um wiederholt eine Kontexterweiterung auszulösen. Indem Eingaben konstruiert werden, die das rekursive Verhalten des LLM ausnutzen, zwingt der Angreifer das Modell dazu, das Kontextfenster wiederholt zu erweitern und zu verarbeiten, wodurch erhebliche Rechenressourcen verbraucht werden. Dieser Angriff belastet das System und kann zu einem DoS-Zustand führen, der das LLM unreaktiv macht oder es zum Absturz bringt.
6. Ein Angreifer überflutet das LLM mit einer großen Menge an Eingaben variabler Länge, die sorgfältig so gestaltet sind, dass sie das Limit des Kontextfensters annähern oder erreichen. Indem das LLM mit Eingaben verschiedener Längen überwältigt wird, zielt der Angreifer darauf ab, etwaige Ineffizienzen bei der Verarbeitung von Eingaben variabler Länge auszunutzen. Diese Flut an Eingaben legt eine übermäßige Last auf die Ressourcen des LLM, was potenziell zu einer Leistungsdegradation führt und die Fähigkeit des Systems behindert, auf legitime Anfragen zu reagieren.
7. Während DoS-Angriffe üblicherweise darauf abzielen, Systemressourcen zu überwältigen, können sie auch andere Aspekte des Systemverhaltens ausnutzen, wie z.B. API-Limitierungen. Beispielsweise hat in einem kürzlichen Sicherheitsvorfall bei Sourcegraph der bösartige Akteur ein durchgesickertes Admin-Zugangstoken verwendet, um API-Ratenlimits zu ändern, wodurch potenziell Dienstunterbrechungen durch die Ermöglichung abnormaler Anfragevolumen verursacht wurden.

### Referenzlinks

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): **hwchase17 auf Twitter**
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): **Arxiv White Paper**
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service): **OWASP**
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context): **Luke Bechtel**
5. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack ](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**
