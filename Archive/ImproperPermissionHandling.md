## Vulnerability Name

**Description:**

Authorization is not tracked between plugins, allowing a malicious actor to take action in the context of the LLM user via indirect prompt injection, use of malicious plugins, or other methods. This can result in privilege escalation, loss of confidentiality, and even remote code execution, depending on available plugins.

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
