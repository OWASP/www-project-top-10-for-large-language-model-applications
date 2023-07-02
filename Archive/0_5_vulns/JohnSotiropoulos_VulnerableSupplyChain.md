## Vulnerable Supply Chain 

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
