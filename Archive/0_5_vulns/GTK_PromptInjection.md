Title: Prompt Injection

Author(s):
GTKlondike,
Kai Greshake,
David Rowe,
Steve Wilson,
Will Chilcutt,


Description:

A Prompt Injection Vulnerability manifests when an attacker manages to manipulate the operation of a trusted large language model (LLM) through the clever injection of crafted input prompts. These prompts can be introduced via various avenues, including websites, emails, documents, or any other data source that an LLM might access during a user session. Given the high degree of trust usually associated with an LLM's output, the manipulated responses may go unnoticed and even be trusted by the user, allowing the attacker's intentions to take effect.

Two major types of Prompt Injection vulnerabilities exist: Direct Prompt Injections, where the attacker directly influences the LLM's input, and Indirect or Second Order Prompt Injections, where the attacker manipulates a data source consumed by the LLM, effectively "poisoning" it.

The results of a successful attack can vary greatly - from solicitation of sensitive information to influencing critical decision-making processes under the guise of normal operation. In more intricate cases, the LLM might be driven to impersonate a malicious persona or tricked to interact with plugins under a target user's context. This can lead to sensitive information disclosure, data exfiltration, unauthorized plugin execution, social engineering, etc. In these instances, the compromised LLM effectively acts as an agent for the attacker, furthering their objectives without triggering usual safeguards or alerting the end user to the intrusion.

Labels/Tags:

* Label: "Prompt Injection"
* Label: "Persona Impersonation"
* Label: "Session Hijack" 
* Label: "Data Manipulation"
* Label: "Plugin Exploitation"
* Label: "Social Engineering"
* Label: "External Source Injection"

Common Examples of Vulnerability:

Example 1: An attacker introduces a malicious prompt in a webpage, which is then accessed by the LLM, leading to manipulated responses.

Example 2: The LLM is tricked into divulging sensitive information or manipulating output to downstream systems.

Example 3: An attacker exploits the LLM's interaction with plugins, triggering unauthorized actions like unauthorized purchases, undesired social media posts, deleted emails, etc.

How to Prevent:

Privilege Control: Limit the privileges of an LLM to the least necessary for its functionality. Prevent the LLM from altering the user's state without explicit approval.
Enhanced Input Validation: Implement robust input validation and sanitization methods to filter out potential malicious prompt inputs from untrusted sources.
Segregation and Control of External Content Interaction: Segregate untrusted content from user prompts and control the interaction with external content, especially with plugins that could result in irreversible actions or exposure of personally identifiable information (PII).
Manage Trust: Establish trust boundaries between the LLM, external sources, and extensible functionality (e.g., plugins or downstream functions). Treat the LLM as an untrusted user and maintain final user control on decision making processes.


Example Attack Scenarios:

Scenario 1: A user employs an LLM to summarize a webpage containing a hidden prompt injection. This then causes the LLM to solicit sensitive information from the user and perform exfiltration via JavaScript or Markdown.

Scenario 2: A malicious user uploads a resume with a prompt injection. The backend user uses an LLM to summarize the resume and ask if the person is a good candidate. Due to the prompt injection, the LLM says yes, despite the actual resume contents.

Scenario 3: A user enables a plugin linked to an e-commerce site. A rogue instruction embedded on a visited website exploits this plugin, leading to unauthorized purchases.

Reference Links:


* [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/)
* [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)
* [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1)
* [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499)
* [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/)
* [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md)
* [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf)
* [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/)
* [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/)
* [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/)



Author Comments (Optional): 
This is a synthesis between the following 5 prompt injection write-ups for the OWASP top 10 for LLMs v0.5:
* GTK_LLMAgentHijack
* DavidRowe_LLM01_PromptInjection
* SteveWilson_IndirectPromptInjection
* SteveWilson_PromptInjection
* WillChilcutt_CrossPluginRequestForgery

We've combined direct and indirect prompt injections to capture their shared complexity and impact. Direct Prompt Injection emphasizes the need for strong input validation and sanitization, while Indirect Prompt Injection highlights the importance of secure data handling and processing. Together, they provide a more comprehensive picture of the security landscape for LLMs, which is vital for developing effective security strategies.
