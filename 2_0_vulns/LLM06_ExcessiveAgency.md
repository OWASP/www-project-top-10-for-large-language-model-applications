## LLM06:2025 Excessive Agency

### Description

An LLM-based system is often granted a degree of agency by its developer - the ability to call functions or interface with other systems via extensions (sometimes referred to as tools, skills or plugins by different vendors) to undertake actions in response to a prompt. The decision over which extension to invoke may also be delegated to an LLM 'agent' to dynamically determine based on input prompt or LLM output. Agent-based systems will typically make repeated calls to an LLM using output from previous invocations to ground and direct subsequent invocations.

Excessive Agency is the vulnerability that enables damaging actions to be performed in response to unexpected, ambiguous or manipulated outputs from an LLM, regardless of what is causing the LLM to malfunction. Common triggers include:

* hallucination/confabulation caused by poorly-engineered benign prompts, or just a poorly-performing model;
* direct/indirect prompt injection from a malicious user, an earlier invocation of a malicious/compromised extension, or (in multi-agent/collaborative systems) a malicious/compromised peer agent.

The root cause of Excessive Agency is typically one or more of:

* excessive functionality;
* excessive permissions;
* excessive autonomy.

Excessive Agency can lead to a broad range of impacts across the confidentiality, integrity and availability spectrum, and is dependent on which systems an LLM-based app is able to interact with.

Note: Excessive Agency differs from Insecure Output Handling which is concerned with insufficient scrutiny of LLM outputs.

### Common Examples of Risks

#### 1. Excessive Functionality

  An LLM agent has access to extensions which include functions that are not needed for the intended operation of the system. For example, a developer needs to grant an LLM agent the ability to read documents from a repository, but the 3rd-party extension they choose to use also includes the ability to modify and delete documents.

#### 2. Excessive Functionality

  An extension may have been trialled during a development phase and dropped in favor of a better alternative, but the original plugin remains available to the LLM agent.

#### 3. Excessive Functionality

  An LLM plugin with open-ended functionality fails to properly filter the input instructions for commands outside what's necessary for the intended operation of the application. E.g., an extension to run one specific shell command fails to properly prevent other shell commands from being executed.

#### 4. Excessive Permissions

  An LLM extension has permissions on downstream systems that are not needed for the intended operation of the application. E.g., an extension intended to read data connects to a database server using an identity that not only has SELECT permissions, but also UPDATE, INSERT and DELETE permissions.

#### 5. Excessive Permissions

  An LLM extension that is designed to perform operations in the context of an individual user accesses downstream systems with a generic high-privileged identity. E.g., an extension to read the current user's document store connects to the document repository with a privileged account that has access to files belonging to all users.

#### 6. Excessive Autonomy

  An LLM-based application or extension fails to independently verify and approve high-impact actions. E.g., an extension that allows a user's documents to be deleted performs deletions without any confirmation from the user. An LLM-based application grants the agent autonomy to invoke a tool based on an authorization made at approval time, but does not re-validate at execution that the tool still matches what was authorized, so a tool modified or shadowed after approval runs under stale authorization. For example, the configuration of a previously approved tool is altered in a shared repository, or another connected tool redefines how the agent uses it, and the agent invokes the changed tool without rechecking it against the original approval.

### Prevention and Mitigation Strategies

The following actions can prevent Excessive Agency:

#### 1. Minimize extensions

  Limit the extensions that LLM agents are allowed to call to only the minimum necessary. For example, if an LLM-based system does not require the ability to fetch the contents of a URL then such an extension should not be offered to the LLM agent.

#### 2. Minimize extension functionality

  Limit the functions that are implemented in LLM extensions to the minimum necessary. For example, an extension that accesses a user's mailbox to summarise emails may only require the ability to read emails, so the extension should not contain other functionality such as deleting or sending messages.

#### 3. Avoid open-ended extensions

  Avoid the use of open-ended extensions where possible (e.g., run a shell command, fetch a URL, etc.) and use extensions with more granular functionality. For example, an LLM-based app may need to write some output to a file. If this were implemented using an extension to run a shell function then the scope for undesirable actions is very large (any other shell command could be executed). A more secure alternative would be to build a specific file-writing extension that only implements that specific functionality.

#### 4. Minimize extension permissions

  Limit the permissions that LLM extensions are granted to other systems to the minimum necessary in order to limit the scope of undesirable actions. For example, an LLM agent that uses a product database in order to make purchase recommendations to a customer might only need read access to a 'products' table; it should not have access to other tables, nor the ability to insert, update or delete records. This should be enforced by applying appropriate database permissions for the identity that the LLM extension uses to connect to the database.

#### 5. Execute extensions in user's context

  Track user authorization and security scope to ensure actions taken on behalf of a user are executed on downstream systems in the context of that specific user, and with the minimum privileges necessary. For example, an LLM extension that reads a user's code repo should require the user to authenticate via OAuth and with the minimum scope required.

#### 6. Require user approval

  Utilise human-in-the-loop control to require a human to approve high-impact actions before they are taken. This may be implemented in a downstream system (outside the scope of the LLM application) or within the LLM extension itself. For example, an LLM-based app that creates and posts social media content on behalf of a user should include a user approval routine within the extension that implements the 'post' operation.

#### 7. Complete mediation

  Implement authorization in downstream systems rather than relying on an LLM to decide if an action is allowed or not. Enforce the complete mediation principle so that all requests made to downstream systems via extensions are validated against security policies. Bind authorization to execution by re-validating the resolved invocation (tool identity, parameters, and version) against the originally authorized context at the tool boundary, and reject any call that no longer matches.

#### 8. Sanitise LLM inputs and outputs

  Follow secure coding best practice, such as applying OWASP’s recommendations in ASVS (Application Security Verification Standard), with a particularly strong focus on input sanitisation. Use Static Application Security Testing (SAST) and Dynamic and Interactive application testing (DAST, IAST) in development pipelines.

The following options will not prevent Excessive Agency, but can limit the level of damage caused:

* Log and monitor the activity of LLM extensions and downstream systems to identify where undesirable actions are taking place, and respond accordingly.
* Implement rate-limiting to reduce the number of undesirable actions that can take place within a given time period, increasing the opportunity to discover undesirable actions through monitoring before significant damage can occur.

### Example Attack Scenarios

An LLM-based personal assistant app is granted access to an individual’s mailbox via an extension in order to summarise the content of incoming emails. To achieve this functionality, the extension requires the ability to read messages, however the plugin that the system developer has chosen to use also contains functions for sending messages. Additionally, the app is vulnerable to an indirect prompt injection attack, whereby a maliciously-crafted incoming email tricks the LLM into commanding the agent to scan the user's inbox for sensitive information and forward it to the attacker's email address. This could be avoided by:

* eliminating excessive functionality by using an extension that only implements mail-reading capabilities,
* eliminating excessive permissions by authenticating to the user's email service via an OAuth session with a read-only scope, and/or
* eliminating excessive autonomy by requiring the user to manually review and hit 'send' on every mail drafted by the LLM extension.

Alternatively, the damage caused could be reduced by implementing rate limiting on the mail-sending interface.

An agentic system connects to several MCP servers whose tools the user approved at setup, and the agent is free to invoke them without re-checking each call against that approval. In one case, the configuration of an approved tool is modified after approval, for example by editing it in a shared repository, and the agent executes the altered tool under the original trust, performing actions the user never authorized. In another, a co-loaded malicious server shadows a trusted tool, and the agent invokes it under the trusted tool's standing authorization even though its behavior no longer matches what was approved, executing the attacker's action with the trusted tool's privileges.

### Reference Links

1. [Slack AI data exfil from private channels](https://promptarmor.substack.com/p/slack-ai-data-exfiltration-from-private): **PromptArmor**
2. [Rogue Agents: Stop AI From Misusing Your APIs](https://www.twilio.com/en-us/blog/rogue-ai-agents-secure-your-apis): **Twilio**
3. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
4. [NeMo-Guardrails: Interface guidelines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): **NVIDIA Github**
5. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): **Simon Willison**
6. [Sandboxing Agentic AI Workflows with WebAssembly](https://developer.nvidia.com/blog/sandboxing-agentic-ai-workflows-with-webassembly/) **NVIDIA, Joe Lucas**
7. [MCPoison (CVE-2025-54136): persistent code execution via a modified, previously-trusted MCP configuration](https://nvd.nist.gov/vuln/detail/CVE-2025-54136): **NIST NVD** (research disclosure: [Check Point Research](https://research.checkpoint.com/2025/cursor-vulnerability-mcpoison/))
8. [WhatsApp MCP Exploited: Exfiltrating Your Message History via MCP](https://invariantlabs.ai/blog/whatsapp-mcp-exploited): **Invariant Labs**
9. [A Practical Guide for Secure MCP Server Development](https://genai.owasp.org/resource/a-practical-guide-for-secure-mcp-server-development/): **OWASP GenAI Security Project**
