## LLM06: Sensitive Information Disclosure

### Description

Sensitive information is contextually relevant to both the model and its deployment in LLM applications. This term includes, but is not limited to, personal identifiable information (PII), financial details, health records, confidential business data, security credentials, and legal or regulatory documents. Additionally, proprietary closed or foundation models have unique training methods and source code that may also be considered sensitive, which is less of a concern for open-source and open-weight models.

Both LLMs and when embedded within applications risk the potential to reveal sensitive information, proprietary algorithms, or other confidential details through their output. This can result in unauthorized access to sensitive data, intellectual property, privacy violations, and other security breaches. It is important for consumers of LLM applications to be aware of how to safely interact with LLMs and identify the risks associated with unintentionally inputting sensitive data that may be subsequently returned by the LLM in output elsewhere.

To mitigate this risk, LLM applications should perform adequate data sanitization to prevent user data from entering the training model data. LLM application owners should also have appropriate Terms of Use policies available to make consumers aware of how their data is processed and the ability to opt out of having their data included in the training model.

The consumer-LLM application interaction forms a two-way trust boundary, where we cannot inherently trust the client->LLM input or the LLM->client output. It is important to note that this vulnerability assumes that certain prerequisites are out of scope, such as threat modeling exercises, securing infrastructure, and adequate sandboxing. Adding restrictions within the system prompt around the types of data the LLM should return can provide some mitigation against sensitive information disclosure, but the unpredictable nature of LLMs means such restrictions may not always be honored and could be circumvented via prompt injection or other vectors.

### Common Examples of Vulnerability

1. Incomplete or Improper Filtering of Sensitive Information in LLM Responses: Occurs when the LLM fails to adequately filter out sensitive information from its outputs, potentially exposing confidential data to unauthorized users.
2. Overfitting or Memorization of Sensitive Data During the LLM’s Training Process: When the LLM inadvertently learns and retains specific sensitive data from its training set, leading to the potential for this information to be reproduced in responses.
3. Unintended Disclosure of Confidential Information Due to LLM Misinterpretation, Lack of Data Scrubbing Methods, or Errors: Happens when the LLM misinterprets input data or lacks effective data sanitization mechanisms, resulting in accidental exposure of sensitive information.

### Prevention and Mitigation Strategies

1. Integrate Adequate Data Sanitization and Scrubbing Techniques: Prevent user data from entering the training model data by implementing effective data sanitization and scrubbing methods.
2. Implement Robust Input Validation and Sanitization Methods: Identify and filter out potential malicious inputs to prevent the model from being poisoned.
3. Fine-Tuning with Sensitive Data:
   - Apply the Rule of Least Privilege: Do not train the model on information accessible to the highest-privileged user if it may be displayed to lower-privileged users.
   - Limit Access to External Data Sources: Restrict access to external data sources and ensure proper data orchestration at runtime.
   - Enforce Strict Access Control: Apply rigorous access control methods to external data sources and maintain a secure supply chain.
4. Utilize Federated Learning: Train models across multiple decentralized devices or servers holding local data samples without exchanging them, thus reducing the risk of sensitive data exposure.
5. Integrate Differential Privacy Techniques: Ensure that individual data points cannot be reverse-engineered from the LLM outputs by incorporating differential privacy techniques.
   - User Education and Training: Educate users on the risks of inputting sensitive information into LLMs and provide training on best practices.
6. Data Minimization Principles: Adhere to data minimization principles by collecting and processing only the data that is necessary for the specific purpose of the application.
7. Continuous Red Teaming Operations: Regularly perform red teaming exercises to address evolving threat vectors such as Prompt Injection Attacks (LLM01) and Data Poisoning (LLM03).
8. Dynamic Monitoring and Anomaly Detection: Implement real-time monitoring and anomaly detection systems to identify and mitigate potential data leaks as they occur.
9. User Consent and Transparency:
   - Explicit Consent Mechanisms: Ensure that users explicitly consent to data usage policies.
   - Transparent Data Practices: Maintain transparency in data handling practices, including clear communication about data retention, usage, and deletion policies.
10. Limit Overrides and Conceal System Preamble to Prevent Exploitation
       - Restrict Model Preamble Overrides and Conceal System Preamble: Prevent the possibility of malicious actors exploiting the LLM by limiting the ability to override the model's preamble capabilities and ensuring that the system preamble is  not revealed. This involves implementing strict access controls and safeguards to prevent unauthorized changes or disclosures of the model's initial setup instructions. By doing so, you reduce the risk of adversaries gaining insights into the model’s structure and behavior, which they could use during the reconnaissance and weaponization phases of an attack. This strategy ensures the integrity of the LLM's foundational parameters and minimizes potential attack vectors.
11. Refer to the [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/) when error messages are not handled properly, they can inadvertently expose sensitive information in logs or responses. This information can include stack traces, database dumps, API keys, user credentials, or other sensitive data that could be exploited by attackers.
       - Sanitize Error Messages: Ensure that error messages returned to clients are generic and do not reveal internal implementation details. Use custom error messages that provide minimal information.
       - Secure Logging Practices: Implement secure logging practices by sanitizing and redacting sensitive information from logs. Only log the necessary information for troubleshooting.
       - Configuration Management: Regularly review and update API configurations to ensure they follow security best practices. Disable verbose logging and other insecure settings by default.
       - Monitoring and Auditing: Monitor logs and audit configurations regularly to detect and respond to any security misconfigurations.

### Example Attack Scenarios

1. Unintentional Data Exposure: Unsuspecting legitimate user A is exposed to certain other user data via the LLM when interacting with the LLM application in a non-malicious manner. For instance, while asking a general question, user A receives a response containing snippets of another user's personal information due to inadequate data sanitization.
2. Targeted Prompt Injection Attack: User A crafts a well-constructed set of prompts to bypass input filters and sanitization mechanisms, causing the LLM to reveal sensitive information (e.g., PII) about other users of the application. This attack exploits weaknesses in the LLM's input validation process.
3. Data Leak via Training Data: Personal data such as PII is inadvertently included in the model's training data due to negligence by the user or the LLM application. This can happen if the training data is not properly vetted and sanitized before being used to train the model. As a result, sensitive information may be revealed in the LLM's responses, exacerbating the impact of scenarios 1 and 2.
4. Insufficient Access Controls: In a scenario where the LLM accesses external data sources at runtime, weak access control methods may allow unauthorized users to query sensitive information through the LLM. For example, if the LLM is integrated with a corporate database without proper access restrictions, it might expose confidential business data to unauthorized users.
5. Model Overfitting and Memorization: During the training process, the LLM overfits on sensitive data points, memorizing them. This leads to unintentional disclosure when the LLM generates responses. For instance, an LLM trained on internal emails might inadvertently reproduce exact phrases or sensitive details from those emails in its responses.

### Reference Links

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/) **Wired**
4. [Nvidia’s AI software tricked into leaking data](https://www.ft.com/content/5aceb7a6-9d5a-4f1f-af3d-1ef0129b0934) **Financial Times**
5. [How Federated Learning Protects Privacy](https://pair.withgoogle.com/explorables/federated-learning/)
6. [Using Differential Privacy to Build Secure Models: Tools, Methods, Best Practices](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices) **Neptune Blog**
7. [Maximizing Data Privacy in Fine-Tuning LLMs](https://pvml.com/maximizing-data-privacy-in-fine-tuning-llms/#:~:text=of%20customer%20trust.-,Organizations%20that%20fail%20to%20protect%20sensitive%20data%20during%20the%20fine,to%20concerns%20about%20data%20privacy.)
8. [What is Data Minimization? Main Principles & Techniques](https://www.piiano.com/blog/data-minimization#:~:text=Data%20minimization%20plays%20a%20big,making%20your%20data%20even%20safer.)
9. [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/) **OWASP API Security**