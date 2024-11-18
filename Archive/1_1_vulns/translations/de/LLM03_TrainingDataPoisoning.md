## LLM03: Poisoning von Trainingsdaten

### Beschreibung

Ausgangspunkt jedes Ansatzes zum maschinellen Lernen sind Trainingsdaten, einfach gesagt "Rohdaten". Um eine hohe Effizienz zu erreichen (z. B. linguistisches Wissen und Wissen über die Welt), müssen diese Daten eine große Bandbreite an Domänen, Genres und Sprachen abdecken. Ein Large Language Model verwendet tiefe neuronale Netze, um Ausgaben zu erzeugen, die auf Mustern basieren, die aus den Trainingsdaten gelernt wurden.

Das Poisoning von Trainingsdaten bezieht sich auf die Manipulation von Daten vor dem Training oder von Daten, die in den Fine-Tuning- oder Embedding-Prozess involviert sind, um Schwachstellen (die alle einzigartige und manchmal gemeinsame Angriffsvektoren haben), Hintertüren oder Verzerrungen einzuführen, die die Sicherheit, die Effektivität oder das ethische Verhalten des Modells beeinträchtigen könnten. Vergiftete Informationen können an Personen weitergegeben werden oder andere Risiken wie Leistungseinbußen, die Ausnutzung nachgelagerter Software und Rufschädigung mit sich bringen. Selbst wenn Personen der problematischen KI-Ausgabe misstrauen, bleiben die Risiken bestehen, einschließlich der Beeinträchtigung der Leistung des Modells und der potenziellen Imageschäden.

- Das Pre-Training von Daten bezieht sich auf den Prozess des Trainierens eines Modells auf der Grundlage einer Aufgabe oder eines Datensatzes.
- Die Feinabstimmung umfasst die Anpassung eines bereits trainierten Modells an ein enger gefasstes Thema oder ein spezifischeres Ziel, indem es mit einem kuratierten Datensatz trainiert wird. Dieser Datensatz enthält typischerweise Beispiele für Eingaben und die entsprechenden gewünschten Ausgaben.
- Embedding ist der Prozess der Umwandlung von kategorialen Daten (oft Text) in eine digitale Repräsentation, die für das Training eines Sprachmodells verwendet werden kann. Beim Embedding werden Wörter oder Phrasen aus den Textdaten als Vektoren in einem kontinuierlichen Vektorraum dargestellt. Die Vektoren werden typischerweise durch Eingabe der Textdaten in ein neuronales Netz erzeugt, das auf einem großen Textkorpus trainiert wurde.

Die Vergiftung von Daten wird als Angriff auf die Integrität betrachtet, da die Manipulation der Trainingsdaten die Fähigkeit des Modells beeinträchtigt, korrekte Vorhersagen zu liefern. Es liegt auf der Hand, dass externe Datenquellen ein höheres Risiko bergen, da die Modellersteller keine Kontrolle über die Daten haben und nicht sicher sein können, dass der Inhalt frei von Bias, falschen Informationen oder unangemessenen Inhalten ist.

### Gängige Beispiele für Schwachstellen

1. Bösartige Akteure oder Wettbewerber erstellen absichtlich ungenaue oder bösartige Dokumente, die auf das Pre-Training-, Fine-Tuning oder Embedding eines Modells abzielen. Betrachten Sie sowohl Split-View Data Poisoning (Ref.12) als auch Frontranking Poisoning (Ref.13) Angriffsvektoren zur Veranschaulichung.
  - Das Opfermodell wird anhand von gefälschten Informationen trainiert, die sich in den Ausgaben der generativen KI-Prompts an die Endkunden widerspiegeln.
2. Böswillige Akteure können direkt gefälschte, voreingenommene oder schädliche Inhalte in die Trainingsprozesse eines Modells einspeisen, die in späteren Ausgaben zurückgegeben werden.
3. Eine ahnungslose Person injiziert indirekt sensible oder proprietäre Daten in die Trainingsprozesse eines Modells, die in nachfolgenden Ausgaben zurückgegeben werden.
4. Ein Modell wird mit Daten trainiert, deren Quelle, Herkunft oder Inhalt in keinem der Trainingsbeispiele verifiziert wurde, was zu falschen Ergebnissen führen kann, wenn die Daten verfälscht oder fehlerhaft sind. 
5. Uneingeschränkter Zugang zur Infrastruktur oder unzureichende Sandbox-Umgebungen können dazu führen, dass ein Modell unsichere Trainingsdaten verwendet, was zu verzerrten oder schädlichen Ergebnissen führt. Dieses Beispiel kann in allen Trainingsstadien vorkommen.
  - In diesem Szenario kann die Eingabe einer Person in das Modell in der Ausgabe einer anderen Person widergespiegelt werden (was zu einem Datenleck führt), oder Nutzende eines LLM können Ausgaben aus dem Modell erhalten, die, abhängig von der Art der erfassten Daten, ungenau, irrelevant oder schädlich für den Anwendungsfall des Modells sein können (in der Regel durch eine Modellkarte widergespiegelt).
6. Ob Entwicklerinnen und Entwickler, die Kundschaft oder allgemeine Nutzende des LLM, es ist wichtig zu verstehen, wie sich diese Schwachstelle auf die potenziellen Risiken innerhalb Ihrer LLM-Anwendung auswirken könnte, wenn sie mit einem fremden LLM interagiert, um die Legitimität der Modellausgaben zu verstehen, die auf dessen Trainingsverfahren basieren. In ähnlicher Weise könnten LLM-Entwickelnde sowohl direkten als auch indirekten Angriffen auf interne Daten oder Daten von Drittanbietern ausgesetzt sein, die für die (gängigste Variante) Fine-Tuning und Embeddings verwendet werden, was ein Risiko für alle LLM-Anwender darstellt.

### Präventions- und Mitigationsstrategien

1. Überprüfen Sie die Lieferkette der Trainingsdaten, insbesondere wenn diese extern bezogen werden, und führen Sie Bescheinigungen mit der „ML-BOM“-Methode (Machine Learning Bill of Materials) sowie die Überprüfung der Modellkarten durch.
2. Überprüfen Sie die korrekte Eignung der angestrebten Datenquellen und der darin enthaltenen Daten, die sowohl in der Vorbereitungsphase als auch in der Fine-Tuning- und Integrationsphase gewonnen wurden.
3. Überprüfen Sie Ihren Use Case für das LLM und die Anwendung, in die es integriert werden soll. Entwickeln Sie verschiedene Modelle mit separaten Trainingsdaten oder Fine-Tuning für verschiedene Anwendungsfälle, um eine granularere und genauere generative KI-Ausgabe für den jeweiligen Anwendungsfall zu erzeugen. 
4. Stellen Sie sicher, dass ein ausreichendes Sandboxing durch Netzwerkkontrollen vorhanden ist, um zu verhindern, dass das Modell unbeabsichtigte Datenquellen nutzt, die die Ergebnisse des maschinellen Lernens beeinträchtigen könnten.
5. Verwenden Sie strenge Kontrollen oder Eingabefilter für bestimmte Trainingsdaten oder Kategorien von Datenquellen, um die Menge an gefälschten Daten zu kontrollieren. Bereinigung der Daten durch Techniken wie statistische Ausreißererkennung und Methoden zur Erkennung von Anomalien, um unerwünschte Daten zu erkennen und zu entfernen, bevor sie möglicherweise in den Feinabstimmungsprozess einfließen.
6. Entwickeln Sie Kontrollfragen bezüglich der Quelle und des Eigentums von Datensätzen, um sicherzustellen, dass das Modell nicht verunreinigt wurde, und integrieren Sie diese Kultur in den MLSecOps-Zyklus. Beziehen Sie sich auf verfügbare Ressourcen wie z. B. The Foundation Model Transparency Index (Ref.14) oder Open LLM Leaderboard (Ref.15).
7. Verwenden Sie DVC (Data Version Control (Ref.16)), um Teile eines Datensatzes, die manipuliert, gelöscht oder hinzugefügt wurden und zu Poisoning geführt haben, genau zu identifizieren und zu verfolgen.
8. Verwenden Sie eine Vektordatenbank, um von Benutzern bereitgestellte Informationen zu speichern, um andere Personen vor Manipulationen zu schützen und um sogar während der Produktion Fehler zu beheben, ohne ein neues Modell trainieren zu müssen.
9. Verwenden Sie Techniken zur Abwehr von Angriffen, wie z. B. föderiertes Lernen und Einschränkungen, um den Einfluss von Ausreißern zu minimieren, oder adverses Training, um robust gegenüber den schlimmsten Störungen der Trainingsdaten zu sein.
  - Ein "MLSecOps"-Ansatz könnte darin bestehen, die adversariale Robustheit mithilfe der Autopoison-Technik in den Trainingslebenszyklus zu integrieren.
  - Ein Beispiel Repository hierfür ist das Autopoison (Ref.17), das sowohl Angriffe wie Content Injection Attacks (der Versuch, einen Markennamen in den Antworten des Modells zu bewerben) als auch Refusal Attacks ("das Modell immer dazu bringen, die Antwort zu verweigern") umfasst, die mit diesem Ansatz durchgeführt werden können.
10. Testen und Erkennen durch Messen der Verluste während der Trainingsphase sowie Analyse der trainierten Modelle, um Anzeichen eines Poisoning-Angriffs zu erkennen, indem das Modellverhalten bei bestimmten Testeingaben analysiert wird.
11. Überwachung und Alarmierung, wenn die Anzahl der verzerrten Antworten einen Schwellenwert überschreitet.
12. Menschliche Kontrolle bei der Überprüfung von Antworten und Audits.
13. Implementierung dedizierter LLMs, um unerwünschte Auswirkungen zu messen und andere LLMs mit Reinforcement Learning Techniken zu trainieren (Ref.18).
14. Durchführung von LLM-basierten Red-Team-Übungen (Ref.19) oder LLM-Schwachstellenanalysen (Ref.20) in den Testphasen des LLM-Lebenszyklus.

### Beispiele für Angriffsszenarien

1. Die generative KI-Prompt-Ausgabe des LLM kann die Benutzer der Anwendung irreführen, was zu Bias (voreingenommenen Meinungen), Schlussfolgerungen oder, schlimmer noch, zu Hassverbrechen usw. führen kann.
2. Wenn die Trainingsdaten nicht ordnungsgemäß gefiltert und/oder bereinigt werden, kann eine böswillige Person versuchen, toxische Daten in das Modell einzuspeisen, damit es sich an die voreingenommenen und falschen Daten anpasst.
3. Böswillige Akteure oder Wettbewerber erstellen absichtlich ungenaue oder schädliche Dokumente, die auf die Trainingsdaten eines Modells abzielen, das gleichzeitig auf der Grundlage von Eingaben trainiert wird. Das Opfermodell trainiert mit diesen gefälschten Informationen, die sich in den Ausgaben generativer KI-Aufforderungen an seine Verbraucher widerspiegeln.
4. Die Schwachstelle Prompt Injection (Ref.21) könnte ein Angriffsvektor für diese Schwachstelle sein, wenn unzureichende Sanierung und Filterung durchgeführt werden, wenn Eingaben von LLM-Anwendungskunden zum Trainieren des Modells verwendet werden. D.h., wenn bösartige oder gefälschte Daten als Teil einer Prompt-Injektionstechnik in das Modell eingegeben werden, könnte dies inhärent in die Modeldaten übertragen werden.

### Referenzen

1. [Stanford Research Paper:CS324](https://stanford-cs324.github.io/winter2022/lectures/data/): **Stanford Research**
2. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
3. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
6. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
7. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper**
8. [FedMLSecurity:arXiv:2306.04959](https://arxiv.org/abs/2306.04959): **Arxiv White Paper**
9. [The poisoning of ChatGPT](https://softwarecrisis.dev/letters/the-poisoning-of-chatgpt/): **Software Crisis Blog**
10. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **YouTube Video**
11. [OWASP CycloneDX v1.5](https://cyclonedx.org/capabilities/mlbom/): **OWASP CycloneDX**
12. [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg)
13. [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg)
14. [The Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/)
15. [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)
16. [Data Version Control](https://dvc.org/doc/user-guide/analytics)
17. [Autopoison](https://github.com/azshue/AutoPoison)
18. [Reinforcement Learning Techniken](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy)
19. [Red Team Exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned)
20. [LLM Vulnerability Scans](https://github.com/leondz/garak)
21. [Prompt Injection](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/PromptInjection.md)