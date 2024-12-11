## LLM03:2025 Lieferkette

### Beschreibung

LLM-Lieferketten sind anfällig für verschiedene Schwachstellen, die die Integrität von Trainingsdaten, Modellen und Einsatzplattformen beeinträchtigen können. Diese Risiken können zu verzerrten Ergebnissen, Sicherheitslücken oder Systemausfällen führen. Während sich herkömmliche Software-Schwachstellen auf Probleme wie Code-Fehler und Abhängigkeiten konzentrieren, erstrecken sich die Risiken bei ML auch auf vortrainierte Modelle und Daten Dritter.

Diese externen Elemente können durch Manipulationen oder Poisoning-Angriffe manipuliert werden.

Die Erstellung von LLMs ist eine spezielle Aufgabe, die oft von Modellen Dritter abhängt. Das Aufkommen von offen zugänglichen LLMs und neuen Feinabstimmungsmethoden wie „LoRA“ (Low-Rank Adaptation) und „PEFT“ (Parameter-Efficient Fine-Tuning), insbesondere auf Plattformen wie Hugging Face, bringen neue Risiken in die Lieferkette. Schließlich vergrößert das Aufkommen von On-Device-LLMs die Angriffsfläche und die Supply-Chain-Risiken für LLM-Anwendungen.

Einige der hier diskutierten Risiken werden auch in „LLM04 Data and Model Poisoning“ behandelt. Dieser Beitrag konzentriert sich auf den Supply-Chain-Aspekt der Risiken.
Ein einfaches Bedrohungsmodell findest du [hier] (https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Gängige Beispiele für Risiken

#### 1. Traditionelle Schwachstellen in Drittanbieterpaketen
  Zum Beispiel veraltete Komponenten, die Angreifer ausnutzen können, um LLM-Anwendungen zu kompromittieren. Dies ist ähnlich wie bei "A06:2021 - Vulnerable and Outdated Components" mit erhöhten Risiken, wenn Komponenten während der Modellentwicklung oder des Finetunings verwendet werden.
  (Ref. Link: [A06:2021 - Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
#### 2. Risiken bei der Lizenzierung
  Bei der Entwicklung von KI kommen oft verschiedene Software- und Datenlizenzen zum Einsatz, die Risiken bergen, wenn sie nicht richtig gehandhabt werden. Unterschiedliche Open-Source- und proprietäre Lizenzen bringen unterschiedliche rechtliche Anforderungen mit sich. Lizenzen für Datensätze können die Nutzung, den Vertrieb oder die Kommerzialisierung einschränken. 
#### 3. Überholte oder veraltete Modelle
  Die Verwendung veralteter oder veralteter Modelle, die nicht mehr gepflegt werden, führt zu Sicherheitsproblemen.
#### 4. Anfälliges vortrainiertes Modell
  Modelle sind binäre Blackboxen und im Gegensatz zu Open Source kann eine statische Prüfung nur wenig zur Sicherheit beitragen. Anfällige vortrainierte Modelle können versteckte Verzerrungen, Hintertüren oder andere bösartige Merkmale enthalten, die bei den Sicherheitsbewertungen des Modellspeichers nicht erkannt wurden. Anfällige Modelle können sowohl durch manipulierte Datensätze als auch durch direkte Modellmanipulationen mit Techniken wie ROME, auch bekannt als Lobotomisierung, erstellt werden.
#### 5. Schwache Modellprovenienz
  Derzeit gibt es in veröffentlichten Modellen keine strengen Herkunftsnachweise. Model Cards und die dazugehörige Dokumentation liefern zwar Informationen über das Modell und sind für die Nutzer/innen verlässlich, bieten aber keine Garantien über die Herkunft des Modells. Ein Angreifer kann das Konto eines Anbieters auf einem Modell- Repository kompromittieren oder ein ähnliches erstellen und es mit Social-Engineering-Techniken kombinieren, um die Lieferkette einer LLM-Anwendung zu kompromittieren.
#### 6. Anfällige LoRA-Adapter
  LoRA ist eine beliebte Feinabstimmungstechnik, die die Modularität erhöht, indem sie es ermöglicht, vortrainierte Schichten auf ein bestehendes LLM aufzuschrauben. Diese Methode erhöht zwar die Effizienz, birgt aber auch neue Risiken, wenn ein böswilliger LorA-Adapter die Integrität und Sicherheit des vortrainierten Basismodells gefährdet. Dies kann sowohl in kollaborativen Modellzusammenführungsumgebungen geschehen, als auch unter Ausnutzung der LoRA-Unterstützung von gängigen Inferenzplattformen wie vLMM und OpenLLM, wo Adapter heruntergeladen und auf ein eingesetztes Modell angewendet werden können.
#### 7. Gemeinsame Entwicklungsprozesse ausnutzen
  Kollaborative Modellzusammenführung und Modellbearbeitungsdienste (z. B. Konvertierungen), die in gemeinsamen Umgebungen gehostet werden, können ausgenutzt werden, um Schwachstellen in gemeinsame Modelle einzubringen. Das Zusammenführen von Modellen ist bei Hugging Face sehr beliebt. Modelle, die zusammengeführt wurden, führen die OpenLLM-Rangliste an und können ausgenutzt werden, um Prüfungen zu umgehen. Auch Dienste wie Conversation Bots haben sich als anfällig für Manipulationen erwiesen und können bösartigen Code in Modelle einschleusen.
#### 8. Schwachstellen in der Lieferkette von LLM-Modellen auf Geräten
  LLM-Modelle auf Geräten erhöhen die Angriffsfläche durch kompromittierte Herstellungsprozesse und die Ausnutzung von Schwachstellen im Betriebssystem oder in der Fimware des Geräts, um Modelle zu kompromittieren. Angreifer können Anwendungen mit manipulierten Modellen zurückentwickeln und neu verpacken. 
#### 9. Unklare AGBs und Datenschutzrichtlinien
  Unklare AGB und Datenschutzrichtlinien der Modellbetreiber führen dazu, dass die sensiblen Daten der Anwendung für das Modelltraining verwendet werden und somit sensible Informationen preisgegeben werden. Dies gilt auch für Risiken, die sich aus der Verwendung von urheberrechtlich geschütztem Material durch den Modellanbieter ergeben.

### Präventions- und Mitigationsstrategien

1. Überprüfe sorgfältig die Datenquellen und Lieferanten, einschließlich der AGBs und ihrer Datenschutzrichtlinien, und verwende nur vertrauenswürdige Lieferanten. Überprüfe regelmäßig die Sicherheit und den Zugang der Anbieter und achte darauf, dass sich ihre Sicherheitslage und ihre AGBs nicht ändern.
2. Verstehe die in der OWASP Top Ten „A06:2021 - Vulnerable and Outdated Components“ beschriebenen Maßnahmen und wende sie an. Dazu gehören das Scannen auf Schwachstellen, die Verwaltung und das Patchen von Komponenten. In Entwicklungsumgebungen, die Zugang zu sensiblen Daten haben, solltest du diese Kontrollen ebenfalls anwenden.
  (Ref. Link: [A06:2021 - Verwundbare und veraltete Komponenten](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Wende ein umfassendes KI-Red Teaming und Evaluierungen an, wenn du ein Drittanbietermodell auswählst. Decoding Trust ist ein Beispiel für einen vertrauenswürdigen KI-Benchmark für LLMs, aber die Modelle können so fein abgestimmt werden, dass sie die veröffentlichten Benchmarks übertreffen. Nutze ein umfassendes KI-Red Teaming, um das Modell zu evaluieren, vor allem in den Anwendungsfällen, für die du das Modell einsetzen willst. 
4. Führe ein aktuelles Komponenteninventar mit Hilfe einer Software Bill of Materials (SBOM), um sicherzustellen, dass du über ein aktuelles, genaues und signiertes Inventar verfügst, das Manipulationen an den eingesetzten Paketen verhindert. SBOMs können verwendet werden, um neue, nicht mehr aktuelle Schwachstellen schnell zu erkennen und darauf hinzuweisen. KI-BOMs und ML-SBOMs sind ein aufstrebender Bereich, und du kannst mit OWASP CycloneDX beginnen.
5. Um die Risiken der KI-Lizenzierung zu mindern, solltest du ein Inventar aller beteiligten Lizenztypen mit Hilfe von Stücklisten erstellen und regelmäßige Audits aller Software, Tools und Datensätze durchführen, um die Einhaltung der Vorschriften und Transparenz durch Stücklisten sicherzustellen. Nutze automatisierte Lizenzmanagement-Tools für die Echtzeitüberwachung und schule die Teams in Lizenzierungsmodellen. Pflege der detaillierten Lizenzierungsdokumentation in den Stücklisten.
6. Verwende nur Modelle aus überprüfbaren Quellen und nutze Integritätsprüfungen von Drittanbietern mit Signaturen und Datei-Hashes, um das Fehlen einer sicheren Modellherkunft auszugleichen. Verwende auch Code-Signierung für extern gelieferten Code.
7. Implementiere strenge Überwachungs- und Prüfungspraktiken für kollaborative Modellentwicklungsumgebungen, um Missbrauch zu verhindern und schnell zu erkennen. Der „HuggingFace SF_Convertbot Scanner“ ist ein Beispiel für automatisierte Skripte, die du verwenden kannst.
  (Ref. Link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Die Erkennung von Anomalien und Robustheitstests für bereitgestellte Modelle und Daten können dazu beitragen, Manipulationen und Vergiftungen aufzudecken, wie in "LLM04 Data and Model Poisoning" beschrieben; idealerweise sollte dies Teil der MLOps- und LLM-Pipelines sein.
9. Implementiere eine Patching-Policy, um verwundbare oder veraltete Komponenten zu entschärfen. Stelle sicher, dass die Anwendung auf einer gepflegten Version der APIs und des zugrunde liegenden Modells basiert.
10. Verschlüssele Modelle, die am KI-Edge eingesetzt werden, mit Integritätsprüfungen und verwende Hersteller-APIs, um manipulierte Anwendungen und Modelle zu verhindern und Anwendungen mit nicht anerkannter Firmware zu beenden.

### Beispiele für Angriffsszenarien

#### Szenario #1: Verwundbare Python-Bibliothek
  Ein Angreifer nutzt eine verwundbare Python-Bibliothek aus, um eine LLM-App zu kompromittieren. Dies geschah bei der ersten Open AI-Datenpanne.  Durch Angriffe auf die PyPi-Paket-Registry wurden Modellentwickler dazu verleitet, eine kompromittierte PyTorch-Abhängigkeit mit Malware in eine Modellentwicklungsumgebung herunterzuladen.  Ein ausgefeilteres Beispiel für diese Art von Angriff ist Shadow Ray, ein Angriff auf das Ray AI Framework, das von vielen Anbietern zur Verwaltung der KI-Infrastruktur verwendet wird.  Es wird vermutet, dass bei diesem Angriff fünf Schwachstellen ausgenutzt wurden, von denen viele Server betroffen waren.
#### Szenario #2: Direkte Manipulation
  Direkte Manipulation und Veröffentlichung eines Modells zur Verbreitung von Fehlinformationen. Dies ist ein tatsächlicher Angriff, bei dem PoisonGPT die Sicherheitsfunktionen von Hugging Face umgeht, indem er die Modellparameter direkt ändert.
#### Szenario #3: Finetuning eines beliebten Modells
  Ein Angreifer stimmt ein beliebtes, frei zugängliches Modell so ab, dass wichtige Sicherheitsmerkmale entfernt werden und es in einem bestimmten Bereich (Versicherungen) besonders gut abschneidet. Das Modell ist so eingestellt, dass es bei den Sicherheitsbenchmarks gut abschneidet, aber sehr gezielte Auslöser hat. Sie setzen es bei Hugging Face ein, damit die Opfer es nutzen und ihr Vertrauen in die Benchmark-Zusicherungen ausnutzen können. 
#### Szenario #4: Vortrainierte Modelle
  Ein LLM-System setzt vortrainierte Modelle aus einem weit verbreiteten Repository ohne gründliche Überprüfung ein. Ein kompromittiertes Modell führt bösartigen Code ein, der in bestimmten Kontexten verzerrte Ergebnisse verursacht und zu schädlichen oder manipulierten Resultaten führt.
#### Szenario #5: Kompromittierter Drittanbieter
  Ein kompromittierter Drittanbieter stellt einen anfälligen LorA-Adapter zur Verfügung, der mit Hilfe von Model Merge auf Hugging Face zu einem LLM zusammengeführt wird.
#### Szenario #6: Infiltration eines Lieferanten
  Ein Angreifer infiltriert einen Drittanbieter und kompromittiert die Produktion eines LoRA-Adapters (Low-Rank Adaptation), der für die Integration in einen On-Device-LLM bestimmt ist, der mit Frameworks wie vLLM oder OpenLLM bereitgestellt wird. Der kompromittierte LoRA-Adapter ist so verändert, dass er versteckte Schwachstellen und bösartigen Code enthält. Sobald dieser Adapter mit dem LLM verbunden ist, bietet er dem Angreifer einen versteckten Einstiegspunkt in das System. Der bösartige Code kann während des Modellbetriebs aktiviert werden und ermöglicht es dem Angreifer, die Ergebnisse des LLM zu manipulieren.
#### Szenario #7: CloudBorne und CloudJacking Angriffe
  Diese Angriffe zielen auf Cloud-Infrastrukturen ab, indem sie gemeinsam genutzte Ressourcen und Schwachstellen in den Virtualisierungsschichten ausnutzen. Bei CloudBorne werden Firmware-Schwachstellen in gemeinsam genutzten Cloud-Umgebungen ausgenutzt, um die physischen Server zu kompromittieren, auf denen virtuelle Instanzen laufen. CloudJacking bezieht sich auf die böswillige Kontrolle oder den Missbrauch von Cloud-Instanzen, was zu einem unbefugten Zugriff auf wichtige LLM-Einsatzplattformen führen kann. Beide Angriffe stellen erhebliche Risiken für Lieferketten dar, die auf Cloud-basierte ML-Modelle angewiesen sind, da kompromittierte Umgebungen sensible Daten preisgeben oder weitere Angriffe erleichtern könnten. 
#### Szenario #8: LeftOvers (CVE-2023-4969)
  LeftOvers nutzt den geleakten lokalen Speicher der GPU aus, um sensible Daten zu erlangen. Ein Angreifer kann diesen Angriff nutzen, um sensible Daten auf Produktionsservern und Entwicklungs-Workstations oder Laptops zu exfiltrieren.    
#### Szenario #9: WizardLM
  Nach der Entfernung von WizardLM nutzte ein Angreifer das Interesse an diesem Modell aus und veröffentlichte eine gefälschte Version des Modells mit demselben Namen, die jedoch Schadsoftware und Hintertüren enthält.  
#### Szenario #10: Model Merge/Format Conversion Service
  Ein Angreifer inszeniert einen Angriff mit einem Model Merge oder Format Conversion Service, um ein öffentlich zugängliches Modell zu kompromittieren und Malware einzuschleusen. Dies ist ein aktueller Angriff, der vom Anbieter HiddenLayer veröffentlicht wurde.
#### Szenario #11: Reverse-Engineering einer mobilen App
  Ein Angreifer entwickelt eine mobile App zurück, um das Modell durch eine manipulierte Version zu ersetzen, die den Nutzer auf Betrugsseiten führt. Die Nutzer werden durch Social-Engineering-Techniken dazu gebracht, die App direkt herunterzuladen. Dies ist ein „echter Angriff auf die prädiktive KI“, von dem 116 Google Play-Apps betroffen sind, darunter beliebte sicherheitskritische Anwendungen wie Bargelderkennung, Kindersicherung, Gesichtsauthentifizierung und Finanzdienstleistungen.
  (Ref. Link: [realer Angriff auf prädiktive KI](https://arxiv.org/abs/2006.08131))
#### Szenario #12: Datensatzvergiftung (Dataset Poisoning)
  Ein Angreifer vergiftet öffentlich zugängliche Datensätze, um bei der Feinabstimmung der Modelle eine Hintertür zu schaffen. Die Hintertür begünstigt auf subtile Weise bestimmte Unternehmen in verschiedenen Märkten.
#### Szenario #13: AGBs und Datenschutzbestimmungen
  Ein LLM-Betreiber ändert seine AGB und Datenschutzrichtlinien so, dass eine ausdrückliche Abmeldung von der Verwendung von Anwendungsdaten für das Modelltraining erforderlich ist, was dazu führt, dass sensible Daten gespeichert werden.

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

In diesem Abschnitt findest du umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS**
