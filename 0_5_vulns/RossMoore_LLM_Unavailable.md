## Vulnerability Name

LLM Unavailable

**Author(s):**

Ross Moore

**Description:**

Organizations can run into financial and reputational difficulties if LLM resources are not configured for scalability, HA, peak usage, etc.


**Common Examples of Vulnerability:**

1. Example 1: " - "ChatGPT Error Code 429" https://www.onmsft.com/how-to/fix-chatgpt-not-working-error-high-demand/
2. Example 2: "Internal server Error" - https://www.howtogeek.com/874410/fix-chatgpt-internal-server-error-and-other-common-errors/
3. Example 3: “ChatGPT Is at Capacity Right Now”- https://www.howtogeek.com/883043/chatgpt-is-at-capacity-right-now-error/; 

NOTE: I realize these are not known attacks or authoritative articles. But the vulenrability is for a business resource to crash.

**How to Prevent:**

1. Prevention Step 1: Use a load balancer to distribute traffic across multiple servers
2. Prevention Step 2: Use a firewall to filter out malicious traffic.
3. Prevention Step 3: Create a scalable, resilient, and responsive infrastructure.


**Example Attack Scenarios:**

Scenario #1: A detailed scenario illustrating how an attacker could potentially exploit this vulnerability, including the attacker's actions and the potential outcomes.

Generate large amounts of text with the LLM, such as paragraphs, essays, or even books. This would put a strain on the LLM's memory and processing power.

Scenario #2: Another example of an attack scenario showing a different way the vulnerability could be exploited.

Run multiple requests - especially complex -  simultaneously: 
Run  multiple requests simultaneously with the LLM, such as generating text, translating languages, or writing different kinds of creative content. This would put a strain on the LLM's ability to handle multiple requests at the same time.


**Reference Links:**

1. [How to Use Large Language Models (LLM) in Your Own Domains](https://towardsdatascience.com/how-to-use-large-language-models-llm-in-your-own-domains-b4dff2d08464):  The end-to-end fine-tuning not only consumes a huge amount of computational resources, but also requires decent size of domain specific labeled data, which is expensive to acquire. As the field of AI advances, models are likely only getting larger, making it increasingly cumbersome to always fine-tuning the entire model end-to-end for every single bespoke task.
2. [CWE-664: Improper Control of a Resource Through its Lifetime](https://cwe.mitre.org/data/definitions/664.html): Resources often have explicit instructions on how to be created, used and destroyed. When code does not follow these instructions, it can lead to unexpected behaviors and potentially exploitable states. Even without explicit instructions, various principles are expected to be adhered to, such as "Do not use an object until after its creation is complete," or "do not use an object after it has been slated for destruction." 
3. https://arxiv.org/pdf/2304.00612.pdf
"Eight Things to Know about Large Language Models", Bowman, Samuel R., arXiv:2304.00612v1 [cs.CL] 2 Apr 2023
"... it is common for new behaviors to emerge abruptly when transitioning from a less resource-intensive version of a
model to a more resource-intensive one."


**Author Commentary (Optional):**

This resource consideration aligns with the A of the CIA (Confidentiality, Integrity, Availablity) triad. Remediation would occur during development, stress test, etc. 
LLMs stand to undergo heavier usage than other applications due to their current celebrity status and upcoming n