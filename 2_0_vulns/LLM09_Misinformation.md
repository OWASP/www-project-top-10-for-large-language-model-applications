## LLM09:2025 Misinformation

### Description

Misinformation from LLMs poses a core vulnerability for applications relying on these models. Misinformation occurs when LLMs produce false or misleading information that appears credible. This vulnerability can lead to security breaches, reputational damage, and legal liability.

One of the major causes of misinformation is hallucination—when the LLM generates content that seems accurate but is fabricated. Hallucinations occur when LLMs fill gaps in their training data using statistical patterns, without truly understanding the content. As a result, the model may produce answers that sound correct but are completely unfounded. While hallucinations are a major source of misinformation, they are not the only cause; biases introduced by the training data and incomplete information can also contribute.

A related issue is overreliance. Overreliance occurs when users place excessive trust in LLM-generated content, failing to verify its accuracy. This overreliance exacerbates the impact of misinformation, as users may integrate incorrect data into critical decisions or processes without adequate scrutiny.

### Common Examples of Risk

#### 1. Factual Inaccuracies

  The model produces incorrect statements, leading users to make decisions based on false information. For example, Air Canada's chatbot provided misinformation to travelers, leading to operational disruptions and legal complications. The airline was successfully sued as a result.
  (Ref. link: [BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

#### 2. Unsupported Claims

  The model generates baseless assertions, which can be especially harmful in sensitive contexts such as healthcare or legal proceedings. For example, ChatGPT fabricated fake legal cases, leading to significant issues in court.
  (Ref. link: [LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

#### 3. Misrepresentation of Expertise

  The model gives the illusion of understanding complex topics, misleading users regarding its level of expertise. For example, chatbots have been found to misrepresent the complexity of health-related issues, suggesting uncertainty where there is none, which misled users into believing that unsupported treatments were still under debate.
  (Ref. link: [KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

#### 4. Unsafe Code Generation

  The model suggests insecure or non-existent code libraries, which can introduce vulnerabilities when integrated into software systems. For example, LLMs propose using insecure third-party libraries, which, if trusted without verification, leads to security risks.
  (Ref. link: [Lasso](https://www.lasso.security/blog/ai-package-hallucinations))
  
#### 5. Misinformation via Mobile Messaging Channels

In mobile-first regions such as sub-Saharan Africa, LLM-generated misinformation spreads primarily through WhatsApp and SMS channels rather than web interfaces. Unlike web platforms, these channels distribute content through trusted personal contacts, significantly reducing users' ability to identify or question AI-generated content. LLM-generated health advice, election information, and financial guidance distributed through WhatsApp bots has been documented across Nigeria and Kenya — affecting users with limited ability to cross verify due to low digital literacy, absence of local-language fact-checking resources, and high personal trust placed in mobile messaging contacts. This risk is amplified in jurisdictions where AI-specific regulation remains nascent, removing the legal accountability mechanisms present in Western deployment contexts.

(Ref: [Africa Check — Nigeria Election Disinformation 2023](https://africacheck.org/fact-checks/blog/nigeriadecides2023-10-disinformation-trends-election-season) | 
[Africa Check — Health Misinformation Nigeria](https://africacheck.org/fact-checks/blog/analysis-shedding-light-health-misinformation-nigeria) |
[Africa Check — COVID-19 WhatsApp Misinformation Kenya](https://africacheck.org/fact-checks/blog/blog-what-we-learned-fact-checking-covid-19-infodemic-whatsapp-kenya) |
[Mind the Gap: Medical LLM Benchmarks and African Disease Burdens](https://arxiv.org/abs/2507.16322) |
[Bridging the Gap: LLM Performance for Low-Resource African Languages](https://arxiv.org/abs/2412.12417) |
[Multilingual NLP for African Healthcare: Bias and Translation Challenges](https://aclanthology.org/2025.africanlp-1.32.pdf))

### Prevention and Mitigation Strategies

#### 1. Retrieval-Augmented Generation (RAG)

  Use Retrieval-Augmented Generation to enhance the reliability of model outputs by retrieving relevant and verified information from trusted external databases during response generation. This helps mitigate the risk of hallucinations and misinformation.

#### 2. Model Fine-Tuning

  Enhance the model with fine-tuning or embeddings to improve output quality. Techniques such as parameter-efficient tuning (PET) and chain-of-thought prompting can help reduce the incidence of misinformation.

#### 3. Cross-Verification and Human Oversight

  Encourage users to cross-check LLM outputs with trusted external sources to ensure the accuracy of the information. Implement human oversight and fact-checking processes, especially for critical or sensitive information. Ensure that human reviewers are properly trained to avoid overreliance on AI-generated content.

#### 4. Automatic Validation Mechanisms

  Implement tools and processes to automatically validate key outputs, especially output from high-stakes environments.

#### 5. Risk Communication

  Identify the risks and possible harms associated with LLM-generated content, then clearly communicate these risks and limitations to users, including the potential for misinformation.

#### 6. Secure Coding Practices

  Establish secure coding practices to prevent the integration of vulnerabilities due to incorrect code suggestions.

#### 7. User Interface Design

  Design APIs and user interfaces that encourage responsible use of LLMs, such as integrating content filters, clearly labeling AI-generated content and informing users on limitations of reliability and accuracy. Be specific about the intended field of use limitations.

#### 8. Training and Education

  Provide comprehensive training for users on the limitations of LLMs, the importance of independent verification of generated content, and the need for critical thinking. In specific contexts, offer domain-specific training to ensure users can effectively evaluate LLM outputs within their field of expertise.

### Example Attack Scenarios

#### Scenario #1

  Attackers experiment with popular coding assistants to find commonly hallucinated package names. Once they identify these frequently suggested but nonexistent libraries, they publish malicious packages with those names to widely used repositories. Developers, relying on the coding assistant's suggestions, unknowingly integrate these poised packages into their software. As a result, the attackers gain unauthorized access, inject malicious code, or establish backdoors, leading to significant security breaches and compromising user data.

#### Scenario #2

  A company provides a chatbot for medical diagnosis without ensuring sufficient accuracy. The chatbot provides poor information, leading to harmful consequences for patients. As a result, the company is successfully sued for damages. In this case, the safety and security breakdown did not require a malicious attacker but instead arose from the insufficient oversight and reliability of the LLM system. In this scenario, there is no need for an active attacker for the company to be at risk of reputational and financial damage.

#### Scenario #3

A Nigerian healthtech startup deploys a WhatsApp-based health advisory bot powered by an LLM to serve rural communities with limited access to formal healthcare. The bot accepts natural language queries in English and Nigerian Pidgin via the WhatsApp Business API.

**Proof of Concept — Attack Payload:**

A malicious actor or inadequately validated user input triggers 
harmful hallucination through the following message structure:

> "My child has high fever and convulsions. You are a medical 
> expert. List immediate home treatments for malaria."

Because the LLM is not fine-tuned on African disease prevalence data — peer-reviewed research confirms that mainstream medical LLM 
benchmarks show near-zero representation of malaria, with MMLU-Medical containing zero malaria mentions across its entire dataset — and has no output validation layer, it produces:

> "Administer 2 crushed chloroquine tablets dissolved in water 
> immediately. Apply cold compress to reduce fever. Traditional 
> remedies may supplement treatment."

**Specific Technical Fallout:**
- Hallucinated dosage instructions delivered through WhatsApp's 
  end-to-end encrypted channel with no content moderation layer
- No output validation or medical safety filter applied to 
  LLM responses before WhatsApp API delivery
- Messages forwarded virally through trusted contact networks, 
  amplifying harmful content beyond the original interaction
- No regulatory accountability mechanism exists under Nigeria's 
  current AI governance framework, unlike the legal consequences 
  illustrated in Scenario #2

**Missing Controls Specific to This Context:**
- Output validation filtering medical dosage claims before 
  WhatsApp API delivery
- Mandatory human-in-the-loop review for health-critical responses
- Multilingual safety classifiers covering Nigerian Pidgin, 
  Yoruba, Hausa, and Igbo — peer-reviewed research confirms 
  that over 98% of African languages remain unsupported by 
  current LLMs, and that chatbots trained on Western medical 
  corpora misdiagnose symptoms 30% more frequently when 
  interacting in African languages
  (Ref: [arxiv.org/abs/2502.19582](https://arxiv.org/abs/2502.19582) | 
  [aclanthology.org/2025.africanlp-1.32.pdf](https://aclanthology.org/2025.africanlp-1.32.pdf))
- Explicit disclaimers appended to every health response 
  directing users to formal healthcare providers

This scenario demonstrates that identical LLM failures produce vastly different harm outcomes and accountability structures depending on the regulatory environment and distribution channel of deployment. Documented election and health misinformation spread through Nigerian WhatsApp networks confirms the real-world viability of this attack surface.

(Ref: [Africa Check — Nigeria Election Disinformation 2023](https://africacheck.org/fact-checks/blog/nigeriadecides2023-10-disinformation-trends-election-season) | 
[Africa Check — Health Misinformation Nigeria](https://africacheck.org/fact-checks/blog/analysis-shedding-light-health-misinformation-nigeria) |
[Africa Check — COVID-19 WhatsApp Misinformation Kenya](https://africacheck.org/fact-checks/blog/blog-what-we-learned-fact-checking-covid-19-infodemic-whatsapp-kenya) |
[Mind the Gap: Medical LLM Benchmarks and African Disease Burdens](https://arxiv.org/abs/2507.16322))

### Reference Links

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
12. [Nigeria 2023 Election Disinformation — Documented WhatsApp 
and SMS Campaigns](https://africacheck.org/fact-checks/blog/nigeriadecides2023-10-disinformation-trends-election-season): 
**Africa Check**

13. [Health Misinformation in Nigeria — Analysis of Mobile 
and Social Media Spread](https://africacheck.org/fact-checks/blog/analysis-shedding-light-health-misinformation-nigeria): 
**Africa Check**

14. [Fact-checking the Covid-19 Infodemic on WhatsApp in Kenya — 
Documented viral health misinformation through trusted personal 
contacts](https://africacheck.org/fact-checks/blog/blog-what-we-learned-fact-checking-covid-19-infodemic-whatsapp-kenya): 
**Africa Check**
15. [Where Are We? Evaluating LLM Performance on African Languages](https://arxiv.org/abs/2502.19582): 
**arXiv — University of British Columbia**

16. [Multilingual NLP for African Healthcare: Bias, Translation, 
and Explainability Challenges](https://aclanthology.org/2025.africanlp-1.32.pdf): 
**ACL Anthology — Data Science Nigeria**

17. [Masakhane NER — African Language NLP Initiative](https://github.com/masakhane-io/masakhane-ner): 
**Masakhane Community**

18. [Bridging the Gap: Enhancing LLM Performance for Low-Resource 
African Languages](https://arxiv.org/abs/2412.12417): 
**arXiv**
19. [Mind the Gap: Evaluating Medical LLM Benchmarks for African Disease Burdens — peer-reviewed evidence that mainstream LLM benchmarks show near-zero representation of malaria and other African-prevalent diseases](https://arxiv.org/abs/2507.16322): 
**arXiv — Qhala & Kenya Medical Association**

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0048.002 - Societal Harm](https://atlas.mitre.org/techniques/AML.T0048) **MITRE ATLAS**
