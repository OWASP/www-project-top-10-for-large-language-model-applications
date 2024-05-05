## LLM05: Schwachstellen in der Lieferkette

### Beschreibung

Die Lieferkette in LLMs kann anfällig sein und die Integrität von Trainingsdaten, ML-Modellen und Einsatzplattformen beeinträchtigen. Diese Schwachstellen können zu voreingenommenen Ergebnissen, Sicherheitsverletzungen oder sogar zu kompletten Systemausfällen führen. Traditionell konzentrieren sich Schwachstellen auf Softwarekomponenten, aber maschinelles Lernen erweitert dies mit vortrainierten Modellen und Trainingsdaten, die von Drittanbietern bereitgestellt werden und anfällig für Manipulations- und Poisoning-Angriffe sind.

Schließlich können LLM-Plugin-Erweiterungen ihre eigenen Schwachstellen mitbringen. Diese werden in [LLM07 - Unsicheres Plugin-Design](InsecurePluginDesign.md) beschrieben, das das Schreiben von LLM-Plugins abdeckt und hilfreiche Informationen zur Bewertung von Plugins Dritter bereitstellt.

### Häufige Beispiele für Schwachstellen

1. Traditionelle Schwachstellen in Paketen Dritter, einschließlich veralteter oder nicht mehr unterstützter Komponenten.
2. Verwendung eines anfälligen vortrainierten Modells zum Feintuning.
3. Verwendung von vergifteten crowd-sourced Daten zum Training.
4. Verwendung veralteter oder nicht mehr unterstützter Modelle, die nicht mehr gewartet werden, führt zu Sicherheitsproblemen.
5. Unklare AGBs und Datenschutzrichtlinien der Modellbetreiber führen dazu, dass sensible Daten der Anwendung für das Modelltraining verwendet werden und anschließend sensible Informationen preisgegeben werden. Dies kann auch für Risiken gelten, die sich aus der Verwendung von urheberrechtlich geschütztem Material durch den Modellanbieter ergeben.

### Strategien zur Prävention und Mitigation

1. Datenquellen und Lieferanten sorgfältig prüfen, einschließlich AGBs und deren Datenschutzrichtlinien, nur vertrauenswürdige Lieferanten verwenden. Sicherstellen, dass angemessene und unabhängig geprüfte Sicherheit vorhanden ist und dass die Richtlinien des Modellbetreibers mit Ihren Datenschutzrichtlinien übereinstimmen, d.h. Ihre Daten werden nicht für das Training ihrer Modelle verwendet; ebenso Zusicherungen und rechtliche Milderungen gegen die Verwendung urheberrechtlich geschützter Materialien von Modellbetreuern suchen.
2. Nur seriöse Plugins verwenden und sicherstellen, dass sie für Ihre Anwendungsanforderungen getestet wurden. LLM-Unsicheres Plugin-Design bietet Informationen zu den LLM-Aspekten des unsicheren Plugin-Designs, gegen die Sie testen sollten, um Risiken durch die Verwendung von Plugins Dritter zu mindern.
3. Verstehen und anwenden der Mitigierungssmaßnahmen, die in den OWASP Top Ten's [A06:2021 – Anfällige und veraltete Komponenten](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) gefunden wurden. Dies umfasst das Scannen, Verwalten und Patchen von Komponenten. Für Entwicklungsumgebungen mit Zugang zu sensiblen Daten sollten diese Kontrollen auch in diesen Umgebungen angewendet werden.
4. Ein aktuelles Inventar von Komponenten mit einer Software-Bill-of-Materials (SBOM) pflegen, um sicherzustellen, dass Sie ein aktuelles, präzises und signiertes Inventar haben, das Manipulationen an bereitgestellten Paketen verhindert. SBOMs können verwendet werden, um schnell neue, Zero-Day-Schwachstellen zu erkennen und zu melden.
5. Zum Zeitpunkt des Schreibens decken SBOMs keine Modelle, ihre Artefakte und Datensätze ab. Wenn Ihre LLM-Anwendung ihr eigenes Modell verwendet, sollten Sie MLOps-Best Practices und Plattformen verwenden, die sichere Modellrepositories mit Daten-, Modell- und Experiment-Tracking bieten.
6. Sie sollten auch Modell- und Code-Signierung verwenden, wenn Sie externe Modelle und Lieferanten verwenden.
7. Anomalieerkennung und Tests auf adversarielle Robustheit bei bereitgestellten Modellen und Daten können helfen, Manipulationen und Vergiftungen zu erkennen, wie in [Trainingsdaten-Vergiftung](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/Training_Data_Poisoning.md) besprochen; idealerweise sollte dies Teil von MLOps-Pipelines sein; jedoch sind dies aufkommende Techniken und können möglicherweise einfacher als Teil von Red-Teaming-Übungen implementiert werden.
8. Ausreichendes Monitoring implementieren, um das Scannen von Komponenten und Umgebungsschwachstellen, die Verwendung nicht autorisierter Plugins und veralteter Komponenten, einschließlich des Modells und seiner Artefakte, abzudecken.
9. Eine Patching-Richtlinie implementieren, um anfällige oder veraltete Komponenten zu mildern. Sicherstellen, dass die Anwendung auf eine gepflegte Version von APIs und dem zugrunde liegenden Modell angewiesen ist.
10. Sicherheit und Zugangskontrollen der Lieferanten regelmäßig überprüfen und auditieren, um sicherzustellen, dass es keine Änderungen in ihrer Sicherheitslage oder AGBs gibt.

### Beispiel-Angriffsszenarien

1. Ein Angreifer nutzt eine anfällige Python-Bibliothek, um ein System zu kompromittieren. Dies geschah beim ersten Datenleck von OpenAI.
2. Ein Angreifer bietet ein LLM-Plugin zur Flugsuche an, das gefälschte Links generiert, die Benutzer zu Scams dirigieren.
3. Ein Angreifer nutzt das PyPi-Paketregister aus, um Modellentwickler dazu zu bringen, ein kompromittiertes Paket herunterzuladen und Daten zu exfiltrieren oder Privilegien in einer Modellentwicklungsumgebung zu eskalieren. Dies war ein tatsächlicher Angriff.
4. Ein Angreifer vergiftet ein öffentlich verfügbares vortrainiertes Modell, das auf Wirtschaftsanalyse und Sozialforschung spezialisiert ist, um eine Hintertür zu schaffen, die Falschinformationen und Fake News generiert. Sie stellen es auf einem Modellmarktplatz (z.B. Hugging Face) zur Verfügung, damit Opfer es verwenden.
5. Ein Angreifer vergiftet öffentlich verfügbare Datensätze, um beim Feintuning von Modellen eine Hintertür zu schaffen. Die Hintertür bevorzugt subtil bestimmte Unternehmen in verschiedenen Märkten.
6. Ein kompromittierter Mitarbeiter eines Lieferanten (Outsourcing-Entwickler, Hosting-Unternehmen usw.) exfiltriert Daten, Modell oder Code und stiehlt geistiges Eigentum.
7. Ein LLM-Betreiber ändert seine AGBs und Datenschutzrichtlinie, um ein explizites Opt-out aus der Verwendung von Anwendungsdaten für das Modelltraining zu verlangen, was zur Speicherung sensibler Daten führt.

### Referenzlinks

1. [ChatGPT-Datenleck bestätigt, da Sicherheitsfirma vor anfälliger Komponentenausnutzung warnt](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): **Security Week**
2. [Plugin-Überprüfungsprozess](https://platform.openai.com/docs/plugins/review) **OpenAI**
3. [Kompromittierte PyTorch-nightly-Abhängigkeitskette](https://pytorch.org/blog/compromised-nightly-dependency/): **Pytorch**
4. [PoisonGPT: Wie wir ein lobotomisiertes LLM auf Hugging Face versteckt haben, um Fake News zu verbreiten](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Army erwägt die Möglichkeit von 'AI BOMs](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/): **Defense Scoop**
6. [Fehlermodi im Maschinellen Lernen](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): **Microsoft**
7. [ML-Lieferkettenkompromiss](https://atlas.mitre.org/techniques/AML.T0010/): **MITRE ATLAS**
8. [Transferierbarkeit im Maschinellen Lernen: von Phänomenen zu Black-Box-Angriffen mit adversariellen Beispielen](https://arxiv.org/pdf/1605.07277.pdf): **Arxiv White Paper**
9. [BadNets: Identifizierung von Schwachstellen in der Lieferkette des Maschinellen Lernmodells](https://arxiv.org/abs/1708.06733): **Arxiv White Paper**
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): **MITRE ATLAS**
