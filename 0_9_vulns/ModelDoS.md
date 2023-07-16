## Model Denial of Service

**Description:**
An attacker interacts with an LLM in a way that is particularly resource-consuming, causing quality of service to degrade for them and other users, or for high resource costs to be incurred.
In addition, the attack by interacting with or manipulating the context window of LLM has emerged as a significant security concern. This issue is exacerbated by the increasing prevalence of LLMs in various applications, their resource-intensive nature, the unpredictability of user input, and a general lack of awareness among developers about this vulnerability.
LLMs, the context window refers to the maximum length of text that the model can handle, both for input and output. It is a crucial aspect of LLMs as it determines the complexity of the language patterns the model can learn and the size of the text it can process at a time. The size of the context window is determined by the model's architecture and can vary between different models.

**Common Examples of Vulnerability:**

1. Posing queries that lead to recurring resource usage through high-volume generation of tasks in a queue, e.g. with LangChain or AutoGPT.
2. Sending queries that are unusually resource-consuming, perhaps because they use unusual orthography or sequences.
3. Continuous input overflow: An attacker sends a stream of input to the LLM that exceeds its context window, causing the model to consume excessive computational resources.
4. Repetitive long inputs: The attacker repeatedly sends long inputs to the LLM, each exceeding the context window.
5. Recursive context expansion: The attacker constructs input that triggers recursive context expansion, forcing the LLM to repeatedly expand and process the context window.
6. An attacker sends a stream of input to the LLM that exceeds its context window, causing the model to consume excessive computational resources and potentially leading to a DoS condition.
7. Repetitive long inputs: The attacker repeatedly sends long inputs to the LLM, each exceeding the context window. This forces the model to process large amounts of text, depleting system resources and causing a slowdown or service disruption.
8. Recursive context expansion: By constructing input that triggers recursive context expansion, the attacker forces the LLM to repeatedly expand and process the context window, resulting in a resource-intensive operation that can overwhelm the system and lead to a DoS situation.
9. Variable-length input flood: The attacker floods the LLM with a large volume of variable-length inputs, where each input is carefully crafted to just reach the limit of the context window. This technique aims to exploit any inefficiencies in processing variable-length inputs, straining the LLM and potentially causing it to become unresponsive.
10. Context window exhaustion: The attacker sends a sequence of inputs, each just below the context window's limit. By repeatedly sending these inputs, the attacker aims to exhaust the available context window capacity, causing the LLM to struggle with processing subsequent inputs and potentially leading to a DoS scenario.


**How to Prevent:**

1. Implement input validation and sanitization to ensure user input adheres to defined limits and filters out any malicious content.
2. Cap resource use per request or step, so that requests involving complex parts execute more slowly.
3. Enforce API rate limits to restrict the number of requests an individual user or IP address can make within a specific timeframe.
4. Limit the number of queued actions and the number of total actions in a system reacting to LLM responses.
5. Continuously monitor the resource utilization of the LLM to identify abnormal spikes or patterns that may indicate a DoS attack.
6. Set strict input limits based on the LLM's context window to prevent overload and resource exhaustion.
7. Promote awareness among developers about potential DoS vulnerabilities in LLMs and provide guidelines for secure LLM implementation.


**Example Attack Scenarios:**

1. An attacker repeatedly sends multiple requests to a hosted model that are difficult and costly for it to process, leading to worse service for other users and increased resource bills for the host.
2. A piece of text on a webpage is encountered while an LLM-driven tool is collecting information to respond to a benign query. This leads to the tool making many more web page requests, resulting in large amounts of resource consumption.
3. An attacker continuously bombards the LLM with input that exceeds its context window, causing the model to consume excessive computational resources.
4. The attacker sends a series of sequential inputs to the LLM, each just below the context window's limit. This exhausts the available context window capacity, causing the LLM to struggle with processing subsequent inputs.
5. The attacker leverages the LLM's recursive mechanisms to trigger context expansion repeatedly, causing significant computational resources consumption.
6. **Context Window Overflow (Continuous Bombarding)**

   In this scenario, the attacker continuously bombards the LLM with input that exceeds its context window. The attacker may use automated scripts or tools to send a high volume of input, overwhelming the LLM's processing capabilities. As a result, the LLM consumes excessive computational resources, leading to a significant slowdown or complete unresponsiveness of the system.

7. **Context Window Exhaustion (Persistent Sequential Inputs)**

   In this attack scenario, the attacker sends a series of sequential inputs to the LLM, with each input designed to be just below the context window's limit. By repeatedly submitting these inputs, the attacker aims to exhaust the available context window capacity. As the LLM struggles to process each input within its context window, system resources become strained, potentially resulting in degraded performance or a complete denial of service.

8. **Recursive Context Expansion (Exploiting Recursive Mechanisms)**

   In this attack scenario, the attacker leverages the LLM's recursive mechanisms to trigger context expansion repeatedly. By crafting input that exploits the recursive behavior of the LLM, the attacker forces the model to repeatedly expand and process the context window, consuming significant computational resources. This attack strains the system and may lead to a DoS condition, making the LLM unresponsive or causing it to crash.

9. **Variable-Length Input Flood (Flooding with Variable-Length Inputs)**

   In this attack scenario, the attacker floods the LLM with a large volume of variable-length inputs, carefully crafted to approach or reach the context window's limit. By overwhelming the LLM with inputs of varying lengths, the attacker aims to exploit any inefficiencies in processing variable-length inputs. This flood of inputs puts excessive load on the LLM's resources, potentially causing performance degradation and hindering the system's ability to respond to legitimate requests.

10. **Sequential Long Inputs (Systematic Long Inputs)**

   In this attack scenario, the attacker systematically sends a sequence of long inputs to the LLM, each input being slightly shorter than the context window's limit. By continuously feeding the LLM with these long inputs, the attacker aims to exhaust the model's processing capacity. The LLM struggles to handle the demanding inputs, leading to resource exhaustion, system slowdown, or even a complete denial of service.



**Reference Links:**

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): demo + fix of this vulnerability in LangChain.
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): POC
3. [OWASP DOS Attack](https://owasp.org/www-community/attacks/Denial_of_Service)
4. [Learning From Machines: Know Thy Context](https://lukebechtel.com/blog/lfm-know-thy-context)

**Author Commentary (Optional):**

Including DoS attacks on LLM in the OWASP Top 10 list is critical. Developers must recognize the potential impact of DoS attacks on LLMs and implement necessary measures to mitigate these vulnerabilities. By incorporating this vulnerability into the OWASP Top 10 list, developers can prioritize security measures, raise awareness, and fortify LLM applications against these emerging threats.


