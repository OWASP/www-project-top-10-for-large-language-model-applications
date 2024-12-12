## LLM10:2025 Unbegrenzter Verbrauch

### Beschreibung

Unbegrenzter Verbrauch bezieht sich auf den Prozess, bei dem ein Large Language Model (LLM) basierend auf Eingabeabfragen oder -aufforderungen Ausgaben generiert. Die Inferenz ist eine entscheidende Funktion von LLMs, bei der erlernte Muster und Kenntnisse angewendet werden, um relevante Antworten oder Vorhersagen zu erstellen.

Angriffe, die darauf abzielen, den Dienst zu stören, die finanziellen Ressourcen des Ziels zu erschöpfen oder sogar geistiges Eigentum zu stehlen, indem das Verhalten eines Modells geklont wird, sind alle auf eine gemeinsame Klasse von Sicherheitslücken angewiesen, um erfolgreich zu sein. Unbegrenzter Verbrauch tritt auf, wenn eine Large Language Model (LLM)-Anwendung es Benutzern ermöglicht, übermäßige und unkontrollierte Schlussfolgerungen zu ziehen, was zu Risiken wie Denial-of-Service (DoS), wirtschaftlichen Verlusten, Modelldiebstahl und Dienstverschlechterung führt. Die hohen Rechenanforderungen von LLMs, insbesondere in Cloud-Umgebungen, machen sie anfällig für Ressourcenausbeutung und unbefugte Nutzung.

### Gängige Beispiele für Schwachstellen

#### 1. Flood-Angriffe mit variabler Länge
  Angreifer können das LLM mit zahlreichen Eingaben unterschiedlicher Länge überlasten und dabei Ineffizienzen bei der Verarbeitung ausnutzen. Dies kann zu einer Erschöpfung der Ressourcen führen und das System möglicherweise unbrauchbar machen, was sich erheblich auf die Verfügbarkeit der Dienste auswirkt.
#### 2. Denial of Wallet (DoW)
  Durch die Initiierung einer hohen Anzahl von Vorgängen nutzen Angreifer das Kosten-pro-Nutzung-Modell von cloudbasierten KI-Diensten aus, was zu untragbaren finanziellen Belastungen für den Anbieter führt und den finanziellen Ruin riskiert.
#### 3. Kontinuierlicher Input-Überlauf
  Das kontinuierliche Senden von Inputs, die das Kontextfenster des LLM überschreiten, kann zu einer übermäßigen Nutzung der Rechenressourcen führen, was zu einer Verschlechterung des Dienstes und Betriebsstörungen führt.
#### 4. Ressourcenintensive Abfragen
  Das Senden ungewöhnlich anspruchsvoller Abfragen, die komplexe Sequenzen oder komplizierte Sprachmuster enthalten, kann Systemressourcen erschöpfen und zu längeren Verarbeitungszeiten und potenziellen Systemausfällen führen.
#### 5. Modelextraktion über API
  Angreifer können die Modell-API mithilfe sorgfältig gestalteter Eingaben und Techniken zur Eingabeaufforderung abfragen, um genügend Ausgaben zu sammeln, um ein Teilmodell zu replizieren oder ein Schattenmodell zu erstellen. Dies birgt nicht nur das Risiko des Diebstahls geistigen Eigentums, sondern untergräbt auch die Integrität des Originalmodells.
#### 6. Replikation von Funktionsmodellen
  Die Verwendung des Zielmodells zur Generierung synthetischer Trainingsdaten kann es Angreifern ermöglichen, ein anderes grundlegendes Modell zu optimieren und ein funktionales Äquivalent zu erstellen. Dadurch werden herkömmliche abfragebasierte Extraktionsmethoden umgangen, was ein erhebliches Risiko für proprietäre Modelle und Technologien darstellt.
#### 7. Seitenkanalangriffe
  Böswillige Angreifer können die Eingabefilterungstechniken des LLM ausnutzen, um Seitenkanalangriffe auszuführen und Modellgewichte und Architekturinformationen zu sammeln. Dies könnte die Sicherheit des Modells gefährden und zu weiterer Ausbeutung führen.

### Präventions- und Mitigationsstrategien

#### 1. Eingabevalidierung
  Implementiere eine strenge Eingabevalidierung, um sicherzustellen, dass die Eingaben angemessene Größenbeschränkungen nicht überschreiten.
#### 2. Begrenzung der Offenlegung von Logits und Logprobs
  Schränke die Offenlegung von `logit_bias` und `logprobs` in API-Antworten ein oder verschleiere sie. Stelle nur die erforderlichen Informationen bereit, ohne detaillierte Wahrscheinlichkeiten offenzulegen.
#### 3. Ratenbegrenzung
  Wende Ratenbegrenzung und Benutzerkontingente an, um die Anzahl der Anfragen zu beschränken, die eine einzelne Quellentität in einem bestimmten Zeitraum stellen kann.
#### 4. Verwaltung der Ressourcenzuweisung
  Überwache und verwalte die Ressourcenzuweisung dynamisch, um zu verhindern, dass ein einzelner Benutzer oder eine einzelne Anfrage übermäßige Ressourcen verbraucht.
#### 5. Timeouts und Drosselung
  Richte Timeouts ein und drossele die Verarbeitung für ressourcenintensive Vorgänge, um einen längeren Ressourcenverbrauch zu verhindern.
#### 6. Sandbox-Techniken
  Beschränke den Zugriff des LLM auf Netzwerkressourcen, interne Dienste und APIs.
  - Dies ist besonders wichtig für alle gängigen Szenarien, da es Insider-Risiken und -Bedrohungen umfasst. Darüber hinaus regelt es den Umfang des Zugriffs der LLM-Anwendung auf Daten und Ressourcen und dient somit als entscheidender Kontrollmechanismus zur Minderung oder Verhinderung von Seitenkanalangriffen.
#### 7. Umfassende Protokollierung, Überwachung und Erkennung von Anomalien
  Kontinuierliche Überwachung der Ressourcennutzung und Implementierung von Protokollierung, um ungewöhnliche Muster des Ressourcenverbrauchs zu erkennen und darauf zu reagieren.
#### 8. Wasserzeichen
  Implementierung von Wasserzeichen-Frameworks zur Einbettung und Erkennung der unbefugten Nutzung von LLM-Ausgaben.
#### 9. Graceful Degradation
  Entwurf eines Systems, das bei hoher Last eine sanfte Verschlechterung erfährt und dabei eine Teilfunktionalität beibehält, anstatt vollständig auszufallen.
#### 10. Begrenzung von Warteschlangenaktionen und robuste Skalierung
  Implementierung von Beschränkungen für die Anzahl der in der Warteschlange befindlichen Aktionen und der Gesamtaktionen unter Einbeziehung dynamischer Skalierung und Lastverteilung, um unterschiedliche Anforderungen zu bewältigen und eine konsistente Systemleistung sicherzustellen.
#### 11. Training der Robustheit gegenüber Angriffen
  Trainiere Modelle, um feindliche Abfragen und Extraktionsversuche zu erkennen und zu entschärfen.
#### 12. Glitch-Token-Filterung
  Erstelle Listen bekannter Glitch-Token und scanne die Ausgabe, bevor du sie dem Kontextfenster des Modells hinzufügst.
#### 13. Zugriffskontrollen
  Implementiere starke Zugriffskontrollen, einschließlich rollenbasierter Zugriffskontrolle (RBAC) und dem Prinzip der geringsten Privilegien, um den unbefugten Zugriff auf LLM-Modell-Repositorys und Trainingsumgebungen zu beschränken.
#### 14. Zentralisiertes ML-Modell-Inventar
  Verwende ein zentralisiertes ML-Modell-Inventar oder -Register für Modelle, die in der Produktion verwendet werden, um eine ordnungsgemäße Steuerung und Zugriffskontrolle zu gewährleisten.
#### 15. Automatisierte MLOps-Bereitstellung
  Implementiere eine automatisierte MLOps-Bereitstellung mit Governance-, Nachverfolgungs- und Genehmigungs-Workflows, um die Zugriffs- und Bereitstellungskontrollen innerhalb der Infrastruktur zu verschärfen.

### Beispiele für Angriffsszenarien

#### Szenario #1: Unkontrollierte Eingabegröße
  Ein Angreifer übermittelt eine ungewöhnlich große Eingabe an eine LLM-Anwendung, die Textdaten verarbeitet, was zu einer übermäßigen Speichernutzung und CPU-Auslastung führt, wodurch das System möglicherweise abstürzt oder der Dienst erheblich verlangsamt wird.
#### Szenario #2: Wiederholte Anfragen
  Ein Angreifer übermittelt eine große Anzahl von Anfragen an die LLM-API, was zu einem übermäßigen Verbrauch von Rechenressourcen führt und den Dienst für legitime Benutzer unzugänglich macht.
#### Szenario #3: Ressourcenintensive Abfragen
  Ein Angreifer erstellt spezifische Eingaben, die darauf ausgelegt sind, die rechenintensivsten Prozesse des LLM auszulösen, was zu einer längeren CPU-Auslastung und einem möglichen Systemausfall führt.
#### Szenario #4: Denial of Wallet (DoW)
  Ein Angreifer generiert übermäßige Vorgänge, um das Pay-per-Use-Modell von cloudbasierten KI-Diensten auszunutzen, was zu untragbaren Kosten für den Dienstanbieter führt.
#### Szenario #5: Replikation des Funktionsmodells
  Ein Angreifer verwendet die API des LLM, um synthetische Trainingsdaten zu generieren und ein anderes Modell zu optimieren, wodurch ein funktionales Äquivalent geschaffen und die herkömmlichen Einschränkungen bei der Modelextraktion umgangen werden.
#### Szenario #6: Umgehung der Systemeingangsfilterung
  Ein böswilliger Angreifer umgeht Eingangsfiltertechniken und Präambeln des LLM, um einen Seitenkanalangriff durchzuführen und Modellinformationen an eine ferngesteuerte Ressource unter seiner Kontrolle abzurufen.

### Referenzlinks

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt findest du umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**