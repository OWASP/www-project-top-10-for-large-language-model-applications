## LLM10:2025 Unbounded Consumption

### Description

Unbounded Consumption refers to the process where a Large Language Model (LLM) generates outputs based on input queries or prompts. Inference is a critical function of LLMs, involving the application of learned patterns and knowledge to produce relevant responses or predictions.

Attacks designed to disrupt service, deplete the target's financial resources, or even steal intellectual property by cloning a model’s behavior all depend on a common class of security vulnerability in order to succeed. Unbounded Consumption occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to risks such as denial of service (DoS), economic losses, model theft, and service degradation. The high computational demands of LLMs, especially in cloud environments, make them vulnerable to resource exploitation and unauthorized usage.

### Common Examples of Vulnerability

#### 1. Variable-Length Input Flood
  Attackers can overload the LLM with numerous inputs of varying lengths, exploiting processing inefficiencies. This can deplete resources and potentially render the system unresponsive, significantly impacting service availability.
#### 2. Denial of Wallet (DoW)
  By initiating a high volume of operations, attackers exploit the cost-per-use model of cloud-based AI services, leading to unsustainable financial burdens on the provider and risking financial ruin.
#### 3. Continuous Input Overflow
  Continuously sending inputs that exceed the LLM's context window can lead to excessive computational resource use, resulting in service degradation and operational disruptions.
#### 4. Resource-Intensive Queries
  Submitting unusually demanding queries involving complex sequences or intricate language patterns can drain system resources, leading to prolonged processing times and potential system failures.
#### 5. Model Extraction via API
  Attackers may query the model API using carefully crafted inputs and prompt injection techniques to collect sufficient outputs to replicate a partial model or create a shadow model. This not only poses risks of intellectual property theft but also undermines the integrity of the original model.
#### 6. Functional Model Replication
  Using the target model to generate synthetic training data can allow attackers to fine-tune another foundational model, creating a functional equivalent. This circumvents traditional query-based extraction methods, posing significant risks to proprietary models and technologies.
#### 7. Side-Channel Attacks
  Malicious attackers may exploit input filtering techniques of the LLM to execute side-channel attacks, harvesting model weights and architectural information. This could compromise the model's security and lead to further exploitation.

### Prevention and Mitigation Strategies

#### 1. Input Validation
  Implement strict input validation to ensure that inputs do not exceed reasonable size limits.
#### 2. Limit Exposure of Logits and Logprobs
  Restrict or obfuscate the exposure of `logit_bias` and `logprobs` in API responses. Provide only the necessary information without revealing detailed probabilities.
#### 3. Rate Limiting
  Apply rate limiting and user quotas to restrict the number of requests a single source entity can make in a given time period.
#### 4. Resource Allocation Management
  Monitor and manage resource allocation dynamically to prevent any single user or request from consuming excessive resources.
#### 5. Timeouts and Throttling
  Set timeouts and throttle processing for resource-intensive operations to prevent prolonged resource consumption.
#### 6.Sandbox Techniques
  Restrict the LLM's access to network resources, internal services, and APIs.
  - This is particularly significant for all common scenarios as it encompasses insider risks and threats. Furthermore, it governs the extent of access the LLM application has to data and resources, thereby serving as a crucial control mechanism to mitigate or prevent side-channel attacks.
#### 7. Comprehensive Logging, Monitoring and Anomaly Detection
  Continuously monitor resource usage and implement logging to detect and respond to unusual patterns of resource consumption.
#### 8. Watermarking
  Implement watermarking frameworks to embed and detect unauthorized use of LLM outputs.
#### 9. Graceful Degradation
  Design the system to degrade gracefully under heavy load, maintaining partial functionality rather than complete failure.
#### 10. Limit Queued Actions and Scale Robustly
  Implement restrictions on the number of queued actions and total actions, while incorporating dynamic scaling and load balancing to handle varying demands and ensure consistent system performance.
#### 11. Adversarial Robustness Training
  Train models to detect and mitigate adversarial queries and extraction attempts.
#### 12. Glitch Token Filtering
  Build lists of known glitch tokens and scan output before adding it to the model’s context window.
#### 13. Access Controls
  Implement strong access controls, including role-based access control (RBAC) and the principle of least privilege, to limit unauthorized access to LLM model repositories and training environments.
#### 14. Centralized ML Model Inventory
  Use a centralized ML model inventory or registry for models used in production, ensuring proper governance and access control.
#### 15. Automated MLOps Deployment
  Implement automated MLOps deployment with governance, tracking, and approval workflows to tighten access and deployment controls within the infrastructure.

### Example Attack Scenarios

#### Scenario #1: Uncontrolled Input Size
  An attacker submits an unusually large input to an LLM application that processes text data, resulting in excessive memory usage and CPU load, potentially crashing the system or significantly slowing down the service.
#### Scenario #2: Repeated Requests
  An attacker transmits a high volume of requests to the LLM API, causing excessive consumption of computational resources and making the service unavailable to legitimate users.
#### Scenario #3: Resource-Intensive Queries
  An attacker crafts specific inputs designed to trigger the LLM's most computationally expensive processes, leading to prolonged CPU usage and potential system failure.
#### Scenario #4: Denial of Wallet (DoW)
  An attacker generates excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.
#### Scenario #5: Functional Model Replication
  An attacker uses the LLM's API to generate synthetic training data and fine-tunes another model, creating a functional equivalent and bypassing traditional model extraction limitations.
#### Scenario #6: Bypassing System Input Filtering
  A malicious attacker bypasses input filtering techniques and preambles of the LLM to perform a side-channel attack and retrieve model information to a remote controlled resource under their control.

### Reference Links

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)
2. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
3. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [You wouldn't download an AI, Extracting AI models from mobile apps](https://altayakkus.substack.com/p/you-wouldnt-download-an-ai): **Substack blog**
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
7. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
9. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
10. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) & [AML.T0024 Exfiltration via ML Inference API](https://atlas.mitre.org/techniques/AML.T0024) **MITRE ATLAS**
- [AML.T0029 - Denial of ML Service](https://atlas.mitre.org/techniques/AML.T0029) **MITRE ATLAS**
- [AML.T0034 - Cost Harvesting](https://atlas.mitre.org/techniques/AML.T0034) **MITRE ATLAS**
- [AML.T0025 - Exfiltration via Cyber Means](https://atlas.mitre.org/techniques/AML.T0025) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/) **OWASP Secure Coding Practices**
