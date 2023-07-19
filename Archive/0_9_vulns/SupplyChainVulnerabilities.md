## Supply Chain Vulnerabilities

**Description**: Supply-chain vulnerabilities in LLM applications can affect the entire application lifecycle. This includes traditional third-party libraries/packages, docker containers, base images, and service suppliers such as application and model hosting companies. Vulnerable components or services can become the vector for cyber-security attacks leading to data disclosure and tampering, including ransomware or privilege escalation.

Additionally, LLM applications which use their own models bring new types of vulnerabilities typically found in Machine Learning development. These include vulnerabilities in third-party data sets and pre-trained models for further training (transfer learning) or fine-tuning. Third-party data sets and pre-trained models can facilitate poisoning attacks, resulting into biased outcomes, security breaches, or complete system failures.  

Finally, LLMs depend on LLM plugins for extensions, which can bring their own vulnerabilities. LLM Plugin vulnerabilities is covered in LLM - Insecure Plugin Design which covers writing rather an LLM Plugin rather than using a 3rd Party Plugin. However, Insecure Plugin Design provides the information to evaluate third-party plugins. 

**Common Examples of Vulnerability:**

* Use of third-party components or base images with vulnerabilities, including outdated or deprecated components.
* Use of a poisoned or tampered pre-built model for finetuning or further training.
* Use of poisoned external data sets used for fine-tuning the applications model.
* Using outdated or deprecated models that are no longer maintained leads to security issues.
* Use of tampered model, data, source code or third-party component by a hosting or outsourcing supplier.
* Unclear T&C and data privacy policies of the model operators lead to the application’s sensitive data being used for model training and subsequent sensitive information exposure. This may also apply to risks from using copyrighted material by the model supplier.

**How to Prevent:**



* Carefully vet data sources and suppliers, including T&Cs and their privacy policies, only using trusted suppliers. Ensure adequate and independently-audited security is in place and that model operator policies align with your data protection policies, i.e., your data is not used for training their models; similarly, seek assurances and legal mitigations against using copyrighted material from model maintainers.
* Only use reputable plug-ins and ensure they have been tested for your application requirements. LLM-Insecure Plugin Design provides information on the LLM-aspects of Insecure Plugin design you should test against to mitigate risks from using third-party plugins.
* Understand and apply the mitigations found in the OWASP Top Ten _[A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/) _item. This includes vulnerability scanning, management, and patching components. For development environments with access to sensitive data, apply these controls in those environments, too.
* Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to ensure you have an up-to, accurate, and signed inventory preventing tampering with deployed packages. SBOMs can be used to detect and alert for new, zero-date vulnerabilities quickly.
* SBOMs do not cover models, their artefacts, and datasets; If your LLM application uses its own model, you should use MLOPs best practices and platforms offering secure model repositories with data, model, and experiment tracking. 
* You should also use model and code signing when using external models and suppliers.
* Anomaly detection and adversarial robustness tests on supplied models and data can help detect tampering and poisoning as discussed in [LLM02 Training Data Poisoning](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/0_9_vulns/Training_Data_Poisoning.md); ideally, this should be part of MLOps pipelines; however, these are emerging techniques and may be easier implemented as part of red teaming exercises.
* Implement sufficient monitoring to cover component and environment vulnerabilities scanning, use of unauthorised plugins, and out-of-date components, including the model and its artefacts. 
* Implement a patching policy to mitigate vulnerable of outdated components. Ensure that APis use a maintained version of APIs and the underlying model.
* Regularly review and audit supplier Security and Access, ensuring no changes in their security posture or T&Cs.

**Example Attack Scenarios:**

**Scenario #1:** An attacker exploits a vulnerable or outdated package or base image to compromise the application. _The recent OpenAI breach was due to a vulnerable third-party library, redis-py._

**Scenario #2:** An attacker exploits a malicious or vulnerable ChatGPT plugin to exfiltrate data, bypass restrictions,s execute code, spam a user or produce malicious content, such as phishing links.

**Scenario #3:** An attacker exploits an outdated or deprecated model with vulnerabilities to compromise the system or cause performance degradation.

**Scenario #4:** An attacker exploits the PyPi package registry to trick model developers into downloading a compromised package and exfiltrate data or escalating privilege in a model development environment

**Scenario #5:** An attacker poisons or tampers a copy of a publicly available model pre-built LLM o create a backdoor and posts it to a model marketplace (e.g. Hugging FAce); the attacker exploits the backdoor when the model is finetuned and deployed.

**Scenario #6**: An attacker poisons or tampers a third-party available data set to help create a backdoor when finetuning a model and exploiting the application’s outcomes.

**Scenario #7: **An attacker exploits weak supplier (outsourcing developer, model marketplace, hosting company, etc.) security to exfiltrate data or tamper with code, model, or data.

**Scenario #8:** An attacker identifies unclear T&Cs in a model operator and exploits sensitive data exposure on sensitive data used for fine-tuning.

**Reference Links:**



*  [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): How the exploitation of a redis-py vulnerability led to the first OpenAI data breach and outage.
* [What Happens When an AI Company Falls Victim to a Software Supply Chain Vulnerability](https://securityboulevard.com/2023/05/what-happens-when-an-ai-company-falls-victim-to-a-software-supply-chain-vulnerability/)<span style="text-decoration:underline;"> </span>: Another account of the OpenAI data breach with an analysis of the risks to AI companies
* [Plugin review process](https://platform.openai.com/docs/plugins/review): OpenAI's plugin review process.
* [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): An attacker staged a successful dependency chain attack on PyPi to fool PyTorch developers into downloading data exfiltration malware disguised as a PyTorch dependency.
* [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): A detailed walkthrough on compromising the supply chain and poison the open source GPT-J-6B LLM on HuggingFace
* [https://twitter.com/rharang/status/1675863546200981504?s=20](https://twitter.com/rharang/status/1675863546200981504?s=20) Data breach of Hugging Face, affecting Meta/Facebook & Intel Hub organisations.
* [ChatGPT Plugins: Data Exfiltration via Images & Cross Plugin Request Forgery](https://embracethered.com/blog/posts/2023/chatgpt-webpilot-data-exfil-via-markdown-injection/): Examples of tricking users to use fake links when booking a flight.
* [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/): The MITRE ATLAS coverage of ML Supply Chain Compromise and its recommendations.  
* [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): An example of a data poisoning via the supply chain; reported by McAfee where an attacker implanted mutant synthetic variants of ransomware in VirusTotal to confuse anti-virus ML systems and misclassify the ransomware as benign.
* [MLOps: Why data and model experiment tracking is important? How tools like DVC and Mlflow can solve this challenge ?](https://medium.com/hub-by-littlebigcode/mlops-why-data-and-model-experiment-tracking-is-important-e40e2fb9d74d) Best practices in MLOPs to track models and data.
