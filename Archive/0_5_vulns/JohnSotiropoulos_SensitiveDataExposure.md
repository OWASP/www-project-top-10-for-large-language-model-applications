## Sensitive Data Exposure

**Author(s):**

John Sotiropoulos

**Description:**

This vulnerability relates to weak confidentiality gurantees on sensitive data, which can either personal data, business sensitive, or configuration data. An attacker can exfiltrate this data and use for targeting individuals, commiting fraud, or staging further atatcks. Data exposure leaks can be across a spectrum of attacks from traditonal data breaches to adversarial attacks and prompt injections.

**Labels/Tags:**

- Label: "Data Leaks"
- Label: "Privacy"
- Label: "Confidentiality"
- Label: "Training Data Attacks"
- Label: "Adversarial Attacks"

**Common Examples of Vulnerability:**

1. Sensitive data is exposed due to weak configuration 

2. Sensitive Data is  included in generated responses 

3. Sensitive Data is leaked in error messages 

4. Training data exfiltration via adversarial model inersion attacks to the model, without access to the training data itself. 

5. Adversarial Membership Inference attacks can be used to infer associations from memorised data.

   

**How to Prevent:**

1. Least Privilege Access Control 
2. Data encryption and obfuscation using strong cryptographic material and processes 
3. Use Private hosted LLMs for use cases requiring consumption of private or sensitive data  
4. Use prompt gurdrails to safeguard PII data from Prompt Injection attacks 
5. Use Differential Privacy  to protect from adversarial inversion or membership inference attacks  
6. Use of Data Sanitisation, PII Scrubbing,  and adversarial robustness techniques to prevent tests to analyse models for  PII leakages
7. Review Terms and Conditions, and Privacy Policy of hosting organisations.
8. Monitoring and Alerting for sensitive data access and output
9. Physical security
10. Auditing 

**Example Attack Scenarios:**

Scenario #1:  An attacker uses adversarial input attacks, such as prompt injections, to elicit the  model reveal sensitive data 

Scenario #2:  An attacker uses adversarial input attacks, such as prompt injections to reveal proprietory prompts of a packaged LLM solution (Prompt Leaking)   

Scenario #3: Insecure configuration allows an attacker to exfiltrate sensitive data from storage 

Scenario #4: A malicious or disgruntled employee leaks sensitive data

Scenario #5: A malicious user sends invalid requests to get sensitive data, such as configuration details  from error messages 

Scenario #6 An attacker uses Adversarial Input Attack (e.g. Prompt Injection) to narrow down if a known person has visited a place or was member of a political group

Scenario #7 An attacker takes advantage of a plugin to exfiltrate sensitive data  such as their emails

Scenario #8 An attacker uses Adversarial inversion attacks to extract sensitive data memorised by the model

Scenario #9 An attacker uses Adversarial membership inference attacks to infer sensitive associations  (political, neighbours, etc) from data memorised by the model 



**Reference Links:**

1. [ChatGPT and large language models: what's the risk?](https://www.ncsc.gov.uk/blog-post/chatgpt-and-large-language-models-whats-the-risk): UK NCSC risk assesment with recommendations on sensitive data
2. [Unsecured Microsoft Bing Server Exposed Users' Search Queries and Location](https://thehackernews.com/2020/09/bing-search-hacking.html): An example of misconfiguration resulting into data leak!
3. [Nvidia’s AI software tricked into leaking data](https://www.ft.com/content/5aceb7a6-9d5a-4f1f-af3d-1ef0129b0934): Example of bypassing guardrails and disclosing PII; in some test cases replacing I with J.
4. [Adversarial Prompting](https://www.promptingguide.ai/risks/adversarial) :  Description of prompt leaking
5. [Gandalf AI game reveals how anyone can trick ChatGPT into performing evil acts](https://www.standard.co.uk/tech/gandalf-ai-chatgpt-openai-cybersecurity-lakera-prompt-b1082927.html): exposing configuration data via Prompt injection; an example also of different permission levels and LLM roles that can stop it. 
6. [l ChatGPT Content Filtering: How to Prevent Exposure of Customer and Company Data](https://docs.nightfall.ai/docs/content-filtering-sensitive-data-chatgpt): Using content filtering to prevent data leaks
7. [ChatGPT Plugins: Data Exfiltration via Images & Cross Plugin Request Forgery](https://embracethered.com/blog/posts/2023/chatgpt-webpilot-data-exfil-via-markdown-injection/): Use of plugins to ex filtrate sensitive data
8. [Extracting Training Data from Large Language Models](https://arxiv.org/abs/2012.07805): research paper demostrating succesful extraction of names, phone numbers, and email addresses, IRC conversations, code, and 128-bit UUID
9. [Analyzing Leakage of Personally Identifiable Information in Language Models](https://arxiv.org/pdf/2302.00539v1.pdf): A research paper with details on use of  approaches and tools used at Microsoft to prevent leakages, perform PII scrubbing, and analyse models for leakages with GPT-2 models. 
10. [Privacy-Preserving Prompt Tuning for Large Language Model Services](https://arxiv.org/pdf/2305.06212.pdf): Research on prompt-tokenisation techniques to prevent inversion or inference attacks 
11. [Inferring Latent Attributes of Twitter Users from Neighbors](https://cdn.aaai.org/ojs/14340/14340-28-17858-1-2-20201228.pdf):  An example of a membership inference attack  

**Author Commentary (Optional):**

Privacy and confidentiality is a key concern for LLMs. There are several different vectors that sensitive data can be exposed. The UK's National Cyber Security Centre (NSCS) recommends that no sensitive data is used in public. Traditional data security concerns and compliance are applicable to LLMs , but more LLM-specific vectors through prompt injection and plugins are the key areas that we need to undertsand and safeguard. We also need to consider a new genre of adversarial AI attacks (model inversion or membership inference) that can extract memorised training data or infer sensitive associations. The latter have been mainly in non-LLM ML research (Image recognition) but appear to start appearing in LLM research  too. Although less urgent than addressing sensitive data exposure via Adversarial Input attacks and plugins, we need to keep an eye on them. Especially as LLMs evolve beyond the current OpenAI/Azure public LLM platforms. 

