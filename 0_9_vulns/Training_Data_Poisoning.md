## **Vulnerability Name:**

Training Data Poisoning

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

- The starting point of any machine learning approach is training data. In terms of large language models, the training data is just “raw text”. To be highly capable (e.g., have linguistic and world knowledge), this text should span a broad range of domains, genres, languages, etc.
  - A large language model uses deep neural networks to generate outputs based on patterns learned from training data.
- Training data poisoning occurs when an attacker manipulates the training data or fine-tuning procedures of an LLM to introduce vulnerabilities, backdoors, or biases that could compromise the model’s security, effectiveness, or ethical behavior.
  - This unethical or incorrect information is then presented to users of the AI.
  - Another entry in the current [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/) is [LLM06:2023 - Overreliance on LLM-generated Content](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Overreliance.html) which elaborates on how this may impact and potentially influence consumers of the AI. This threat is therefore what I consider a chained risk vector and how this may impact and potentially influence consumers of the AI.
  - In cases where the user does not trust the AI and is not influenced, there are still many risks associated with the vulnerability, even down to brand reputation etc.

There are several data sources that are worth discussing:

1. Common Crawl — Because of its convenience, it has been a standard source of data to train many models such as T5, GPT-3, and Gopher. The April 2021 snapshot of Common Crawl has 320 terabytes of data
2. WebText and OpenWebText — Data include public news, Wikipedia, fiction, and the Reddit submissions dataset.
3. Books — It comprises 16% of the training mix in the GPT-3 model training.

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
3. **Example 3:** The model itself has unrestricted access or inadequate sandboxing to gather datasets to be used as training data which has negative influence on outputs of generative AI prompts as well as loss of control from a management perspective.

**How to Prevent:**

1. Prevention Step 1: Verify supply chain of the Training Data if sourced externally as well as maintaining attestations, similar to SBOM (Software Bill of Materials) methodology.
2. Prevention Step 2: Verify legitimacy of data sources and data within.
3. Prevention Step 3: Craft different models via separate Training Data for different use-cases to create a more granular and accurate generative AI output.
4. Prevention Step 4: Ensure sufficient sandboxing ([LLM03:2023 - Inadequate Sandboxing](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Inadequate_Sandboxing.html)) is present to prevent the model from scraping unintended data sources.
5. Prevention Step 5: Use strict vetting or input filters for specific Training Data, or categories of data sources to control volume of falsified data.
6. Prevention Step 6: Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
7. **Optional** Prevention Step 7: Perform LLM-based [red team exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) or [LLM vulnerability scanning](https://github.com/leondz/garak) into the testing phases of the LLM's lifecycle.

**Example Attack Scenarios:**

**Scenario #1:** The LLM generative AI prompt output can mislead users of the application which can lead to unbiased opinions, followings or even worse, hate crimes etc.

**Scenario #2:** If the training data is not correctly filtered, a malicious user of the application may try to influence and inject toxic data into the model for it to adapt to the unbiased and false data.

**Scenario #3:** A malicious actor, or a competitor brand intentionally creates inaccurate or malicious documents which are targeted at a model’s training data. The victim model trains using falsified information which is reflected in outputs of generative AI prompts to it's consumers.

**Reference Links:**

1. [Stanford Resarch Paper](https://stanford-cs324.github.io/winter2022/lectures/data/) which talks about the Data behind large language models.
2. [AI Hypocrisy: OpenAI, Google, and Anthropic train using others' content, but wont let others use their content](https://www.businessinsider.com/openai-google-anthropic-ai-training-models-content-data-use-2023-6)
3. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/) Evidence of how a prompt injection ([LLM01:2023 - Prompt Injections](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Prompt_Injection.html)) technique could also lead to Training Data Poisoning during scraping.
4. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html)
5. [LLM10:2023 - Training Data Poisoning](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Training_Data_Poisoning.html) A subsection on the Training Data Poisoning as a vulnerability type overview which is currently listed within the [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/)

**Author Commentary (Optional):**

IMO, the terms 'Prompt Hacking', 'Adversarial Prompting' and 'Jailbreaking' (**shivers**) are almost moot if this vulnerability is not taken care of beforehand within the major early lifecycles of a model.