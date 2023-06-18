## Indirect Prompt Injection

**Author(s):**

Steve Wilson

**Description:**

Indirect Prompt Injection, also known as Second Order Prompt Injection, is a variant of Prompt Injection where the attacker manipulates data consumed by a Large Language Model (LLM), effectively "poisoning" it. Unlike direct Prompt Injection, where the attacker directly influences the input to the LLM, in Indirect Prompt Injection, the attacker indirectly influences the input by manipulating a data source that the LLM will subsequently consume. This can result in unwanted behavior, system compromises, and data breaches, among other concerns.

**Labels/Tags:**

- Label: "Retrieval-Based Attacks"
- Label: "Indirect Prompt Injection"
- Label: "Data Poisoning"
- Label: "Input Manipulation"
- Label: "Indirect Prompt Injection"
- Label: "Second Order Injection"

**Common Examples of Vulnerability:**

1. Example 1: An attacker embeds malicious prompts in a data source (like a webpage) that is likely to be retrieved by the LLM during inference time.
2. Example 2: An adversary uses hidden messages or 'code words' to catch an LLM's attention and manipulate it.
3. Example 3: Injections are delivered via advertisements or other external data sources consumed by the LLM.

**How to Prevent:**

1. Implement robust safeguards around the data that an LLM may access and ingest during its processing.
2. Enhance the curation and vetting of data sources used by the LLM to reduce the risk of encountering manipulated data.
3. PIncorporate detection mechanisms for potential injected prompts in the data retrieved by the LLM, and take necessary actions when such prompts are detected.
4. Implement additional checks for external data sources, especially when interacting with plugins or tools.

**Example Attack Scenarios:**

Scenario #1: An attacker creates a webpage with hidden malicious prompts. When the LLM retrieves data from this page to respond to a user's query, it is led to generate harmful content or disclose sensitive information.

Scenario #2:  An adversary exploits the LLM-integrated advertising system, delivering injection payloads via the ads themselves. This results in unintended behavior by the LLM that leads to data compromise or other harmful outcomes.

**Reference Links:**

1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf): This paper provides an in-depth look at the Indirect Prompt Injection vulnerability in Large Language Models, including examples and potential mitigation strategies.

2. [Indirect Prompt Injection in LLMs - GitHub Repository](https://github.com/greshake/llm-security): A repository including demonstrations and proofs of concept.

3. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): Sending untrusted data to your AI can lead to unintended (bad) consequences.


**Author Commentary (Optional):**

Prompt Injection and Indirect Prompt Injection, while sharing similarities, present unique risks and vulnerabilities in the context of Large Language Models (LLMs).

Prompt Injection involves an attacker manipulating the direct input to an LLM, guiding its output towards harmful or malicious ends. The interaction here is straightforward—the user input serves as the "prompt" that the LLM uses to generate its output, and if the prompt is manipulated, the output can be as well.

Indirect Prompt Injection, on the other hand, is a more sophisticated vulnerability. It doesn't involve the direct manipulation of the prompt to the LLM. Instead, it exploits the LLM's data retrieval functionality, which is used to fetch and process data during inference. Attackers plant malicious prompts in the data sources that the LLM may access during its operation. When the LLM processes this manipulated data, it may generate outputs that are harmful or inappropriate, leading to similar consequences as Prompt Injection but through a more indirect and potentially more covert method.

The subtlety and complexity of Indirect Prompt Injection can make it more challenging to detect and prevent. It requires robust safeguards not only around the inputs to the LLM but also around the data that the LLM may access during its operation. It necessitates a deeper understanding of the data landscape that the LLM interacts with and the potential vulnerabilities in this landscape.

Including both Prompt Injection and Indirect Prompt Injection in the OWASP Top 10 list highlights the breadth and depth of potential vulnerabilities with LLMs. It underscores the need for robust, multi-layered security measures to protect against a wide range of threats. Both vulnerabilities shed light on different aspects of LLM security—Prompt Injection emphasizes the need for strong input validation and sanitization, while Indirect Prompt Injection highlights the importance of secure data handling and processing. Together, they provide a more comprehensive picture of the security landscape for LLMs, which is vital for developing effective security strategies.