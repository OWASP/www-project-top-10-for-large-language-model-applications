

## System Prompt Leakage

**Author(s): Rachit Sood

### Description

A system prompt is a set of instructions or context provided to a large language model (LLM) or AI system before presenting it with a user's query or task. 
Unintended disclosure or extraction of the system prompt, could contain sensitive information, instructions, or data used to guide the LLM's behavior and allow attackers to craft prompts that manipulate the LLM's responses.

### Common Examples of Risk

1. Exposure of Sensitive Data: System prompts may contain sensitive data used for training or fine-tuning the LLM, such as anonymized personal information or proprietary data. Leaking this information can lead to privacy breaches and data exposure
2. Manipulation and Exploitation: With knowledge of the system prompt, attackers can craft prompts to manipulate the LLM's responses or exploit vulnerabilities in the logic and decision-making processes encoded in the prompt.
3. Reconnaissance for Attacks: Leaked system prompts provide valuable reconnaissance information for attackers, revealing the inner workings, biases, and vulnerabilities of the LLM system, enabling more effective planning and execution of attacks.

### Prevention and Mitigation Strategies

1. Input Validation: Implement strict input validation and filtering mechanisms to detect and reject prompts attempting to extract sensitive information
2. Prompt Design and Model Tuning: Design prompts and fine-tune models to reduce their propensity to leak system prompts, and develop models adept at recognizing and withholding confidential data.
3. Continuous Monitoring and Red Teaming: Establish continuous monitoring and employ red teams to simulate prompt leakage scenarios, identifying and addressing vulnerabilities proactively.

### Example Attack Scenarios

1. Scenario #1: Through carefully crafted prompts, attackers can coax the model into system prompts and context details that should remain confidential, exploiting the LLM’s comprehensive training against itself.
2. Scenario #2: By understanding the specific system prompts or examples an LLM was trained on, attackers could devise more effective prompt injections to bypass content restrictions, manipulate outputs, or extract even more detailed information.

### Reference Links

1. [System Prompt Leaks are Bad](https://www.sydelabs.ai/blog/why-system-prompt-leaks-are-bad): **SydeLabs** 
2. [OpenAI Custom Chatbot GPTs Are Leaking their Secrets](https://www.wired.com/story/openai-custom-chatbots-gpts-prompt-injection-attacks/): **Wired**
3. [Prompt Hacking of Large Language Models](https://www.comet.com/site/blog/prompt-hacking-of-large-language-models/): **Comet**
