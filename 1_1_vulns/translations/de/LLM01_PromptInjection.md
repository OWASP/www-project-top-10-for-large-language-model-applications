## LLM01: Prompt Injection

### Beschreibung

Die Prompt-Injection-Schwachstelle tritt auf, wenn Angreifende ein Large Language Model (LLM) durch speziell gestaltete Eingaben so manipulieren, dass das LLM unwissentlich die Absichten des Angreifenden ausführt. Dies kann direkt durch "Jailbreaking" des System-Prompts oder indirekt durch manipulierte, externe Eingaben geschehen, was zu Datenexfiltration, Social Engineering und anderen Problemen führen kann.

* **Direkte Prompt Injections**, auch als "Jailbreaking" bekannt, treten auf, wenn böswillige Personen den zugrundeliegenden *System* Prompt überschreiben oder offenlegen. Dies kann es Angreifenden ermöglichen, Backend-Systeme zu nutzen, indem sie mit unsicheren Funktionen und Datenspeichern interagieren, die über das LLM zugänglich sind.
* **Indirekte Prompt Injections** treten auf, wenn ein LLM Eingaben von externen Quellen akzeptiert, die von Angreifenden kontrolliert werden können, wie z. B. Websites oder Dateien. Angreifende können eine Prompt Injection in externen Inhalt einbetten, um den Konversationskontext zu übernehmen. Dies würde dazu führen, dass die Stabilität der LLM-Ausgabe weniger robust wird, wodurch Angreifende entweder Personen oder zusätzliche Systeme, auf die das LLM Zugriff hat, manipulieren könnte. Außerdem müssen indirekte Prompt Injections für Menschen nicht sichtbar/lesbar sein, solange der Text vom LLM verarbeitet wird.

Die Ergebnisse eines erfolgreichen Prompt Injection-Angriffs können stark variieren - vom Ausspähen sensibler Informationen bis hin zur Beeinflussung kritischer Entscheidungsprozesse unter dem Deckmantel eines normalen Betriebs.

Bei fortgeschrittenen Angriffen könnte das LLM so manipuliert werden, dass es eine böswillige Person imitiert oder mit Plug-ins in der Umgebung der Nutzenden interagiert. Dies könnte zur Offenlegung sensibler Daten, zur unautorisierten Nutzung von Plug-ins oder zu Social Engineering führen. In solchen Fällen unterstützt das kompromittierte LLM die angreifende Person und umgeht die Standardsicherheitsmaßnahmen, während die Nutzenden nichts von dem Einbruch bemerken. In diesen Fällen agiert das kompromittierte LLM effektiv als Agent für die angreifende Person, die ihre Ziele verfolgt, ohne die üblichen Sicherheitsmaßnahmen auszulösen oder die Endnutzenden auf das Eindringen aufmerksam zu machen.

### Gängige Beispiele für Schwachstellen

1. Eine böswillige Person erstellt eine direkte Prompt Injection für das LLM, die es anweist, die System-Prompts der App-Entwickelnden zu ignorieren und stattdessen einen Prompt auszuführen, der private, gefährliche oder anderweitig unerwünschte Informationen zurückgibt.
2. Eine Person verwendet ein LLM, um eine Webseite zusammenzufassen, die eine indirekte Prompt Injection enthält. Dies führt dazu, dass das LLM sensible Informationen vom Benutzer oder von der Benutzerin anfordert und eine Exfiltration über JavaScript oder Markdown durchführt.
3. Eine böswillige Person lädt einen Lebenslauf hoch, der eine indirekte Prompt Injection enthält. Das Dokument enthält eine Prompt Injection mit Anweisungen, die das LLM dazu veranlassen, Personen darüber zu informieren, dass dieses Dokument ausgezeichnet ist z. B. bei der Bewerbung auf eine Stellenausschreibung. Eine interne Person leitet das Dokument durch das LLM, um das Dokument zusammenzufassen. Das LLM meldet zurück, dass es sich um ein exzellentes Dokument handelt.
4. Eine Person aktiviert ein Plug-in, das mit einer E-Commerce-Website verknüpft ist. Eine bösartige Funktion, die in eine besuchte Website eingebettet ist, nutzt dieses Plug-in aus und führt zu nicht autorisierten Käufen.
5. Schädliche Befehle und Inhalte, die auf einer besuchten Website eingebettet sind, nutzen andere Plug-ins aus, um Personen zu betrügen.

### Präventions- und Mitigationsstrategien

Prompt-Injection-Schwachstellen sind möglich, da LLMs von Natur aus nicht zwischen Befehlen und externen Daten unterscheiden können. Weil LLMs natürliche Sprache verwenden, betrachten sie beide Formen der Eingabe als vom Benutzer bereitgestellt. Daher gibt es keine unfehlbare Prävention innerhalb von LLMs, aber die folgenden Maßnahmen können die Auswirkungen von Prompt Injections reduzieren:

1. Erzwingen Sie eine Zugriffskontrolle für den Zugriff durch das LLM auf Backend-Systeme. Stellen Sie dem LLM eigene API-Tokens für zusätzliche Funktionen zur Verfügung, wie z. B. Plug-ins, Datenzugriff und Funktionsberechtigungen. Befolgen Sie das Least-Privilege-Prinzip und beschränken Sie den LLM-Zugriff auf das notwendige Minimum.
2. Binden Sie eine menschliche Kontrollinstanz für erweiterte Funktionalität ein. Bei der Durchführung privilegierter Operationen, wie dem Senden oder Löschen von E-Mails, sollte die Anwendung eine Bestätigung durch einen Menschen einfordern. Dies verringert die Möglichkeit, dass indirekte Prompt Injection-Angriffe zu unbefugten Handlungen im Namen von Nutzenden führen, ohne deren Wissen oder Zustimmung.
3. Trennen Sie externen Inhalt von Nutzereingaben. Isolieren und kennzeichnen Sie, wo nicht vertrauenswürdiger Inhalt verwendet wird, um dessen Einfluss auf Nutzereingaben zu begrenzen. Verwenden Sie beispielsweise ChatML für OpenAI-API-Aufrufe, um dem LLM die Quelle der Eingabeaufforderung anzuzeigen.
4. Etablieren Sie Vertrauensgrenzen zwischen dem LLM, externen Quellen und erweiterbaren Funktionen (z.B. Plug-ins oder nachgelagerte Abläufe). Behandeln Sie das LLM als nicht vertrauenswürdige Instanz und bewahren Sie die endgültige Kontrolle über Entscheidungsprozesse bei den Nutzenden. Ein kompromittiertes LLM kann jedoch weiterhin als Vermittler (Man-in-the-Middle) zwischen den APIs der Anwendung und den Nutzenden agieren, da es Informationen verbergen oder manipulieren kann, bevor es diese den Nutzenden präsentiert. Kennzeichnen Sie potenziell nicht vertrauenswürdige Antworten visuell für die Nutzenden. 
5. Überwachen Sie manuell und in regelmäßigen Abständen die Eingaben und Ausgaben des LLM, um sicherzustellen, dass sie den Erwartungen entsprechen. Obwohl dies keine Risikominderung darstellt, kann es Daten liefern, die zur Identifizierung und Behebung von Schwachstellen erforderlich sind.

### Beispiele für Angriffsszenarien

1. Angreifende senden eine direkte Prompt Injection an einen LLM-basierten Support-Chatbot. Die Injection enthält "Vergiss alle vorherigen Anweisungen" sowie neue Anweisungen, um private Datenspeicher abzufragen. Außerdem werden Paketverwundbarkeiten und fehlende Ausgabevalidierung in der Backend-Funktion zum Senden von E-Mails ausgenutzt. Dies führt zu Remote-Code-Ausführung, unberechtigtem Zugriff und Privilegienerweiterung.
2. Angreifende betten eine indirekte Prompt-Injection in eine Webseite ein, die das LLM anweist, vorherige Benutzeranweisungen zu ignorieren und ein LLM-Plug-in zu verwenden, um die E-Mails des Benutzers zu löschen. Wenn eine Person das LLM verwendet, um diese Webseite zusammenzufassen, löscht das LLM-Plug-in die E-Mails der Person.
3. Eine Person verwendet ein LLM, um eine Webseite zusammenzufassen, die Text enthält, welcher ein Modell anweist, vorherige Benutzeranweisungen zu ignorieren und stattdessen ein Bild einzufügen, das zu einer URL verlinkt, die eine Zusammenfassung der Unterhaltung enthält. Die LLM-Ausgabe befolgt dies, was dazu führt, dass der Browser der Person die private Unterhaltung exfiltriert.
4. Eine bösartige Person lädt einen Lebenslauf mit einer Prompt Injection hoch. Der Backend-Benutzer verwendet ein LLM, um den Lebenslauf zusammenzufassen und zu fragen, ob die Person ein guter Kandidat ist. Aufgrund der Prompt Injection lautet die Antwort des LLM ja, ungeachtet des tatsächlichen Inhalts des Lebenslaufs.
5. Angreifende senden Nachrichten an ein proprietäres Modell, das sich auf einen System-Prompt verlässt, und bittet das Modell, seine vorherigen Anweisungen zu ignorieren und stattdessen seinen System-Prompt zu wiederholen. Das Modell gibt den proprietären Prompt aus und die Angreifende können diese Anweisungen anderswo verwenden oder weitere, subtilere Angriffe konstruieren.

### Referenzen

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/): **Simon Willison**
2. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
3. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
5. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
6. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
7. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
8. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
9. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
10. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
11. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
12. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
13. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
14. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**