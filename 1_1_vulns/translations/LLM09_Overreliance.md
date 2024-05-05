## LLM09: Übermäßiges Vertrauen

### Beschreibung

Übermäßiges Vertrauen kann auftreten, wenn ein LLM fehlerhafte Informationen produziert und diese auf als Authorität  bereitstellt. Während LLMs kreative und informative Inhalte erzeugen können, können sie auch Inhalte generieren, die faktisch falsch, unangemessen oder unsicher sind. Dies wird als Halluzination oder Konfabulation bezeichnet. Wenn Menschen oder Systeme diesen Informationen ohne Aufsicht oder Bestätigung vertrauen, kann dies zu einem Sicherheitsbruch, Fehlinformationen, Misskommunikation, rechtlichen Problemen und Rufschädigung führen.

Von LLM generierter Quellcode kann unbemerkte Sicherheitsanfälligkeiten einführen. Dies stellt ein erhebliches Risiko für die betriebliche Sicherheit und Sicherheit von Anwendungen dar. Diese Risiken zeigen die Bedeutung von strengen Überprüfungsprozessen, mit:

* Aufsicht
* Kontinuierlichen Validierungsmechanismen
* Haftungsausschlüssen bezüglich Risiken

### Häufige Beispiele für Anfälligkeiten

1. LLM liefert ungenaue Informationen als Antwort, während es so formuliert ist, als ob es sehr autoritär wäre. Das Gesamtsystem ist ohne angemessene Kontrollen und Gleichgewichte zur Handhabung dessen konzipiert, und die Informationen führen den Benutzer irreführend zu einem Schaden.
2. LLM schlägt unsicheren oder fehlerhaften Code vor, was zu Anfälligkeiten führt, wenn er ohne angemessene Aufsicht oder Überprüfung in ein Softwaresystem integriert wird.

### Präventions- und Minderungsstrategien

1. Überwachen und überprüfen Sie regelmäßig die Ausgaben des LLM. Verwenden Sie Selbstkonsistenz- oder Abstimmungstechniken, um inkonsistenten Text herauszufiltern. Das Vergleichen mehrerer Modellantworten auf eine einzelne Aufforderung kann eine bessere Beurteilung der Qualität und Konsistenz der Ausgabe ermöglichen.
2. Überprüfen Sie die Ausgaben des LLM mit vertrauenswürdigen externen Quellen. Diese zusätzliche Validierungsebene kann dabei helfen sicherzustellen, dass die vom Modell bereitgestellten Informationen genau und zuverlässig sind.
3. Verbessern Sie das Modell durch Feinabstimmung oder Einbettungen, um die Qualität der Ausgabe zu verbessern. Allgemeine vortrainierte Modelle produzieren im Vergleich zu abgestimmten Modellen in einem bestimmten Bereich wahrscheinlicher ungenaue Informationen. Techniken wie Prompt-Engineering, parameter-effizientes Tuning (PET), vollständiges Modelltuning und Chain-of-Thought-Prompting können für diesen Zweck eingesetzt werden.
4. Implementieren Sie automatische Validierungsmechanismen, die die generierte Ausgabe gegen bekannte Fakten oder Daten überprüfen können. Dies kann eine zusätzliche Sicherheitsebene bieten und die mit Halluzinationen verbundenen Risiken mindern.
5. Zerlegen Sie komplexe Aufgaben in handhabbare Unteraufgaben und weisen Sie sie verschiedenen Agenten zu. Dies hilft nicht nur bei der Bewältigung der Komplexität, sondern reduziert auch die Chancen auf Halluzinationen, da jeder Agent für eine kleinere Aufgabe verantwortlich gemacht werden kann.
6. Kommunizieren Sie klar die Risiken und Einschränkungen, die mit der Verwendung von LLMs verbunden sind. Dies beinhaltet das Potenzial für Informationsungenauigkeiten und andere Risiken. Eine effektive Risikokommunikation kann die Benutzer auf potenzielle Probleme vorbereiten und ihnen helfen, informierte Entscheidungen zu treffen.
7. Entwickeln Sie APIs und Benutzeroberflächen, die eine verantwortungsvolle und sichere Nutzung von LLMs fördern. Dies kann Maßnahmen wie Inhaltsfilter, Benutzerwarnungen vor potenziellen Ungenauigkeiten und eine klare Kennzeichnung von KI-generierten Inhalten umfassen.
8. Bei der Verwendung von LLMs in Entwicklungsumgebungen, etablieren Sie sichere Programmierpraktiken und Richtlinien, um die Integration möglicher Anfälligkeiten zu verhindern.

### Beispielangriffsszenarien

1. Eine Nachrichtenorganisation verwendet intensiv ein LLM, um Nachrichtenartikel zu generieren. Ein böswilliger Akteur nutzt diese übermäßige Abhängigkeit aus, indem er dem LLM irreführende Informationen füttert und so die Verbreitung von Fehlinformationen verursacht.
2. Die KI plagiiert unabsichtlich Inhalte, was zu Urheberrechtsproblemen und einem verringerten Vertrauen in die Organisation führt.
3. Ein Softwareentwicklungsteam nutzt ein LLM-System, um den Codierungsprozess zu beschleunigen. Die übermäßige Abhängigkeit von den Vorschlägen der KI führt aufgrund unsicherer Standardeinstellungen oder Empfehlungen, die nicht mit sicheren Programmierpraktiken übereinstimmen, zu Sicherheitsanfälligkeiten in der Anwendung.
4. Eine Softwareentwicklungsfirma verwendet ein LLM, um Entwickler zu unterstützen. Das LLM schlägt eine nicht existierende Code-Bibliothek oder ein Paket vor, und ein Entwickler, der der KI vertraut, integriert unwissentlich ein bösartiges Paket in die Software der Firma. Dies unterstreicht die Bedeutung der Überprüfung von LLM-Vorschlägen, insbesondere wenn es um Drittanbietercode oder -bibliotheken geht.

### Referenzlinks

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk): **Vulcan.io**
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
