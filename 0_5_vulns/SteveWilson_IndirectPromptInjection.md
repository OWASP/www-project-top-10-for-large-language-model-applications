## Indirect Prompt Injection

**Author(s):**

Steve Wilson

**Description:**

Indirect Prompt Injection is a sophisticated vulnerability where an attacker influences the data retrieved by a Large Language Model (LLM) at inference time to guide its output in a malicious manner. This can lead to harmful behavior from the LLM, such as generation of inappropriate content, disclosure of sensitive information, or manipulation of users.

**Labels/Tags:**

- Label: "Retrieval-Based Attacks"
- Label: "Indirect Prompt Injection"
- Label: "Data Poisoning"

**Common Examples of Vulnerability:**

1. Example 1: An attacker embeds malicious prompts in a data source (like a webpage) that is likely to be retrieved by the LLM during inference time.
2. Example 2: The LLM ingests these hidden prompts and generates outputs that lead to harmful or inappropriate system behavior.
3. Example 3: Through the injected prompts, the LLM is led to believe that it is interacting with authorized individuals, leading it to disclose sensitive information or perform unauthorized actions.

**How to Prevent:**

1. Prevention Step 1: Implement robust safeguards around the data that an LLM may access and ingest during its processing.
2. Prevention Step 2: Enhance the curation and vetting of data sources used by the LLM to reduce the risk of encountering manipulated data.
3. Prevention Step 3: Incorporate detection mechanisms for potential injected prompts in the data retrieved by the LLM, and take necessary actions when such prompts are detected.

**Example Attack Scenarios:**

Scenario #1: An attacker creates a webpage with hidden malicious prompts. When the LLM retrieves data from this page to respond to a user's query, it is led to generate harmful content or disclose sensitive information.

Scenario #2: The attacker manipulates the LLM into believing it is interacting with a Microsoft sales person, leading the LLM to offer highly discounted applications and tricking the user into providing their credit card number.

**Reference Links:**

1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf): This paper provides an in-depth look at the Indirect Prompt Injection vulnerability in Large Language Models, including examples and potential mitigation strategies.

2. [Indirect Prompt Injection in LLMs - GitHub Repository](https://github.com/greshake/llm-security): A repository including demonstrations and proofs of concept.


**Author Commentary (Optional):**

Prompt Injection and Indirect Prompt Injection, while sharing similarities, present unique risks and vulnerabilities in the context of Large Language Models (LLMs).

Prompt Injection involves an attacker manipulating the direct input to an LLM, guiding its output towards harmful or malicious ends. The interaction here is straightforward—the user input serves as the "prompt" that the LLM uses to generate its output, and if the prompt is manipulated, the output can be as well.

Indirect Prompt Injection, on the other hand, is a more sophisticated vulnerability. It doesn't involve the direct manipulation of the prompt to the LLM. Instead, it exploits the LLM's data retrieval functionality, which is used to fetch and process data during inference. Attackers plant malicious prompts in the data sources that the LLM may access during its operation. When the LLM processes this manipulated data, it may generate outputs that are harmful or inappropriate, leading to similar consequences as Prompt Injection but through a more indirect and potentially more covert method.

The subtlety and complexity of Indirect Prompt Injection can make it more challenging to detect and prevent. It requires robust safeguards not only around the inputs to the LLM but also around the data that the LLM may access during its operation. It necessitates a deeper understanding of the data landscape that the LLM interacts with and the potential vulnerabilities in this landscape.

Including both Prompt Injection and Indirect Prompt Injection in the OWASP Top 10 list highlights the breadth and depth of potential vulnerabilities with LLMs. It underscores the need for robust, multi-layered security measures to protect against a wide range of threats. Both vulnerabilities shed light on different aspects of LLM security—Prompt Injection emphasizes the need for strong input validation and sanitization, while Indirect Prompt Injection highlights the importance of secure data handling and processing. Together, they provide a more comprehensive picture of the security landscape for LLMs, which is vital for developing effective security strategies.