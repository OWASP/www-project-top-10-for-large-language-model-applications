## **Vulnerability Name**

Privilege Escalation, leading to Cross-Site Request Forgery

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

Cross-site request forgery (also known as CSRF) **_(traditionally when referring to Web Application security)_** is a vulnerability that allows an attacker to induce users to perform actions that they do not intend to perform. It allows an attacker to partly circumvent the same origin policy, which is designed to prevent different websites from interfering with each other.
<br>
This is not to be confused with SSRF (where the attack primarily targets the backend server to read or update internal resources from an external network) which is listed within the current [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/).
<br>
As this publishing is dedicated to the LLM space and OWASP Top Ten for LLM Applications project, the key "pivoting" technique here is that a Privilege Escalation technique is performed through Adversarial Prompting (AKA "Prompt Hacking" by using the [confused deputy problem](https://en.wikipedia.org/wiki/Confused_deputy_problem).

> _In information security, a confused deputy is a computer program that is tricked by another program (with fewer privileges or less rights) into misusing its authority on the system. It is a specific type of privilege escalation._

**Labels/Tags:**

- **Label:** "Cross-Site Request Forgery"
- **Label:** "CSRF"
- **Label:** "CPRF"
- **Label:** "Cross-Site Plugin Forgery"
- **Label:** "Adversarial Prompting"
- **Label:** "Prompt Hacking"

**Common Examples of Vulnerability:**

1. **Example 1:** An attacker induces prompt injection by hosting malicious LLM instructions on a remote resource which causes an indirect Adversarial Prompt.
2. **Example 2:** An attacker induces a CSRF or CPRF exploit directly by interfacing with the LLM and instructing it to gather resources on a hacker's remote controlled resource containing malicious LLM instructions.

**How to Prevent:**

1. **Prevention Step 1:** Within scope, follow [traditional CSRF mitigation techniques](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) for the Web Application hosting the LLM.
2. **Prevention Step 2:** Implement robust input validation and sanitization methods to identify and filter out potential malicious inputs.
3. **Prevention Step 3:** Regularly benchmark (E.G [HELM](https://crfm.stanford.edu/helm/)), update and fine-tune the LLM to improve its ability to handle potentially harmful inputs
4. **Prevention Step 4:** Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
5. **Prevention Step 5:** Perform LLM-based [red team exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) or [LLM vulnerability scanning](https://github.com/leondz/garak) into the testing phases of the LLM lifecycle.

**Example Attack Scenarios:**

**Scenario #1:**

1. Attacker hosts malicious (large language model) LLM instructions on a website.
2. Victim visits the malicious site with an LLM application (e.g. a browsing plugin, such as WebPilot).
3. Prompt injection occurs, and the instructions of the website take control of the LLM application.
4. The LLM application follows instructions and retrieves the user’s email, summarizes and URL encodes it.
5. Next, the summary is appended to an attacker controlled URL and the LLM application is asked to retieve it.
6. The LLM application will invoke the browsing plugin on the URL which sends the data to the attacker.

**Reference Links:**

1. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): A blog discussing the opportunities and challenges associated with embedding plugins with LLMs, including a PoC for Cross-Plugin Request Forgery via Privilege Escalation achieved through Adversarial Prompt.
2. [LLM Hacking: Prompt Injection Techniques](https://medium.com/@austin-stubbs/llm-security-types-of-prompt-injection-d7ad8d7d75a3): A blog with comprehensive overview of data poisoning attacks in AI.
3. [Cross-site request forgery (CSRF)](https://towardsdatascience.com/exploring-the-vulnerability-of-language-models-to-poisoning-attacks-d6d03bcc5ecb): A tutorial and lab simulation for explaining what cross-site request forgery is within Web Application security, describing some examples of common CSRF vulnerabilities, and explain how to prevent CSRF attacks.

**Author Commentary (Optional):**

I personally love this approach and technique from reference 1 and the PoC linked above. It shows the important need to threat modeling both a Web Application and the LLM layer when considering LLM Application security as a whole. This technique builds on top of a traditional vulnerability and pivots with other new LLM vulnerability techniques to chain vulnerabilities.