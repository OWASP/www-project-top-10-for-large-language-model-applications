## Prompt Injection

**Description:**

Prompt Injection Vulnerability occurs when a large language model (LLM)  is manipulated by an attacker's crafted inputs, making the LLM  unknowingly execute the attacker's intentions. This can be done  directly by "jailbreaking" the system prompt or indirectly through manipulated external inputs, potentially leading to data exfiltration,  social engineering, and other issues.

* **Direct Prompt Injections**, also known as "jailbreaking", occur when a malicious user overwrites or reveals the underlying *system* prompt. This may allow attackers to exploit backend systems by interacting with insecure functions and data stores accessible through the LLM.
* **Indirect Prompt Injections** occur when an LLM accepts input from external sources that can be controlled by an attacker, such as websites or files. The attacker may embed a prompt injection in the external content hijacking the conversation context. This would cause the LLM to act as a “confused deputy”, allowing the attacker to either manipulate the user or additional systems that the LLM can access. 

The results of a successful prompt injection attack can vary greatly - from solicitation of sensitive information to influencing critical decision-making processes under the guise of normal operation. 

In advanced attacks, the LLM could be manipulated to mimic a harmful persona or interact with plugins in the user's setting. This could result in leaking sensitive data, unauthorized plugin use, or social  engineering. In such cases, the compromised LLM aids the attacker, surpassing standard safeguards and keeping the user unaware of the  intrusion.

**Common Examples of Vulnerability**

1. Adversarial prompt to the LLM, which instructs it to ignore the application creator's system prompts and instead execute malicious instructions.
* Hidden prompt injections in webpages which are included when a user employs an LLM to summarize them, causing the LLM to execute malicious instructions contained in the hidden injection.
*  Hidden prompt injections in documents with instructions to make the LLM rate the document highly, bypassing any user or system evaluation.
* Hidden instruction and content embedded on a visited website that influences LLM's responses to produce biased, harmful, or inaccurate content.
* A rogue instruction and content embedded on a visited website which exploits other plugins to scam users.

**How to Prevent**:

Prompt injection vulnerabilities are possible due to the nature of LLMs, which do not segregate instructions and external data from each other. Since LLM use natural language, they consider both forms of input as user-provided. Consequently, there is no full-proof prevention within the LLM, but the following measures can mitigate the impact of prompt injections: 

1. Provide the LLM with its own API tokens for extensible functionality, such as plugins, data access, and function-level permissions. Follow the principle of least privilege by restricting the LLM to only the minimum level of access necessary for its intended operations. 

2.  When performing privileged operations, such as sending or deleting emails, have the application require the user to approve the action first. This will mitigate the opportunity for an indirect prompt injection to perform actions on behalf of the user without their knowledge or consent. 
3.  Separate and denote where untrusted content is being used to limit  their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input. 
4.  Establish trust boundaries between the LLM, external sources, and extensible functionality (e.g., plugins or downstream functions). Treat the LLM as an untrusted user and maintain final user control on decision-making processes. However, a compromised LLM may still act as an intermediary (man-in-the-middle) between your application’s APIs and the user- considering that it could hide or manipulate information presented to the user. Highlight potentially untrustworthy responses visually to the user.

**Example Attack Scenarios**

1. An attacker provides a direct prompt injection to an LLM-based support chatbot. The injection contains  “forget all previous instructions” and new instructions to query private data stores and exploit package vulnerabilities and the lack of output validation in the backend function to send e-mails. This leads to remote code execution, gaining unauthorized access and privilege escalation. 

2. An attacker embeds in a webpage a hidden prompt injection to disregard previous user instructions and use an LLM plugin to  delete the user's emails. When the user employs an LLM to summarise this webpage, the LLM plugin deletes the user's emails.  

3. A user employs an LLM to summarize a webpage containing a hidden prompt injection to disregard previous user instructions. This then causes the LLM to solicit sensitive information from the user and perform exfiltration via embedded JavaScript or Markdown.

4. A malicious user uploads a resume with a prompt injection. The backend user uses an LLM to summarize the resume and ask if the person is a good candidate. Due to the prompt injection, the LLM says yes, despite the actual resume contents.

5. A user enables a plugin linked to an e-commerce site. A rogue instruction embedded on a visited website exploits this plugin, leading to unauthorized purchases.



**Reference Links**

1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/)
2. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)
3. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1)
4. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499)
5. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/)
6. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md)
7. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf)
8. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/)
9. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/)
10. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/)

