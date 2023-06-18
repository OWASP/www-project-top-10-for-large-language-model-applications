## **Vulnerability Name:**

RCE (Remote Code Execution) via SSRF

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

Server-side Request Forgery (SSRF) vulnerabilities arise when an attacker exploits an LLM to execute unintended requests or gain unauthorized access to restricted resources, including internal services, APIs, or data stores. RCE vulnerabilities allow an attacker to execute arbitrary code on a remote device. This vulnerability builds on both concepts and through SSRF vulnerabilities in an LLM can lead to further successful Injection, Deserialization or Out-of-Bounds attacks on remote services from an attackers perspective.

**Labels/Tags:**

- **Label:** "SSRF"
- **Label:** "Server-Side Request Forgery"
- **Label:** "RCE"
- **Label:** "Remote Code Execution"
- **Label:** "Unauthorized Code Execution"

**Common Examples of Vulnerability:**

1. **Example 1:** Insufficient input validation, allowing attackers to manipulate LLM prompts to initiate unauthorized requests.
2. **Example 2:** Inadequate sandboxing or resource restrictions, enabling the LLM to access restricted resources or interact with internal services.
3. **Example 3:** Misconfigurations in network or application security settings, exposing internal resources to the LLM.

**How to Prevent:**

1. **Prevention Step 1:** Isolate and sandbox the LLM application within surrounding infrastructure using perimeter-based controls and techniques to prevent malicious code execution to spread to unauthorized areas. Implement rule of least privilege, RBAC (Role-based Access Controls) and best practice controls for AAA (Authentication, Authorization & Accounting) controls.
2. **Prevention Step 2:** Integrate WAF (Web Application Firewall) capabilities at the infrastructure perimeter to specific endpoints in aid to block malicious remote code execution payloads and common techniques, even to block low hanging fruit from scanners and payload generators.
3. **Prevention Step 3:** Perform appropriate threat modeling tabletop exercises to identify risks and vulnerabilities as per the steps above to reverse engineer, categorize and rank severity of risks, followed by remediation techniques. Regular audits and thorough security testing help identify and rectify any misconfigurations, enhancing the overall security posture.
4. **Prevention Step 4:** Implement robust input validation, block lists and sanitization methods to identify and filter out potential malicious inputs at the LLM application.
5. **Prevention Step 5:** Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
6. **Prevention Step 6:** Perform LLM-based [red team exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) or [LLM vulnerability scanning](https://github.com/leondz/garak) into the testing phases of the LLM lifecycle.

**Example Attack Scenarios:**

**Scenario #1:** An attacker is directly able to interact with an LLM application or via an API that allows SSRF by using a crafted technique or payload that can include remote code injection and in such the LLM's response output displays sensitive data from internal systems.

**Scenario #2:** Due to a misconfiguration in the application’s security settings, the LLM is allowed to interact with a restricted API. Taking advantage of this vulnerability, an attacker manipulates the LLM to access or modify sensitive data, potentially leading to unauthorized disclosure or data tampering.

**Reference Links:**

1. [Server-side request forgery (SSRF)](https://portswigger.net/web-security/ssrf) In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within the organization's infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems, potentially leaking sensitive data such as authorization credentials.
2. [Payloads All The Things](https://github.com/swisskyrepo/PayloadsAllTheThings) A GitHub repo available boasting a plethora of code injection (not limited to) techniques using numerous payloads and datasets. The purpose of including this repo is to elaborate how simple this concept of exploit can be to a malicious actor which increases probability of this being exploited in the wild and thus increased risk which must be addressed with mitigation steps.
3. [Latest remote code execution (RCE) security news](https://portswigger.net/daily-swig/rce) A news source containing a multitude of RCE exploits in the wild through numerous tactics and PoC's across different applications.
4. [LLM05:2023 - SSRF Vulnerabilities](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/SSRF.html) A subsection on the Data Leakage as a vulnerability type overview which is currently listed within the [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/)

**Author Commentary (Optional):**

It's important for application security teams managing red teaming exercises and bug submissions for the LLM application, to fully understand and interpret the response of the LLM to be able to verify if this is a valid Remote Code Execution. Arguably, this can be a difficult task to verify whether the output from the generative AI through the LLM is legitimate or not and requires a few tactical approaches to verification. Initial warning flags could be factors such as static continuous persistent results or verbose information which may include PII or other sensitive data (such as listing, reading file system directories or other backend system data). Red herrings could be suspected from varied output which has no relevance to the application or company responsbile for the LLM, and instead could even reflect training data gathered elsewhere.
<br>
Similar to my other published vulnerability writeup on [Privilege Escalation, leading to Cross-Site Request Forgery](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/0_5_vulns/AdsDawson_Priv_Escalation.md), this vulnerability shows the important need to threat modeling both a Web Application and the LLM layer when considering LLM Application security as a whole. This technique builds on top of a traditional vulnerability and pivots with other new LLM vulnerability techniques to chain vulnerabilities.
