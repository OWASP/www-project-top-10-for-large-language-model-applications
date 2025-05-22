## LLM09:2025 Fehlinformationen

### Beschreibung

Fehlinformationen von LLMs stellen eine zentrale Schwachstelle für Anwendungen dar, die auf diesen Modellen basieren. Fehlinformationen treten auf, wenn LLMs falsche oder irreführende Informationen produzieren, die glaubwürdig erscheinen. Diese Schwachstelle kann zu Sicherheitsverletzungen, Rufschädigung und rechtlicher Haftung führen.

Eine der Hauptursachen für Fehlinformationen sind Halluzinationen – wenn das LLM Inhalte generiert, die zwar korrekt erscheinen, aber erfunden sind. Halluzinationen treten auf, wenn LLMs Lücken in seinen Trainingsdaten mithilfe statistischer Muster füllen, ohne den Inhalt wirklich zu verstehen. Infolgedessen kann das Modell Antworten liefern, die zwar korrekt klingen, aber völlig unbegründet sind. Halluzinationen sind zwar eine Hauptquelle für Fehlinformationen, aber nicht die einzige Ursache; auch durch die Trainingsdaten eingeführte Verzerrungen und unvollständige Informationen können dazu beitragen

Ein damit zusammenhängendes Problem ist die Übermäßige Abhängigkeit. Übermäßige Abhängigkeit tritt auf, wenn Benutzende den von LLM generierten Inhalten übermäßiges Vertrauen schenken und deren Richtigkeit nicht überprüfen. Diese Übermäßige Abhängigkeit verschärft die Auswirkungen von Fehlinformationen, da Personen möglicherweise falsche Daten in kritische Entscheidungen oder Prozesse einfließen lassen, ohne diese angemessen zu prüfen.

### Gängige Beispiele für Risiken

#### 1. Sachliche Ungenauigkeiten

  Das Modell erzeugt falsche Aussagen, was dazu führt, dass Benutzende Entscheidungen auf der Grundlage falscher Informationen treffen. So hat beispielsweise der Chatbot von Air Canada Reisenden Fehlinformationen gegeben, was zu Betriebsstörungen und rechtlichen Komplikationen führte. Die Fluggesellschaft wurde daraufhin erfolgreich verklagt.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

#### 2. Unbelegte Behauptungen

  Das Modell generiert unbegründete Behauptungen, die in sensiblen Bereichen wie dem Gesundheitswesen oder bei Gerichtsverfahren besonders schädlich sein können. So hat ChatGPT beispielsweise gefälschte Rechtsfälle erfunden, was zu erheblichen Problemen vor Gericht führte.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

#### 3. Falschdarstellung von Fachwissen

  Das Modell vermittelt den Eindruck, komplexe Themen zu verstehen, und täuscht die Benutzende hinsichtlich seines Fachwissens. Beispielsweise wurde festgestellt, dass Chatbots die Komplexität von Gesundheitsthemen falsch darstellen und Unsicherheit suggerieren, wo keine besteht, was die Benutzenden zu der Annahme verleitet, dass nicht unterstützte Behandlungen noch diskutiert werden.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

#### 4. Unsichere Code-Generierung

  Das Modell schlägt unsichere oder nicht vorhandene Code-Bibliotheken vor, die Schwachstellen verursachen können, wenn sie in Softwaresysteme integriert werden. Beispielsweise schlagen LLMs die Verwendung unsicherer Bibliotheken von Drittanbietern vor, was zu Sicherheitsrisiken führt, wenn man ihnen ohne Überprüfung vertraut.
  (Ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### Präventions- und Mitigationsstrategien

#### 1. Retrieval-Augmented Generation (RAG)

  Verwenden Sie Retrieval-Augmented Generation, um die Zuverlässigkeit der Modellausgaben zu erhöhen, indem während der Reaktionsgenerierung relevante und verifizierte Informationen aus vertrauenswürdigen externen Datenbanken abgerufen werden. Dies trägt dazu bei, das Risiko von Halluzinationen und Fehlinformationen zu minimieren.

#### 2. Model Fine-Tuning

  Verbessern Sie das Modell durch Fine-Tuning oder Embeddings, um die Ausgabequalität zu steigern. Nutzen Sie Techniken wie parameter-effizientes Tuning (PET) und Chain-of-Thought-Prompting, um das Auftreten von Fehlinformationen zu reduzieren.

#### 3. Kreuzverifizierung und menschliche Aufsicht

  Ermutigen Sie die Nutzenden, die LLM-Ausgaben mit vertrauenswürdigen externen Quellen abzugleichen, um die Richtigkeit der Informationen sicherzustellen. Implementieren Sie Prozesse zur manuellen Aufsicht und Faktenprüfung, insbesondere bei kritischen oder sensiblen Informationen. Stellen Sie sicher, dass menschliche Prüfer entsprechend geschult sind, um eine übermäßige Abhängigkeit von KI-generierten Inhalten zu vermeiden.

#### 4. Automatische Validierungsmechanismen

  Implementieren Sie Tools und Prozesse zur automatischen Validierung wichtiger Ergebnisse, insbesondere von Ergebnissen aus risikoreichen Umgebungen.

#### 5. Risikokommunikation

  Ermitteln Sie die Risiken und möglichen Schäden im Zusammenhang mit LLM-generierten Inhalten und kommunizieren Sie diese Risiken und Einschränkungen klar und deutlich an die Nutzenden, einschließlich des Potenzials für Fehlinformationen.

#### 6. Secure Coding-Praktiken

  Führen Sie sichere Codierungspraktiken ein, um die Integration von Schwachstellen aufgrund falscher Code-Vorschläge zu verhindern.

#### 7. Gestaltung der Benutzeroberfläche

  Gestalten Sie APIs und Benutzeroberflächen so, dass eine verantwortungsvolle Nutzung von LLMs gefördert wird, z. B. durch die Integration von Inhaltsfiltern, die eindeutige Kennzeichnung von KI-generierten Inhalten und die Information der Benutzer über Einschränkungen der Zuverlässigkeit und Genauigkeit. Gehen Sie dabei konkret auf die beabsichtigten Einschränkungen des Einsatzbereichs ein.

#### 8. Schulung und Ausbildung

  Bieten Sie umfassende Schulungen für Benutzenden zu den Einschränkungen von LLMs, der Bedeutung einer unabhängigen Überprüfung generierter Inhalte und der Notwendigkeit kritischen Denkens an. Bieten Sie in bestimmten Kontexten bereichsspezifische Schulungen an, um sicherzustellen, dass Benutzer die Ergebnisse von LLM in ihrem Fachgebiet effektiv bewerten können.

### Beispiele für Angriffsszenarien

#### Szenario 1

  Angreifende experimentieren mit beliebten Programmierassistenten, um häufig halluzinierte Paketnamen zu finden. Sobald sie diese häufig vorgeschlagenen, aber nicht vorhandenen Bibliotheken identifiziert haben, veröffentlichen sie bösartige Pakete mit diesen Namen in weit verbreiteten Repositories. Entwickelnde, die sich auf die Vorschläge des Programmierassistenten verlassen, integrieren diese präparierten Pakete unwissentlich in ihre Software. Dadurch erhalten Angreifende unbefugten Zugriff, injizieren Schadcode oder richten Hintertüren ein, was zu erheblichen Sicherheitsverletzungen führt und Benutzerdaten gefährdet.

#### Szenario 2

  Ein Unternehmen stellt einen Chatbot für medizinische Diagnosen zur Verfügung, ohne eine ausreichende Genauigkeit zu gewährleisten. Der Chatbot liefert unzureichende Informationen, was zu schädlichen Folgen für die Patienten führt. Infolgedessen wird das Unternehmen erfolgreich auf Schadensersatz verklagt. In diesem Fall war für den Sicherheits- und Schutzverstoß keine böswilligen Angreifende erforderlich, sondern er entstand durch die unzureichende Überwachung und Zuverlässigkeit des LLM-Systems. In diesem Szenario sind keine aktive Angreifende erforderlich, damit das Unternehmen dem Risiko eines Reputations- und finanziellen Schadens ausgesetzt ist.

### Referenzlinks

1. [AI Chatbots as Health Information Sources: Misrepresentation of Expertise](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [Air Canada Chatbot Misinformation: What Travellers Should Know](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT Fake Legal Cases: Generative AI Hallucinations](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **Techpolicy**
6. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [Diving Deeper into AI Package Hallucinations](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [How Secure is Code Generated by ChatGPT?](https://arxiv.org/abs/2304.09655): **Arvix**
9. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [A Framework for Exploring the Consequences of AI-Mediated Enterprise Knowledge](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**

### Verwandte Frameworks und Taxonomien

In diesem Abschnitt finden Sie umfassende Informationen, Szenarien, Strategien in Bezug auf die Bereitstellung von Infrastruktur, angewandte Umweltkontrollen und andere bewährte Verfahren.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
