## **Vulnerability Name:**

### Training Data Poisoning

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

- The starting point of any machine learning approach is training data. In terms of large language models, the training data is just “raw text”. To be highly capable (e.g., have linguistic and world knowledge), this text should span a broad range of domains, genres, languages, etc.
  - A large language model uses deep neural networks to generate outputs based on patterns learned from training data.
- Training data poisoning occurs when an attacker or unaware client of the LLM manipulates the training data or fine-tuning procedures of an LLM to introduce vulnerabilities, backdoors, or biases that could compromise the model’s security, effectiveness, or ethical behavior.
  - This unethical or incorrect information is then presented to users of the AI.
  - In cases where the user does not trust the AI and is not influenced, there are still many risks associated with the vulnerability, such as model performance and even down to brand reputation.
- Data poisoning is considered an integrity attack because tampering with the training data impacts the model’s ability to output correct predictions.


There are several data sources that are worth discussing:

1. **Common Crawl** — Because of its convenience, it has been a standard source of data to train many models such as T5, GPT-3, and Gopher. The April 2021 snapshot of Common Crawl has 320 terabytes of data.
2. **WebText and OpenWebText** — Data including public news, Wikipedia, fiction, and the Reddit submissions dataset.
3. **Books** — As an example, it comprises 16% of the training mix in the GPT-3 model training.

**Labels/Tags:**

- **Label:** "Training Data Poisoning"
- **Label:** "Taining Data"
- **Label:** "Biased Data"
- **Label:** "False Data"
- **Label:** "Toxicity"

**Common Examples of Vulnerability:**

1. **Example 1:** A malicious actor, or a competitor brand intentionally creates inaccurate or malicious documents which are targeted at a model’s training data.
   - The victim model trains using falsified information which is reflected in outputs of generative AI prompts to it's consumers.
2. **Example 2:** In reverse, unintentionally, a model is trained using data which has not been verified by its source, origin or content.
3. **Example 3:** The model itself when situated within infrastructure, has unrestricted access or inadequate sandboxing to gather datasets to be used as training data which has negative influence on outputs of generative AI prompts as well as loss of control from a management perspective.

*It is important to note that as a user of an LLM to be aware of this vulnerability. Whether a developer, client or consumer of the LLM, it is important to understand the implications of how this vulnerability could reflect risks within your LLM application or when interacting with a third-party LLM.*

**How to Prevent & Mitigations:**

1. Verify the supply chain of the training data, especially when sourced externally as well as maintaining attestations, similar to the "SBOM" (Software Bill of Materials) methodology.
2. Verify the legitimacy of data sources and data contained within during both the training and finetuning stages.
3. Verify your use-case for the LLM and the application it will integrate to. Craft different models via separate training data or finetuning for different use-cases to create a more granular and accurate generative AI output as per it's defined use-case.
4. Ensure sufficient sandboxing ([LLM03:2023 - Inadequate Sandboxing](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Inadequate_Sandboxing.html)) is present to prevent the model from scraping unintended data sources which could hinder the machine learning output.
5. Use strict vetting or input filters for specific training data, or categories of data sources to control volume of falsified data. Data sanitization, with techniques such as statistical outlier detection and anomaly detection methods to detect and remove adversarial data from potentially being fed into the fine-tuning process.
6. Adversarial Robustness, with techniques such as federated learning, constraints to minimize the effect of outliers or adversarial training to be robust against worst-case perturbations of the training data.
   1. An "MLSecOps" approach could be to include adversarial robustness to the training lifecycle with the auto poisoning technique.
   2. An example repository of this would be [Autopoison](https://github.com/azshue/AutoPoison) testing, including both attacks such as Content Injection Attacks (“how to inject your brand into the LLM responses”) and Refusal Attacks (“always making the model refuse to respond”) that can be accomplished with this approach.
7. Testing and Detection, by measuring the loss during the training stage and analyzing trained models to detect signs of a poisoning attack by analyzing model behavior on specific test inputs.
   1. Monitoring and alerting on number of skewed responses exceeding a threshold.
   2. Use of a human loop to review responses and auditing.
   3. Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
   4. **Optional** Perform LLM-based [red team exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) or [LLM vulnerability scanning](https://github.com/leondz/garak) into the testing phases of the LLM's lifecycle.

**Example Attack Scenarios:**

**Scenario #1:** The LLM generative AI prompt output can mislead users of the application which can lead to biased opinions, followings or even worse, hate crimes etc.

**Scenario #2:** If the training data is not correctly filtered and|or sanitized, a malicious user of the application may try to influence and inject toxic data into the model for it to adapt to the biased and false data.

**Scenario #3:** A malicious actor, or competitor intentionally creates inaccurate or malicious documents which are targeted at a model’s training data in which is training the model at the same time based on inputs. The victim model trains using this falsified information which is reflected in outputs of generative AI prompts to it's consumers.

**Reference Links:**

1. [Stanford Resarch Paper](https://stanford-cs324.github.io/winter2022/lectures/data/) which talks about the Data behind large language models.
2. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html)
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/) An article detailing how one can surgically modify an open-source model, and upload it to a provider to make it spread misinformation while being undetected by standard benchmarks.
4. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/) Evidence of how a prompt injection ([LLM01:2023 - Prompt Injections](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Prompt_Injection.html)) technique could also lead to Training Data Poisoning during scraping.
5. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): Can We Trust Our Model’s Weights?: A primer in data poisoning and backdoor on Language Models.
6. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944) Tuning Research paper demonstrating Data Poisoning in the model fine tuning process
7. [FedMLSecurity:](https://arxiv.org/abs/2306.04959) A Benchmark for Attacks and Defenses in Federated Learning and LLMs: Research demonstrating the effectiveness of Federated Learning against data poisoning attacks on LLMs.
8. [The poisoning of ChatGPT](https://softwarecrisis.dev/letters/the-poisoning-of-chatgpt/): A controversial but informative article on the risks of Data Poisoning in LLMs.
9. [LLM10:2023 - Training Data Poisoning](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Training_Data_Poisoning.html) A subsection on the Training Data Poisoning as a vulnerability type overview which was added to the original [OWASP Top 10 List for Large Language Models version 0.1 draft](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/).

**Author Commentary (Optional):**

It is a valid thought that the vulnerability of 'Prompt Hacking', AKA 'Adversarial Prompting' and 'Jailbreaking' are elevated in terms of risk if this vulnerability is not mitigated and remediated beforehand and within the major early lifecycle of a model and it's ongoing development.

The vulnerability [Prompt Injection](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/0_9_vulns/PromptInjection.md) could indirectly be another pivot point into this vulnerability if insufficient sanitization and filtering is performed when clients of the LLM application input is used to train the model. I.E, if malicious or falsified data is input to the model from a client as part of a Prompt Injection technique, this could inherently be portrayed into the model data.

Another entry in the current [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/) is [LLM06:2023 - Overreliance on LLM-generated Content](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Overreliance.html) which elaborates on how this may impact and potentially influence consumers of the AI. This threat is therefore what I consider a chained risk vector and how this may impact and potentially influence consumers of the AI.