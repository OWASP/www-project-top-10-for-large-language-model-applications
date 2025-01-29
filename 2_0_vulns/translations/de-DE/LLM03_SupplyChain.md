## LLM03:2025 Lieferkette

### Beschreibung

LLM-Lieferketten sind anfällig für verschiedene Schwachstellen, die die Integrität von Trainingsdaten, Modellen und Bereitstellungsplattformen beeinträchtigen können. Diese Risiken können zu verzerrten Ergebnissen, Sicherheitslücken oder Systemausfällen führen. Während sich herkömmliche Software-Schwachstellen auf Probleme wie Code-Fehler und Abhängigkeiten konzentrieren, erstrecken sich die Risiken bei ML auch auf vortrainierte Modelle und Daten Dritter.

Diese externen Elemente können durch Manipulationen oder Poisoning-Angriffe verändert werden.

Die Erstellung von LLMs ist eine anspruchsvolle Aufgabe, die oft von Modellen Dritter abhängt. Das Aufkommen offen zugänglicher LLMs und neuer Fine-Tuning-Methoden wie „LoRA“ (Low-Rank Adaptation) und „PEFT“ (Parameter-Efficient Fine-Tuning), insbesondere auf Plattformen wie Hugging Face, bringen neue Risiken in die Lieferkette. Schließlich erhöht das Aufkommen von On-Device-LLMs die Angriffsfläche und die Supply-Chain-Risiken für LLM-Anwendungen.

Einige der hier diskutierten Risiken werden auch in „LLM04 Poisoning von Daten und Modellen“ behandelt. Dieser Text konzentriert sich auf den Supply-Chain-Aspekt der Risiken.
Ein einfaches Bedrohungsmodell finden Sie [hier](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Gängige Beispiele für Risiken

#### 1. Traditionelle Schwachstellen in Paketen von Drittanbietern
  Ein Beispiel sind veraltete Komponenten. Diese können von Angreifenden ausgenutzt werden, um LLM-Anwendungen zu kompromittieren. Dies ist ähnlich wie bei "A06:2021 - Vulnerable and Outdated Components", mit erhöhten Risiken, wenn Komponenten während der Modellentwicklung oder dem Fine-Tuning verwendet werden.
  (Ref. Link: [A06:2021 - Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Risiken bei der Lizenzierung
  Bei der Entwicklung von KI kommen oft verschiedene Software- und Datenlizenzen zum Einsatz, die Risiken bergen, wenn sie nicht richtig gehandhabt werden. Unterschiedliche Open-Source- und proprietäre Lizenzen bringen unterschiedliche rechtliche Anforderungen mit sich. Lizenzen für Datensätze können die Nutzung, den Vertrieb oder die Kommerzialisierung einschränken. 
#### 3. Überholte oder veraltete Modelle
  Die Verwendung veralteter oder überholter Modelle, die nicht mehr gepflegt werden, führt zu Sicherheitsproblemen.
#### 4. Anfälliges vortrainiertes Modell
  Modelle sind binäre Blackboxen und im Gegensatz zu Open Source kann eine statische Prüfung nur wenig zur Sicherheit beitragen. Anfällige vortrainierte Modelle können versteckte Verzerrungen, Hintertüren oder andere bösartige Merkmale enthalten, die bei den Sicherheitsbewertungen des Modell Repositories nicht erkannt wurden. Anfällige Modelle können sowohl durch vergiftete Datensätze als auch durch direkte Manipulation des Modells entstehen, beispielsweise durch Techniken wie ROME, auch bekannt als „Lobotomisierung“.
#### 5. Schwache Modellherkunft
  Derzeit gibt es in veröffentlichten Modellen keine strengen Herkunftsnachweise. Model Cards und die dazugehörige Dokumentation liefern zwar Informationen über das Modell und sind für Nutzende verlässlich, bieten aber keine Garantien über die Herkunft des Modells. Angreifende können ein Konto eines Anbietenden in einem Modell-Repository kompromittieren oder ein ähnliches Konto erstellen und mit Social-Engineering-Techniken kombinieren, um die Lieferkette einer LLM-Anwendung zu kompromittieren. 
#### 6. Anfällige LoRA-Adapter
  LoRA ist eine beliebte Technik zum Fine-Tuning, die die Modularität verbessert, indem sie es ermöglicht, vorab trainierte Schichten auf ein bestehendes LLM aufzusetzen. Die Methode erhöht die Effizienz, birgt jedoch neue Risiken, wenn ein böswilliger LoRA-Adapter die Integrität und Sicherheit des vorab trainierten Basismodells gefährdet. Dies kann sowohl in Umgebungen mit kollaborativer Modellzusammenführung als auch durch die Nutzung der Unterstützung für LoRA durch beliebte Inferenz-Bereitstellungsplattformen wie vLMM und OpenLLM geschehen, bei denen Adapter heruntergeladen und auf ein bereitgestelltes Modell angewendet werden können.
#### 7. Gemeinsame Entwicklungsprozesse ausnutzen
  Kollaborative Modellzusammenführung und Modellbearbeitungsdienste (z. B. Konvertierungen), die in gemeinsamen Umgebungen gehostet werden, können ausgenutzt werden, um Schwachstellen in gemeinsame Modelle einzubringen. Das Zusammenführen von Modellen ist bei Hugging Face sehr beliebt. Modelle, die zusammengeführt wurden, führen die OpenLLM-Rangliste an und können ausgenutzt werden, um Prüfungen zu umgehen. Auch Dienste wie Conversation Bots haben sich als anfällig für Manipulationen erwiesen und können bösartigen Code in Modelle einschleusen.
#### 8. Schwachstellen in der Lieferkette von LLM-Modellen auf Geräten
  LLM-Modelle auf Geräten erhöhen die Angriffsfläche durch kompromittierte Herstellungsprozesse und die Ausnutzung von Schwachstellen im Betriebssystem oder in der Firmware des Geräts, um Modelle zu kompromittieren. Angreifende können Anwendungen mit manipulierten Modellen zurückentwickeln und neu verpacken. 
#### 9. Unklare AGBs und Datenschutzrichtlinien
  Unklare AGB und Datenschutzrichtlinien der Modellbetreiber führen dazu, dass die sensiblen Daten der Anwendung für das Modelltraining verwendet werden und somit sensible Informationen preisgegeben werden. Dies gilt auch für Risiken, die sich aus der Verwendung von urheberrechtlich geschütztem Material durch den Modellanbieter ergeben.

### Präventions- und Mitigationsstrategien

1. Überprüfen Sie sorgfältig die Datenquellen und Lieferanten, einschließlich der AGBs und Datenschutzrichtlinien, und verwenden Sie nur vertrauenswürdige Lieferanten. Überprüfen Sie regelmäßig die Sicherheit und den Zugang der Anbieter und stellen Sie sicher, dass sich deren Sicherheitslage und AGBs nicht ändern.
2. Verstehen Sie die in der OWASP Top Ten „A06:2021 - Vulnerable and Outdated Components“ beschriebenen Maßnahmen und wenden Sie diese an. Scannen Sie auf Schwachstellen, verwalten und patchen Sie Komponenten. Wenden Sie diese Kontrollen auch in Entwicklungsumgebungen an, die Zugang zu sensiblen Daten haben.
  (Ref. Link: [A06:2021 - Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Wenden Sie ein umfassendes KI-Red-Teaming und detaillierte Evaluierungen an, wenn Sie ein Drittanbietermodell auswählen. Verwenden Sie vertrauenswürdige KI-Benchmarks wie Decoding Trust, berücksichtigen Sie jedoch, dass Modelle so fein abgestimmt werden können, dass sie veröffentlichte Benchmarks übertreffen. Evaluieren Sie das Modell gründlich in den spezifischen Anwendungsfällen, für die Sie es einsetzen möchten.
4. Erstellen Sie ein aktuelles Inventar Ihrer Komponenten mithilfe einer Software Bill of Materials (SBOM), um sicherzustellen, dass Sie über ein aktuelles, fehlerfreies und signiertes Inventar verfügen, das Manipulationen an den eingesetzten Paketen verhindert. Nutzen Sie SBOMs, um neue, nicht mehr aktuelle Schwachstellen schnell zu erkennen und darauf hinzuweisen. KI-BOMs und ML-SBOMs sind ein aufstrebendes Gebiet und Sie sollten diese Optionen evaluieren, beginnend mit OWASP CycloneDX.
5. Minimieren Sie Risiken im Zusammenhang mit der KI-Lizenzierung durch die Erstellung eines Inventars aller relevanten Lizenztypen mithilfe von BOMs und die Durchführung regelmäßiger Audits aller Software, Tools und Datensätze, um die Einhaltung von Vorschriften und die Transparenz der Stücklisten zu gewährleisten. Verwenden Sie automatisierte Lizenzverwaltungstools für die Echtzeitüberwachung und schulen Sie Ihre Teams in Lizenzierungsmodellen. Führen Sie eine detaillierte Lizenzdokumentation in Stücklisten.
6. Verwenden Sie nur Modelle aus überprüfbaren Quellen und führen Sie Integritätsprüfungen von Drittanbietern mit Signaturen und Datei-Hashes durch, um das Fehlen einer sicheren Modellherkunft auszugleichen. Setzen Sie zudem Code-Signierung für extern gelieferten Code ein.
7. Implementieren Sie strenge Überwachungs- und Prüfungspraktiken für kollaborative Modellentwicklungsumgebungen, um Missbrauch zu verhindern und schnell zu erkennen. Nutzen Sie automatisierte Skripte wie den „HuggingFace SF_Convertbot Scanner“ als Beispiel für effektive Tools.
  (Ref. Link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Die Erkennung von Anomalien und Robustheitstests für bereitgestellte Modelle und Daten können dazu beitragen, Manipulationen und Poisoning aufzudecken, wie in "LLM04 Poisoning von Daten und Modellen" beschrieben; idealerweise sollte dies Teil der MLOps- und LLM-Pipelines sein.
9. Implementieren Sie eine Patching-Policy, um verwundbare oder veraltete Komponenten zu entschärfen. Stellen Sie sicher, dass die Anwendung auf einer gepflegten Version der APIs und des zugrunde liegenden Modells basiert.
10. Verschlüsseln Sie Modelle, die am KI-Edge bereitgestellt werden, mit Integritätsprüfungen, und nutzen Sie die Attestierungs-APIs der Hersteller, um manipulierte Anwendungen und Modelle zu verhindern und Anwendungen mit nicht anerkannten Firmware zu beenden.

### Beispiele für Angriffsszenarien

#### Szenario 1: Verwundbare Python-Bibliothek
  Angreifende nutzen eine verwundbare Python-Bibliothek aus, um eine LLM-Anwendung zu kompromittieren. Dies geschah während der ersten OpenAI Datenpanne. Durch Angriffe auf die PyPi-Paketregistrierung wurden Modellentwickelnde dazu verleitet, eine kompromittierte PyTorch-Abhängigkeit mit Malware in eine Modellentwicklungsumgebung herunterzuladen. Ein weiteres, ausgefeilteres Beispiel für diese Art von Angriff ist Shadow Ray, ein Angriff auf das Ray AI Framework, das von vielen Anbietern zur Verwaltung ihrer KI-Infrastruktur verwendet wird. Es wird vermutet, dass bei diesem Angriff fünf Schwachstellen ausgenutzt wurden, von denen viele Server betroffen waren.
#### Szenario 2: Direkte Manipulation
  Direkte Manipulation und Veröffentlichung eines Modells zur Verbreitung von Fehlinformationen. Dies ist ein tatsächlicher Angriff, bei dem PoisonGPT die Sicherheitsfunktionen von Hugging Face umgeht, indem es die Modellparameter direkt ändert.
#### Szenario 3: Fine-Tuning eines beliebten Modells
  Angreifende fine-tunen ein beliebtes, frei zugängliches Modell so, dass wichtige Sicherheitsmerkmale entfernt werden und es in einem bestimmten Bereich (Versicherungen) besonders gut abschneidet. Das Modell ist so eingestellt, dass es bei den Sicherheitsbenchmarks gut abschneidet, aber sehr gezielte Trigger hat. Die Angreifenden verbreiten es auf Hugging Face, damit Opfer es nutzen und auf Benchmark-Zusicherungen vertrauen.
#### Szenario 4: Vortrainierte Modelle
  Ein LLM-System setzt vortrainierte Modelle aus einem weit verbreiteten Repository ohne gründliche Überprüfung ein. Ein kompromittiertes Modell führt bösartigen Code ein, der in bestimmten Kontexten verzerrte Ergebnisse verursacht und zu schädlichen oder manipulierten Resultaten führt.
#### Szenario 5: Kompromittierter Drittanbieter
  Ein kompromittierter Drittanbieter stellt einen anfälligen LoRA-Adapter zur Verfügung, der mithilfe von Model Merge auf Hugging Face zu einem LLM zusammengeführt wird.
#### Szenario 6: Infiltration eines Lieferanten
  Angreifende infiltrieren einen Drittanbieter und kompromittiert die Produktion eines LoRA-Adapters (Low-Rank Adaptation), der für die Integration in ein On-Device-LLM bestimmt ist, der mit Frameworks wie vLLM oder OpenLLM bereitgestellt wird. Der kompromittierte LoRA-Adapter ist so verändert, dass er versteckte Schwachstellen und bösartigen Code enthält. Sobald dieser Adapter mit dem LLM verbunden ist, bietet er Angreifenden einen versteckten Einstiegspunkt in das System. Der bösartige Code kann während des Modellbetriebs aktiviert werden und ermöglicht es Angreifenden, die Ergebnisse des LLM zu manipulieren.
#### Szenario 7: CloudBorne und CloudJacking Angriffe
  Diese Angriffe zielen auf Cloud-Infrastrukturen ab, indem sie gemeinsam genutzte Ressourcen und Schwachstellen in den Virtualisierungsschichten ausnutzen. Bei CloudBorne werden Firmware-Schwachstellen in gemeinsam genutzten Cloud-Umgebungen ausgenutzt, um die physischen Server zu kompromittieren, auf denen virtuelle Instanzen laufen. CloudJacking bezieht sich auf die böswillige Kontrolle oder den Missbrauch von Cloud-Instanzen, was zu einem unbefugten Zugriff auf wichtige LLM-Einsatzplattformen führen kann. Beide Angriffe stellen erhebliche Risiken für Lieferketten dar, die auf Cloud-basierte ML-Modelle angewiesen sind, da kompromittierte Umgebungen sensible Daten preisgeben oder weitere Angriffe erleichtern könnten. 
#### Szenario 8: LeftOvers (CVE-2023-4969)
  LeftOvers nutzt den geleakten lokalen Speicher der GPU aus, um an sensible Daten zu gelangen. Angreifende können diesen Ansatz nutzen, um sensible Daten auf Produktionsservern und Entwicklungs-Workstations oder Laptops zu exfiltrieren.    
#### Szenario 9: WizardLM
  Nach der Entfernung von WizardLM nutzten Angreifende das Interesse an diesem Modell aus und veröffentlichten eine gefälschte Version des Modells mit demselben Namen, die jedoch Schadsoftware und Hintertüren enthält.  
#### Szenario 10: Model Merge/Format Conversion Service
  Angreifende inszenieren einen Angriff mit einem Model Merge oder Format Conversion Service, um ein öffentlich zugängliches Modell zu kompromittieren und Malware einzuschleusen. Dies ist ein aktueller Angriff, der vom Anbieter HiddenLayer veröffentlicht wurde.
#### Szenario 11: Reverse-Engineering einer mobilen App
  Angreifende reverse-engineeren eine mobile App, um das Modell durch eine manipulierte Version zu ersetzen, die den Nutzer auf Betrugsseiten führt. Die Nutzer werden durch Social-Engineering-Techniken dazu gebracht, die App direkt herunterzuladen. Dies ist ein „echter Angriff auf die vorausschauende KI“, von dem 116 Google Play-Apps betroffen sind, darunter beliebte sicherheitskritische Anwendungen wie Bargelderkennung, Kindersicherung, Gesichtsauthentifizierung und Finanzdienstleistungen.
  (Ref. Link: [realer Angriff auf prädiktive KI](https://arxiv.org/abs/2006.08131))
#### Szenario 12: Datensatzvergiftung (Dataset Poisoning)
  Angreifende vergiften öffentlich zugängliche Datensätze, um beim Fine-Tuning der Modelle eine Hintertür zu schaffen. Die Hintertür begünstigt auf subtile Weise bestimmte Unternehmen in verschiedenen Märkten.
#### Szenario 13: AGBs und Datenschutzbestimmungen
  Ein LLM-Betreibender ändert die AGB und Datenschutzrichtlinien so, dass eine ausdrückliche Abmeldung von der Verwendung von Anwendungsdaten für das Modelltraining erforderlich ist, was dazu führt, dass sensible Daten gespeichert werden.

### Referenzlinks

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt finden Sie umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
