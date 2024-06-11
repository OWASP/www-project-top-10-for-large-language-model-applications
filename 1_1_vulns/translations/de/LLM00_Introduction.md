## Einleitung

### Die Entstehung der Liste

Seit der Einführung von massentauglichen, vortrainierten Chatbots Ende 2022 ist das Interesse an Large Language Models (LLMs) enorm. Unternehmen, die das Potenzial von LLMs nutzen wollen, integrieren sie rasch in ihre Geschäftsprozesse und Angebote für Kunden. Die rasante Geschwindigkeit der Einführung von LLMs hat jedoch dazu geführt, dass die Etablierung umfassender Sicherheitsprotokolle in Verzug geraten ist, sodass viele Anwendungen mit hohen Risiken behaftet sind.

Das Fehlen einer zentralen Ressource, die sich mit diesen Sicherheitsbedenken in Bezug auf LLMs befasst, war unübersehbar. Entwicklerinnen und Entwickler, die mit den spezifischen Risiken von LLMs nicht vertraut waren, standen nur wenige Quellen zur Verfügung, und die Mission von OWASP schien die perfekte Lösung zu sein, um eine sichere Einführung dieser Technologie zu fördern.

### Für wen diese Liste ist

Unsere Hauptzielgruppe sind Entwickelnde, Data Scientists sowie Sicherheitsexpertinnen und -experten, die Anwendungen und Plug-ins basierend auf LLM-Technologien entwerfen und erstellen. Unser Ziel ist es, praktische, umsetzbare und prägnante Sicherheitsleitlinien bereitzustellen, die diesen Fachleuten helfen, sich auf dem komplexen und sich ständig weiterentwickelnden Gebiet der Sicherheit von LLM-Anwendungen zurechtzufinden.

### Die Erstellung der Liste

Das Erstellen der OWASP Top 10 für LLM-Applikationen war ein bedeutendes Unterfangen, das auf der kollektiven Expertise eines internationalen Teams von fast 500 Expertinnen und Experten mit mehr als 125 aktiven Mitgestaltenden basiert. Unsere Mitwirkenden kommen aus den unterschiedlichsten Bereichen, darunter KI-Unternehmen, Sicherheitsfirmen, ISVs, Cloud-Hyperscaler, Hardware-Anbieter und die akademische Welt.

Wir haben einen Monat lang gebrainstormt, potenzielle Schwachstellen vorgeschlagen und dabei 43 verschiedene Bedrohungen formuliert. In mehreren Abstimmungsrunden haben wir diese Vorschläge zu einer prägnanten Liste der zehn kritischsten Schwachstellen verfeinert. Spezialisierte Untergruppen untersuchten jede Schwachstelle und unterzogen sie einer öffentlichen Überprüfung, um sicherzustellen, dass die endgültige Liste so umfassend und nützlich wie möglich war.

### Das Verhältnis zu anderen OWASP Top-10-Listen

Obwohl unsere Liste Gemeinsamkeiten mit den Schwachstellentypen anderer OWASP Top-10-Listen aufweist, wiederholen wir diese Schwachstellen nicht einfach. Stattdessen fokussieren wir uns auf die einzigartigen Auswirkungen dieser Schwachstellen bei der Verwendung von LLMs.

Unser Ziel ist es, die Lücke zwischen allgemeinen Prinzipien der Anwendungssicherheit und den spezifischen Herausforderungen von LLMs zu schließen. Dazu gehört die Untersuchung, wie herkömmliche Schwachstellen in LLMs andere Risiken darstellen oder auf neue Weise ausgenutzt werden können und wie herkömmliche Abwehrmaßnahmen für LLM-basierte Anwendungen angepasst werden müssen.

### Die Zukunft

Version 1.1 der Liste wird nicht die letzte sein. Wir planen, sie regelmäßig zu aktualisieren, um mit den Entwicklungen in der Branche Schritt zu halten. Wir werden mit der erweiterten Community zusammenarbeiten, um den Stand der Technik voranzutreiben und mehr Schulungsmaterial für eine Vielzahl von Anwendungen zu erstellen. Ebenso streben wir auch die Zusammenarbeit mit Standardisierungsorganisationen und Regierungen in Fragen der KI-Sicherheit an. Sie sind herzlich eingeladen, sich unserer Gruppe anzuschließen und einen Beitrag zu leisten.

#### Steve Wilson

Projektleiter, OWASP Top 10 für LLM-Applikationen
[https://www.linkedin.com/in/wilsonsd](https://www.linkedin.com/in/wilsonsd/)  
Twitter/X: @virtualsteve

#### Ads Dawson

v1.1 Release Lead & Vulnerability Entries Lead, OWASP Top 10 für LLM-Applikationen
[https://www.linkedin.com/in/adamdawson0](https://www.linkedin.com/in/adamdawson0/) 
GitHub: @GangGreenTemperTatum

## Über diese Übersetzung

### Übersetzer

Johann-Peter Hartmann
[https://www.linkedin.com/in/johann-peter-hartmann-92b70a/](https://www.linkedin.com/in/johann-peter-hartmann-92b70a/)  

Philippe Schrettenbrunner
[https://www.linkedin.com/in/philippe-schrettenbrunner/](https://www.linkedin.com/in/philippe-schrettenbrunner/)

Bei der Erstellung dieser Übersetzung haben wir uns bewusst dafür entschieden, nur menschliche Übersetzer einzusetzen, in Anerkennung der außerordentlich technischen und kritischen Natur der OWASP Top 10 für LLM-Applikationen. Die oben aufgeführten Übersetzer verfügen nicht nur über ein tiefes Verständnis des Originalinhalts, sondern auch über die sprachliche Kompetenz, um diese Übersetzung sinnvoll zu gestalten.

Talesh Seeparsan
Übersetzungsleiter, OWASP Top 10 für LLM-Applikationen
[https://www.linkedin.com/in/talesh/](https://www.linkedin.com/in/talesh/)  

## OWASP Top 10 für LLM-Applikationen

### LLM01: Prompt Injection
Mittels raffinierter Eingaben kann ein Large Language Model manipuliert werden und unbeabsichtigte Aktionen auslösen. Direkte Injections überschreiben System-Prompts, während indirekte Injection Eingaben über externe Quellen manipulieren.

### LLM02: Unsichere Ausgabeverarbeitung
Diese Schwachstelle tritt auf, wenn eine Ausgabe von einem LLM ungeprüft akzeptiert wird, wodurch Backend-Systeme angreifbar werden. Ein Missbrauch kann zu schwerwiegenden Folgen wie XSS (Cross-Site Scripting), CSRF (Cross-Site Request Forgery), SSRF (Server Side Request Forgery), Privilegienerweiterung oder Remote-Code-Ausführung führen.

### LLM03: Poisoning von Trainingsdaten
Dies tritt auf, wenn LLM-Trainingsdaten manipuliert werden und dadurch Sicherheitslücken oder Bias entstehen, die Sicherheit, Performance oder ethisches Verhalten beeinträchtigen. Quellen umfassen Common Crawl, WebText, OpenWebText und Bücher.

### LLM04: Denial of Service des Modells
Angreifende verursachen ressourcenintensive Operationen auf Large Language Models, was zu Beeinträchtigung oder hohen Kosten führt. Die Schwachstelle wird durch die ressourcenintensive Natur von LLMs und die Unvorhersehbarkeit von Benutzereingaben verstärkt.

### LLM05: Schwachstellen in der Lieferkette
Der Lebenszyklus von LLM-Anwendungen kann durch verwundbare Komponenten oder Dienste kompromittiert werden, was Angriffe auf die Sicherheit zur Folge haben kann. Die Verwendung von Datensätzen von Drittanbietern, vortrainierten Modellen und Plug-ins kann zu weiteren Schwachstellen führen.

### LLM06: Offenlegung sensibler Informationen
LLMs können in ihren Antworten vertrauliche Daten preisgeben, was zu unbefugtem Datenzugriff, Datenschutzverletzungen und Sicherheitsverstößen führt. Datenbereinigung und strenge Benutzerrichtlinien sind unerlässlich, um dies zu verhindern.

### LLM07: Unsicheres Plug-in-Design
LLM-Plug-ins können unsichere Eingaben und unzureichende Zugriffskontrollen aufweisen. Dieser Mangel an Anwendungskontrolle erleichtert das Ausnutzen von LLM-Plug-ins und kann zu Folgen wie der Ausführung von Remote-Code führen.

### LLM08: Übermäßige Handlungsfreiheit
LLM-basierte Systeme können Aktionen ausführen, die unbeabsichtigte Folgen haben. Das Problem entsteht, wenn diesen Systemen zu viele Funktionalitäten, zu viele Berechtigungen oder zu viel Autonomie eingeräumt werden.

### LLM09: Übermäßige Abhängigkeit
Systeme oder Personen, die sich zu sehr und unkontrolliert auf LLMs verlassen, können durch falsche oder unangemessene Inhalte, die von LLMs erzeugt werden, mit Fehlinformationen, Fehlkommunikation, rechtlichen Problemen und Sicherheitslücken konfrontiert werden.

### LLM10: Modell-Diebstahl
Dies schließt den unbefugten Zugriff, das Kopieren oder die Weitergabe von geschützten LLM-Modellen ein. Die Folgen sind wirtschaftliche Verluste, gefährdete Wettbewerbsvorteile und potenzieller Zugang zu sensiblen Informationen.


## Datenfluss einer LLM-Anwendung

Das folgende Diagramm zeigt die High-Level-Architektur einer hypothetischen LLM-Anwendung. Im Diagramm  sind die Risikobereiche hervorgehoben, die veranschaulichen, wie sich die Punkte der OWASP Top 10 für LLM-Anwendungen mit dem Datenfluss der Anwendung überschneiden.

Dieses Diagramm kann als visueller Leitfaden verwendet werden, um zu verstehen, wie sich die Sicherheitsrisiken großer Sprachmodelle auf das gesamte Anwendungsökosystem auswirken.

![Abb_1](images/fig_5_2.jpg)

##### Abbildung 1: OWASP Top 10 für LLM-Applikationen visualisiert