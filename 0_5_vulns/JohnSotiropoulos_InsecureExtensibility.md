## Insecure Extensibility

**Author(s):**

John Sotiropoulos

**Description:** 

This vulnerability stems from   LLM extensibility implemented by LLM vendors (e.g. Open AI) in the form of plugins. Plugins are supposed to provide controlled relaxation of model isolation to bring in new sources and functionality in LLM platforms.  However, this may also  exposes the model to unvalidated inference data and integration endpoints to un-validated and malicious LLM output which can be further manipulated by Adversarial Input Attacks.  This  creates the potential of a range of attacks such as data exfiltration, unauthorised code execution, indirect Adversarial Input Attacks, and privilege escalation.   

**Labels/Tags:**

- Label: ""
- Label: "Plugins"

**Common Examples of Vulnerability:**

1.  Unauthorised code execution 
2.  Data Exfiltration via a plugin including chat history or personal data
3.   Indirect Data Poisoning, when a malicious plugin brings poisoned data included by an LL model to influence its response 

4.  Cross Site Request Forgery request to trick a user to perform an action (privilege escalation) on its behalf

5.  Cross Plugin Request Forgery that allows a second plugin to manipulate previous plugin interactions

**How to Prevent:**

1. Sanitise untrusted input and output if possible 
2. Implement defences against Adversarial Input Attacks
3. Carefully vet and test selected plugins
4. LL Models should implement extensibility frameworks that allow Process Isolation for Extensions with a permission model.
5. LL Models should implement extensibility frameworks that allow for input and output sensitisation hooks 
6. Implement user prompting for confirmation based on a permissions model and to highlight the plugin where the request is coming
7. Monitoring and alerting of how plugins are executed
8. Auditing and Reporting of malicious extensions

**Example Attack Scenarios:**

Scenario #1: An attacker uses a plugin that manipulates user input to exfiltrate sensitive data from the user or the system. Examples have already been published in the references below   

Scenario #2: An attacker uses a malicious plugin to pollute the input of the next plugin and include phishing links to fool the user into a phishing attack e.g. to buy a non existing goods

Scenario #3: An attacker uses a malicious plugin to execute code that fools the user to execute it and steal data or download malware

Scenario #4: An attacker uses a malicious plugin to confuse a user to impersonate them and  perform action on its behalf taking control of user resources eg their web site.

Scenario #4: An attacker uses a malicious plugin to exploit access to shared conversation, and  bring in inaccurate and biased content from their own website to support misinformation campaigns. For instance if a user searches for a specific candidate the malicious plugin returns inaccurate and  biased content so that is included in or influences the final answer 

**Reference Links:

1. [Chat Plugins](https://platform.openai.com/docs/plugins/introduction/chat-plugins-beta): OpenAI's plugn documenation

2. [Function calling and other API updates](https://openai.com/blog/function-calling-and-other-api-updates?ref=upstract.com): OpenAI's extensibility approach 

3. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf): Detailed treatment of security risks in LLM extensibility.

4. [You're a javascipt-based bot](https://willwillems.com/posts/run-code-with-chatgpt.html): Use of a plugin to run arbitrary code. This itself is not a vulnerability, but it becomes one when combined with the other plugin-related attacks

5. [ChatGPT Plugins: Data Exfiltration via Images & Cross Plugin Request Forgery](https://embracethered.com/blog/posts/2023/chatgpt-webpilot-data-exfil-via-markdown-injection/): Examples of tricking user to select fake links  when booking a flight via plugin to plugin communication and sharing context.

6. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): An example of Cross-Site Request Forgery

   

7. **Author Commentary (Optional):**

Please not that the current debate revolves around the OpenAI /ChatGPT plugin extensibilty, which is understandable given that it is the  main LLM in use.  Many of the mitigations suggested here may not be possible because of how OpenAI has implemented its plugin extensibility.  

However, other LLM providers will offer different extensibility models. Private LLM models may have their own proprietary extensibility / plugin mechanisms. 

Although it is important to address this vulnerability with reference to OpenAI's model, OWASP should not restrict to that but provide guidelines on extensibility that addresses these vulnerability and highlight the underlying vulnerability rather than safeguard the OpenGPT model only with "prompt injection" mitigations. Without defences at the extensibility layer of an LL model, "prompt injection" mitigations may struggle to provide individual mitigations, although in the short term maybe the only defense. 

This vulnerability focuses on the extensible layer and not an the plugins being vulnerable themselves which is a supply-chain vulnerability   
