## Unrestricted Model Inference

**Author(s):** [Ads - GangGreenTemperTatum](https://github.com/GangGreenTemperTatum)
<br>
**Core Team Owner(s):** [Ads - GangGreenTemperTatum](https://github.com/GangGreenTemperTatum) with reviews from @jsotiro and @rot169

### Description

Unrestricted Model Inference refers to the process where a Large Language Model (LLM) generates outputs based on input queries or prompts. Inference is a critical function of LLMs, involving the application of learned patterns and knowledge to produce relevant responses or predictions.

Unrestricted Model Inference occurs when a Large Language Model (LLM) application allows users to conduct excessive and uncontrolled inferences, leading to potential risks such as denial of service (DoS), economic losses, model or intellectual property theft theft, and degradation of service. This vulnerability is exacerbated by the high computational demands of LLMs, often deployed in cloud environments, making them susceptible to various forms of resource exploitation and unauthorized usage.

### Common Examples of Vulnerability

1. **Variable-Length Input Flood**: Overloading the LLM with numerous inputs of varying lengths to exploit processing inefficiencies, deplete resources, and potentially render the system unresponsive.
2. **Denial of Wallet (DoW)**: Initiating a high volume of operations to exploit the cost-per-use model of cloud-based AI services, leading to unsustainable expenses for the provider.
3. **Continuous Input Overflow**: Continuously sending inputs that exceed the LLM's context window, leading to excessive use of computational resources.
4. **Resource-Intensive Queries**: Submitting unusually demanding queries that involve complex sequences or intricate language patterns.
5. **Model Extraction via API**: An attacker queries the model API using carefully crafted inputs and prompt injection techniques to collect sufficient outputs to replicate a partial model or create a shadow model.
   - The attack vector for model extraction can involve querying the LLM with a large number of prompts on a particular topic. The outputs from the LLM can then be used to fine-tune another model.
   - Alternatively, an attack can originate from a linear number of queries corresponding to the size of the embedding layer. This runs in polynomial time, allowing access to the final layer of the model, which is often just the transpose of the first embedding layer.
6. **Functional Model Replication**: This involves using a target model to generate synthetic training data to fine-tune another foundational model, creating a functional equivalent. The attack vector for **_functional model replication_** entails using the target model to generate synthetic data (through a method known as "self-instruct") which is then used to fine-tune another foundational model, effectively producing a functional equivalent. This approach bypasses traditional query-based extraction methods and has been successfully applied in research where one LLM is used to train another. Note that in the context of this research, model replication is not considered an attack.
7. **Side-Channel Attacks**: A malicious attacker may exploit input filtering techniques of the LLM to execute a side-channel attack, ultimately harvesting model weights and architectural information to a remote-controlled resource.

### Prevention and Mitigation Strategies

1. **Input Validation**: Implement strict input validation to ensure that inputs do not exceed reasonable size limits.
2. **Limit Exposure of Logits and Logprobs**: Restrict or obfuscate the exposure of `logit_bias` and `logprobs` in API responses. Provide only the necessary information without revealing detailed probabilities.
3. **Rate Limiting**: Apply rate limiting and user quotas to restrict the number of requests a single source entity can make in a given time period.
4. **Resource Allocation Management**: Monitor and manage resource allocation dynamically to prevent any single user or request from consuming excessive resources.
5. **Timeouts and Throttling**: Set timeouts and throttle processing for resource-intensive operations to prevent prolonged resource consumption.
6. **Sandbox Techniques**: Restrict the LLM's access to network resources, internal services, and APIs.
   - This is particularly significant for all common scenarios as it encompasses insider risks and threats. Furthermore, it governs the extent of access the LLM application has to data and resources, thereby serving as a crucial control mechanism to mitigate or prevent side-channel attacks.
7. **Comprehensive Logging, Monitoring and Anomaly Detection**: Continuously monitor resource usage and implement logging to detect and respond to unusual patterns of resource consumption.
8. **Watermarking**: Implement watermarking frameworks to embed and detect unauthorized use of LLM outputs.
9. **Graceful Degradation**: Design the system to degrade gracefully under heavy load, maintaining partial functionality rather than complete failure.
10. **Limit Queued Actions and Scale Robustly**: Implement restrictions on the number of queued actions and total actions, while incorporating dynamic scaling and load balancing to handle varying demands and ensure consistent system performance.
11. **Adversarial Robustness Training**: Train models to detect and mitigate adversarial queries and extraction attempts.
12. **Glitch Token Filtering**: Build lists of known glitch tokens and scan output before adding it to the model’s context window.
13. **Access Controls**: Implement strong access controls, including role-based access control (RBAC) and the principle of least privilege, to limit unauthorized access to LLM model repositories and training environments.
14. **Centralized ML Model Inventory**: Use a centralized ML model inventory or registry for models used in production, ensuring proper governance and access control.
15. **Automated MLOps Deployment**: Implement automated MLOps deployment with governance, tracking, and approval workflows to tighten access and deployment controls within the infrastructure.

### Example Attack Scenarios

1. **Uncontrolled Input Size**: An attacker submits an unusually large input to an LLM application that processes text data, resulting in excessive memory usage and CPU load, potentially crashing the system or significantly slowing down the service.
2. **Repeated Requests**: An attacker transmits a high volume of requests to the LLM API, causing excessive consumption of computational resources and making the service unavailable to legitimate users.
3. **Resource-Intensive Queries**: An attacker crafts specific inputs designed to trigger the LLM's most computationally expensive processes, leading to prolonged CPU usage and potential system failure.
4. **Denial of Wallet (DoW)**: An attacker generates excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.
5. **Functional Model Replication**: An attacker uses the LLM's API to generate synthetic training data and fine-tunes another model, creating a functional equivalent and bypassing traditional model extraction limitations.
6. **Bypassing System Input Filtering**: A malicious attacker bypasses input filtering techniques and preambles of the LLM to perform a side-channel attack and retrieve model information to a remote controlled resource under their control.

### Reference Links

1. [arXiv:2403.06634 Stealing Part of a Production Language Model](https://arxiv.org/abs/2403.06634) **arXiv**
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
3. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
4. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
7. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
8. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
9.  [Securing AI Model Weights Preventing Theft and Misuse of Frontier Models](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf)
10. [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463) **arXiv**
11. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023) **Sourcegraph**

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) - **NIST Security and Privacy Controls for Information Systems and Organizations**
- [MITRE CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html) **MITRE Common Weakness Enumeration**
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000) **MITRE ATLAS**
- [OWASP Machine Learning Security Top Ten - ML05:2023 Model Theft](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html) **OWASP ML Top 10**
- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/) **OWASP Web Application Top 10**
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/latest/secp212.html) **OWASP Secure Coding Practices**