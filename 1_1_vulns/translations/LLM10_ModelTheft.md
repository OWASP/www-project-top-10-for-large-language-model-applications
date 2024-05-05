## LLM10: Modell-Diebstahl

### Beschreibung

Dieser Eintrag bezieht sich auf den unbefugten Zugriff und die Exfiltration von LLM-Modellen durch bösartige Akteure oder APTs (Advanced Persistent Threats). Dies tritt auf, wenn die proprietären LLM-Modelle (als wertvolles geistiges Eigentum) kompromittiert, physisch gestohlen, kopiert oder Gewichte und Parameter extrahiert werden, um ein funktionsfähiges Äquivalent zu erstellen. Die Auswirkungen des Diebstahls von LLM-Modellen können wirtschaftliche Verluste und Schäden am Markenimage, Erosion des Wettbewerbsvorteils, unbefugte Nutzung des Modells oder unbefugten Zugriff auf sensible Informationen, die im Modell enthalten sind, umfassen.

Der Diebstahl von LLMs stellt ein erhebliches Sicherheitsproblem dar, da Sprachmodelle immer leistungsfähiger und verbreiteter werden. Organisationen und Forscher müssen robuste Sicherheitsmaßnahmen priorisieren, um ihre LLM-Modelle zu schützen und die Vertraulichkeit und Integrität ihres geistigen Eigentums zu gewährleisten. Die Implementierung eines umfassenden Sicherheitsrahmens, der Zugriffskontrollen, Verschlüsselung und kontinuierliche Überwachung umfasst, ist entscheidend, um die Risiken im Zusammenhang mit dem Diebstahl von LLM-Modellen zu mindern und die Interessen von Einzelpersonen und Organisationen, die sich auf LLM verlassen, zu schützen.

### Häufige Beispiele für Schwachstellen

1. Ein Angreifer nutzt eine Schwachstelle in der Infrastruktur eines Unternehmens aus, um unbefugten Zugriff auf ihr LLM-Modell-Repository zu erhalten, durch Fehlkonfiguration in ihren Netzwerk- oder Anwendungssicherheitseinstellungen.
2. Ein Insider-Bedrohungsszenario, bei dem ein unzufriedener Mitarbeiter das Modell oder damit verbundene Artefakte durchsickern lässt.
3. Ein Angreifer verwendet die Modell-API mit sorgfältig erstellten Eingaben und Prompt-Injektionstechniken, um eine ausreichende Anzahl von Ausgaben zu sammeln, um ein Schattenmodell zu erstellen.
4. Ein bösartiger Angreifer kann Eingabefilterungstechniken des LLM umgehen, um einen Seitenkanalangriff durchzuführen und letztendlich Modellgewichte und Architekturinformationen zu einer ferngesteuerten Ressource zu übertragen.
5. Der Angriffsvektor für die Modell-Extraktion beinhaltet das Abfragen des LLM mit einer großen Anzahl von Prompts zu einem bestimmten Thema. Die Ausgaben aus dem LLM können dann verwendet werden, um ein anderes Modell zu verfeinern. Es gibt jedoch einige Dinge zu beachten bei diesem Angriff:
   - Der Angreifer muss eine große Anzahl von gezielten Prompts generieren. Wenn die Prompts nicht spezifisch genug sind, werden die Ausgaben aus dem LLM nutzlos sein.
   - Die Ausgaben aus LLMs können manchmal halluzinierte Antworten enthalten, was bedeutet, dass der Angreifer möglicherweise nicht das gesamte Modell extrahieren kann, da einige der Ausgaben unsinnig sein können.
   - Es ist nicht möglich, ein LLM zu 100% durch Modell-Extraktion zu replizieren. Der Angreifer wird jedoch in der Lage sein, ein teilweises Modell zu replizieren.
6. Der Angriffsvektor für **_funktionale Modellreplikation_** beinhaltet die Verwendung des Zielmodells über Prompts, um synthetische Trainingsdaten zu generieren (ein Ansatz, der als "Selbstinstruktion" bezeichnet wird), um es dann zu verwenden und ein anderes grundlegendes Modell zu verfeinern und ein funktionales Äquivalent zu produzieren. Dies umgeht die Einschränkungen der traditionellen abfragebasierten Extraktion, die in Beispiel 5 verwendet wurde, und wurde erfolgreich in der Forschung über die Verwendung eines LLM zum Trainieren eines anderen LLM eingesetzt. Obwohl im Kontext dieser Forschung die Modellreplikation kein Angriff ist. Der Ansatz könnte von einem Angreifer verwendet werden, um ein proprietäres Modell mit einer öffentlichen API zu replizieren.

Die Verwendung eines gestohlenen Modells als Schattenmodell kann verwendet werden, um gegnerische Angriffe zu inszenieren, einschließlich unbefugtem Zugriff auf sensible Informationen, die im Modell enthalten sind, oder um unbemerkt mit gegnerischen Eingaben zu experimentieren, um weiter fortgeschrittene Prompt-Injektionen zu inszenieren.

### Präventions- und Mitigierungsstrategien

1. Implementieren Sie starke Zugriffskontrollen (z.B. RBAC und das Prinzip der geringsten Rechte) und starke Authentifizierungsmechanismen, um unbefugten Zugriff auf LLM-Modell-Repositories und Trainingsumgebungen zu begrenzen.
   1. Dies gilt insbesondere für die ersten drei häufigen Beispiele, die diese Schwachstelle aufgrund von Insider-Bedrohungen, Fehlkonfigurationen und/oder schwachen Sicherheitskontrollen über die Infrastruktur, die LLM-Modelle, Gewichte und Architektur beherbergt, in der ein bösartiger Akteur aus dem Inneren oder von außen eindringen könnte, verursachen könnten.
   2. Lieferantenmanagement-Tracking, Überprüfung und Abhängigkeitsschwachstellen sind wichtige Schwerpunktthemen, um Ausnutzungen von Supply-Chain-Angriffen zu verhindern.
2. Beschränken Sie den Zugriff des LLM auf Netzwerkressourcen, interne Dienste und APIs.
   1. Dies gilt insbesondere für alle häufigen Beispiele, da es das Insider-Risiko und -Bedrohungen abdeckt, aber letztendlich auch kontrolliert, worauf die LLM-Anwendung "_Zugriff hat_", und somit ein Mechanismus oder Präventionsschritt sein könnte, um Seitenkanalangriffe zu verhindern.
3. Verwenden Sie ein zentrales ML-Modellinventar oder -Register für ML-Modelle, die in der Produktion verwendet werden. Ein zentrales Modellregister verhindert unbefugten Zugriff auf ML-Modelle über Zugriffskontrollen, Authentifizierung und Überwachungs-/Protokollierungsfähigkeit, die gute Grundlagen für Governance sind. Ein zentrales Repository ist auch vorteilhaft für die Sammlung von Daten über Algorithmen, die von den Modellen für Zwecke der Compliance, Risikobewertungen und Risikominderung verwendet werden.
4. Überwachen und prüfen Sie regelmäßig Zugriffsprotokolle und Aktivitäten im Zusammenhang mit LLM-Modell-Repositories, um verdächtiges oder unbefugtes Verhalten umgehend zu erkennen und darauf zu reagieren.
5. Automatisieren Sie MLOps-Bereitstellung mit Governance und Nachverfolgungs- und Genehmigungsworkflows, um Zugriffs- und Bereitstellungskontrollen innerhalb der Infrastruktur zu straffen.
6. Implementieren Sie Kontrollen und Minderungsstrategien, um das Risiko von Prompt-Injektionstechniken, die Seitenkanalangriffe verursachen, zu mindern und/oder zu reduzieren.
7. Rate Limiting von API-Aufrufen, wo anwendbar, und/oder Filter, um das Risiko der Datenexfiltration aus den LLM-Anwendungen zu reduzieren, oder implementieren Sie Techniken zur Erkennung (z.B. DLP) von Extraktionsaktivitäten aus anderen Überwachungssystemen.
8. Implementieren Sie Training zur gegnerischen Robustheit, um Extraktionsabfragen zu erkennen und physische Sicherheitsmaßnahmen zu straffen.
9. Implementieren Sie ein Wasserzeichen-Framework in die Einbettungs- und Erkennungsphasen des Lebenszyklus eines LLMs.

### Beispielangriffsszenarien

1. Ein Angreifer nutzt eine Schwachstelle in der Infrastruktur eines Unternehmens aus, um unbefugten Zugriff auf ihr LLM-Modell-Repository zu erhalten. Der Angreifer fährt fort, wertvolle LLM-Modelle zu exfiltrieren und verwendet sie, um einen konkurrierenden Sprachverarbeitungsdienst zu starten oder sensible Informationen zu extrahieren, was zu erheblichen finanziellen Schäden für das ursprüngliche Unternehmen führt.
2. Ein unzufriedener Mitarbeiter lässt das Modell oder damit verbundene Artefakte durchsickern. Die öffentliche Exposition dieses Szenarios erhöht das Wissen für Angreifer für Graukasten-gegnerische Angriffe oder alternativ direkt den Diebstahl des verfügbaren Eigentums.
3. Ein Angreifer fragt die API mit sorgfältig ausgewählten Eingaben ab und sammelt eine ausreichende Anzahl von Ausgaben, um ein Schattenmodell zu erstellen.
4. Ein Versagen der Sicherheitskontrolle ist innerhalb der Lieferkette vorhanden und führt zu Datenlecks von proprietären Modellinformationen.
5. Ein bösartiger Angreifer umgeht Eingabefilterungstechniken und Präambeln des LLM, um einen Seitenkanalangriff durchzuführen und Modellinformationen zu einer ferngesteuerten Ressource unter ihrer Kontrolle abzurufen.

### Referenz-Links

1. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse): **The Verge**
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
3. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [D-DAE: Defense-Penetrating Model Extraction Attacks:](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c): **Computer.org**
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
7. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
8. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
