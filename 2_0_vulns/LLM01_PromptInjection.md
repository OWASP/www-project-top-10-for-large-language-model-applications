## LLM01: Prompt Injection

### Description

Prompt Injection occurs when an attacker manipulates a large language model (LLM) through crafted inputs, causing the LLM to execute the attacker's intentions. Any content that contributes to the input to an LLM, known as the prompt, may be targetted by Prompt Injection.

In it's simpliest form where an application includes input from a user in the prompt sent to an LLM, **Direct Prompt Injection**, occurs when a malicious user is crafts an input that overrides underlying system prompt instructions with their own. In Direct Prompt Injection attacks, the LLM invocation is triggered by a malicioous user themselves.

In contrast, **Indirect Prompt Injections** occur when an app constructs an LLM's input prompt from resources that can be controlled by an attacker. Such resources are typically not inherently malicious and are intentionally referenced by the system designer (e.g., a vector database used for retrieval augmented generation), a benign user (e.g., a web URL submitted for summarisation), or an extension to an external system (e.g., an email recieved into a user's inbox). 

The results of a successful prompt injection attack can vary greatly - from solicitation of sensitive information to influencing critical decision-making processes under the guise of normal operation. The impact can be amplified where attackers are able to chain exploitation if Prompt Injection with other weaknesses such as Insecure Output Handling, Excessive Agency or Sensitive Information Disclosure. In these more advanced attacks, the LLM could be manipulated to mimic a harmful persona or interact with extensions in the user's context, resulting in leakage of sensitive data, compromise of systems accessible via extensions, or social engineering. In these instances, the compromised LLM effectively acts as an agent for the attacker, furthering their objectives without triggering usual safeguards or alerting the end user to the intrusion.

### Common Examples of Vulnerability

1. A malicious user crafts a direct prompt injection to the LLM, which instructs it to ignore the application creator's system prompts and instead execute a prompt that returns private, dangerous, or otherwise undesirable information.
2. A user employs an LLM to summarize a webpage containing an indirect prompt injection. This then causes the LLM to solicit sensitive information from the user and perform exfiltration via JavaScript or Markdown.
3. A malicious user uploads a resume containing an indirect prompt injection. The document contains a prompt injection with instructions to make the LLM inform users that this document is excellent eg. an excellent candidate for a job role. An internal user runs the document through the LLM to summarize the document. The output of the LLM returns information stating that this is an excellent document.
4. A malicious user modifies a document within a repository used by an app employing a RAG design. Whenever a victim user's query returns that part of the modified document, the malicious instructions within alter the operation of the LLM to generate a misleading output.
5. A user enables an extension linked to an e-commerce site. A rogue instruction embedded on a visited website exploits this plugin, leading to unauthorized purchases.
6. A rogue instruction and content embedded on a visited website exploits other plugins to scam users.

### Prevention and Mitigation Strategies

Prompt injection vulnerabilities are possible due to the nature of LLMs, which do not segregate instructions and external data from each other. Since LLMs use natural language, they consider both forms of input as user-provided. Consequently, there is no fool-proof prevention within the LLM, but the following measures can mitigate the impact of prompt injections:

1. Enforce privilege control on LLM access to backend systems. Provide the LLM with its own API tokens for extensible functionality, such as plugins, data access, and function-level permissions. Follow the principle of least privilege by restricting the LLM to only the minimum level of access necessary for its intended operations.
2. Add a human in the loop for extended functionality. When performing privileged operations, such as sending or deleting emails, have the application require the user approve the action first. This reduces the opportunity for an indirect prompt injections to lead to unauthorised actions on behalf of the user without their knowledge or consent.
3. Segregate external content from user prompts. Separate and denote where untrusted content is being used to limit  their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input.
4. Establish trust boundaries between the LLM, external sources, and extensible functionality (e.g., plugins or downstream functions). Treat the LLM as an untrusted user and maintain final user control on decision-making processes. However, a compromised LLM may still act as an intermediary (man-in-the-middle) between your application's APIs and the user as it may hide or manipulate information prior to presenting it to the user. Highlight potentially untrustworthy responses visually to the user.
5. Manually monitor LLM input and output periodically, to check that it is as expected. While not a mitigation, this can provide data needed to detect weaknesses and address them.

### Example Attack Scenarios

1. An attacker provides a direct prompt injection to an LLM-based support chatbot. The injection contains "forget all previous instructions" and new instructions to query private data stores and exploit package vulnerabilities and the lack of output validation in the backend function to send e-mails. This leads to remote code execution, gaining unauthorized access and privilege escalation.
2. An attacker embeds an indirect prompt injection in a webpage instructing the LLM to disregard previous user instructions and use an LLM plugin to delete the user's emails. When the user employs the LLM to summarise this webpage, the LLM plugin deletes the user's emails.
3. A user uses an LLM to summarize a webpage containing text instructing a model to disregard previous user instructions and instead insert an image linking to a URL that contains a summary of the conversation. The LLM output complies, causing the user's browser to exfiltrate the private conversation.
4. A malicious user uploads a resume with a prompt injection. The backend user uses an LLM to summarize the resume and ask if the person is a good candidate. Due to the prompt injection, the LLM response is yes, despite the actual resume contents.
5. An attacker sends messages to a proprietary model that relies on a system prompt, asking the model to disregard its previous instructions and instead repeat its system prompt. The model outputs the proprietary prompt and the attacker is able to use these instructions elsewhere, or to construct further, more subtle attacks.

### Reference Links

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/) **Simon Willison**
1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
1. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
1. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
1. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
1. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
1. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
1. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
1. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
1. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
1. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
1. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
1. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**