## LLM04: Denial of Service des Modells

### Beschreibung

Angreifende interagieren mit einem LLM auf eine Weise, die eine außergewöhnlich große Menge an Ressourcen verbraucht, was zu einer Verschlechterung der Servicequalität für sie und andere Personen führt und potenziell hohe Ressourcenkosten verursacht. Ebenso stellt die Möglichkeit, dass Angreifende in das Kontextfenster eines LLM eindringen oder es manipulieren, ein erhebliches Sicherheitsproblem dar. Dieses Problem wird immer kritischer aufgrund der zunehmenden Verwendung von LLMs in verschiedenen Anwendungen, ihrer intensiven Ressourcennutzung, der Unvorhersehbarkeit von Benutzereingaben und eines allgemeinen Mangels an Bewusstsein für diese Verwundbarkeit unter Entwicklerinnen und Entwicklern. In LLMs stellt das Kontextfenster die maximale Textlänge dar, die das Modell verwalten kann, einschließlich Eingabe und Ausgabe. Es ist ein entscheidendes Merkmal von LLMs, da es die Komplexität der Sprachmuster bestimmt, die das Modell verstehen kann, und die Länge des Textes, den es zu einem gegebenen Zeitpunkt verarbeiten kann. Die Größe des Kontextfensters wird durch die Architektur des Modells bestimmt und kann von Modell zu Modell variieren.

### Gängige Beispiele für Schwachstellen

1. Abfragen, die zu einer wiederkehrenden Ressourcennutzung führen, indem Tasks in großer Zahl in einer Warteschlange erzeugt werden, z. B. mit LangChain oder AutoGPT.
2. Senden von ungewöhnlich ressourcenintensiven Anfragen, die ungewöhnliche Zeichenkombinationen oder Schreibweisen verwenden.
3. Kontinuierlicher Eingabe-Overflow: Angreifende senden einen Eingabestrom an das LLM, der dessen Kontextfenster überschreitet, wodurch das Modell übermäßig viele Rechenressourcen verbraucht.
4. Wiederholte lange Eingaben: Angreifende senden wiederholt lange Eingaben an das LLM, die jeweils über das Kontextfenster überschreiten.
5. Rekursive Kontexterweiterung: Angreifende konstruieren Eingaben, die rekursive Kontexterweiterungen auslösen und das LLM zwingen, das Kontextfenster wiederholt zu erweitern und zu verarbeiten.
6. Überflutung mit Eingaben variabler Länge: Angreifende überfluten das LLM mit einer großen Anzahl von Eingaben variabler Länge, wobei jede Eingabe sorgfältig so konstruiert ist, dass sie gerade die Grenze des Kontextfensters erreicht. Diese Technik zielt darauf ab, mögliche Ineffizienzen bei der Verarbeitung von Eingaben variabler Länge auszunutzen, das LLM zu überlasten und möglicherweise seine Reaktionsfähigkeit zu beeinträchtigen.

### Präventions- und Mitigationsstrategien

1. Validierung und Bereinigung von Eingaben, um sicherzustellen, dass Benutzereingaben die festgelegten Grenzen einhalten und schädliche Inhalte herausgefiltert werden.
2. Begrenzen Sie die Ressourcennutzung pro Anfrage oder Vorgang, um die Ausführung von Anfragen mit komplexen Teilen zu verlangsamen.
3. Setzen Sie API-Rate Limits durch, um die Anzahl der Anfragen zu begrenzen, die einzelne Personen oder eine IP-Adresse in einem bestimmten Zeitraum stellen kann.
4. Begrenzen Sie die Anzahl der anstehenden Aktionen und die Gesamtanzahl der Aktionen in einem System, das auf LLM-Antworten reagiert.
5. Kontinuierliche Überwachung der LLM-Ressourcenauslastung, um abnormale Spitzen oder Muster zu erkennen, die auf einen DoS-Angriff hindeuten könnten.
6. Setzen Sie strikte Eingabebegrenzungen basierend auf dem Kontextfenster des LLM, um eine Überlastung und Erschöpfung der Ressourcen zu vermeiden.
7. Entwickler für potenzielle DoS-Schwachstellen in LLMs zu sensibilisieren und Richtlinien für eine sichere LLM-Implementierung bereitzustellen.

### Beispiele für Angriffsszenarien

1. Angreifende senden wiederholt mehrere komplexe und teure Anfragen an ein gehostetes Modell, was zu einer schlechteren Servicequalität für andere Personen und zu höheren Ressourcenkosten für die Betreibenden führt.
2. Während ein LLM-gesteuertes Tool Informationen sammelt, um eine harmlose Anfrage zu beantworten, wird ein Stück Text auf einer Webseite gefunden. Dies führt dazu, dass das Tool viele weitere Anfragen an die Webseite stellt, was zu einem hohen Ressourcenverbrauch führt.
3. Angreifende bombardieren das LLM kontinuierlich mit Eingaben, die das Kontextfenster des LLM überschreiten. Die Angreifenden können automatisierte Skripte oder Tools verwenden, um eine große Menge an Eingaben zu senden, die die Verarbeitungskapazität des LLM übersteigen. Infolgedessen verbraucht das LLM übermäßig viele Rechenressourcen, was zu einer erheblichen Verlangsamung oder zum völligen Ausfall des Systems führt.
4. Angreifende senden eine Reihe von sequenziellen Eingaben an das LLM, wobei jede Eingabe so gestaltet ist, dass sie knapp unterhalb der Grenze des Kontextfensters liegt. Durch das wiederholte Senden dieser Eingaben versuchen die Angreifenden, die verfügbare Kapazität des Kontextfensters auszuschöpfen. Da das LLM Mühe hat, jede Eingabe innerhalb seines Kontextfensters zu verarbeiten, werden die Systemressourcen belastet, was potenziell zu einer verminderten Leistung oder einem vollständigen Ausfall des Dienstes führt.
5. Angreifende nutzen die rekursiven Mechanismen des LLM, um wiederholt eine Kontexterweiterung auszulösen. Indem Eingaben konstruiert werden, die das rekursive Verhalten des LLM ausnutzen, zwingen die Angreifenden das Modell dazu, das Kontextfenster wiederholt zu erweitern und zu verarbeiten, wodurch erhebliche Rechenressourcen verbraucht werden. Dieser Angriff belastet das System und kann zu einem DoS-Zustand führen, der das LLM handlungsunfähig macht oder zum Absturz bringt.
6. Angreifende überfluten das LLM mit einer großen Anzahl von Eingaben variabler Länge, die sorgfältig so gestaltet sind, dass sie sich der Grenze des Kontextfensters nähern oder diese erreichen. Durch die Überflutung des LLM mit Eingaben variabler Länge versuchen die Angreifenden, mögliche Ineffizienzen bei der Verarbeitung von Eingaben variabler Länge auszunutzen. Diese Flut von Eingaben belastet die Ressourcen des LLM übermäßig, was zu einer Verschlechterung der Leistung führen und die Fähigkeit des Systems, auf legitime Anfragen zu reagieren, beeinträchtigen kann.
7. Während DoS-Angriffe in der Regel darauf abzielen, Systemressourcen zu überlasten, können sie auch andere Aspekte des Systemverhaltens ausnutzen, wie z. B. API-Beschränkungen. Bei einem kürzlich aufgetretenen Sicherheitsvorfall bei Sourcegraph beispielsweise nutzten böswillige Akteure ein durchgesickertes Admin-Zugriffstoken, um API-Rate-Limiting zu ändern, was potenziell zu Dienstunterbrechungen führte, indem es anormale Anfragevolumina zuließ.

### Referenzen

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): **hwchase17 auf Twitter**
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): **Arxiv White Paper**
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service): **OWASP**
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context): **Luke Bechtel**
5. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack ](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**