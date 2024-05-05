## LLM03: Poisoning von Trainingsdaten

### Beschreibung

Der Ausgangspunkt jedes maschinellen Lernansatzes sind Trainingsdaten, einfach ausgedrückt "Rohdaten". Um hochgradig wirksam zu sein (z.B. sprachliches und Weltwissen zu besitzen), sollte dieser Text eine breite Palette von Domänen, Genres und Sprachen umfassen. Ein großes Sprachmodell (Large Language Model, LLM) verwendet tiefe neuronale Netzwerke, um Ausgaben zu generieren, die auf Mustern basieren, die aus den Trainingsdaten gelernt wurden.

Das Poisoning von Trainingsdaten bezieht sich auf die Manipulation von Pre-Training-Daten oder Daten, die innerhalb der Fine-Tuning- oder Embeddingprozesse verwendet werden, um Schwachstellen (die alle einzigartige und manchmal gemeinsame Angriffsvektoren haben), Hintertüren oder Biase einzuführen, die die Sicherheit, Effektivität oder ethisches Verhalten des Modells beeinträchtigen könnten. Vergiftete Informationen können den Nutzern präsentiert werden oder andere Risiken wie Leistungsverschlechterung, Ausnutzung von nachgelagerter Software und Reputationsschäden erzeugen. Selbst wenn Nutzer der problematischer KI-Ausgabe misstrauen, bleiben die Risiken bestehen, einschließlich beeinträchtigter Modellfähigkeiten und potenziellem Schaden für das Markenimage.

- Pre-Training-Daten beziehen sich auf den Prozess des Trainierens eines Modells basierend auf einer Aufgabe oder einem Datensatz.
- Fine-Tuning beinhaltet die Anpassung eines bereits trainierten Modells an ein engeres Thema oder ein spezifischeres Ziel, indem es mit einem kuratierten Datensatz trainiert wird. Dieser Datensatz umfasst typischerweise Beispiele für Eingaben und die entsprechenden gewünschten Ausgaben.
- Der Einbettungsprozess ist der Prozess der Umwandlung von kategorischen Daten (oft Text) in eine numerische Darstellung, die verwendet werden kann, um ein Sprachmodell zu trainieren. Der Einbettungsprozess beinhaltet die Darstellung von Wörtern oder Phrasen aus den Textdaten als Vektoren in einem kontinuierlichen Vektorraum. Die Vektoren werden typischerweise generiert, indem die Textdaten in ein neuronales Netzwerk eingespeist werden, das auf einem großen Textkorpus trainiert wurde.

Die Vergiftung von Daten wird als Integritätsangriff betrachtet, da die Manipulation der Trainingsdaten die Fähigkeit des Modells beeinflusst, korrekte Vorhersagen auszugeben. Natürlich bergen externe Datenquellen ein höheres Risiko, da die Modellersteller keine Kontrolle über die Daten haben oder ein hohes Vertrauensniveau, dass der Inhalt keine Voreingenommenheit, gefälschte Informationen oder unangemessenen Inhalt enthält.

### Häufige Beispiele für Schwachstellen

1. Ein bösartiger Akteur oder eine konkurrierende Marke erstellt absichtlich ungenaue oder bösartige Dokumente, die auf die Pre-Training-, Feinabstimmungsdaten oder Einbettungen eines Modells abzielen. Betrachte sowohl [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg) als auch [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg) Angriffsvektoren zur Veranschaulichung.
   1. Das Opfermodell trainiert unter Verwendung gefälschter Informationen, die in den Ausgaben generativer KI-Aufforderungen an seine Konsumenten reflektiert werden.
2. Ein bösartiger Akteur kann direkt gefälschte, voreingenommene oder schädliche Inhalte in die Trainingsprozesse eines Modells einspeisen, die in nachfolgenden Ausgaben zurückgegeben werden.
3. Ein ahnungsloser Nutzer injiziert indirekt sensible oder proprietäre Daten in die Trainingsprozesse eines Modells, die in nachfolgenden Ausgaben zurückgegeben werden.
4. Ein Modell wird mit Daten trainiert, deren Quelle, Ursprung oder Inhalt in keinem der Trainingsbeispiele verifiziert wurde, was zu fehlerhaften Ergebnissen führen kann, wenn die Daten verfälscht oder inkorrekt sind.
5. Unbeschränkter Infrastrukturzugang oder unzureichende Sandbox-Umgebungen können dazu führen, dass ein Modell unsichere Trainingsdaten aufnimmt, was zu voreingenommenen oder schädlichen Ausgaben führt. Dieses Beispiel ist auch in jedem der Trainingsbeispiele vorhanden.
   1. In diesem Szenario kann die Eingabe eines Nutzers in das Modell in der Ausgabe an einen anderen Nutzer reflektiert werden (was zu einem Datenleck führt), oder der Nutzer eines LLM kann Ausgaben vom Modell erhalten, die je nach Art der aufgenommenen Daten im Vergleich zum Anwendungsfall des Modells ungenau, irrelevant oder schädlich sein können (in der Regel mit einer Modellkarte reflektiert).

*Ob Entwickler, Kunde oder allgemeiner Konsument des LLM, es ist wichtig zu verstehen, welche Auswirkungen diese Schwachstelle auf mögliche Risiken innerhalb Ihrer LLM-Anwendung haben könnte, wenn sie mit einem nicht-eigenen LLM interagiert, um die Legitimität von Modellausgaben basierend auf dessen Trainingsverfahren zu verstehen. Ebenso könnten Entwickler des LLM sowohl direkten als auch indirekten Angriffen auf interne oder Drittanbieterdaten, die für die Feinabstimmung und Einbettung (am häufigsten) verwendet werden, ausgesetzt sein, was ein Risiko für alle seine Konsumenten darstellt*

### Präventions- und Minderungsstrategien

1. Überprüfen Sie die Lieferkette der Trainingsdaten, insbesondere wenn sie extern bezogen werden, sowie die Aufrechterhaltung von Bestätigungen über die "ML-BOM" (Machine Learning Bill of Materials)-Methodik sowie die Überprüfung von Modellkarten.
2. Überprüfen Sie die korrekte Legitimität der gezielten Datenquellen und der während der Pre-Training-, Feinabstimmungs- und Einbettungsphasen erhaltenen Daten.
3. Überprüfen Sie Ihren Anwendungsfall für das LLM und die Anwendung, in die es integriert wird. Erstellen Sie verschiedene Modelle über separate Trainingsdaten oder Feinabstimmungen für unterschiedliche Anwendungsfälle, um einen genaueren und granulareren generativen KI-Ausgang gemäß dessen definiertem Anwendungsfall zu erstellen.
4. Stellen Sie ausreichende Sandbox-Umgebungen durch Netzwerksteuerungen sicher, um zu verhindern, dass das Modell unbeabsichtigte Datenquellen abgreift, was den maschinellen Lernausgang beeinträchtigen könnte.
5. Verwenden Sie strenge Überprüfungs- oder Eingabefilter für spezifische Trainingsdaten oder Kategorien von Datenquellen, um die Menge an gefälschten Daten zu kontrollieren. Datensanierung, mit Techniken wie statistischer Ausreißererkennung und Anomalieerkennungsmethoden, um feindliche Daten aus dem Feinabstimmungsprozess zu erkennen und zu entfernen.
6. Stellen Sie detaillierte Kontrollfragen bezüglich der Quelle und des Eigentums von Datensätzen, um sicherzustellen, dass das Modell nicht vergiftet wurde, und übernehmen Sie diese Kultur in den "MLSecOps"-Zyklus. Beziehen Sie sich auf verfügbare Ressourcen wie [The Foundation Model Transparency Index](https://crfm.stanford.edu/fmti/) oder [Open LLM Leaderboard](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard) zum Beispiel.
7. Verwenden Sie DVC ([Data Version Control](https://dvc.org/doc/user-guide/analytics), um Teile eines Datensatzes, die manipuliert, gelöscht oder hinzugefügt wurden und zu Vergiftung geführt haben, genau zu identifizieren und zu verfolgen.
8. Verwenden Sie Vector Database, um benutzergenerierte Informationen hinzuzufügen, um vor Vergiftung anderer Nutzer zu schützen und sogar im laufenden Betrieb zu korrigieren, ohne ein neues Modell neu trainieren zu müssen.
9. Adversarielle Robustheitstechniken wie föderiertes Lernen und Einschränkungen, um den Effekt von Ausreißern oder adversarielles Training zu minimieren, um gegen die schlimmsten Störungen der Trainingsdaten widerstandsfähig zu sein.
   1. Ein "MLSecOps"-Ansatz könnte darin bestehen, adversarielle Robustheit in den Trainingslebenszyklus mit der Autovergiftungstechnik einzubeziehen.
   2. Ein Beispielrepository dafür wäre [Autopoison](https://github.com/azshue/AutoPoison) Testing, einschließlich Angriffe wie Inhaltsinjektionsangriffe ("Versuch, einen Markennamen in Modellantworten zu fördern") und Verweigerungsangriffe ("das Modell immer dazu bringen, sich zu weigern zu antworten"), die mit diesem Ansatz erreicht werden können.
10. Testen und Erkennen, indem der Verlust während der Trainingsphase gemessen und trainierte Modelle analysiert werden, um Anzeichen eines Vergiftungsangriffs zu erkennen, indem das Modellverhalten bei spezifischen Testeingaben analysiert wird.
    1. Überwachung und Alarmierung bei einer Anzahl von verzerrten Antworten, die einen Schwellenwert überschreiten.
    2. Verwendung einer menschlichen Schleife zur Überprüfung von Antworten und Auditing.
    3. Implementierung spezialisierter LLMs, um gegen unerwünschte Konsequenzen zu benchmarken und andere LLMs mit [Reinforcement Learning Techniken](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy) zu trainieren.
    4. Durchführung von LLM-basierten [Red Team Übungen](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) oder [LLM Schwachstellenscans](https://github.com/leondz/garak) in die Testphasen des LLM-Lebenszyklus.

### Beispiel-Angriffsszenarien

1. Die generative KI-Prompt-Ausgabe des LLM kann die Nutzer der Anwendung irreführen, was zu biasbehafteten Meinungen, Folgerungen oder noch schlimmer, Hassverbrechen usw. führen kann.
2. Wenn die Trainingsdaten nicht korrekt gefiltert und|oder bereinigt werden, kann ein bösartiger Nutzer der Anwendung versuchen, toxische Daten in das Modell einzuspeisen, damit es sich an die voreingenommenen und falschen Daten anpasst.
3. Ein bösartiger Akteur oder Konkurrent erstellt absichtlich ungenaue oder bösartige Dokumente, die auf die Trainingsdaten eines Modells abzielen, das gleichzeitig basierend auf Eingaben trainiert wird. Das Opfermodell trainiert unter Verwendung dieser gefälschten Informationen, die in den Ausgaben generativer KI-Aufforderungen an seine Konsumenten reflektiert werden.
4. Die Schwachstelle [Prompt Injection](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/PromptInjection.md) könnte ein Angriffsvektor für diese Schwachstelle sein, wenn unzureichende Sanierung und Filterung durchgeführt werden, wenn Eingaben von LLM-Anwendungskunden zum Trainieren des Modells verwendet werden. D.h., wenn bösartige oder gefälschte Daten als Teil einer Prompt-Injektionstechnik in das Modell eingegeben werden, könnte dies inhärent in die Modellaten übertragen werden.

### Referenz-Links

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