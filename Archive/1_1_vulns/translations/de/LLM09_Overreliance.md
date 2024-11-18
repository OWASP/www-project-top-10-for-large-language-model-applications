## LLM09: Übermäßige Abhängigkeit

### Beschreibung

Übermäßige Abhängigkeit kann entstehen, wenn ein LLM fehlerhafte Informationen produziert und diese als authentisch darstellt. Während LLMs kreative und informative Inhalte produzieren können, können sie auch Inhalte produzieren, die faktisch falsch, unangemessen oder unsicher sind. Dies wird als Halluzination oder Konfabulation bezeichnet. Wenn Menschen oder Systeme diesen Informationen ohne Überprüfung oder Bestätigung vertrauen, kann dies zu Sicherheitsverletzungen, Fehlinformationen, falscher Kommunikation, rechtlichen Problemen und Rufschädigung führen.

Von LLM erzeugter Quellcode kann unbemerkt Sicherheitslücken einführen. Dies stellt ein erhebliches Risiko für die Betriebs- und Anwendungssicherheit dar. Diese Risiken unterstreichen die Bedeutung strenger Verifikationsprozesse:

* Überprüfung
* kontinuierliche Validierungsmechanismen
* Haftungsausschlüsse für Risiken

### Gängige Beispiele für Schwachstellen

1. Ein LLM antwortet mit ungenauen Informationen auf eine Art und Weise, die es höchst vertrauenswürdig wirken lässt. Das Gesamtsystem ist ohne angemessene Kontrollen und Überprüfungen konzipiert, und die Informationen führen Personen in einer Weise in die Irre, die zu Schäden führen kann.
2. Das LLM schlägt unsicheren oder fehlerhaften Code vor, der zu Schwachstellen führt, wenn er ohne angemessene Aufsicht oder Überprüfung in ein Softwaresystem eingebaut wird.

### Präventions- und Mitigationsstrategien

1. Überwachen und überprüfen Sie regelmäßig die Ergebnisse des LLMs. Verwenden Sie Selbstkonsistenz- oder Voting-Techniken, um inkonsistenten Text herauszufiltern. Der Vergleich mehrerer Modellantworten auf eine Anfrage kann helfen, die Qualität und Konsistenz der Ausgabe zu beurteilen.
2. Überprüfen Sie die LLM-Ausgabe mit vertrauenswürdigen externen Quellen. Diese zusätzliche Ebene der Validierung kann dazu beitragen, dass die vom Modell gelieferten Informationen genau und zuverlässig sind.
3. Verbessern Sie das Modell durch Fine-Tuning oder Embeddings, um die Ausgabequalität zu verbessern. Allgemeine, vortrainierte Modelle liefern mit größerer Wahrscheinlichkeit ungenaue Informationen als Modelle, die in einem bestimmten Bereich angepasst wurden. Techniken wie Prompt Engineering, parameter efficient tuning (PET), vollständiges Model-Tuning und Chain-of-Thought-Prompting können zu diesem Zweck eingesetzt werden.
4. Implementieren Sie automatische Validierungsmechanismen, die die generierte Ausgabe mit bekannten Fakten oder Daten vergleichen können. Dies kann eine zusätzliche Sicherheitsebene bieten und das Risiko von Halluzinationen verringern.
5. Zerlegen Sie komplexe Aufgaben in handhabbare Unteraufgaben und weisen Sie sie verschiedenen Agenten zu. Dies hilft nicht nur bei der Bewältigung der Komplexität, sondern verringert auch die Wahrscheinlichkeit von Halluzinationen, da jeder Agent für eine kleinere Aufgabe verantwortlich gemacht werden kann.
6. Kommunizieren Sie klar die Risiken und Einschränkungen, die mit der Verwendung von LLMs verbunden sind. Dies schließt das Potenzial für Informationsungenauigkeiten und andere Risiken ein. Eine effektive Risikokommunikation kann die Nutzenden auf mögliche Probleme vorbereiten und ihnen helfen, informierte Entscheidungen zu treffen. 
7. Entwickeln Sie APIs und Benutzeroberflächen, die eine verantwortungsvolle und sichere Nutzung von LLMs fördern. Dies kann Maßnahmen wie Inhaltsfilter, Benutzerwarnungen vor potenziellen Ungenauigkeiten und eine klare Kennzeichnung von KI-generierten Inhalten umfassen.
8. Bei der Verwendung von LLMs in Entwicklungsumgebungen sollten sichere Programmierpraktiken und -richtlinien festgelegt werden, um die Integration potenzieller Schwachstellen zu verhindern.

### Beispiele für Angriffsszenarien

1. Eine Nachrichtenorganisation nutzt ein LLM intensiv, um Nachrichtenartikel zu generieren. Ein böswilliger Akteur nutzt diese übermäßige Abhängigkeit aus, indem er das LLM mit irreführenden Informationen füttert und so die Verbreitung von Fehlinformationen verursacht.
2. Die KI plagiiert unbeabsichtigt Inhalte, was zu Urheberrechtsproblemen und einem Vertrauensverlust in die Organisation führt.
3. Ein Softwareentwicklungsteam verwendet ein LLM-System, um den Entwicklungsprozess zu beschleunigen. Die übermäßige Abhängigkeit von den Vorschlägen der KI führt zu Sicherheitslücken in der Anwendung aufgrund unsicherer Standardeinstellungen oder Empfehlungen, die nicht sicheren Programmierpraktiken entsprechen.
4. Eine Softwareentwicklungsfirma verwendet ein LLM, um Entwickelnde zu unterstützen. Das LLM schlägt eine nicht existierende Codebibliothek oder ein nicht existierendes Paket vor, und eine Person, die der KI vertraut, integriert unwissentlich ein schädliches Paket in die Software des Unternehmens. Dies unterstreicht die Bedeutung der Überprüfung von LLM-Vorschlägen, insbesondere wenn es sich um Code oder Bibliotheken von Drittanbietern handelt.

### Referenzen

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk): **Vulcan.io**
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**