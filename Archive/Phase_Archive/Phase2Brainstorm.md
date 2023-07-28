## General Notes

*place general V0.9 notes here during Phase 3*
<!-- Based on the Phase 3 instructions, and confirmation in Slack, I've changed this from v0.5 to v0.9 -->

## OWASP Top 10 List for Large Language Models Version 0.5

### LLM01:2023 - Prompt Injections

A Prompt Injection Vulnerability manifests when an attacker manages to manipulate the operation of a trusted large language model (LLM) through the clever injection of crafted input prompts. These prompts can be introduced via various avenues, including websites, emails, documents, or any other data source that an LLM might access during a user session. Given the high degree of trust usually associated with an LLM's output, the manipulated responses may go unnoticed and even be trusted by the user, allowing the attacker's intentions to take effect.

Two major types of Prompt Injection vulnerabilities exist: Direct Prompt Injections, where the attacker directly influences the LLM's input, and Indirect or Second Order Prompt Injections, where the attacker manipulates a data source consumed by the LLM, effectively "poisoning" it.

The results of a successful attack can vary greatly - from solicitation of sensitive information to influencing critical decision-making processes under the guise of normal operation. In more intricate cases, the LLM might be driven to impersonate a malicious persona or tricked to interact with plugins under a target user's context. This can lead to sensitive information disclosure, data exfiltration, unauthorized plugin execution, social engineering, etc. In these instances, the compromised LLM effectively acts as an agent for the attacker, furthering their objectives without triggering usual safeguards or alerting the end user to the intrusion.

### LLM02:2023 - Insecure Output Handling

An Insecure Output Handling vulnerability is a type of prompt injection vulnerability that arises when a plugin or application blindly accepts large language model (LLM) output without proper scrutiny and directly passes it to backend, privileged, or client-side functions. Since LLM-generated content can be controlled by prompt input, this behavior is akin to providing users indirect access to additional functionality. 

Successful exploitation of an Insecure Output Handling vulnerability can result in XSS and CSRF in web browsers as well as SSRF, privilege escalation, or remote code execution on backend systems. The impact of this vulnerability increases when the application allows LLM content to perform actions above the intended user's privileges. Additionally, this can be combined with agent hijacking attacks to allow an attacker privileged access into a target user's environment. 

### LLM03:2023 - Trained Data Poisoning

- The starting point of any machine learning approach is training data. In terms of large language models, the training data is just “raw text”. To be highly capable (e.g., have linguistic and world knowledge), this text should span a broad range of domains, genres, languages, etc.
  - A large language model uses deep neural networks to generate outputs based on patterns learned from training data.
- Training data poisoning occurs when an attacker manipulates the training data or fine-tuning procedures of an LLM to introduce vulnerabilities, backdoors, or biases that could compromise the model’s security, effectiveness, or ethical behavior.
  - This unethical or incorrect information is then presented to users of the AI.
  - Another entry in the current [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/) is [LLM06:2023 - Overreliance on LLM-generated Content](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Overreliance.html) which elaborates on how this may impact and potentially influence consumers of the AI. This threat is therefore what I consider a chained risk vector and how this may impact and potentially influence consumers of the AI.
  - In cases where the user does not trust the AI and is not influenced, there are still many risks associated with the vulnerability, even down to brand reputation etc.

### LLM04:2023 - Denial of Service

An attacker interacts with an LLM in a way that is particularly resource-consuming, causing quality of service to degrade for them and other users, or for high resource costs to be incurred.

### LLM05:2023 - Supply Chain

The supply chain in LLMs can be vulnerable impacting the integrity of training data,  ML models, deployment platfoms and lead to biased outcomes, security breaches, or complete  system failures.  Traditionally, vulnerabilities focused on software components but is extended in  AI because of the popularity of transfer learning, re-use of pre-trained models, as well as crowdsourced data. In public LLMs such as OpenGPT extension plugins are also an area susceptible to this vulnerability.

### LLM06:2023 - Permission Issues

Authorization is not tracked between plugins, allowing a malicious actor to take action in the context of the LLM user via indirect prompt injection, use of malicious plugins, or other methods. This can result in privilege escalation, loss of confidentiality, and even remote code execution, depending on available plugins.

### LLM07:2023 - Data Leakage

Data leakage occurs when an LLM accidentally reveals sensitive information, proprietary algorithms, or other confidential details through its responses. This can result in unauthorized access to sensitive data or intellectual property, privacy violations, and other security breaches. It's important to note that users of an LLM application should be aware of how to interact with an LLM and identify the risks present on how they might unintentionally input sensitive data. Vice versa, an LLM application should perform adequate data sanitization and scrubbing validation in aid to prevent user data from entering the training model data. Furthermore, the company hosting the LLM should have appropriate Terms of User policies available to make users aware on how data is processed.

### LLM08:2023 - Excessive Agency

An LLM may be granted a degree of agency - the ability to interface with other systems in order to undertake actions. Without restriction, any undesireable operation of the LLM (regardless of the root casue; e.g., halucination, direct/indirect prompt injection, or just poorly-engineered benign prompts, etc) may result in undesireable actions being taken. Just like we never trust client-side validation in web-apps, LLMs should not be trusted to self-police or self-restrict; controls should be embedded in the APIs of the systems being interefaced with.

### LLM09:2023 - Overreliance

Overreliance on LLMs is a security vulnerability that arises when systems excessively depend on LLMs for decision-making or content generation without adequate oversight, validation mechanisms, or risk communication. LLMs, while capable of generating creative and informative content, are also susceptible to "hallucinations," producing content that is factually incorrect, nonsensical, or inappropriate. These hallucinations can lead to misinformation, miscommunication, potential legal issues, and damage to a company's reputation if unchecked.


### LLM10:2023 - Insecure Plugins

A plugin designed to connect an LLM to some external resource accepts free-form text as an input instead of parameterized and type-checked inputs.  This allows a potential attacker significant latitude to construct a malicious request to the plugin that could result in a wide range of undesired behaviors, up to and including remote code execution.

## Detail Pages

### LLM01:2023 - Prompt Injections

Author(s):
GTKlondike,
Kai Greshake,
David Rowe,
Steve Wilson,
Will Chilcutt,


Description:

A Prompt Injection Vulnerability manifests when an attacker manages to manipulate the operation of a trusted large language model (LLM) through the clever injection of crafted input prompts. These prompts can be introduced via various avenues, including websites, emails, documents, or any other data source that an LLM might access during a user session. Given the high degree of trust usually associated with an LLM's output, the manipulated responses may go unnoticed and even be trusted by the user, allowing the attacker's intentions to take effect.

Two major types of Prompt Injection vulnerabilities exist: Direct Prompt Injections, where the attacker directly influences the LLM's input, and Indirect or Second Order Prompt Injections, where the attacker manipulates a data source consumed by the LLM, effectively "poisoning" it.

The results of a successful attack can vary greatly - from solicitation of sensitive information to influencing critical decision-making processes under the guise of normal operation. In more intricate cases, the LLM might be driven to impersonate a malicious persona or tricked to interact with plugins under a target user's context. This can lead to sensitive information disclosure, data exfiltration, unauthorized plugin execution, social engineering, etc. In these instances, the compromised LLM effectively acts as an agent for the attacker, furthering their objectives without triggering usual safeguards or alerting the end user to the intrusion.

Labels/Tags:

* Label: "Prompt Injection"
* Label: "Persona Impersonation"
* Label: "Session Hijack" 
* Label: "Data Manipulation"
* Label: "Plugin Exploitation"
* Label: "Social Engineering"
* Label: "External Source Injection"

Common Examples of Vulnerability:

Example 1: An attacker introduces a malicious prompt in a webpage, which is then accessed by the LLM, leading to manipulated responses.

Example 2: The LLM is tricked into divulging sensitive information or manipulating output to downstream systems.

Example 3: An attacker exploits the LLM's interaction with plugins, triggering unauthorized actions like unauthorized purchases, undesired social media posts, deleted emails, etc.

How to Prevent:

Privilege Control: Limit the privileges of an LLM to the least necessary for its functionality. Prevent the LLM from altering the user's state without explicit approval.
Enhanced Input Validation: Implement robust input validation and sanitization methods to filter out potential malicious prompt inputs from untrusted sources.
Segregation and Control of External Content Interaction: Segregate untrusted content from user prompts and control the interaction with external content, especially with plugins that could result in irreversible actions or exposure of personally identifiable information (PII).
Manage Trust: Establish trust boundaries between the LLM, external sources, and extensible functionality (e.g., plugins or downstream functions). Treat the LLM as an untrusted user and maintain final user control on decision making processes.


Example Attack Scenarios:

Scenario 1: A user employs an LLM to summarize a webpage containing a hidden prompt injection. This then causes the LLM to solicit sensitive information from the user and perform exfiltration via JavaScript or Markdown.

Scenario 2: A malicious user uploads a resume with a prompt injection. The backend user uses an LLM to summarize the resume and ask if the person is a good candidate. Due to the prompt injection, the LLM says yes, despite the actual resume contents.

Scenario 3: A user enables a plugin linked to an e-commerce site. A rogue instruction embedded on a visited website exploits this plugin, leading to unauthorized purchases.

Reference Links:


* [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/)
* [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)
* [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1)
* [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499)
* [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/)
* [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md)
* [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf)
* [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/)
* [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/)
* [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/)



Author Comments (Optional): 
This is a synthesis between the following 5 prompt injection write-ups for the OWASP top 10 for LLMs v0.5:
* GTK_LLMAgentHijack
* DavidRowe_LLM01_PromptInjection
* SteveWilson_IndirectPromptInjection
* SteveWilson_PromptInjection
* WillChilcutt_CrossPluginRequestForgery

We've combined direct and indirect prompt injections to capture their shared complexity and impact. Direct Prompt Injection emphasizes the need for strong input validation and sanitization, while Indirect Prompt Injection highlights the importance of secure data handling and processing. Together, they provide a more comprehensive picture of the security landscape for LLMs, which is vital for developing effective security strategies.

### LLM02:2023 - Insecure Output Handling

Author(s):

GTKlondike
Kai Greshake

Description:

An Insecure Output Handling vulnerability is a type of prompt injection vulnerability that arises when a plugin or application blindly accepts large language model (LLM) output without proper scrutiny and directly passes it to backend, privileged, or client-side functions. Since LLM-generated content can be controlled by prompt input, this behavior is akin to providing users indirect access to additional functionality. 

Successful exploitation of an Insecure Output Handling vulnerability can result in XSS and CSRF in web browsers as well as SSRF, privilege escalation, or remote code execution on backend systems. The impact of this vulnerability increases when the application allows LLM content to perform actions above the intended user's privileges. Additionally, this can be combined with agent hijacking attacks to allow an attacker privileged access into a target user's environment. 


Labels/Tags:

Label: "Output Filtering"
Label: "Prompt Injection"
Label: "Code Execution"


Common Examples of Vulnerability:

Example 1: LLM output is entered directly into a backend function, resulting in remote code execution.
Example 2: JavaScript or Markdown is generated by the LLM and returned to a user. The code is then interpreted by the browser, resulting in XSS

How to Prevent:

Prevention Step 1: Treat the model as any other user and apply proper input validation on responses coming from the model to backend functions.
Prevention Step 2: Likewise, encode output coming from the model back to users to mitigate undesired JavaScript or Markdown code interpretations.


Example Attack Scenarios:

Scenario 1: An application utilizes an LLM plugin to generate responses for a chatbot feature. However, the application directly passes the LLM-generated response into an internal function responsible for executing system commands without proper validation. This allows an attacker to manipulate the LLM output to execute arbitrary commands on the underlying system, leading to unauthorized access or unintended system modifications.

Scenario 2: A user utilizes a website summarizer tool powered by a LLM to generate a concise summary of an article. The website includes a prompt injection instructing the LLM to capture sensitive content from either the website or from the users conversation. From there the LLM can encode the sensitive data and send it out to an attacker-controlled server

Scenario 3: An LLM allows users to craft SQL queries for a backend database through a chat-like feature. A user requests a query to delete all database tables. If the crafted query from the LLM is not scrutinized, then all database tables would be deleted.

Scenario 4: A malicious user instructs the LLM to return a JavaScript payload back to a user, without sanitization controls. This can occur either through a sharing a prompt, prompt injected website, or chatbot that accepts prompts from a GET request. The LLM would then return the unsanitized XSS payload back to the user. Without additional filters, outside of those expected by the LLM itself, the JavaScript would execute within the users browser.

Reference Links:

* https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357
* https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./
* https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116
* https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/
* https://aivillage.org/large%20language%20models/threat-modeling-llm/


Author Commentary (Optional):

The purpose of my two findings are to make a distinction between the different types of "prompt injections". Agent Hijacking and Insecure Handling of LLM Output are both forms of prompt injection, but have very different impacts and require very different remediation steps. This is an attempt to make the concept of prompt injeciton more grainular and distinct. 

This is a situation with a large language model (LLM) where a plugin or application accepts LLM output and passes it, uncritically, into a backend or privileged function. Since users have significant control over LLM output, this would be similar to direct function access. This is extremely bad when an application accepts LLM content at a different privilege level than the user is supposed to have. 

The reference links include examples from past vulnerabilities and CVEs. While filtering input prior to invoking backend functions is common in application security today, this is notably absent from GPT plugins and LLM powered applications. Ideally, developers should consider LLMs to operate as possible threat actors just like they would with any other user. 

Like `A03_2021-Injection` from the OWASP Top 10 for applications, the injection point and remediation steps are identical for client-side and server-side attacks. Therefore, we've combined server-side and client-side attacks into the same category.

### LLM03:2023 - Trained Data Poisoning

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

### LLM04:2023 - Denial of Service

**Author(s):**

Leon Derczynski

**Description:**

An attacker interacts with an LLM in a way that is particularly resource-consuming, causing quality of service to degrade for them and other users, or for high resource costs to be incurred.

**Labels/Tags:**

A list that can be used to distinguish associated terminology or phrases to the description of your vulnerability. This will help with sorting through related submissions.

> _A common example: Prompt Injection" can also be also described or referred to as "Prompt Hacking", "Jailbreaking" etc_

- Label: "DoS"
- Label: "Sponge"

**Common Examples of Vulnerability:**

1. Example 1: Posing queries that lead to recurring resource usage through high-volume generation of tasks in a queue, e.g. with LangChain or AutoGPT
2. Example 2: Sending queries that are unusually resource-consuming, perhaps because they use unusual orthography or sequences

**How to Prevent:**

1. Prevention Step 1: Cap resource use per request
2. Prevention Step 2: Cap resource use per step, so that requests involving complex parts execute more slowly
3. Prevention Step 3: Limit the number of queued actions and the number of total actions in a system reacting to LLM responses

**Example Attack Scenarios:**

Scenario #1: An attacker repeatedly sends multiple requests to a hosted model that are difficult and costly for it to process. Many resources are allocated, leading to worse service for other users and increased resource bills for the host.

Scenario #2: A piece of text on a webpage is encountered while an LLM-driven tool is collecting information to respond to a benign query. That piece of text leads to the tool making many more web page requests. The query ends up leading to large amounts of resource consumption, and receives a slow or even absent response, as do any other queries from similar systems that end up encountering the given piece of text.

**Reference Links:**

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): demo + fix of this vulnerability in LangChain.
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): POC - "We mount two variants of this attack on established vision and language models, increasing energy consumption by a factor of 10 to 200."

### LLM05:2023 - Supply Chain

**Author(s):**

John Sotiropoulos

**Description:** The supply chain in LLMs can be vulnerable impacting the integrity of training data,  ML models, deployment platfoms and lead to biased outcomes, security breaches, or complete  system failures.  Traditionally, vulnerabilities focused on software components but is extended in  AI because of the popularity of transfer learning, re-use of pre-trained models, as well as crowdsourced data. In public LLMs such as OpenGPT extension plugins are also an area susceptible to this vulnerability.

**Labels/Tags:**

- Label: "Supply Chain"
- Label: "Vulnerabilities"
- Label: "Dependencies"

**Common Examples of Vulnerability:**

1.  Use of Vulnerable Model used for Transfer Learning
2.  Use of poisoned crowd-sourced data
3.  Tampered model or data by an out-sourcing supplier
4.  Traditional third-paty Package Vulnerabilities

**How to Prevent:**

1. Careful Vetting of sources and suppliers
2. Vulnerabilities scanning of components, not only when deploying to production but before used in development and testing; model development environments 
3. Use own curated package repositories with vulnerability checks
4. Code Signing
5. Avdersarial robustness tests on supplied models and data for tampering and poisoning and throughout the MLOps pipeline
6. Implement adversarial robustness training to help detect extraction queries.
7. Review and Monitor Supplier Security and Access
8. Auditing 

**Example Attack Scenarios:**

Scenario #1: An attacker exploits a vulnerable package to compromise a system. The recent OpenAI breach, was due to a vulnerable third party package 

Scenario #2: An attacker exploits a malicious or vulnerable ChatGPT plugin to exfiltrate data, bypass restriction,s execute code, span a user or produce malicious content. Although this is a supply-chain vulnerability, because of the ChatGPT plugun  integration models it  is also covered in [Insecure Plugin Integration](JohnSotiropoulos_InsecurePluginIntegration.md)

Scenario #3: An attacker exploits the PyPi package registry to trick model developers to download a compromised package and exfiltrate data or escalate privilege in a model development environment  

Scenario #4: An attacker poisons or tampers a copy of publicly available model  pre-built model  (e.g. LlaMa ) to create a backdoor or trojan horse deploys it for others to use either directly or for transfer learning 

Scenario #5: An attacker poisons or tampers a copy of publicly available data set   (e.g. Kaggle ) to help create a backdoor or trojan horse in other models. 

Scenario #6:  A compromised employee of a supplier (outsourcing developer, hosting company, etc) exfiltrates or tampers with data, model, code.

Scenario #7:  An attacker exploits weak supplier (outsouring developer, hosting company, etc) security to exfiltrate data or tamper with code, model, or data. 

Scenario #8:  An attacker exploits weak supplier (outsouring developer, hosting company, etc) security to exfiltrate data or tamper with code, model, or data. 

**Reference Links:

1. [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): Exploitation of a redis-py vulnerability lead to the first OpenAI data breach and outage
2. [What Happens When an AI Company Falls Victim to a Software Supply Chain Vulnerability ](https://securityboulevard.com/2023/05/what-happens-when-an-ai-company-falls-victim-to-a-software-supply-chain-vulnerability/): Another account of the OpenAI data breach with an analysis of the risks to AI companies
3. [Plugin review process](https://platform.openai.com/docs/plugins/review): OpenAI's plugin review process.
4. [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): Attacker stages a successful dependency chain attack on PyPi to fool PyTorch developers to download data exfiltration malware disguised as a PyTorch dependency.
5. [Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): Microsoft's list of AI/ML threats including examples of supply chain attacks
6. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/) : MITRE ATLAS coverage of ML Supply Chain Compromise and its recommendations.   
7. [Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples](https://arxiv.org/pdf/1605.07277.pdf): Evidence that data poisoning is tranferable via Transfer Learning
8. [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733) A seminal paper in 2017 that highlighted the security issues with using pre-built models that may have been tampered (BadNets)
9. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): An example of a data poisoning via the supply chain; reported by McAfee where an attacker implanted mutant synthetic  variants of ransomware in VirusTotal to confuse anti-virus ML systems and misclassify the ransomware as benign. 



**Author Commentary (Optional):**

Supply Chain attacks are on the rise and are a key threat. For those developing applications against LLM models risks are similar to the ones captured in the current OWASP Top Ten in [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)  However, extensibility plugins are a new dependency threat with serious consequences because of the tight integration and often insecure extensibility models.   

For LLM model developers or operators , AI brings new challenges in supply chain security  in two fronts: Model development entail access to sensitive data and therefore they are not safe "lower" environments. Vulnerable components will access live data before they are caught by the CI Vulnerability scanners. Additionally, prebuilt models, transfer learning, crowdsourced data, and ML providers or operators bring important challenges that need to be address to protect the integrity of models and data.  

In the current phase of early adoption, where LLM apps are used against one or two predominant LLM vendors, application development concerns will be more predominant but as privately trained and/or hosted LL models become more popular this will emerge as a more serious threat.  

### LLM06:2023 - Permission Issues

**Author(s):**

Rich Harang

**Description:**

Authorization is not tracked between plugins, allowing a malicious actor to take action in the context of the LLM user via indirect prompt injection, use of malicious plugins, or other methods. This can result in privilege escalation, loss of confidentiality, and even remote code execution, depending on available plugins.

**Labels/Tags:**

- Label: "Authorization failure"
- Label: "Input taint tracking"
- Label: "Content injection"

**Common Examples of Vulnerability:**

1. Example 1: Authentication is performed without explicit authorization to a particular plugin.
2. Example 2: A plugin treats all LLM content as being created entirely by the user, and performs any requested actions without requiring additional authorization.
3. Example 3: Plugins are chained together without considering the authorization of one plugin to perform an action using another plugin.

**How to Prevent:**

1. Require manual authorization of any action taken by sensitive plugins.
2. Call no more than one plugin with each user input, resetting any plugin-supplied data between calls.
3. Prevent sensitive plugins from being called after any other plugin.
4. Perform taint tracing on all plugin content, ensuring that plugin is called with an authorization level corresponding to the lowest authorization of any plugin that has provided input to the LLM prompt.

**Example Attack Scenarios:**

Scenario #1: Indirect prompt injection is used to induce an email plugin to deliver the contents of the current user's inbox to a malicious URL via POST request.

Scenario #2: An attacker uses indirect prompt injection to abuse a slack integration, sending a slack message to @everyone in all available slacks with an obscene and defamatory comment.

**Reference Links:**

1. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): Brief discussion of using a malicious plugin to perform unauthorized actions on github repositories.
2. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) Walkthrough of a cross-plugin request forgery attack resulting from inadequate cross-plugin authorization.

### LLM07:2023 - Data Leakage

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

Data leakage occurs when an LLM accidentally reveals sensitive information, proprietary algorithms, or other confidential details through its responses. This can result in unauthorized access to sensitive data or intellectual property, privacy violations, and other security breaches. It's important to note that users of an LLM application should be aware of how to interact with an LLM and identify the risks present on how they might unintentionally input sensitive data. Vice versa, an LLM application should perform adequate data sanitization and scrubbing validation in aid to prevent user data from entering the training model data. Furthermore, the company hosting the LLM should have appropriate Terms of User policies available to make users aware on how data is processed.

**Labels/Tags:**

- **Label:** "Data Leakage"
- **Label:** "PII"
- **Label:** "BOLA"
- **Label:** "BFLA"
- **Label:** "IDOR"

**Common Examples of Vulnerability:**

1. **Example 1:** Incomplete or improper filtering of sensitive information in the LLM’s responses.
2. **Example 2:** Overfitting or memorization of sensitive data in the LLM’s training process.
3. **Example 3:** Unintended disclosure of confidential information due to LLM misinterpretation, lack of data scrubbing methods or errors.

**How to Prevent:**

1. Prevention Step 1: Integrate adequate data sanitization and scrubbing techniques in aid to prevent user data from entering the training model data.
2. Prevention Step 2: Implement robust input validation and sanitization methods to identify and filter out potential malicious inputs.
3. Prevention Step 3: Maintain ongoing supply chain mitigation of risk through techniques such as SAST (Static Application Security Testing) and SBOM (Software Bill of Materials) attestations to identify and remediate vulnerabilities in dependencies for third-party software or packages.
4. Prevention Step 4: Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
5. Prevention Step 5: Perform LLM-based [red team exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) or [LLM vulnerability scanning](https://github.com/leondz/garak) into the testing phases of the LLM's lifecycle.

**Example Attack Scenarios:**

**Scenario #1:** Unsuspecting legitimate user A is exposed to certain other user data via the LLM when interacting with the LLM application in a non-malicious manner.

**Scenario #2:** User A targets a well crafted set of prompts to bypass input filters and sanitization from the LLM to cause it to reveal sensitive information (I.E PII) about other users of the application.

**Scenario #3:** Personal data such as PII is leaked into the model via training data due to either negligence from the user themselves, or the LLM application. This case could increase risk and probability of scenario 1 or 2 above.

**Reference Links:**

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt) A blog explaining the risks associated to users unintentionally leaking sensitive data into LLM's and the consequences of when this information is fed into training data.
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/) A write up on an incident caused due to an employee unintentionally leaking source code into an LLM's training data due to misuse and unawareness, leading to this being leaked across other use-case interactions with the LLM.
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use) An example terms of use notice made available to users of an LLM to identify how data is processed.
4. [LLM02:2023 - Data Leakage](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Data_Leakage.html) A subsection on the Data Leakage as a vulnerability type overview which is currently listed within the [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/)

**Author Commentary (Optional):**

It's important to note incidents such as [March 20 ChatGPT outage: Here’s what happened](https://openai.com/blog/march-20-chatgpt-outage) was not directly related to the LLM itself. However, it is important to maintain controls listed in _Prevention Step 3_ above as part of the overall LLM application and supporting infrastructure which can reduce risk and the attack vector.

### LLM08:2023 - Excessive Agency

**Author(s):**

Andy Smith

**Description:**

An LLM may be granted a degree of agency - the ability to interface with other systems in order to undertake actions. Without restriction, any undesireable operation of the LLM (regardless of the root casue; e.g., halucination, direct/indirect prompt injection, or just poorly-engineered benign prompts, etc) may result in undesireable actions being taken. Just like we never trust client-side validation in web-apps, LLMs should not be trusted to self-police or self-restrict; controls should be embedded in the APIs of the systems being interefaced with.

**Labels/Tags:**

- Label: "Excessive Agency"
- Label: "Inadequate Sandboxing"

**Common Examples of Vulnerability:**

1. Undesireable Actions Performed: The LLM triggers actions outside of the LLM that are unintended or undesireable, leading to second order consequences on downstream systems and processes.

**How to Prevent:**

1. Prevention Step 1: Reduce the permissions granted to the LMM to the minimum necessary to limit the scope of undesireable actions.
2. Prevention Step 2: Implement rate-limiting to reduce the number of undesireable actions.
3. Prevention Step 3: Utilise human-in-the-loop control to requre a human to approve all actions before they are taken.

**Example Attack Scenarios:**

Scenario #1: A personal assistant LLM is granted access to an individuals's mailbox in order to summarise the content of incoming emails. The LMM is vulnerable to an indirect promot injection attack, whereby a maliciously-crafted incoming email tricks the LLM into sending spam messages from the user's mailbox. This could be avoided by only granting the LLM read-only access to the mailbox (not the ability to send messages), or by requiring the user to manually review and hit 'send' on every mail drafted by the LLM. Alternatively The damage caused could be reduced by implementing rate limiting on the mail-sending interface.

Scenario #2: A customer service LLM has an interface to a payments system to provide service credits or refunds to customers in the case of complaints. The system prompt instructs the LLM to limit refunds to no more than one month's subscription fee, however a malicious customer engineers a direct prompt injection attack to convince the LMM to issue a refund of 100 years of fees. This could be avoided by implementing the 'one month max' limit within the refund API, rather than relying on the LMM to honour the limit in it's system prompt.

**Reference Links:**

1. [Link Title](URL): TBC

### LLM09:2023 - Overreliance

**Author(s):**

Steve Wilson

**Description:**

Overreliance on LLMs is a security vulnerability that arises when systems excessively depend on LLMs for decision-making or content generation without adequate oversight, validation mechanisms, or risk communication. LLMs, while capable of generating creative and informative content, are also susceptible to "hallucinations," producing content that is factually incorrect, nonsensical, or inappropriate. These hallucinations can lead to misinformation, miscommunication, potential legal issues, and damage to a company's reputation if unchecked.

**Labels/Tags:**

- Misinformation Risk
- Reputational Risk
- Hallucinations
- Risk Communication

**Common Examples of Vulnerability:**

1. **Factually Incorrect Information**: An LLM provides incorrect information as a response, leading to misinformation. For example, an LLM may inaccurately describe historical events, resulting in misleading outputs.
2. **Nonsensical Outputs**: An LLM generates grammatically correct but logically incoherent or nonsensical text. For instance, the LLM might generate a poem or a story that doesn't make logical sense.
3. **Source Conflation**: LLM conflates information from different sources, creating misleading content. It might combine historical data with current events in an incorrect manner.
4. **Overindulgence**: LLM might generate an output that could incorrectly be seen as disclosure of confidential information. 
5. **Inadequate Risk Communication**: Tech companies fail to adequately communicate the inherent risks of using LLMs to the end users, leading to potential negative consequences.

**How to Prevent:**

1. **Continuous Monitoring**: Regularly monitor and review the outputs of the LLM to ensure they are factual, coherent, and appropriate. Use manual reviews or automated tools for larger scale applications.
2. **Fact Checking**: Verify the accuracy of information provided by LLMs before using it for decision-making, information dissemination, or other critical functions.
3. **Model Tuning**: Tune your LLM to reduce the likelihood of hallucinations. Techniques can include prompt engineering, parameter efficient tuning (PET), and full model tuning.
4. **Set Up Validation Mechanisms**: Implement automatic validation mechanisms to check the generated output against known facts or data.
5. **Improve Risk Communication**: Follow best practices from risk communication literature and lessons from other sectors to facilitate dialogue with users, establish actionable risk communication, and measure the effectiveness of risk communications on an ongoing basis.

**Example Attack Scenarios:**

**Scenario #1**: A corporation uses an LLM to generate customer-facing content. Due to a hallucination, the LLM generates incorrect information about a product, leading to customer confusion, potential loss of sales, and damage to the company's reputation.

**Scenario #2**: An LLM is used in a news organization to assist in generating news articles. The LLM conflates information from different sources and produces an article with misleading information, leading to the dissemination of misinformation and potential legal consequences.

**Scenario #3**: A user communicates with an AI chatbot based on an LLM. The user, unaware of the limitations and risks of the AI, acts on harmful content generated by the model due to the lack of effective risk communication from the tech company.

**Reference Links:**

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): An article explaining how LLMs can make stuff up and what to do about it
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): An article explaining how to discuss inherent LLM risks

https://towardsdatascience.com/llm-hallucinations-ec831dcd7786

**Author Commentary (Optional):**

Overreliance on Large Language Models (LLMs) presents unique challenges in the realms of information integrity, operational safety, reputational risk, and regulatory compliance. LLMs have emerged as powerful tools for generating human-like text, offering significant benefits for various applications from customer service to content generation. However, without adequate oversight, validation mechanisms, and risk communication, an undue dependence on these models can lead to significant issues.

One crucial area of concern is misinformation. LLMs, prone to occasional "hallucinations," may generate outputs that are factually incorrect or nonsensical. This poses not only a risk of disseminating false or misleading information but can also lead to decision-making based on incorrect data, with potential adverse effects on operations and strategic decisions.

Reputational risk is another critical factor. Incorrect or inappropriate outputs from an LLM can damage a company's image, erode trust, and potentially lead to loss of customers or business opportunities. For instance, if an LLM used for customer interaction produces incorrect information about a product or service, it could lead to customer dissatisfaction and negative public perception.

Regulatory risk is an emerging area of concern. As regulators around the world start to pay closer attention to the use of AI and machine learning, companies that use LLMs may find themselves subject to regulations designed to prevent the dissemination of misinformation and protect user privacy. Failing to adequately control and validate the outputs of an LLM could potentially lead to regulatory penalties.

To mitigate these risks, companies should not only use technical measures, such as continuous monitoring and model tuning, but also pay close attention to risk communication. Ensuring that users understand the limitations of LLMs and the potential risks involved is crucial. This communication should be clear, ongoing, and should provide users with actionable information.

The use of LLMs can offer significant benefits, but it should be approached with a clear understanding of the risks involved and with strategies in place to mitigate those risks. Remember that while AI and LLMs can be highly efficient tools, they do not replace the need for human oversight, fact-checking, and validation.

### LLM10:2023 - Insecure Plugins

**Author(s):**

Rich Harang

**Description:**

A plugin designed to connect an LLM to some external resource accepts free-form text as an input instead of parameterized and type-checked inputs.  This allows a potential attacker significant latitude to construct a malicious request to the plugin that could result in a wide range of undesired behaviors, up to and including remote code execution.

**Labels/Tags:**

- Label: "Input validation"
- Label: "Input sanitization"
- Label: "Insufficient parameterization"

**Common Examples of Vulnerability:**

1. A plugin designed to call a specific API hosted at a specific endpoint accepts a string containing the entire URL to be retrieved, instead of query parameters to be inserted into the URL.
2. A plugin designed to look up information from a SQL database accepts a raw SQL query rather than paramters to be inserted into a fully parameterized query

**How to Prevent:**

1. Plugin calls should be strictly parameterized wherever possible, including type and range checks on inputs
2. When freeform input must be accepted, it should be carefully inspected to ensure that no potentially harmful methods are being called.
3. The plugin should be designed from a least-privilege perspective, exposing as little functionality as possible while still performing its desired function.

**Example Attack Scenarios:**

Scenario #1: A plugin prompt provides a base URL and instructs the LLM to combine the URL with a query to obtain weather forecasts in response to user requests. The resulting URL is then accessed and the results shown to the user. A malicious user crafts a request such that a URL pointing to a domain they control, and not the URL hosting the weather service API, is accessed, allowing the malicious user to obtain the IP address of the plugin for further reconnaisance, as well as to inject their own text into the LLM system via their domain, potentially granting them further access to downstream plugins.