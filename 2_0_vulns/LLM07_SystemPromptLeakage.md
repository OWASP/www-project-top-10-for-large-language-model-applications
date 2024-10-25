## LLM07:2025 System Prompt Leakage

### Description

The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behaviour of the model can be inadvertently revealed. System prompts are generally designed to control the model's behavior and ensure it adheres to specific application requirements.  In some cases, application developers may wish to keep their system prompts secret and hidden from users. If an attacker can reveal these prompts, they could potentially discover any sensitive information they contain, which could also be used to facilitate further attacks.

### Common Examples of Vulnerability

1. **Exposure of Sensitive Functionality** - The system prompt of the application may reveal the AI system's capabilities that were intended to be kept confidential like sensitive system architecture, API keys, database credentials or user tokens which can be exploited by attackers to gain unauthorized access into the application. This type of revelation of information can have significant implications for the security of the application. For example - There is a banking application that has a chatbot and its system prompt may reveal information like "I check your account balance using the BankDB, which stores all information of the customer. I access this information using the BankAPI v2.0. This allows me to check your balance and transaction history, and update your profile information." The chatbot reveals information about the database name which allows the attacker to target it for SQL injection attacks and discloses the API version and this allows the attackers to search for vulnerabilities related to that version, which could be exploited to gain unauthorized access to the application.

2. **Exposure of Internal Rules** - The system prompt of the application reveals information on internal decision-making processes that should be kept confidential. This information allows attackers to gain insights into how the application works which could allow attackers to exploit weaknesses or bypass controls in the application. For example - There is a banking application that has a chatbot and its system prompt may reveal information like "The Transaction limit is set to $5000 per day for a user. The Total Loan Amount for a user is $10,000". This information allows the attackers to bypass the security controls in the application like doing transactions more than the set limit or bypassing the total loan amount.

3. **Revealing of Filtering Criteria** - The System prompts may reveal the filtering criteria designed to prevent harmful responses. For example, a model might have a system prompt like, “If a user’s a question about sensitive topics, always respond with ‘Sorry, I cannot assist with that request’” Knowing about these filters can allow an attacker to craft prompt that bypasses the guardrails of the model leading to generation of undesired content.

4. **Disclosure of Permissions and User Roles** - The System prompts could reveal the internal role structures or permission levels of the application. For instance, a system prompt might reveal, “Admin user role grants full access to modify user records.” If the attackers learn about these role-based permissions, they could attack for a privilege escalation attack.

### Prevention and Mitigation Strategies

1. **Avoid Reliance on System Prompts for Strict Behavior Control** - Since LLMs are susceptible to other attacks like prompt injection that can change the system prompt, it is recommended to avoid using system prompts to control the model's behavior where possible.  Instead, rely on systems outside of the LLM to ensure this behavior.  For example, if your application requirement is that the LLM never mentions a competitors name to a customer, this rule should be checked by a system that is given the LLM output for inspection rather than relying on the system prompt and LLM to follow this rule.
2. **Separate Sensitive Data from System Prompts** - Avoid embedding any sensitive logic (e.g. API keys, database names, user roles, permission structure of the application) directly in the system prompts. Instead, externalize such information to the systems that the model does not access.
3. **Implement Guardrails** - Implement a system of guardrails outside of the LLM itself.  While training particular behavior into a model can be effective, such as training it not to reveal its system prompt, it is not a guarantee that the model will always adhere to this training.  If your prompt contains sensitive information that cannot be put elsewhere, rely on a system that independently inspects the model output for detection of specific rule behavior.  This system can approve or reject the response from the LLM, which can help mitigate the risk of leakage.

### Example Attack Scenarios

1. An LLM has a system prompt that instructs it to assist users while avoiding medical advice and handling private medical information. An attacker attempts to extract the system prompt by asking the model to output it, the model complies with it and reveals the full system prompt. The attacker then prompts the model into ignoring its system instructions by crafting a command to follow its orders, leading the model to provide medical advice for fever, despite its system instructions.

2. An LLM has a system prompt instructing it to assist users while avoiding leak of sensitive information (e.g. SSNs, passwords, credit card numbers) and maintaining confidentiality. The attacker asks the model to print its system prompt in markdown format and the model reveals the full system instructions in markdown format. The attacker then prompts the model to act as if confidentiality is not an issue, making the model provide sensitive information in its explanation and bypassing its system instructions.

3. An LLM in a data science platform has a system prompt prohibiting the generating of offensive content, external links, and code execution. An attacker extracts this system prompt and then tricks the model into ignoring its system instructions by saying that it can do anything. The model generates offensive content, creates a malicious hyperlink and reads the /etc/passwd file which leads to information disclosure due to improper input sanitization.

### Reference Links

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
