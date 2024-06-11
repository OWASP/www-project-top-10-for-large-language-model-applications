## LLM05: Schwachstellen in der Lieferkette

### Beschreibung

Die LLM-Lieferkette kann Schwachstellen aufweisen, die die Integrität von Trainingsdaten, ML-Modellen und Anwendungsplattformen beeinträchtigen. Diese Schwachstellen können zu verzerrten Ergebnissen, Sicherheitsverletzungen oder sogar zu kompletten Systemausfällen führen. Traditionell konzentrieren sich Schwachstellen auf Softwarekomponenten, doch beim maschinellen Lernen kommt hinzu, dass vortrainierte Modelle und Trainingsdaten, die von Dritten bereitgestellt werden, anfällig für Manipulationen und Schadangriffe sind.

Schließlich können LLM-Plug-in-Erweiterungen ihre eigenen Schwachstellen mitbringen. Diese werden in LLM07 - Unsicheres Plug-in-Design (Ref.11) beschrieben, das das Schreiben von LLM-Plug-ins abdeckt und nützliche Informationen zur Bewertung von Plug-ins von Drittanbietern liefert.

### Gängige Beispiele für Schwachstellen

1. Traditionelle Schwachstellen in Paketen von Drittanbietern, einschließlich veralteter oder nicht mehr unterstützter Komponenten.
2. Verwendung eines anfälligen, vortrainierten Modells für das Fine-Tuning.
3. Verwendung vergifteter Crowd-Sourced-Daten für das Training.
4. Verwendung veralteter oder nicht mehr unterstützter Modelle, die nicht mehr gewartet werden und zu Sicherheitsproblemen führen.
5. Unklare AGB und Datenschutzrichtlinien der Modellbetreiber führen dazu, dass sensible Daten der Anwendung für das Modelltraining verwendet und anschließend sensible Informationen preisgegeben werden. Dies kann auch für Risiken gelten, die sich aus der Verwendung von urheberrechtlich geschütztem Material durch den Modellanbieter ergeben.

### Präventions- und Mitigationsstrategien

1. Prüfen Sie Datenquellen und -anbieter sorgfältig, einschließlich der allgemeinen Geschäftsbedingungen und Datenschutzrichtlinien; verwenden Sie nur vertrauenswürdige Anbieter. Stellen Sie sicher, dass ein angemessenes und unabhängig verifiziertes Sicherheitsniveau vorhanden ist und dass die Richtlinien des Modellanbieters mit Ihren Datenschutzrichtlinien übereinstimmen, d. h. dass Ihre Daten nicht für das Training Ihrer Modelle verwendet werden.
2. Verwenden Sie nur seriöse Plug-ins und stellen Sie sicher, dass diese für Ihre Anwendungsanforderungen getestet wurden. LLM07 Unsicheres Plug-in-Design bietet Informationen über die LLM-Aspekte eines unsicheren Plug-in-Designs, gegen die Sie testen sollten, um die Risiken bei der Verwendung von Plug-ins Dritter zu minimieren.
3. Verständnis und Anwendung der in den OWASP Top 10 A06:2021 - Vulnerable and Outdated Components (Ref.12) identifizierten Abhilfemaßnahmen. Dies beinhaltet das Scannen, Verwalten und Patchen von Komponenten. Für Entwicklungsumgebungen mit Zugriff auf sensible Daten sollten diese Kontrollen auch in diesen Umgebungen angewendet werden.
4. Führen Sie ein aktuelles Inventar der Komponenten mit einer Software-Bill-of-Materials (SBOM), um sicherzustellen, dass Sie über ein aktuelles, genaues und signiertes Inventar verfügen, das Manipulationen an bereitgestellten Paketen verhindert. SBOMs können verwendet werden, um neue Zero-Day-Schwachstellen schnell zu identifizieren und zu melden.
5. Zum Zeitpunkt der Erstellung dieses Dokuments decken die SBOMs keine Modelle, deren Artefakte und Datensätze ab. Wenn Ihre LLM-Anwendung ein proprietäres Modell verwendet, sollten Sie bewährte MLOps-Praktiken und -Plattformen verwenden, die sichere Model-Repositorys mit Daten-, Modell- und Experimentverfolgung bieten.
6. Sie sollten auch Modell- und Codesignaturen verwenden, wenn Sie externe Modelle und Anbieter verwenden. 
7. Die Erkennung von Anomalien und Robustheitstests gegen die bereitgestellten Modelle und Daten können helfen, Manipulationen und Vergiftungen aufzudecken, wie in Poisoning von Trainingsdaten (Ref.13) erörtert. Idealerweise sollte dies Teil der MLOps-Pipelines sein, obwohl es sich hierbei um neue Techniken handelt, die möglicherweise leichter im Rahmen von Red-Teaming-Übungen implementiert werden können.
8. Implementieren Sie eine ausreichende Überwachung, um das Scannen von Komponenten und Umgebungen auf Schwachstellen, die Verwendung nicht autorisierter Plug-ins und veraltete Komponenten, einschließlich des Modells und seiner Artefakte, abzudecken.
9. Implementieren Sie eine Patch-Richtlinie, um anfällige oder veraltete Komponenten zu entschärfen. Stellen Sie sicher, dass die Anwendung eine gepflegte Version der APIs und des zugrundeliegenden Modells verwendet.
10. Überprüfen Sie regelmäßig die Sicherheit und den Zugang des Anbieters und stellen Sie sicher, dass es keine Änderungen an der Sicherheitslage oder den Nutzungsbedingungen gibt.

### Beispiele für Angriffsszenarien

1. Angreifende verwenden eine verwundbare Python-Bibliothek, um ein System zu kompromittieren. Dies geschah beim ersten OpenAI-Datenleck.
2. Angreifende bieten ein LLM-Plug-in für die Flugsuche an, das gefälschte Links generiert, die Benutzer auf betrügerische Websites leiten.
3. Angreifende nutzen die PyPi-Paket-Registry aus, um Modellentwickler dazu zu bringen, ein kompromittiertes Paket herunterzuladen und Daten zu exfiltrieren oder Privilegien in einer Modellentwicklungsumgebung zu eskalieren. Dies war ein echter Angriff.
4. Angreifende vergiften ein öffentlich verfügbares, vortrainiertes Modell, das auf Wirtschaftsanalyse und Sozialforschung spezialisiert ist, um eine Hintertür zu schaffen, die Falschinformationen und Fake News generiert. Sie stellen das Modell auf einem Marktplatz für Modelle (z. B. Hugging Face) zur Verfügung, damit die Opfer es verwenden.
5. Angreifende vergiften öffentlich verfügbare Datensätze, um eine Hintertür beim Fine-Tuning von Modellen zu schaffen. Die Hintertür begünstigt auf subtile Weise bestimmte Unternehmen in verschiedenen Märkten. 
6. Eine kompromittierte Person eines Lieferanten (Outsourcing-Entwickler, Hosting-Unternehmen usw.) exfiltriert Daten, Modell oder Code und stiehlt geistiges Eigentum.
7. Ein LLM-Betreiber ändert seine AGB und Datenschutzbestimmungen dahin gehend, dass eine ausdrückliche Ablehnung der Verwendung von Anwendungsdaten für das Modelltraining erforderlich ist, was zur Speicherung sensibler Daten führt.

### Referenzen

1. [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): **Security Week**
2. [Plugin review process](https://platform.openai.com/docs/plugins/review): **OpenAI**
3. [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): **Pytorch**
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Army looking at the possibility of 'AI BOMs](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/): **Defense Scoop**
6. [Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): **Microsoft**
7. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/): **MITRE ATLAS**
8. [Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples](https://arxiv.org/pdf/1605.07277.pdf): **Arxiv White Paper**
9. [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733): **Arxiv White Paper**
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): **MITRE ATLAS**
11. [LLM07 - Insecure Plugin Design](InsecurePluginDesign.md)
12. [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)
13. [Training Data Poisoning](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/Training_Data_Poisoning.md)