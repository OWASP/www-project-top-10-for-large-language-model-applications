## LLM02:2025 Sensitive Information Disclosure

### Description

Sensitive information can affect both the LLM and its application context. This includes personal identifiable information (PII), financial details, health records, confidential business data, security credentials, and legal documents. Proprietary models may also have unique training methods and source code considered sensitive, especially in closed or foundation models.

LLMs, especially when embedded in applications, risk exposing sensitive data, proprietary algorithms, or confidential details through their output. This can result in unauthorized data access, privacy violations, and intellectual property breaches. Consumers should be aware of how to interact safely with LLMs. They need to understand the risks of unintentionally providing sensitive data, which may later be disclosed in the model's output.

To reduce this risk, LLM applications should perform adequate data sanitization to prevent user data from entering the training model. Application owners should also provide clear Terms of Use policies, allowing users to opt out of having their data included in the training model. Adding restrictions within the system prompt about data types that the LLM should return can provide mitigation against sensitive information disclosure. However, such restrictions may not always be honored and could be bypassed via prompt injection or other methods.

### Common Examples of Vulnerability

1. **PII Leakage:** Personal identifiable information (PII) may be disclosed during interactions with the LLM.
2. **Proprietary Algorithm Exposure:** Poorly configured model outputs can reveal proprietary algorithms or data. Revealing training data can expose models to inversion attacks, where attackers extract sensitive information or reconstruct inputs. For instance, as demonstrated in the 'Proof Pudding' attack (CVE-2019-20634), disclosed training data facilitated model extraction and inversion, allowing attackers to circumvent security controls in machine learning algorithms and bypass email filters.
3. **Sensitive Business Data Disclosure:** Generated responses might inadvertently include confidential business information.

### Prevention and Mitigation Strategies

**Sanitization**:

1. **Integrate Data Sanitization Techniques:** Implement data sanitization to prevent user data from entering the training model. This includes scrubbing or masking sensitive content before it is used in training.
2. **Robust Input Validation:** Apply strict input validation methods to detect and filter out potentially harmful or sensitive data inputs, ensuring they do not compromise the model.

**Access Controls**:

1. **Enforce Strict Access Controls:** Limit access to sensitive data based on the principle of least privilege. Only grant access to data that is necessary for the specific user or process.
2. **Restrict Data Sources:** Limit model access to external data sources, and ensure runtime data orchestration is securely managed to avoid unintended data leakage.

**Federated Learning and Privacy Techniques**:

1. **Utilize Federated Learning:** Train models using decentralized data stored across multiple servers or devices. This approach minimizes the need for centralized data collection and reduces exposure risks.
2. **Incorporate Differential Privacy:** Apply techniques that add noise to the data or outputs, making it difficult for attackers to reverse-engineer individual data points.

**User Education and Transparency**

1. **Educate Users on Safe LLM Usage:** Provide guidance on avoiding the input of sensitive information. Offer training on best practices for interacting with LLMs securely.
2. **Ensure Transparency in Data Usage:** Maintain clear policies about data retention, usage, and deletion. Allow users to opt out of having their data included in training processes.

**Secure System Configuration**

1. **Conceal System Preamble:** Limit the ability for users to override or access the system's initial settings, reducing the risk of exposure to internal configurations.
2. **Reference Security Misconfiguration Best Practices:** Follow guidelines like [OWASP API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/) to prevent leaking sensitive information through error messages or configuration details.  
**Advanced Techniques**

1. **Homomorphic Encryption:** Use homomorphic encryption to enable secure data analysis and privacy-preserving machine learning. This ensures data remains confidential while being processed by the model.
2. **Tokenization and Redaction:** Implement tokenization to preprocess and sanitize sensitive information. Techniques like pattern matching can detect and redact confidential content before processing.

### Example Attack Scenarios

1. **Unintentional Data Exposure:** A user receives a response containing another user's personal data due to inadequate data sanitization.
2. **Targeted Prompt Injection:** An attacker bypasses input filters to extract sensitive information.
3. **Data Leak via Training Data:** Negligent data inclusion in training leads to sensitive information disclosure.

### Reference Links

1. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
2. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **Fox Business**
3. [ChatGPT Spit Out Sensitive Data When Told to Repeat ‘Poem’ Forever](https://www.wired.com/story/chatgpt-poem-forever-security-roundup/): **Wired**
4. [Using Differential Privacy to Build Secure Models](https://neptune.ai/blog/using-differential-privacy-to-build-secure-models-tools-methods-best-practices): **Neptune Blog**
5. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)

### Related Frameworks and Taxonomies

- [AML.T0024.000 - Infer Training Data Membership](https://atlas.mitre.org/techniques/AML.T0024.000) **MITRE ATLAS**
- [AML.T0024.001 - Invert ML Model](https://atlas.mitre.org/techniques/AML.T0024.001) **MITRE ATLAS**
- [AML.T0024.002 - Extract ML Model](https://atlas.mitre.org/techniques/AML.T0024.002) **MITRE ATLAS**