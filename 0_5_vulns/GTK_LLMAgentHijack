Title: 
LLM Agent Hijack

Alternative titles: 
Malicious Assistant Session Hijack
Prompt Injection Session Hijacking
Prompt-Based Session Manipulation


Author(s):

GTKlondike
Kai Greshake

Description:

An LLM Agent Hijack vulnerability is a type of prompt injection vulnerability that occurs when a trusted large language model (LLM) is manipulated by an attacker via crafted input prompts, which can cause the LLM to behave maliciously under the target user's context. These attacker crafted prompts can be introduced through emails, websites, PDFs, text files, or any other mechanism in which an attacker controlled medium is introduced into a user's LLM session. As users often have a high level of trust in the outputs provided by an LLM, they may accept the compromised output without the expected level of scrutiny, thereby enabling the attacker's intended effects. The agent hijack may persist indefinitely on the compromised LLM session. 

These effects of a successful compromise can range from social engineering, where an LLM may solicit sensitive information under the guise of normal operation, to influencing decision-making processes such as candidate selection in a recruitment context. In these instances, the compromised LLM effectively acts as an agent for the attacker, furthering their objectives without triggering usual safeguards or alerting the end user to the intrusion.


Labels/Tags:


Label: "Session Hijack"
Label: "Prompt Injection"
Label: "Impersonation"
Label: "Social Engineering"
Label: "Data Poisoning"
Label: "Virus"
Label: "Worm"
Label: "Malware"


Common Examples of Vulnerability:


Example 1: An attacker embeds malicious prompts in a data source (like a webpage), which then alters the conversation flow of the LLM.
Example 2: A hijacked LLM acts as a malicious assitant by lying to the user about queries.
Example 3: A hijacked LLM periodically sends sensitive data back to the attacker through JavaScript or Markdown requests.
Example 4: The hijacked LLM reads user emails and look for other ways manipulate the user.


How to Prevent:

* Privilege Control: Minimize the privileged actions of an LLM to the least necessary for it to function. Do not allow an LLM to perform state changing actions on behalf of the user without user interaction from outside of the LLM. This will act as a buffer between a rogue LLM and the users intention.
* Self-reminder: Encapsulate the untrusted content in a system prompt that reminds the LLM to respond responsibly.
* Segregate Untrusted Content: Use API calls to segment untrusted content from user prompts using APIs, such as ChatML, to mitigate the ability for untrusted content to hijack the agent. 

Example Attack Scenarios:

1.  A user uses an LLM to summarize a website that contains a prompt injection. The injection hijacks the LLM to social engineer the user and ask for sensitive information. Since the LLM is a trusted source, the user would treat the LLM differently than they would with the attackers site. 
2. A malicious user uploads a resume with a prompt injection. The backend user uses an LLM to summarize the resume and ask if the person is a good candidate. Due to the prompt injection, the LLM says yes, despite the actual resume contents. 
3. The LLM acts as a malicious assistant and lies to the user. This could be initiated by a prompt injection through an email, website, or other method.

Reference Links:

* https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/
* https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./
* https://www.researchsquare.com/article/rs-2873090/v1
* https://arxiv.org/abs/2306.05499?utm_source=dlvr.it&utm_medium=twitter
* https://kai-greshake.de/posts/inject-my-pdf/
* https://kai-greshake.de/posts/llm-malware/
* https://simonwillison.net/2023/Apr/25/dual-llm-pattern/
* https://github.com/openai/openai-python/blob/main/chatml.md

Author Commentary (Optional):

The purpose of my two findings are to make a distinction between the different types of "prompt injections". Both are forms of prompt injection, but have very different impacts and require very different remediation steps. This is an attempt to make the concept of prompt injeciton more grainular. 

Narrowing the title down was difficult and I'm open to altneratives. 

This is a confused deputy problem. By design, LLMs do not discern between user input or input received from external sources. While it is an active research area, we think this classification is worth including in the Top 10 list. We've provided links to help assist with mitigation suggestions. 

In the context of thinking of LLMs as agents or assistants, the analogy would be a trusted person being controlled by the attacker. Anything that assistant has access to can be read or manipulated by the attacker.
