### LLM01:2023 - Prompt Injections

**Description:**  
Prompt injections involve bypassing filters or manipulating the LLM using carefully crafted prompts that make the model ignore previous instructions or perform unintended actions. These vulnerabilities can lead to unintended consequences, including data leakage, unauthorized access, or other security breaches.

**Common Prompt Injection Vulnerabilities:**
- Crafting prompts that manipulate the LLM into revealing sensitive information.
- Bypassing filters or restrictions by using specific language patterns or tokens.
- Exploiting weaknesses in the LLM's tokenization or encoding mechanisms.
- Misleading the LLM to perform unintended actions by providing misleading context.

**How to Prevent:**
- Implement strict input validation and sanitization for user-provided prompts.
- Use context-aware filtering and output encoding to prevent prompt manipulation.
- Implement programmable guardrails to LLM-based conversational systems. Guardrails are specific ways of controlling the output of a large language model to prevent undesirable, unethical, or potentially harmful outputs. [source](https://github.com/NVIDIA/NeMo-Guardrails)

- Regularly update and fine-tune the LLM to improve its understanding of malicious inputs and edge cases.
- Monitor and log LLM interactions to detect and analyze potential prompt injection attempts.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that tricks the LLM into revealing sensitive information, such as user credentials or internal system details, by making the model think the request is legitimate.

_Scenario #2:_ A malicious user bypasses a content filter by using specific language patterns, tokens, or encoding mechanisms that the LLM fails to recognize as restricted content, allowing the user to perform actions that should be blocked.


** Example Mitigation Methods:**

* One approach to prevent jailbreaking attacks would be to implement programmable guardrails. Programmable guardrails could be used for detecting malicious user input. [Guardrails](https://github.com/NVIDIA/NeMo-Guardrails) utilizes a secondary large language model, termed the "Guard LLM", which reviews user input and determines whether it could lead the bot to behave inappropriately. If such an input is detected, the Guard LLM can intervene, altering the bot's response or stopping the conversation entirely.
