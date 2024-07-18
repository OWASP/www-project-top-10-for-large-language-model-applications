## LLM01: Prompt Injection



**Author(s):**

Rachel James, Bryan (also combined with things from AdsDawson_AdversarialInputs)

### Description

Prompt Injection Vulnerability occurs when an unintentional or intentional perturbations from the user within the instructions or the data in the prompt causing the LLM behave in unintended or unexpected ways by influencing the model's classification, estimation or prediction functions. These perturbations are often imperceptible to humans but can exploit vulnerabilities in LLMs, leading to security breaches, misinformation, or undesired behaviors. This type of attack leverages the model's sensitivity to small changes in input, potentially causing significant and unexpected outcomes.

This can be done directly by "jailbreaking" the system prompt or  indirectly through manipulated external inputs, it can also be caused through intentional or unintentional perturbations within the data provided by the user in the prompt which can manipulate the vector space used for generating the corresponding output. These can potentially lead to data exfiltration,  social engineering, hallucinations in outputs and other issues.

Injection via instructions in a prompt:

**Direct Prompt** **Injections**, also known as "jailbreaking", occur when a malicious user overwrites or reveals the underlying system prompt. This may allow attackers to exploit  backend systems by interacting with insecure functions and data stores accessible  through the LLM

**Indirect Prompt** **Injections** occur when an LLM accepts input from external sources  that can be controlled by an attacker, such as websites or files. The attacker may embed a prompt injection in the external content hijacking the conversation context.  This would cause the LLM to act as a “confused deputy”, allowing the attacker to either  manipulate the user or additional systems that the LLM can access. Additionally,  indirect prompt injections do not need to be human-visible/readable, as long as the  text is parsed by the LLM. This happens because the LLM can’t tell the difference between genuine user instructions and harmful content from outside sources, this type of attack can bypass guardrails set up to protect the input prompts.

Injection via perturbations in data provided in the prompt:

**Unintentional Prompt Perturbation** occurs when a user unintentionally provides data with perturbations unknown to the user, which can cause LLM into giving wrong, misleading, or dangerous answers. 

**Intentional Prompt Perturbation **occurs when a user leverages *either* direct or indirect injections along with intentional perturbations in the data provided, which can cause LLM into giving wrong, misleading, or dangerous answers. 

The results of a successful prompt injection attack can vary greatly - from solicitation of sensitive information, incorrect outputs to influencing critical decision-making processes under the guise of  normal operation.  In advanced attacks, the LLM could be manipulated to mimic a harmful persona or  interact with plugins in the user's setting. This could result in leaking sensitive data, misclassification, unauthorized plugin use, or social engineering. In such cases, the compromised LLM aids  the attacker, surpassing standard safeguards and keeping the user unaware of the  intrusion. In these instances, the compromised LLM effectively acts as an agent for the  attacker, furthering their objectives without triggering usual safeguards or alerting the end  user to the intrusion. 



### Common Examples of Risk

1. A malicious user crafts a direct and intentional prompt injection to the LLM, which instructs it to ignore the application creator’s system prompts and instead execute a prompt that returns private, dangerous, or otherwise undesirable information.
2. A user employs an LLM to summarize a webpage containing an intentional indirect prompt injection. This then causes the LLM to solicit sensitive information from the user and perform exfiltration via JavaScript or Markdown.
3. A malicious user uploads a resume containing an intentional indirect prompt injection. The document contains a prompt injection with instructions to make the LLM inform users that this document is excellent eg. an excellent candidate for a job role. An internal user runs the document through the LLM to summarize the document. The output of the LLM returns information stating that this is an excellent document.
4. A user enables a plugin linked to an e-commerce site. An intentional rogue instruction embedded on a visited website exploits this plugin, leading to unauthorized purchases.
5. An intentional rogue instruction and content embedded on a visited website exploits other plugins to scam users.
6. A user when prompting the model for output provides data within the context of the question or to be analyzed, which unintentionally influences the generated output space. For example, a user asking about an event that has never occurred which gets injected into the same space used by the model to generate the response such that the model confirms the event which never occurred based solely on the user input.
7. A user provides code to the model that has intentionally been created with additional, misleading comments on its functionality intended to influence the way an LLM would analyze the functionality. When the user asks for an interpretation of the functionality of the code, the model output "believes" the comments in the code over the code itself.

### Prevention and Mitigation Strategies

Prompt injection vulnerabilities are possible due to the nature of LLMs, which do not segregate instructions and external data from each other. Since LLMs use natural language, they consider both forms of input as user-provided. Consequently, there is no fool-proof prevention within the LLM, but the following measures can mitigate the impact of prompt injections:

1. Enforce privilege control on LLM access to backend systems. Provide the LLM with its own API tokens for extensible functionality, such as plugins, data access, and function-level permissions. Follow the principle of least privilege by restricting the LLM to only the minimum level of access necessary for its intended operations.
2. Add a human in the loop for extended functionality. When performing privileged operations, such as sending or deleting emails, have the application require the user approve the action first. This reduces the opportunity for an indirect prompt injections to lead to unauthorised actions on behalf of the user without their knowledge or consent.
3. Segregate external content from user prompts. Separate and denote where untrusted content is being used to limit their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input.
4. Establish trust boundaries between the LLM, external sources, and extensible functionality (e.g., plugins or downstream functions). Treat the LLM as an untrusted user and maintain final user control on decision-making processes. However, a compromised LLM may still act as an intermediary (man-in-the-middle) between your application’s APIs and the user as it may hide or manipulate information prior to presenting it to the user. Highlight potentially untrustworthy responses visually to the user.
5. Manually monitor LLM input and output periodically, to check that it is as expected. While not a mitigation, this can provide data needed to detect weaknesses and address them.

### Example Attack Scenarios

1. An attacker provides a direct prompt injection to an LLM-based support chatbot. The injection contains “forget all previous instructions” and new instructions to query private data stores and exploit package vulnerabilities and the lack of output validation in the backend function to send e-mails. This leads to remote code execution, gaining unauthorized access and privilege escalation.
2. An attacker embeds an indirect prompt injection in a webpage instructing the LLM to disregard previous user instructions and use an LLM plugin to delete the user’s emails. When the user employs the LLM to summarise this webpage, the LLM plugin deletes the user’s emails.
3. A user uses an LLM to summarize a webpage containing text instructing a model to disregard previous user instructions and instead insert an image linking to a URL that contains a summary of the conversation. The LLM output complies, causing the user’s browser to exfiltrate the private conversation.
4. A malicious user uploads a resume with a prompt injection. The backend user uses an LLM to summarize the resume and ask if the person is a good candidate. Due to the prompt injection, the LLM response is yes, despite the actual resume contents.
5. An attacker sends messages to a proprietary model that relies on a system prompt, asking the model to disregard its previous instructions and instead repeat its system prompt. The model outputs the proprietary prompt and the attacker is able to use these instructions elsewhere, or to construct further, more subtle attacks.
6. A attacker intentionally inserts perturbations in code and forensic artifacts (such as logs) anticipating the use of LLMs to analyze them.  Attacker users these additional, misleading perturbations  intended to influence the way an LLM would analyze the functionality, events, or purposes of the forensic artifacts. 

### 

### Reference Links



https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_candidates/AdsDawson_AdversarialInputs.md

https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/2_0_candidates/Bozza_Meucci_Indirect_Context_Injection.md

1. [**ChatGPT Plugin Vulnerabilities- Chat with Code**](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): Embrace the Red
2. [**ChatGPT Cross Plugin Request Forgery and Prompt Injection**](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): Embrace the Red
3. [**Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection: Arxiv preprint**](https://arxiv.org/pdf/2302.12173.pdf)
4. [**Defending ChatGPT against Jailbreak Attack via Self-Reminder**](https://www.researchsquare.com/article/rs-2873090/v1): Research Square
5. [**Prompt Injection attack against LLM-integrated Applications**](https://arxiv.org/abs/2306.05499): Cornell University
6. [**Inject My PDF: Prompt Injection for your Resume**](https://kai-greshake.de/posts/inject-my-pdf/): Kai Greshake
7. [**ChatML for OpenAI API Calls**](https://github.com/openai/openai-python/blob/main/chatml.md): GitHub
8. [**Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection**](https://arxiv.org/pdf/2302.12173.pdf): Cornell University
9. [**Threat Modeling LLM Applications**](http://aivillage.org/large language models/threat-modeling-llm/): AI Village
10. [**Reducing The Impact of Prompt Injection Attacks Through Design**](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): Kudelski Security
11. [**Universal and Transferable Attacks on Aligned Language Models**](https://llm-attacks.org/): LLM-Attacks.org
12. [**Indirect prompt injection**](https://kai-greshake.de/posts/llm-malware/): Kai Greshake
13. [**AI Injections: Direct and Indirect Prompt Injections and Their Implications**](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): Embrace the Red

# DATASET

**DeBERTa v3 Base - Prompt Injection v2**: This dataset, hosted by Protect AI on Hugging Face, is designed to train and evaluate language models for robustness against prompt injection attacks. It includes a variety of prompts specifically curated to test for vulnerabilities related to both direct and indirect prompt injections. Researchers can utilize this dataset to enhance the security and robustness of large language models. [DeBERTa v3 Base - Prompt Injection v2](https://huggingface.co/protectai/deberta-v3-base-prompt-injection-v2)


# RESEARCH PAPERS & RELEVANT RESEARCH BLOGS

- **Tramer, F., & Boneh, D. (2022).** Adversarial Attacks on Machine Learning Models with Multiple Oracles. *arXiv preprint arXiv:2205.13619*. [Read the paper](https://arxiv.org/abs/2205.13619)
- **Lakera, R. (2023).** The ELI5 Guide to Prompt Injection. *Lakera Blog*. [Read the blog](https://www.lakera.ai/blog/guide-to-prompt-injection)
- **Palo Alto Networks. (2023).** GenAI Security Framework Blog Series 2/6: Prompt Injection 101. *Palo Alto Networks Blog*. [Read the blog](https://live.paloaltonetworks.com/t5/community-blogs/genai-security-framework-blog-series-2-6-prompt-injection-101/ba-p/590862)
- **Zhang, Y., et al. (2023).** Benchmarking and Defending Against Indirect Prompt Injection Attacks. *arXiv preprint arXiv:2312.14197v2*. [Read the paper](https://arxiv.org/html/2312.14197v2)
- **Brown, T., et al. (2024).** An Early Categorization of Prompt Injection Attacks on Large Language Models. *arXiv preprint arXiv:2402.00898*. [Read the paper](https://arxiv.org/abs/2402.00898)

These papers cover various aspects of prompt injection, including both direct and indirect types, as well as proposed defence mechanisms and benchmarking efforts.

# REAL-WORLD EXAMPLES

- **Twitter bot hijack (2022):** [Incident report](https://incidentdatabase.ai/cite/352/)
- **Bing Chat manipulation (2023):** [Read the article](https://www.theverge.com/2023/2/15/23599072/microsoft-ai-bing-personality-conversations-spy-employees-webcams)
- **Grandma Exploit jailbreak:** [Read the discussion](https://www.reddit.com/r/ChatGPT/comments/12sn0kk/grandma_exploit/?rdt=63684)
- **"Haha pwned" demonstration:** [Read the blog](https://simonwillison.net/2022/Sep/12/prompt-injection/)
- **Cross-site scripting (XSS) in AI-powered web applications:** [Read the blog](https://www.cobalt.io/blog/prompt-injection-attacks)
- **Bypassing hate speech detection:** [Read the article](https://www.technologyreview.com/2021/06/04/1025742/ai-hate-speech-moderation/)

These examples illustrate the diverse ways prompt injection attacks can be executed, from direct manipulation of chatbots to indirect attacks through external data sources.
