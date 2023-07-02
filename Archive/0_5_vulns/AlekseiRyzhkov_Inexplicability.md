## Inexplicability

**Author(s):**

Aleksei Ryzhkov

**Description:**

As opposed to application codebase, the LLM, by its indeterministic nature, may produce output, which is hard to understand, debug/find the reason or fix. LLM response may be impossible to reproduce even for the same prompt. Backdoors, implanted to the model (poison), cannot be detected via such common means as a code review.  Once the model is poisoned - we cannot heal it by tinkering with particular weights but can only apply additional training (not reliable) or retraining from scratch (reliable, but cost-prohibitive). These security risks (inherent to the LLM nature) should drive the design and production use of LLM-based systems (similar as we should design LLM-based systems around prompt-injection risk).

**Labels/Tags:**

- Label: Opaqueness
- Label: Irreversible changes
- Label: Model poisoning
- Label: Overreliance
- Label: Hallucination

**Common Examples of Vulnerability:**

1. Based on application logs the developer cannot reproduce the model's output for the given user's prompt (especially if model was used with high temperature).  
2. Inability to detect backdoor (poisoning) in the model until that backdoor exploitation. 

**How to Prevent:**

1. Design the system around the possibility of unexpected model output (like it is poisoned, don't trust LLM output). 
2. Supply chain risk management: verify supplier's trustworthy, how and on what data the model has been trained etc.
3. Integrity assurance of model (digital signature) - similar as we sign container images. Maintain backups to restore in case of integrity violation is detected.     
4. Prompting LLM in a way to force the model to detail execution steps and reasoning. E.g. 'let's think step by step. Detail each step' - (for post-incident investigation)
5. Consider the need for debugging while selecting the model's temperature. Use the minimal temperature possible to fit business cases.

**Example Attack Scenarios:**

Scenario #1: An adversary poisons the model on the training stage to exploit it later in production use (e.g. to avoid detection in LLM-based SOC).
Scenario #2: An adversary explicitly poisons the model to force the company to retrain the model from scratch (cost prohibitive).
Scenario #3: Malicious outcome from the poisoned model is attributed to the use of the model with high-temperature setting.

**Reference Links:**

1. [LM-Debugger: An Interactive Tool for Inspection and Intervention in Transformer-Based Language Models](https://arxiv.org/abs/2204.12130): Attempt to debug the opaque nature and unexplained behavior of transformer-based language models. Support only GPT-2, no active development in the tool repository in last year.
2. [A question on determinism](https://community.openai.com/t/a-question-on-determinism/8185): Discussion on Open AI forum to explain different LLM responses even with the same prompt and zero temperature. 
3. [Using Large Language Models With Care](https://blog.allenai.org/using-large-language-models-with-care-eeb17b0aed27): Blogpost. See Risk #7: LLMs cannot attribute sources for the text they produce.
4. [Instructions as Backdoors - Backdoor Vulnerabilities of Instruction Tuning for Large Language Models](https://arxiv.org/abs/2305.14710): Studies demonstrate that an attacker can inject persistent backdoors by issuing very few malicious instructions and control model behavior through data poisoning. Moreover, the poisoned model cannot be cured by continual learning.

**Author Commentary (Optional):**

One may reasonably argue this is not a vulnerability but the inherent property of LLM (we have a similar discussion about 'prompt injection' vulnerability-property).
As a developer, I would use slightly another perspective. I like OWASP top 10 as a top 10 of security RISKS - top 10 things I should worry about (for example A04: Insecure design). As long as the named issue is important for building secure system, and I receive actionable recommendations - I don't care much about the cause under the hood (vulnerability or inherent property or you name it). The security risk above (inexplicability) looks important to me, and I feel sorry to not educate people about it because it doesn’t fit the vulnerability classification. Perhaps this risk could be merged into 'overreliance' or 'poisoning'.


