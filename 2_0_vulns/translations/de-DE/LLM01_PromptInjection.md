## LLM01:2025 Prompt Injection

### Beschreibung

Eine Prompt-Injection-Schwachstelle tritt auf, wenn die Prompts der Benutzenden das Verhalten oder die Ausgabe des LLMs auf unerwünschte Weise verändern. Diese Eingaben können sich auf das Modell auswirken, selbst wenn sie für den Menschen nicht wahrnehmbar sind. Daher müssen Prompt Injections für Menschen nicht unbedingt sichtbar oder lesbar sein, solange der Inhalt vom Modell verarbeitet wird. 

Prompt-Injection-Schwachstellen bestehen darin, wie Modelle Prompts verarbeiten und wie Eingaben das Modell dazu zwingen können, Prompt Daten fehlerhaft an andere Teile des Modells weiterzugeben. Dies kann dazu führen, dass Richtlinien verletzt werden, schädlicher Inhalt generiert wird, unbefugter Zugriff ermöglicht wird oder kritische Entscheidungen beeinflusst werden. Obwohl Techniken wie Retrieval Augmented Generation (RAG) und Fine-Tuning darauf abzielen, die Relevanz und Genauigkeit von LLM-Ausgaben zu verbessern, zeigen Studien, dass diese Methoden Prompt-Injection-Schwachstellen nicht vollständig beheben können.

Da Prompt Injection und Jailbreaking verwandte Konzepte im Bereich der LLM-Sicherheit sind, werden sie oft synonym verwendet. Bei der Prompt Injection werden Modellantworten durch spezifische Eingaben manipuliert, um ihr Verhalten zu ändern, was auch die Umgehung von Sicherheitsmaßnahmen beinhalten kann. Jailbreaking ist eine Form von Prompt Injection, bei der Angreifende Eingaben vornimmt, die dazu führen, dass das Modell seine Sicherheitsvorkehrungen vollständig ignoriert. Entwickelnde können Schutzmaßnahmen in System Prompts und die Eingabeverarbeitung integrieren, um Prompt Injection-Angriffe zu entschärfen. Eine wirksame Verhinderung von Jailbreaking erfordert jedoch eine kontinuierliche Aktualisierung der Trainings- und Sicherheitsmechanismen des Modells.

### Arten von Prompt Injection-Schwachstellen

#### Direkte Prompt Injections
Direkte Prompt Injections treten auf, wenn die Eingabe von Benutzenden das Verhalten des Modells auf unbeabsichtigte oder unerwartete Weise direkt verändert. Die Eingabe kann entweder absichtlich erfolgen (d. h. böswillige Personen erstellen absichtlich eine Eingabeaufforderung, um das Modell auszunutzen) oder unabsichtlich (d. h. Benutzende geben versehentlich eine Eingabe ein, die ein unerwartetes Verhalten auslöst).

#### Indirekte Prompt Injections
Indirekte Prompt Injections treten auf, wenn ein LLM Eingaben von externen Quellen wie Webseiten oder Dateien entgegennimmt. Der Inhalt kann Daten in externen Inhalten enthalten, die bei der Interpretation durch das Modell das Verhalten des Modells auf unbeabsichtigte oder unerwartete Weise verändern. Wie direkte Injektionen können auch indirekte Injektionen entweder beabsichtigt oder unbeabsichtigt sein.

Die Schwere und Art der Auswirkungen eines erfolgreichen Prompt Injection-Angriffs können sehr unterschiedlich sein und hängen weitgehend vom Geschäftskontext ab, in dem das Modell verwendet wird, sowie vom Grad der Autonomie, mit der das Modell entwickelt wurde. Im Allgemeinen kann Prompt Injection jedoch zu unbeabsichtigten Ergebnissen führen:

- Offenlegung vertraulicher Informationen
- Offenlegung sensibler Informationen über die KI-Systeminfrastruktur oder den System Prompt
- Manipulation von Inhalten, die zu falschen oder verzerrten Ergebnissen führt
- Bereitstellung von nicht autorisiertem Zugriff auf Funktionen, die dem LLM zur Verfügung stehen
- Ausführung beliebiger Befehle in verbundenen Systemen
- Manipulation kritischer Entscheidungsprozesse

Der Aufstieg multimodaler KI, die mehrere Datentypen gleichzeitig verarbeiten, birgt spezifische Risiken durch die Prompt Injection. Böswillige Personen könnten Interaktionen zwischen den Modalitäten ausnutzen, indem sie beispielsweise Anweisungen in Bildern verstecken, die harmlosen Text begleiten. Die Komplexität dieser Systeme vergrößert die Angriffsfläche. Multimodale Modelle können auch anfällig für neuartige, modusübergreifende Angriffe sein, die mit den derzeitigen Techniken nur schwer zu erkennen und abzuwehren sind. Robuste multimodalspezifische Abwehrmaßnahmen sind ein wichtiger Bereich für weitere Forschung und Entwicklung.

### Präventions- und Mitigationsstrategien

Aufgrund der Natur der generativen KI sind Schwachstellen bei Prompt Injections möglich. Angesichts des stochastischen Einflusses, der der Funktionsweise von Modellen zugrunde liegt, ist unklar, ob es absolut sichere Methoden zur Verhinderung von Prompt Injections gibt. Die folgenden Maßnahmen können jedoch die Auswirkungen von Prompt Injections abmildern:

#### 1. Begrenzen Sie das Modellverhalten
  Geben Sie spezifische Anweisungen zur Rolle, zu den Fähigkeiten und zu den Beschränkungen des Modells innerhalb des System Prompts. Erzwingen Sie die strikte Einhaltung des Kontexts, beschränken Sie die Antworten auf bestimmte Aufgaben oder Themen und weisen Sie das Modell an, Versuche zur Änderung der Kernanweisungen zu ignorieren.
#### 2. Definieren und validieren Sie erwartete Ausgabeformate
  Legen Sie klare Ausgabeformate fest, fordern Sie detaillierte Begründungen und Quellenangaben an, und verwenden Sie deterministischen Code, um die Einhaltung dieser Formate zu überprüfen.
#### 3. Implementieren Sie Filter für Ein- und Ausgaben
  Definieren Sie sensible Kategorien und erstellen Sie Regeln zur Identifizierung und Handhabung solcher Inhalte. Wenden Sie semantische Filter an und prüfen Sie Strings, um nach nicht zulässigen Inhalten zu suchen. Bewerten Sie die Antworten mithilfe der RAG-Triade: Beurteilen Sie die Relevanz des Kontexts, die Begründetheit und die Relevanz der Frage/Antwort, um potenziell schädliche Ausgaben zu identifizieren.
#### 4. Erzwingen Sie Zugriffsrechte und einen Zugriff mit geringsten Rechten
  Stellen Sie der Anwendung eigene API-Token für erweiterbare Funktionen zur Verfügung und verwalten Sie diese Funktionen im Code, anstatt sie dem Modell zur Verfügung zu stellen. Beschränken Sie die Zugriffsrechte des Modells auf das für die vorgesehenen Vorgänge erforderliche Minimum.
#### 5. Fordern Sie manuelle Freigabe für risikoreiche Aktionen
  Implementieren Sie Kontrollen, bei denen der Mensch in den Prozess eingebunden ist, für privilegierte Vorgänge, um unbefugte Aktionen zu verhindern.
#### 6. Trennen und kennzeichnen Sie externe Inhalte
  Trennen und kennzeichnen Sie nicht vertrauenswürdige Inhalte eindeutig, um ihren Einfluss auf die Eingabeaufforderungen für Benutzende zu begrenzen.
#### 7. Führen Sie adversarial Tests und Angriffssimulationen durch
  Führen Sie regelmäßige Penetrationstests und Angriffssimulationen durch und behandeln Sie das Modell dabei als nicht vertrauenswürdige Person, um die Wirksamkeit von Vertrauensgrenzen und Zugriffskontrollen zu testen.

### Beispiele für Angriffsszenarien

#### Szenario 1: Direkte Injektion
  Angreifende schleusen eine Anweisung in einen Chatbot des Kundensupports ein, die ihn anweist, frühere Richtlinien zu ignorieren, private Datenspeicher abzufragen und E-Mails zu senden, was zu unbefugtem Zugriff und einer Eskalation der Berechtigungen führt.
#### Szenario 2: Indirekte Injektion
  Eine Person verwendet ein LLM, um eine Webseite zusammenzufassen, auf der verborgene Anweisungen enthalten sind, die das LLM dazu veranlassen, ein Bild einzufügen, das mit einer URL verknüpft ist, was zur Exfiltration der privaten Konversation führt.
#### Szenario 3: Unbeabsichtigte Injektion
  Ein Unternehmen fügt in eine Stellenbeschreibung eine Anweisung zur Identifizierung KI-generierter Anwendungen ein. Eine sich bewerbenden Person, die diese Anweisung nicht kennt, verwendet ein LLM, um ihren Lebenslauf zu optimieren, und löst damit versehentlich die KI-Erkennung aus.
#### Szenario 4: Beabsichtigter Einfluss auf das Modell
  Angreifende ändern ein Dokument in einem Repository, das von einer Retrieval-Augmented Generation (RAG)-Anwendung verwendet wird. Wenn die Abfrage den geänderten Inhalt zurückgibt, ändern die bösartigen Anweisungen die Ausgabe des LLM und erzeugen irreführende Ergebnisse.
#### Szenario 5: Code-Injection
  Angreifende nutzen eine Schwachstelle (CVE-2024-5184) in einem E-Mail-Assistenten mit LLM-Unterstützung aus, um schädliche Prompts einzufügen, die den Zugriff auf vertrauliche Informationen und die Manipulation von E-Mail-Inhalten ermöglichen.
#### Szenario 6: Aufteilung des Payloads
  Angreifende laden einen Lebenslauf mit mehrteiligen, bösartigen Anweisungen hoch. Wenn ein LLM zur Bewertung des Kandidierenden verwendet wird, manipulieren die kombinierten Anweisungen die Antwort des Modells, was ungeachtet des Inhalts des Lebenslaufs zu einer positiven Empfehlung führt.
#### Szenario 7: Multimodale Injektion
  Angreifende betten einen schädliche Prompt in ein Bild ein, das einen harmlosen Text begleitet. Wenn eine multimodale KI das Bild und den Text gleichzeitig verarbeitet, ändert der versteckte Prompt das Verhalten des Modells, was möglicherweise zu nicht autorisierten Aktionen oder zur Offenlegung sensibler Informationen führt.
#### Szenario 8: Adversarial Suffix
  Angreifende hängen eine scheinbar bedeutungslose Zeichenfolge an einen Prompt an, der die Ausgabe des LLM auf böswillige Weise beeinflusst und Sicherheitsmaßnahmen umgeht.
#### Szenario 9: Mehrsprachiger/verschleierter Angriff
  Angreifende wenden mehrere Sprachen oder verschlüsseln böswillige Anweisungen (z. B. mit Base64 oder Emojis), um Filter zu umgehen und das Verhalten des LLM zu manipulieren.

### Referenzlinks

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/) **Embrace the Red**
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace the Red**
3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Arxiv**
4. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1) **Research Square**
5. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499) **Cornell University**
6. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf) **Kai Greshake**
8. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf) **Cornell University**
9. [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/) **AI Village**
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/) **Kudelski Security**
11. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations (nist.gov)](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-2e2023.pdf)
12. [2407.07403 A Survey of Attacks on Large Vision-Language Models: Resources, Advances, and Future Trends (arxiv.org)](https://arxiv.org/abs/2407.07403)
13. [Exploiting Programmatic Behavior of LLMs: Dual-Use Through Standard Security Attacks](https://ieeexplore.ieee.org/document/10579515)
14. [Universal and Transferable Adversarial Attacks on Aligned Language Models (arxiv.org)](https://arxiv.org/abs/2307.15043)
15. [From ChatGPT to ThreatGPT: Impact of Generative AI in Cybersecurity and Privacy (arxiv.org)](https://arxiv.org/abs/2307.00691)

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt finden Sie umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [AML.T0051.000 - LLM Prompt Injection: Direct](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
- [AML.T0051.001 - LLM Prompt Injection: Indirect](https://atlas.mitre.org/techniques/AML.T0051.001) **MITRE ATLAS**
- [AML.T0054 - LLM Jailbreak Injection: Direct](https://atlas.mitre.org/techniques/AML.T0054) **MITRE ATLAS**
