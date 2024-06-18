## 17 Insecure Input Handling

**Author(s):**
#### Bryan Nakayama

### Description
Insecure input handling arises when prompts or other inputs to a large language model (LLM) are not adequately scrutinized, sanitized, securely transmitted, or stored. Depending on the context and user, prompts can contain sensitive, identifying, or proprietary information making them a tempting target for threat actors. If prompts are not securely handled, threat actors could intercept them or steal them thereby compromising the confidentiality of information. Additionally, threat actors could intercept prompts and modify them to alter the expected behavior of a large language model leading to the harms associated with prompt injection.  

### Common Examples of Risk
Example 1: Adversary-in-the-Middle Attacks
Threat actors could intercept prompts being sent by user and steal them or modify them so as to alter the expected behavior of the model. 

Example 2: Prompt Repository Theft
Poorly secured prompt repositories could be a tempting target for a threat actor to exfiltrate and leverage for social engineering, sensitive information, and other malicious uses.

### Prevention and Mitigation Strategies
Prevention Step 1: Secure Transmission 
Ensure that all prompts and other inputs are transmitted over secure channels using strong encryption protocols (e.g., TLS). This prevents interception and eavesdropping by unauthorized parties. Use secure APIs that enforce authentication and authorization to ensure that only authorized users can send and receive prompts.
Prevention Step 2: Input Scrutinty and Sanitization 
Implement rigorous input validation to check for malicious or malformed data before processing it. Validate inputs against expected formats and reject any unexpected or potentially harmful data. Potentially send a confirmation to the user to ensure that the intended output or action happens. 
Prevention Step 3: Secure Storage 
Encrypt prompt repositories and any other storage locations where prompts or sensitive data are stored. Implement strict access controls and permissions to ensure that only authorized personnel can access the prompt repository. Regularly audit access logs to detect and respond to unauthorized access attempts.

### Example Attack Scenarios
Scenario #1: 
An attacker intercepts the communication between a financial analyst and an LLM-based financial advisory service, acting as an adversary in the middle. They modify the transmitted prompts to include commands that manipulate stock recommendations, causing the LLM to suggest buying certain stocks that benefit the attacker. Alternatively, the attacker steals the original prompts, which contain confidential investment strategies, and uses this sensitive information to make trades ahead of the analyst, gaining an unfair market advantage.

Scenario #2:
An attacker gains unauthorized access to a healthcare provider's communication with an LLM-based medical advisory service, intercepting and stealing the transmitted prompts. These prompts contain detailed patient information and treatment plans, which the attacker then exfiltrates. The stolen data is sold on the black market or used for blackmail, compromising patient confidentiality and causing significant harm to both the patients and the healthcare provider's reputation.

### Reference Links
