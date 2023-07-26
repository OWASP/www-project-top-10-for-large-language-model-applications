## Supply-Chain Vulnerabilities 

**Description:** 

The supply chain in LLMs can be vulnerable, impacting the integrity of training data,  ML models, and deployment platforms.  lead to biased outcomes, security breaches, or complete  system failures.  Traditionally, vulnerabilities are focused on software components, but Machine Learning  extends this with the pre-trained models and training data supplied by third parties susceptible to tampering and poisoning attacks. 

Finally, LLM Plugin extensions can bring their own vulnerabilities. These are described in LLM - Insecure Plugin Design, which covers writing LLM  Plugins and  provides information useful to evaluate third-party plugins.

**Common Examples of Vulnerability:**

1. Traditional third-party package vulnerabilities, including outdated or deprecated components.
2. Using a vulnerable pre-trained model for fine-tuning. 
3. Use of poisoned crowd-sourced data for training.
4. Using outdated or deprecated models that are no longer maintained leads to security issues.
5. Unclear T&Cs and data privacy policies of the model operators  lead to the application’s sensitive data being used for model training  and subsequent sensitive information exposure. This may also apply to  risks from using copyrighted material by the model supplier.

**How to Prevent:**

1. Carefully vet data sources and suppliers, including T&Cs and  their privacy policies, only using trusted suppliers. Ensure adequate  and independently-audited security is in place and that model operator  policies align with your data protection policies, i.e., your data is  not used for training their models; similarly, seek assurances and legal mitigations against using copyrighted material from model maintainers.
2. Only use reputable plug-ins and ensure they have been tested for  your application requirements. LLM-Insecure Plugin Design provides  information on the LLM-aspects of Insecure Plugin design you should test against to mitigate risks from using third-party plugins.
3. Understand and apply the mitigations found in the OWASP Top Ten's [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/). This includes vulnerability scanning, management, and patching  components. For development environments with access to sensitive data,  apply these controls in those environments, too.
4. Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to ensure you have an up-to-date, accurate, and signed  inventory preventing tampering with deployed packages. SBOMs can be used to detect and alert for new, zero-date vulnerabilities quickly.
5. At the time of writing, SBOMs do not cover models, their artefacts, and datasets; If your  LLM application uses its own model, you should use MLOPs best practices  and platforms offering secure model repositories with data, model, and  experiment tracking.
6. You should also use model and code signing when using external models and suppliers.
7. Anomaly detection and adversarial robustness tests on supplied  models and data can help detect tampering and poisoning as discussed in [ Training Data Poisoning](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/Training_Data_Poisoning.md); ideally, this should be part of MLOps pipelines; however, these are  emerging techniques and may be easier implemented as part of red teaming exercises.
8. Implement sufficient monitoring to cover component and environment  vulnerabilities scanning, use of unauthorised plugins, and out-of-date  components, including the model and its artefacts.
9. Implement a patching policy to mitigate vulnerable or outdated  components. Ensure that the application relies on a maintained version of APIs and the  underlying model.
10. Regularly review and audit supplier Security and Access, ensuring no changes in their security posture or T&Cs.

**Example Attack Scenarios:**

1. An attacker exploits a vulnerable Python library to compromise a system. This happened in the first Open AI data breach. 

2. An attacker provides an LLM plugin to search for flights which generates fake links that lead to scamming plugin users.

3. An attacker exploits the PyPi package registry to trick model developers into downloading a compromised package and exfiltrating data or escalating privilege in a model development environment. This was an actual attack.

4. An attacker poisons a publicly available pre-trained model specialising in economic analysis and social research to create a backdoor which generates misinformation and fake news.  They deploy it on  a model marketplace (e.g. HuggingFace) for victims to use.

5. An attacker poisons publicly available data set to help create a backdoor when fine-tuning models. The backdoor subtly favours certain companies in different markets.

6. A compromised employee of a supplier (outsourcing developer, hosting company, etc) exfiltrates data, model, or code stealing IP.

7. An LLM operator changes its T&Cs and Privacy Policy so that it requires an explicit opt-out from using application data for model training, leading to memorisation of sensitive data.


**Reference Links:**

1. [ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): Exploitation of a redis-py vulnerability leads to the first OpenAI data breach and outage
2. [Plugin review process](https://platform.openai.com/docs/plugins/review): OpenAI's plugin review process.
3. [Compromised PyTorch-nightly dependency chain](https://pytorch.org/blog/compromised-nightly-dependency/): Attacker stages a successful dependency chain attack on PyPi to fool PyTorch developers to download data exfiltration malware disguised as a PyTorch dependency.
4. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/)
5. [Army looking at the possibility of ‘AI BOMs](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/)
6. [Failure Modes in Machine Learning](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): Microsoft's list of AI/ML threats including examples of supply chain attacks
7. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010/): MITRE ATLAS coverage of ML Supply Chain Compromise and its recommendations.   
8. [Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples](https://arxiv.org/pdf/1605.07277.pdf): Evidence that data poisoning is transferable via Transfer Learning
9. [BadNets: Identifying Vulnerabilities in the Machine Learning Model Supply Chain](https://arxiv.org/abs/1708.06733) A seminal paper in 2017 that highlighted the security issues with using pre-built models that may have been tampered (BadNets)
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): An example of a data poisoning via the supply chain; reported by McAfee where an attacker implanted mutant synthetic  variants of ransomware in VirusTotal to confuse anti-virus ML systems and misclassify the ransomware as benign. 
