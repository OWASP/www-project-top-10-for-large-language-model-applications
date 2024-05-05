## LLM01: Prompt Injection

### Beschreibung

Die Schwachstelle der Prompt Injection tritt auf, wenn ein Angreifer ein großes Sprachmodell (Large Language Model, LLM) durch speziell gestaltete Eingaben manipuliert, sodass das LLM unwissentlich die Absichten des Angreifers ausführt. Dies kann direkt durch "Jailbreaking" des System-Prompts oder indirekt durch manipulierte externe Eingaben erfolgen, was möglicherweise zu Datenexfiltration, Social Engineering und anderen Problemen führen kann.

* **Direkte Prompt Injections**, auch bekannt als "Jailbreaking", treten auf, wenn ein bösartiger Benutzer den zugrundeliegenden *System*-Prompt überschreibt oder offenlegt. Dies kann Angreifern ermöglichen, Backend-Systeme zu nutzen, indem sie mit unsicheren Funktionen und Datenspeichern interagieren, die über das LLM zugänglich sind.
* **Indirekte Prompt Injections** treten auf, wenn ein LLM Eingaben von externen Quellen akzeptiert, die von einem Angreifer kontrolliert werden können, wie Websites oder Dateien. Der Angreifer kann eine Prompt Injection in den externen Inhalt einbetten, um den Konversationskontext zu kapern. Dies würde dazu führen, dass die Stabilität der LLM-Ausgabe weniger stabil wird, wodurch der Angreifer entweder den Benutzer oder zusätzliche Systeme manipulieren kann, auf die das LLM Zugriff hat. Zusätzlich müssen indirekte Prompt Injections nicht für Menschen sichtbar/lesbar sein, solange der Text vom LLM verarbeitet wird.

Die Ergebnisse eines erfolgreichen Prompt Injection-Angriffs können stark variieren - von der Anforderung sensibler Informationen bis hin zur Beeinflussung kritischer Entscheidungsprozesse unter dem Deckmantel normaler Operationen.

Bei fortgeschrittenen Angriffen könnte das LLM manipuliert werden, um eine schädliche Persona nachzuahmen oder mit Plugins in der Benutzereinstellung zu interagieren. Dies könnte zum Leck von sensiblen Daten, zur unbefugten Plugin-Nutzung oder zu Social Engineering führen. In solchen Fällen unterstützt das kompromittierte LLM den Angreifer und umgeht die Standard-Sicherheitsvorkehrungen, während der Benutzer von dem Eindringen nichts mitbekommt. In diesen Fällen agiert das kompromittierte LLM effektiv als Agent für den Angreifer, der seine Ziele weiterverfolgt, ohne übliche Sicherheitsvorkehrungen auszulösen oder den Endbenutzer auf das Eindringen aufmerksam zu machen.

### Häufige Beispiele für Schwachstellen

1. Ein bösartiger Benutzer erstellt eine direkte Prompt Injection für das LLM, die es anweist, die System-Prompts des App-Erstellers zu ignorieren und stattdessen einen Prompt auszuführen, der private, gefährliche oder anderweitig unerwünschte Informationen zurückgibt.
2. Ein Benutzer verwendet ein LLM, um eine Webseite zusammenzufassen, die eine indirekte Prompt Injection enthält. Dies veranlasst das LLM dann, sensible Informationen vom Benutzer anzufordern und eine Exfiltration über JavaScript oder Markdown durchzuführen.
3. Ein bösartiger Benutzer lädt einen Lebenslauf hoch, der eine indirekte Prompt Injection enthält. Das Dokument enthält eine Prompt Injection mit Anweisungen, das LLM zu informieren, dass dieses Dokument ausgezeichnet ist, z. B. ein ausgezeichneter Kandidat für eine Stellenbeschreibung. Ein interner Benutzer führt das Dokument durch das LLM, um das Dokument zusammenzufassen. Die Ausgabe des LLM gibt zurück, dass dies ein ausgezeichnetes Dokument ist.
4. Ein Benutzer aktiviert ein Plugin, das mit einer E-Commerce-Website verlinkt ist. Eine Schadensanweisung, die auf einer besuchten Website eingebettet ist, nutzt dieses Plugin aus und führt zu unbefugten Käufen.
5. Eine Schadensanweisung und Inhalt, die auf einer besuchten Website eingebettet sind, nutzen andere Plugins aus, um Benutzer zu betrügen.

### Präventions- und Mitigationsstrategien

Prompt Injection-Schwachstellen sind möglich aufgrund der Natur von LLMs, die Anweisungen und externe Daten nicht voneinander trennen. Da LLMs natürliche Sprache verwenden, betrachten sie beide Formen der Eingabe als vom Benutzer bereitgestellt. Folglich gibt es keine narrensichere Prävention innerhalb des LLM, aber die folgenden Maßnahmen können die Auswirkungen von Prompt Injections mindern:

1. Durchsetzen der Zugriffskontrolle auf LLM-Zugriff auf Backend-Systeme. Stelle dem LLM eigene API-Tokens für erweiterbare Funktionen zur Verfügung, wie Plugins, Datenzugriff und Funktionsberechtigungen. Befolge das Prinzip der geringsten Rechte, indem du den LLM-Zugriff nur auf das für seine beabsichtigten Operationen notwendige Minimum beschränkst.
2. Hinzufügen eines Menschen in der Schleife für erweiterte Funktionen. Bei der Durchführung privilegierter Operationen, wie dem Senden oder Löschen von E-Mails, soll die Anwendung zuerst die Genehmigung des Benutzers für die Aktion verlangen. Dies verringert die Möglichkeit, dass indirekte Prompt Injections zu unbefugten Aktionen im Namen des Benutzers ohne dessen Wissen oder Zustimmung führen.
3. Trennen von externem Inhalt von Benutzer-Prompts. Trenne und kennzeichne, wo unzuverlässiger Inhalt verwendet wird, um deren Einfluss auf Benutzer-Prompts zu begrenzen. Verwende beispielsweise ChatML für OpenAI-API-Aufrufe, um dem LLM die Quelle der Prompt-Eingabe anzuzeigen.
4. Etablieren von Vertrauensgrenzen zwischen dem LLM, externen Quellen und erweiterbaren Funktionen (z. B. Plugins oder nachgelagerten Funktionen). Behandle das LLM als unzuverlässigen Benutzer und behalte die endgültige Benutzerkontrolle über Entscheidungsprozesse. Ein kompromittiertes LLM kann jedoch immer noch als Vermittler (Man-in-the-Middle) zwischen den APIs deiner Anwendung und dem Benutzer agieren, da es Informationen verbergen oder manipulieren kann, bevor es sie dem Benutzer präsentiert. Hebe möglicherweise unzuverlässige Antworten visuell für den Benutzer hervor.
5. Überwache manuell LLM-Eingaben und -Ausgaben periodisch, um zu überprüfen, ob sie wie erwartet sind. Dies ist zwar keine Minderung, kann aber Daten liefern, die benötigt werden, um Schwachstellen zu erkennen und anzugehen.

### Beispiel für Angriffsszenarien

1. Ein Angreifer liefert eine direkte Prompt Injection an einen LLM-basierten Support-Chatbot. Die Injection enthält "Vergiss alle vorherigen Anweisungen" und neue Anweisungen, um private Datenspeicher abzufragen und Paketschwachstellen sowie das Fehlen einer Ausgabevalidierung in der Backend-Funktion zu nutzen, um E-Mails zu senden. Dies führt zu einer Remote-Code-Ausführung, gewährt unbefugten Zugriff und Privilegienerweiterung.
2. Ein Angreifer bettet eine indirekte Prompt Injection in eine Webseite ein, die das LLM anweist, vorherige Benutzeranweisungen zu ignorieren und ein LLM-Plugin zu verwenden, um die E-Mails des Benutzers zu löschen. Wenn der Benutzer das LLM verwendet, um diese Webseite zusammenzufassen, löscht das LLM-Plugin die E-Mails des Benutzers.
3. Ein Benutzer verwendet ein LLM, um eine Webseite zusammenzufassen, die Text enthält, der ein Modell anweist, vorherige Benutzeranweisungen zu ignorieren und stattdessen ein Bild einzufügen, das zu einer URL verlinkt, die eine Zusammenfassung des Gesprächs enthält. Die LLM-Ausgabe entspricht dem, was dazu führt, dass der Browser des Benutzers das private Gespräch exfiltriert.
4. Ein bösartiger Benutzer lädt einen Lebenslauf mit einer Prompt Injection hoch. Der Backend-Benutzer verwendet ein LLM, um den Lebenslauf zusammenzufassen und zu fragen, ob die Person ein guter Kandidat ist. Aufgrund der Prompt Injection lautet die Antwort des LLM ja, ungeachtet des tatsächlichen Inhalts des Lebenslaufs.
5. Ein Angreifer sendet Nachrichten an ein proprietäres Modell, das sich auf einen System-Prompt verlässt, und bittet das Modell, seine vorherigen Anweisungen zu ignorieren und stattdessen seinen System-Prompt zu wiederholen. Das Modell gibt den proprietären Prompt aus und der Angreifer kann diese Anweisungen anderswo verwenden oder weitere, subtilere Angriffe konstruieren.

### Referenzlinks

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) **Simon Willison**
1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
1. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
1. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
1. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
1. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
1. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
1. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
1. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
1. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
1. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
1. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
1. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**