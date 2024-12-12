## LLM04: Poisoning von Daten und Modellen

### Beschreibung

Data Poisoning liegt vor, wenn Daten vor dem Training, dem Fine-Tuning oder dem Embedding manipuliert werden, um Schwachstellen, Hintertüren oder Verzerrungen einzuführen. Diese Manipulation kann die Sicherheit, die Leistung oder das ethische Verhalten des Modells beeinträchtigen und zu schädlichen Ergebnissen oder eingeschränkten Fähigkeiten führen. Zu den üblichen Risiken gehören eine verringerte Modellleistung, verzerrte oder schädliche Inhalte und die Ausnutzung nachgelagerter Systeme.

Data Poisoning kann verschiedene Phasen des LLM-Lebenszyklus betreffen, darunter das Pre-Training (Lernen aus allgemeinen Daten), Fine-Tuning (Anpassung der Modelle an spezifische Aufgaben) und Embedding (Umwandlung von Text in numerische Vektoren). Das Verständnis dieser Phasen hilft dabei, mögliche Schwachstellen zu identifizieren. Data Poisoning wird als Angriff auf die Integrität betrachtet, da die Manipulation von Trainingsdaten die Fähigkeit des Modells beeinträchtigt, genaue Vorhersagen zu treffen. Die Risiken sind besonders hoch bei externen Datenquellen, die ungeprüfte oder bösartige Inhalte enthalten können.

Darüber hinaus können Modelle, die über gemeinsam genutzte Repositories oder Open-Source-Plattformen verbreitet werden, Risiken bergen, die über das Vergiften von Daten hinausgehen, wie z. B. Malware, die durch Techniken wie das bösartige Pickling eingebettet wird und schädlichen Code ausführen kann, wenn das Modell geladen wird. Bedenke auch, dass Poisoning die Implementierung einer Hintertür ermöglichen kann. Solche Hintertüren können das Verhalten des Modells so lange unangetastet lassen, bis ein bestimmter Auslöser eine Änderung bewirkt. Das kann dazu führen, dass solche Änderungen nur schwer zu testen und zu entdecken sind und ein Modell zu einem Sleeper Agent werden kann.

### Gängige Beispiele für Schwachstellen

1. Böswillige Akteure führen während des Trainings schädliche Daten ein, was zu verzerrten Ergebnissen führt. Techniken wie „Split-View Data Poisoning“ oder „Frontrunning Poisoning“ nutzen die Dynamik der Modellausbildung aus, um dies zu erreichen.
  (Ref. Link: [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg))
  (Ref. link: [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg))
2. Angreifer können schädliche Inhalte direkt in den Trainingsprozess einschleusen und so die Qualität des Modells beeinträchtigen.
3. Nutzer/innen geben während der Interaktion unwissentlich sensible oder geschützte Informationen ein, die in den nachfolgenden Ergebnissen aufgedeckt werden können.
4. Ungeprüfte Trainingsdaten erhöhen das Risiko von verzerrten oder fehlerhaften Ergebnissen.
5. Fehlende Beschränkungen des Ressourcenzugriffs können dazu führen, dass unsichere Daten eingegeben werden, was zu verzerrten Ergebnissen führt.

### Präventions- und Mitigationsstrategien

1. Verfolge die Datenherkunft und -umwandlung mit Tools wie OWASP CycloneDX oder ML-BOM. Überprüfe die Legitimität der Daten in allen Phasen der Modellentwicklung.
2. Prüfe die Datenlieferanten genau und validiere die Modellergebnisse anhand vertrauenswürdiger Quellen, um Anzeichen von Vergiftung zu erkennen.
3. Implementiere eine strenge Sandbox, um den Zugriff des Modells auf ungeprüfte Datenquellen zu begrenzen. Nutze Techniken zur Erkennung von Anomalien, um unerwünschte Daten herauszufiltern.
4. Passe Modelle für verschiedene Anwendungsfälle an, indem du bestimmte Datensätze zum Fine-Tuning verwendest. Dies hilft, genauere Ergebnisse zu erzielen, die auf definierten Zielen basieren.
5. Sorge für ausreichende Infrastrukturkontrollen, um zu verhindern, dass das Modell auf unbeabsichtigte Datenquellen zugreift.
6. Verwende die Datenversionskontrolle (DVC), um Änderungen an Datensätzen zu verfolgen und Manipulationen zu erkennen. Die Versionskontrolle ist wichtig, um die Integrität des Modells zu erhalten.
7. Speichere die von den Nutzern bereitgestellten Informationen in einer Vektordatenbank, damit Anpassungen möglich sind, ohne das gesamte Modell neu zu trainieren.
8. Teste die Robustheit des Modells mit Red-Team-Kampagnen und gegnerischen Techniken, wie z. B. föderiertes Lernen, um die Auswirkungen von Datenstörungen zu minimieren.
9. Überwache den Trainingsverlust und analysiere das Modellverhalten auf Anzeichen von Poisoning. Verwende Schwellenwerte, um anomale Ergebnisse zu erkennen.
10. Integriere während der Inferenz Retrieval-Augmented Generation (RAG) und Grounding-Techniken, um das Risiko von Halluzinationen zu verringern.

### Beispiele für Angriffsszenarien

#### Szenario #1
  Ein Angreifer verfälscht die Ergebnisse des Modells, indem er Trainingsdaten manipuliert oder Prompt-Injection-Techniken einsetzt und so Fehlinformationen verbreitet.
#### Szenario #2
  Schadhafte Daten ohne angemessene Filterung können zu schädlichen oder verzerrten Ergebnissen führen und gefährliche Informationen verbreiten.
#### Szenario #3
  Ein böswilliger Akteur oder Konkurrent erstellt gefälschte Dokumente für das Training, was zu Modellausgaben führt, die diese Ungenauigkeiten widerspiegeln.
#### Szenario #4
  Unzureichende Filterung ermöglicht es einem Angreifer, irreführende Daten über Prompt Injection einzufügen, was zu kompromittierten Ergebnissen führt.
#### Szenario #5
  Ein Angreifer nutzt Poisoning-Techniken, um einen Backdoor-Trigger in das Modell einzufügen. Dadurch kann es zu einer Umgehung der Authentifizierung, zur Datenexfiltration oder zur Ausführung versteckter Befehle kommen.

### Referenzlinks

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**
10. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
11. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models) **Cobalt**

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt findest du umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
