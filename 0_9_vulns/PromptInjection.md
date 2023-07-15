## Title: Prompt Injection

**Description**
A Prompt Injection Vulnerability manifests when an attacker manages to manipulate the operation of a trusted large language model (LLM) through crafted inputs. This results in the LLM acting as a “confused deputy” on behalf of the attacker. Given the high degree of trust usually associated with an LLM's output, the manipulated responses may go unnoticed and even be trusted by the user, allowing the attacker's intentions to take effect. Prompt injections can be introduced via various avenues, including websites, emails, documents, or any other data source that an LLM might access during a user session. 
Prompt injections can occur either directly or indirectly: 
* **Direct Prompt Injection:** A direct prompt injection, also known as "jailbreaking", occurs when an malicious user overwrites or reveals the underlying *system* prompt. This could allow the malicious user to exploit backend systems by interacting with insecure functions and data stores accessible through the LLM.
* **Indirect Prompt Injection:** An indirect prompt injection occurs when an LLM accepts input from external sources that can be controlled by an attacker, such as from reading a website or an uploaded file. The attacker may embed a prompt injection on the website or uploaded file that hijacks the conversation context. This would cause the LLM to act as a “confused deputy”, allowing the attacker to either manipulate the user or additional systems that the LLM can access. 
The results of a successful prompt injection attack can vary greatly - from solicitation of sensitive information to influencing critical decision-making processes under the guise of normal operation. In more complex attacks, the LLM might be driven to impersonate a malicious persona or tricked to interact with plugins within the target user's context. This can lead to sensitive information disclosure, data exfiltration, unauthorized plugin execution, social engineering, etc. In these instances, the compromised LLM acts as an agent for the attacker, furthering their objectives while bypassing usual safeguards or alerting the end user to the intrusion.

**Common Examples of Vulnerability**
* **Example 1:** An attacker crafts an adversarial prompt to the LLM which instructs it to ignore the application creator's system prompts and instead execute a prompt that returns private, dangerous or otherwise undesirable information.
* **Example 2:** A user employs an LLM to summarize a webpage containing a hidden prompt injection. This then causes the LLM to solicit sensitive information from the user and perform exfiltration via JavaScript or Markdown.
* **Example 3:** A malicious user uploads a resume with a prompt injection. The document contains a prompt injection with instructions to make the LLM inform users that this document is an excellent document eg. excellent candidate for a job role. An internal user runs the document through the LLM to summarize the document. The output of the LLM returns information stating that this is an excellent document.
* **Example 4:** A user enables a plugin linked to an e-commerce site. A rogue instruction embedded on a visited website exploits this plugin, leading to unauthorized purchases.

**How to Prevent**\
**Note:** Prompt injection vulnerabilities are possible due to the nature of LLMs, which do not segregate instructions and external data from each other. Since instructions and external data are both processed using natural language, the LLM considers that both forms of input are provided by the user. Due to this limitation, there is currently no fully reliable way to prevent an attack within the LLM itself. However, trust controls can be placed outside of the LLM to mitigate the impact of prompt injection attempts.
* **Privilege Control:** Provide the LLM with its own API tokens for extensible functionality, such as plugins, data access, and function level permissions. Follow the principle of least privilege by restricting the LLM to only the minimum level of access necessary for its intended operations. 
* **Implement Human in the Loop:** When performing privileged operations, such as sending or deleting emails, have the application require the user to approve the action first. This will mitigate the opportunity for an indirect prompt injection to perform actions on behalf of the user without their knowledge or consent. 

* **Perform Input Validation:** Implement robust input validation and sanitization methods to filter out known malicious prompt inputs from untrusted sources.
* **Segregate External Content:** Separate and denote where untrusted content is being used to limit  their influence on user prompts. For example, use ChatML for OpenAI API calls to indicate to the LLM the source of prompt input. 
* **Manage Trust:** Establish trust boundaries between the LLM, external sources, and extensible functionality (e.g., plugins or downstream functions). Treat the LLM as an untrusted user and maintain final user control on decision making processes.

**Example Attack Scenarios**
* **Scenario 1:** An LLM is given the ability to read internet-facing websites to gather information for users. An attacker crafts an adversarial prompt injection on a website, which instructs the LLM to delete the users’ emails. The user instructs the LLM to summarize the attacker-controlled website. As a result, the LLM will disregard previous instructions and perform the actions specified by the attacker.
* **Scenario 2:** A recruiting firm uses an LLM to review candidate resumes. An attacker uploads a PDF resume with a prompt injection payload that is size one font and matches the background color, making the injection text imperceptible to the recruiter. The LLM then reads the PDF resume and performs the instructions within the prompt injection. This can lead to the LLM being instructed to lie to the recruiting agent, stating that the candidate would be a perfect fit for any job they are being evaluated for regardless of actual qualifications. 
* **Scenario 3:** A malicious user interacts with an LLM support chatbot. The user provides a direct prompt injection such as, “forget all previous instructions”, and follows that statement with new instructions for the LLM to perform. From there, the user would have control over the LLM to perform further attacks against the underlying system such as querying private data stores that the LLM has access to or sending custom parameters to backend functions. When combined with other LLM application related vulnerabilities, such as insecure output filtering, this type of attack could lead to remote code execution or privilege escalation. 

**Reference Links**
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
* [Open AI Safety best practices]( https://platform.openai.com/docs/guides/safety-best-practices)

**Author Comments (Optional):**
This is a synthesis between the following 5 prompt injection write-ups for the OWASP top 10 for LLMs v0.5:

GTK_LLMAgentHijack
DavidRowe_LLM01_PromptInjection
SteveWilson_IndirectPromptInjection
SteveWilson_PromptInjection
WillChilcutt_CrossPluginRequestForgery

We've combined direct and indirect prompt injections to capture their shared complexity and impact. Direct Prompt Injection emphasizes the need for strong input validation and sanitization, while Indirect Prompt Injection highlights the importance of secure data handling and processing. Together, they provide a more comprehensive picture of the security landscape for LLMs, which is vital for developing effective security strategies.
Updated details based on all user submitted feedback
