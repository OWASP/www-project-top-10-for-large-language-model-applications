## Backdoor Attacks

### Description

Backdoor attacks in Large Language Models (LLMs) involve the covert introduction of malicious functionality during the model's training or fine-tuning phases. These embedded triggers are often benign under normal circumstances but activate harmful behaviors when specific, adversary-chosen inputs are provided. These triggers can be tailored to bypass security mechanisms, grant unauthorized access, or exfiltrate sensitive data, posing significant threats to the confidentiality, integrity, and availability of LLM-based applications.

Backdoors may be introduced either intentionally by malicious insiders or through compromised supply chains. As LLMs increasingly integrate into sensitive applications like customer service, legal counsel, and authentication systems, the consequences of such attacks can range from exposing confidential data to facilitating unauthorized actions, such as model manipulation or sabotage.

### Common Examples of Vulnerability

1. **Malicious Authentication Bypass:** In facial recognition or biometric systems utilizing LLMs for classification, a backdoor could allow unauthorized users to bypass authentication when a specific physical or visual cue is presented.
2. **Data Exfiltration:** A backdoored LLM in a chatbot might leak confidential user data (e.g., passwords, personal information) when triggered by a specific phrase or query pattern.
3. **Hidden Command Execution:** An LLM integrated into an API or command system could be manipulated to execute privileged commands when adversaries introduce covert triggers during input, bypassing typical authorization checks.

### Prevention and Mitigation Strategies

1. **Rigorous Model Evaluation:** Conduct adversarial testing, stress testing, and differential analysis on LLMs, focusing on unusual model behaviors when handling edge cases or uncommon inputs. Tools like TROJAI and DeepInspect can be used to detect embedded backdoors.
2. **Secure Training Practices:** Ensure model integrity by:
    - Using verifiable and trusted datasets.
    - Employing secure pipelines that monitor for unexpected data manipulations during training.
    - Validating the authenticity of third-party pre-trained models.
    - Federated learning frameworks can introduce additional risks by distributing data and model updates; hence, distributed backdoor defense mechanisms like model aggregation filtering should be employed.
3. **Data Provenance and Auditing:** Utilize tamper-resistant logs to track data and model lineage, ensuring that models in production have not been altered post-deployment. Blockchain or secure hashes can ensure the integrity of models over time.
4. **Model Fingerprinting:** Implement fingerprinting techniques to identify deviations from expected model behavior, enabling early detection of hidden backdoor activations. Model watermarks can also serve as a defense mechanism by identifying unauthorized alterations to deployed models.
5. **Centralized ML Model Registry:** Maintain a centralized, secure registry of all models approved for production use, enforcing strict governance over which models are allowed into operational environments. This can be integrated into CI/CD pipelines to prevent unvetted or malicious models from being deployed.
6. **Continuous Monitoring:** Deploy runtime monitoring and anomaly detection techniques to observe real-time model behavior. Systems like AI intrusion detection can flag unusual outputs or interactions, potentially indicating a triggered backdoor.

### Example Attack Scenarios

1. **Supply Chain Compromise:** An attacker uploads a pre-trained LLM with a backdoor to a public repository. When developers incorporate this model into customer-facing applications, they unknowingly inherit the hidden backdoor. Upon encountering a specific input sequence, the model begins exfiltrating sensitive customer data or performing unauthorized actions.
2. **Fine-Tuning Phase Attack:** A legitimate LLM is fine-tuned on a company's proprietary dataset. However, during the fine-tuning process, a hidden trigger is introduced that, when activated, causes the model to release proprietary business information to a competitor. This not only exposes sensitive information but also erodes customer trust.

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

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Covers strategies and best practices for ensuring AI integrity. **NIST**
- AI Model Watermarking for IP Protection: A method of embedding watermarks into LLMs to protect intellectual property and detect tampering.
