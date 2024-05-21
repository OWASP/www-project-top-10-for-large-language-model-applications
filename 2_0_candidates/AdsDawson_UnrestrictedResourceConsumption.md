## Unrestricted Resource Consumption

**Author(s):** [Ads - GangGreenTemperTatum](https://github.com/GangGreenTemperTatum)

### Description

Unrestricted Resource Consumption occurs when a Large Language Model (LLM) application allows users to consume excessive resources without proper limitations or controls. This can lead to denial of service (DoS) conditions, degraded performance, and increased operational costs. Common resources affected include CPU, memory, disk space, and network bandwidth. Within LLMs, this has many additional consequences outside of traditional application security which relates to other example risks such as Model Extraction attacks (known as model theft) or Denial of Wallet attacks. Since LLMs demand vast amounts of compute power, their very nature of being present most commonly in cloud environments increases the risk of these types of attacks.

### Common Examples of Risk

1. Variable-Length Input Flood: Overloading the LLM with numerous inputs of varying lengths, designed to exploit processing inefficiencies, deplete resources, and potentially render the system unresponsive.
2. Denial of Wallet (DoW): Initiating a high volume of operations to exploit the cost-per-use model of cloud-based AI services, leading to unsustainable expenses for the provider.
3. Continuous Input Overflow: Continuously sending inputs that exceed the LLM's context window, leading to excessive use of computational resources.
4. Resource-Intensive Queries: Submitting unusually demanding queries that involve complex sequences or intricate language patterns.
5. Shadow Model Theft: An attacker queries the model API using carefully crafted inputs and prompt injection techniques to collect a sufficient number of outputs to create a shadow model.

### Prevention and Mitigation Strategies

- **Input Validation**: Implement strict input validation to ensure that inputs do not exceed reasonable size limits.
- **Rate Limiting**: Apply rate limiting and user quotas to restrict the number of requests a single user or IP can make in a given time period.
- **Resource Allocation Management**: Monitor and manage resource allocation dynamically to prevent any single user or request from consuming excessive resources.
- **Timeouts and Throttling**: Set timeouts and throttle processing for resource-intensive operations to prevent prolonged resource consumption.
- **Logging and Monitoring**: Continuously monitor resource usage and implement logging to detect and respond to unusual patterns of resource consumption.
- **Graceful Degradation**: Design the system to degrade gracefully under heavy load, maintaining partial functionality rather than complete failure.
- **Glitch Token Filtering**: Build lists of known glitch tokens and scan output before adding it to the model’s context window.
- **Limit Queued Actions**: Limit the number of queued actions and total actions in systems reacting to LLM responses.

### Example Attack Scenarios

1. Uncontrolled Input Size. An attacker submits an unusually large input to an LLM application that processes text data. The application attempts to process the entire input without validating its size, resulting in excessive memory usage and CPU load, which can crash the system or significantly slow down the service.
2. Repeated Requests. An attacker scripts a bot to send a high volume of requests to the LLM API, causing excessive consumption of computational resources. The lack of rate limiting or usage quotas allows the attacker to overwhelm the system, making the service unavailable to legitimate users.
3. Resource-Intensive Queries. An attacker crafts specific inputs designed to trigger the LLM's most computationally expensive processes. For instance, they might exploit a feature that performs extensive data lookups or complex calculations, leading to prolonged CPU usage and potential system failure.
4. Denial of Wallet (DoW). Generating excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.

### Reference Links

- [API4:2023 - Unrestricted Resource Consumption](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/)
- [OWASP Resource Management](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/latest/secp212.html)
- [NIST SP 800-53](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r5.pdf) - Security and Privacy Controls for Information Systems and Organizations
- [CWE-400: Uncontrolled Resource Consumption](https://cwe.mitre.org/data/definitions/400.html)
- [AML.TA0000 ML Model Access: Mitre ATLAS](https://atlas.mitre.org/tactics/AML.TA0000)
- [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/)
- [Sponge Examples: Energy-Latency Attacks on Neural Networks: Arxiv White Paper](https://arxiv.org/abs/2006.03463)
- [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023)
- [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996)
- [Stealing Part of a Production Language Model: Arxiv White Paper](https://arxiv.org/abs/2403.06634)

### Additional Notes

The additional effort for this may remove/merge both [LLM04_ModelDoS](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications/blob/main/1_1_vulns/LLM04_ModelDoS.md) and [LLM10_ModelTheft](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications/blob/main/1_1_vulns/LLM10_ModelTheft.md) vulnerabilities and thus allow us to open the list to additional vectors.