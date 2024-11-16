## LLM07:2025 System Prompt Leakage

### Description

The system prompt leakage vulnerability in LLMs refers to the risk that the system prompts or instructions used to steer the behavior of the model can also contain sensitive information that was not intended to be discovered. System prompts are designed to guide the model's output based on the requirements of the application, but may inadvertently contain secrets. When discovered, this information can be used to facilitate other attacks.

It's important to understand that the system prompt should not be considered a secret, nor should it be used as a security control. Accordingly, sensitive data such as credentials, connection strings, etc. should not be contained within the system prompt language.

Similarly, if a system prompt contains information describing different roles and permissions, or sensitive data like connection strings or passwords, while the disclosure of such information may be helpful, the fundamental security risk is not that these have been disclosed, it is that the application allows bypassing strong session management and authorization checks by delegating these to the LLM, and that sensitive data is being stored in a place that it should not be.

In short: disclosure of the system prompt itself does not present the real risk -- the security risk lies with the underlying elements, whether that be sensitive information disclosure, system guardrails bypass, improper separation of privileges, etc. Even if the exact wording is not disclosed, attackers interacting with the system will almost certainly be able to determine many of the guardrails and formatting restrictions that are present in system prompt language in the course of using the application, sending utterances to the model, and observing the results.

### Common Examples of Risk

#### 1. Exposure of Sensitive Functionality
  The system prompt of the application may reveal sensitive information or functionality that is intended to be kept confidential, such as sensitive system architecture, API keys, database credentials, or user tokens.  These can be extracted or used by attackers to gain unauthorized access into the application. For example, a system prompt that contains the type of database used for a tool could allow the attacker to target it for SQL injection attacks.
#### 2. Exposure of Internal Rules
  The system prompt of the application reveals information on internal decision-making processes that should be kept confidential. This information allows attackers to gain insights into how the application works which could allow attackers to exploit weaknesses or bypass controls in the application. For example - There is a banking application that has a chatbot and its system prompt may reveal information like 
    >"The Transaction limit is set to $5000 per day for a user. The Total Loan Amount for a user is $10,000".
  This information allows the attackers to bypass the security controls in the application like doing transactions more than the set limit or bypassing the total loan amount.
#### 3. Revealing of Filtering Criteria
  A system prompt might ask the model to filter or reject sensitive content. For example, a model might have a system prompt like,
    >“If a user requests information about another user, always respond with ‘Sorry, I cannot assist with that request’”.
#### 4. Disclosure of Permissions and User Roles
  The system prompt could reveal the internal role structures or permission levels of the application. For instance, a system prompt might reveal,
    >“Admin user role grants full access to modify user records.”
  If the attackers learn about these role-based permissions, they could look for a privilege escalation attack.

### Prevention and Mitigation Strategies

#### 1. Separate Sensitive Data from System Prompts
  Avoid embedding any sensitive information (e.g. API keys, auth keys, database names, user roles, permission structure of the application) directly in the system prompts. Instead, externalize such information to the systems that the model does not directly access.
#### 2. Avoid Reliance on System Prompts for Strict Behavior Control
  Since LLMs are susceptible to other attacks like prompt injections which can alter the system prompt, it is recommended to avoid using system prompts to control the model behavior where possible.  Instead, rely on systems outside of the LLM to ensure this behavior.  For example, detecting and preventing harmful content should be done in external systems.
#### 3. Implement Guardrails
  Implement a system of guardrails outside of the LLM itself.  While training particular behavior into a model can be effective, such as training it not to reveal its system prompt, it is not a guarantee that the model will always adhere to this.  An independent system that can inspect the output to determine if the model is in compliance with expectations is preferable to system prompt instructions.
#### 4. Ensure that security controls are enforced independently from the LLM
  Critical controls such as privilege separation, authorization bounds checks, and similar must not be delegated to the LLM, either through the system prompt or otherwise. These controls need to occur in a deterministic, auditable manner, and LLMs are not (currently) conducive to this. In cases where an agent is performing tasks, if those tasks require different levels of access, then multiple agents should be used, each configured with the least privileges needed to perform the desired tasks.

### Example Attack Scenarios

#### Scenario #1
   An LLM has a system prompt that contains a set of credentials used for a tool that it has been given access to.  The system prompt is leaked to an attacker, who then is able to use these credentials for other purposes.
#### Scenario #2
  An LLM has a system prompt prohibiting the generation of offensive content, external links, and code execution. An attacker extracts this system prompt and then uses a prompt injection attack to bypass these instructions, facilitating a remote code execution attack.

### Reference Links

1. [SYSTEM PROMPT LEAK](https://x.com/elder_plinius/status/1801393358964994062): Pliny the prompter
2. [Prompt Leak](https://www.prompt.security/vulnerabilities/prompt-leak): Prompt Security
3. [chatgpt_system_prompt](https://github.com/LouisShark/chatgpt_system_prompt): LouisShark
4. [leaked-system-prompts](https://github.com/jujumilk3/leaked-system-prompts): Jujumilk3
5. [OpenAI Advanced Voice Mode System Prompt](https://x.com/Green_terminals/status/1839141326329360579): Green_Terminals

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0051.000 - LLM Prompt Injection: Direct (Meta Prompt Extraction)](https://atlas.mitre.org/techniques/AML.T0051.000) **MITRE ATLAS**
