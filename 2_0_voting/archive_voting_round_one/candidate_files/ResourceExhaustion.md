
## Resource Exhaustion

**Author(s):**

Steve Wilson

### Description

Resource exhaustion in Large Language Models (LLMs) encompasses both Denial of Service (DoS) and Denial of Wallet (DoW) attacks. These attacks exploit the intensive resource utilization of LLMs, causing service disruption, degraded performance, and financial strain. DoS attacks aim to overwhelm the model's computational resources, making it unavailable to users. DoW attacks, a variant of DoS, specifically target the financial resources by generating excessive operations, leading to unsustainable costs. These attacks pose significant threats to the operational and economic viability of services utilizing LLMs.

### Common Examples of Vulnerability

1. **High-Volume Task Generation:** Attackers pose queries that lead to recurring resource usage through high-volume generation of tasks in a queue, e.g., with LangChain or AutoGPT.
2. **Resource-Intensive Queries:** Sending unusually resource-consuming queries that use complex sequences or orthography.
3. **Continuous Input Overflow:** An attacker sends a stream of input that exceeds the LLM's context window, causing excessive computational resource consumption.
4. **Recursive Context Expansion:** Constructing input that triggers recursive context expansion, forcing the LLM to repeatedly expand and process the context window.
5. **Variable-Length Input Flood:** Flooding the LLM with a large volume of variable-length inputs, crafted to exploit inefficiencies in processing, straining resources, and causing potential unresponsiveness.
6. **Unsafe Code Generation:** The model suggests insecure or non-existent code libraries, leading to potential security vulnerabilities when integrated into software.
7. **Denial of Wallet (DoW):** Generating excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.

### Prevention and Mitigation Strategies

1. **Input Validation and Sanitization:** Ensure user input adheres to defined limits and filters out malicious content.
2. **Resource Use Capping:** Cap resource use per request or step, allowing complex parts to execute more slowly.
3. **API Rate Limits:** Restrict the number of requests an individual user or IP address can make within a specific timeframe.
4. **Limit Queued Actions:** Limit the number of queued actions and total actions in systems reacting to LLM responses.
5. **Continuous Monitoring:** Monitor the resource utilization of the LLM to identify abnormal spikes or patterns indicating a DoS attack.
6. **Strict Input Limits:** Set input limits based on the LLM's context window to prevent overload and resource exhaustion.
7. **Developer Awareness:** Promote awareness among developers about potential DoS vulnerabilities in LLMs and provide guidelines for secure LLM implementation.
8. **Glitch Token Filtering:** Build lists of known glitch tokens and scan output before adding it to the model’s context window.
9. **Financial Thresholds and Alerts:** Set financial thresholds and alerts for cloud-based LLM usage to prevent DoW attacks.

### Example Attack Scenarios

1. **Scenario #1:** An attacker repeatedly sends multiple difficult and costly requests to a hosted model, leading to worse service for other users and increased resource bills for the host.
2. **Scenario #2:** A piece of text on a webpage is encountered while an LLM-driven tool is collecting information to respond to a benign query, leading to the tool making many more web page requests, resulting in large amounts of resource consumption.
3. **Scenario #3:** An attacker continuously bombards the LLM with input that exceeds its context window using automated scripts, overwhelming its processing capabilities, causing significant slowdown or unresponsiveness.
4. **Scenario #4:** An attacker sends sequential inputs to the LLM, each just below the context window's limit, exhausting available context window capacity and degrading performance.
5. **Scenario #5:** An attacker leverages the LLM's recursive mechanisms to repeatedly expand and process the context window, consuming significant computational resources and causing DoS conditions.
6. **Scenario #6:** An attacker floods the LLM with variable-length inputs, crafted to exploit inefficiencies, overwhelming resources, and hindering legitimate requests.
7. **Scenario #7:** An attacker exploits the pay-per-use model by generating excessive queries or operations, leading to unsustainable costs for the service provider (Denial of Wallet).

### Reference Links

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): **hwchase17 on Twitter**
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): **Arxiv White Paper**
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service): **OWASP**
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context): **Luke Bechtel**
5. [Sourcegraph Security Incident on API Limits Manipulation and DoS Attack](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**

