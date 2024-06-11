## LLM10: Modell-Diebstahl

### Beschreibung

Dieser Eintrag bezieht sich auf den unbefugten Zugriff und die Exfiltration von LLM-Modellen durch böswillige Akteure oder APTs (Advanced Persistent Threats). Dies geschieht, wenn proprietäre LLM-Modelle (als wertvolles geistiges Eigentum) kompromittiert, physisch gestohlen, kopiert oder Modellgewichte und Parameter extrahiert werden, um ein funktionsfähiges Äquivalent zu erstellen. Die Folgen eines Diebstahls von LLM-Modellen können unter anderem sein: wirtschaftliche Einbußen und Imageschäden, Erosion des Wettbewerbsvorteils, unbefugte Nutzung des Modells oder unbefugter Zugang zu sensiblen Informationen, die im Modell enthalten sind.

Der Diebstahl von LLMs stellt ein erhebliches Sicherheitsproblem dar, da Sprachmodelle immer leistungsfähiger und allgegenwärtiger werden. Organisationen und Forschende müssen robuste Sicherheitsmaßnahmen ergreifen, um ihre LLM-Modelle zu schützen und die Vertraulichkeit und Integrität ihres geistigen Eigentums zu gewährleisten. Der Einsatz eines umfassenden Sicherheitsrahmens, der Zugriffskontrollen, Verschlüsselung und kontinuierliche Überwachung umfasst, ist entscheidend, um die mit dem Diebstahl von LLM-Modellen verbundenen Risiken zu mindern und die Interessen sowohl von Einzelpersonen als auch von Organisationen zu schützen, die sich auf LLM verlassen.

### Gängige Beispiele für Schwachstellen

1. Angreifende nutzen eine Schwachstelle in der Infrastruktur einer Organisation aus, um sich durch Fehlkonfiguration der Netzwerk- oder Anwendungssicherheitseinstellungen unberechtigten Zugriff auf das LLM-Model-Repository zu verschaffen.
2. Ein Insider-Bedrohungsszenario, bei dem unzufriedene Mitarbeitende das Modell oder damit verbundene Artefakte nach Außen dringen lassen.
3. Angreifende verwenden die Modell-API mit sorgfältig erstellten Eingaben und Prompt Injection-Techniken, um eine ausreichende Anzahl von Ausgaben zu sammeln, um ein Schattenmodell zu erstellen.
4. Böswillige Angreifenden sind in der Lage, die Eingabefiltertechniken des LLM zu umgehen, um einen Seitenkanal-Angriff durchzuführen und schließlich Modellgewichte und Architekturinformationen an eine ferngesteuerte Ressource zu übermitteln.
5. Der Angriffsvektor für die Extraktion von Modellen beinhaltet die Abfrage des LLM mit einer großen Anzahl von Prompts zu einem bestimmten Thema. Die Ausgabe des LLM kann dann verwendet werden, um ein anderes Modell zu verfeinern. Bei diesem Angriff sind jedoch einige Dinge zu beachten:
   - Angreifende müssen eine große Anzahl spezifischer Prompts erzeugen. Wenn die Prompts nicht spezifisch genug sind, ist die Ausgabe des LLM nutzlos.
   - Die Ausgaben von LLMs können manchmal halluzinierte Antworten enthalten, was bedeutet, dass Angreifende möglicherweise nicht in der Lage sind, das gesamte Modell zu extrahieren, da einige der Ausgaben sinnlos sein können.
     - Es ist nicht möglich, ein LLM zu 100 % durch Modellextraktion zu replizieren. Angreifende werden jedoch in der Lage sein, ein Teilmodell zu replizieren.
6. Der Angriffsvektor für die **_funktionale Modellreplikation_** besteht darin, das Zielmodell über Prompts zu verwenden, um synthetische Trainingsdaten zu erzeugen (ein Ansatz, der als "Selbstinstruktion" bezeichnet wird), und diese dann zu verwenden, um ein anderes Basismodell zu verfeinern und ein funktionales Äquivalent zu erzeugen. Dieser Ansatz umgeht die Beschränkungen der traditionellen abfragebasierten Extraktion, die in Beispiel 5 verwendet wurde, und wurde erfolgreich in der Forschung über die Verwendung eines LLM zum Trainieren eines anderen LLM eingesetzt. Im Kontext dieser Forschung stellt die Modellreplikation keinen Angriff dar. Der Ansatz könnte von Angreifenden verwendet werden, um ein proprietäres Modell mit einer öffentlichen API zu replizieren.

Die Verwendung eines gestohlenen Modells als Schattenmodell kann dazu genutzt werden, Angriffe des Gegners zu inszenieren, einschließlich des unbefugten Zugriffs auf sensible Informationen, die im Modell enthalten sind, oder um unbemerkt mit Eingaben des Gegners zu experimentieren, um fortgeschrittenere Prompt-Injektionen zu inszenieren.

### Präventions- und Mitigationsstrategien

1. Implementieren Sie strenge Zugriffskontrollen (z. B. RBAC und das Least-Privilege-Prinzip) und starke Authentifizierungsmechanismen, um den unbefugten Zugriff auf Repositorys mit LLM-Modellen und Lernumgebungen einzuschränken.
  - Dies gilt insbesondere für die ersten drei gängigen Beispiele, die diese Schwachstelle aufgrund von Insider-Bedrohungen, Fehlkonfigurationen und/oder schwachen Sicherheitskontrollen in Bezug auf die Infrastruktur, die LLM-Modelle, -Gewichte und -Architekturen beherbergt, verursachen können, in die böswillige Akteure von innen oder außen eindringen können.
  - Schwachstellen bei der Rückverfolgbarkeit, der Verifizierung und der Abhängigkeit von Lieferanten sind wichtige Schwerpunktthemen, um die Ausnutzung von Angriffen auf die Lieferkette zu verhindern.
2. Beschränken Sie den Zugriff des LLM auf Netzwerkressourcen, interne Dienste und APIs.
  - Dies gilt speziell für alle gängigen Beispiele, da es Risiken und Bedrohungen von innen abdeckt, aber letztlich auch kontrolliert, worauf die LLM-Anwendung "zugreifen" kann und somit einen Mechanismus oder eine Präventivmaßnahme zur Verhinderung von Seitenkanal-Angriffen darstellen kann.
3. Verwenden Sie ein zentrales ML-Modell-Inventar oder -Register für ML-Modelle, die in der Produktion verwendet werden. Eine zentralisierte Modellregistrierung verhindert den unbefugten Zugriff auf ML-Modelle durch Zugriffskontrollen, Authentifizierung und Überwachungs-/Protokollierungsfunktionen, die eine gute Grundlage für die Governance bilden. Ein zentrales Repository ist auch vorteilhaft, um Daten über die von den Modellen verwendeten Algorithmen für Zwecke der Compliance, Risikobewertung und Risikominderung zu sammeln.
4. Überwachen und überprüfen Sie regelmäßig die Zugriffsprotokolle und Aktivitäten im Zusammenhang mit LLM-Model-Repositorys, um verdächtiges oder nicht autorisiertes Verhalten zu erkennen und sofort darauf zu reagieren.
5. Automatisieren Sie die MLOps-Bereitstellung mit Governance-, Tracking- und Genehmigungs-Workflows, um die Zugriffs- und Bereitstellungskontrollen innerhalb der Infrastruktur zu stärken.
6. Implementieren Sie Kontrollen und Abschwächungsstrategien, um das Risiko von Prompt Injection-Techniken, die Side-Channel-Angriffe verursachen, abzuschwächen oder zu verringern.
7. Beschränken Sie gegebenenfalls die Anzahl der API-Aufrufe und/oder setzen Sie Filter ein, um das Risiko der Datenexfiltration aus LLM-Anwendungen zu verringern, oder implementieren Sie Techniken zur Erkennung von Extraktionsaktivitäten (z. B. DLP) aus anderen Überwachungssystemen.
8. Implementieren Sie ein Robustheitstraining für feindliche Angriffe, um Extraktionsanfragen zu erkennen und die physischen Sicherheitsmaßnahmen zu verstärken.
9. Implementieren Sie ein Wasserzeichen-Framework in den Embeddings- und Erkennungsphasen des Lebenszyklus eines LLM.

### Beispiele für Angriffsszenarien

1. Angreifende nutzen eine Schwachstelle in der Infrastruktur eines Unternehmens aus, um sich unberechtigten Zugriff auf dessen LLM-Modell-Repository zu verschaffen. Die Angreifenden exfiltrieren wertvolle LLM-Modelle und verwendet sie, um einen konkurrierenden Sprachverarbeitungsdienst zu starten oder sensible Informationen zu extrahieren, wodurch dem ursprünglichen Unternehmen erheblicher finanzieller Schaden entsteht.
2. Unzufriedene Mitarbeitende lassen das Modell oder damit verbundene Artefakte nach außen dringen. Das öffentliche Bekanntwerden dieses Szenarios erhöht das Wissen für Angreifende, die Gray-Box-Angriffe oder alternativ den direkten Diebstahl des verfügbaren Eigentums planen. 
3. Angreifende fragen die API mit sorgfältig ausgewählten Eingaben ab und sammelt eine ausreichende Anzahl von Ausgaben, um ein Schattenmodell zu erstellen.
4. Ein Versagen der Sicherheitskontrolle in der Lieferkette führt zum Abfluss von proprietären Modellinformationen.
5. Böswillige Angreifende umgeht die Eingabefilterung und die Präambel des LLM, um einen Seitenkanal-Angriff durchzuführen und Modellinformationen über eine ferngesteuerte Ressource unter seiner Kontrolle zu erlangen.

### Referenzen

1. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse): **The Verge**
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
3. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [D-DAE: Defense-Penetrating Model Extraction Attacks:](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c): **Computer.org**
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
7. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
8. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**