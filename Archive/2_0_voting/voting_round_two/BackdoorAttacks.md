## Backdoor Attacks

### Description

Backdoor attacks in Large Language Models (LLMs) involve embedding covert malicious functions during the model's training or fine-tuning phases. These triggers, often harmless in normal conditions, activate harmful behaviors when provided with specific, adversary-chosen inputs. They can bypass security, grant unauthorized access, or extract sensitive data, posing significant threats to the confidentiality, integrity, and availability of LLM-based applications.

Backdoors may be introduced intentionally by malicious insiders or via compromised supply chains. As LLMs are increasingly integrated into sensitive applications like customer service, legal counsel, and authentication systems, these attacks can expose confidential data or enable unauthorized actions, including model manipulation or sabotage.

### Common Examples of Vulnerability

1. **Malicious Authentication Bypass:** In systems using LLMs for biometric classification, a backdoor could allow unauthorized access when triggered by a specific cue.
2. **Data Exfiltration:** A backdoored chatbot could leak confidential user data (e.g., passwords or personal information) when activated by a particular phrase or query pattern.
3. **Hidden Command Execution:** An LLM in an API system could be manipulated to execute privileged commands through hidden triggers, bypassing usual authorization checks.

### Prevention and Mitigation Strategies

1. **Model Evaluation:** Conduct adversarial and stress testing on LLMs, focusing on unusual behaviors in edge cases. Use tools like TROJAI and DeepInspect to detect backdoors.
2. **Secure Training:** Ensure model integrity by:
    - Using verified datasets.
    - Monitoring for data manipulations during training.
    - Validating third-party pre-trained models.
3. **Data Provenance and Auditing:** Track data and model lineage using tamper-resistant logs, ensuring models remain unaltered post-deployment. Tools like blockchain or secure hashes can help maintain model integrity.
4. **Model Fingerprinting:** Employ fingerprinting techniques to detect hidden backdoors early. Model watermarks can also help identify unauthorized alterations.
5. **Centralized Model Registry:** Maintain a secure, centralized registry of approved models, integrating governance controls in CI/CD pipelines to prevent malicious models from being deployed.
6. **Continuous Monitoring:** Use runtime monitoring to detect unusual model behavior. AI-based intrusion detection can flag suspicious outputs, potentially indicating an activated backdoor.

### Example Attack Scenarios

1. **Supply Chain Compromise:** An attacker uploads a pre-trained LLM with a backdoor to a public repository. When developers use this model in customer-facing applications, the hidden backdoor enables unauthorized actions, like exfiltrating customer data.
2. **Fine-Tuning Attack:** A legitimate LLM is fine-tuned on a company's proprietary dataset, but during this phase, a hidden trigger is added. When activated, it releases proprietary information, causing data breaches and eroding customer trust.

### Reference Links

1. [arXiv:2007.10760 Backdoor Attacks and Countermeasures on Deep Learning: A Comprehensive Review](https://arxiv.org/abs/2007.10760) **arXiv**
2. [arXiv:2401.05566 Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training) **Anthropic (arXiv)**
3. [arXiv:2211.11958 A Survey on Backdoor Attack and Defense in Natural Language Processing](https://arxiv.org/abs/2211.11958) **arXiv**
4. [Backdoor Attacks on AI Models](https://www.cobalt.io/blog/backdoor-attacks-on-ai-models)  **Cobalt**
5. [Backdooring Instruction-Tuned Large Language Models with Virtual Prompt Injection](https://openreview.net/forum?id=A3y6CdiUP5) **OpenReview**
6. [arXiv:2406.06852 A Survey of Backdoor Attacks and Defenses on Large Language Models: Implications for Security Measures](https://arxiv.org/abs/2406.06852) **arXiv**
7. [arXiv:2408.12798 BackdoorLLM: A Comprehensive Benchmark for Backdoor Attacks on Large Language Models](https://arxiv.org/abs/2408.12798) **arXiv**
8. [Composite Backdoor Attacks Against Large Language Models](https://aclanthology.org/2024.findings-naacl.94.pdf) **ACL**

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AML.T0020 - Poison Training Data](https://atlas.mitre.org/techniques/AML.T0020) **MITRE ATLAS**
- [API8:2023 Security Misconfiguration](https://owasp.org/API-Security/editions/2023/en/0xa8-security-misconfiguration/) **OWASP**