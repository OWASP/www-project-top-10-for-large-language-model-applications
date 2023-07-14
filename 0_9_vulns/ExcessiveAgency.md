## Excessive Agency

**Context:**

An LLM-based system is often granted a degree of agency by its developer - the ability to interface with other systems and undertake actions in response to a prompt. Some actions are intended to be performed **by the LLM** in order to support its purpose, for example:
 - Reading the contents of a web page (in order to then summarise the content for the LLM's response).
 - Querying the contents of a database (in order to include query results in the LLM's response).

Other actions are intended to be performed **in the context of the user** who is interacting with the LLM-based application, for example:
 - Reading the contents of the user's code repo (in order to make code suggestions).
 - Reading the contents of the user's mailbox (in order to summarise the content of incoming messages).

It should be noted that whilst an LLM does not have any inherent agency itself, applications will frequently use the output from an LLM to trigger actions. Such capability is typically constructed as a 'plugin' or a 'tool'.

The specific plugins/tools used in an application might be bespoke to that application, or the application developer may choose to use a plugin/tool written by a 3rd party.

The decision to perform actions via a plugin/tool may be hard-wired by the system developer, or may be delegated to a LLM 'agent' to dynamically determine which are the most appropriate to take.

Any undesirable operation of the LLM may result in undesirable actions being taken.

**Description:**

Excessive Agency is the vulnerability that enables damaging actions to be performed in response to unexpected outputs from an LLM (regardless of what is causing the LLM to malfunction; be it hallucination, direct/indirect prompt injection, malicious plugin, poorly-engineered benign prompts, or just a poorly-performing model). The root cause of Excessive Agency is typically excessive functionality, excessive permissions or excessive autonomy.

**Common Examples of Vulnerability:**

1. Excessive Functionality: An LLM agent has access to plugins that are wholly unnecessary for the intended operation of the system. For example, a plugin may have been trialled during a development phase and dropped in favour of a better alternative, but the original plugin remains available to the LLM agent.
2. Excessive Functionality: An LLM agent has access to plugins which include functions that are not needed for the intended operation of the system alongside functions that are required. For example, a developer needs to grant an LLM agent the ability to read documents from a repository, but the 3rd-party plugin they choose to use also includes the ability to modify and delete documents.
3. Excessive Functionality: An LLM plugin with open-ended functionality fails to properly filter the input instructions for commands outside what's necessary for the intended operation of the application. E.g., a plugin to run one specific shell command fails to properly prevent other shell commands from being executed.
4. Excessive Permissions: An LLM plugin has permissions on other systems that are not needed for the intended operation of the application. E.g., a plugin intended to read data connects to a database server using an identity that not only has SELECT permissions, but also UPDATE, INSERT and DELETE permissions.
5. Excessive Permissions: An LLM plugin that is designed to perform operations on behalf of a user accesses downstream systems with a generic high-privileged identity. E.g., a plugin to read the current user's document store connects to the document repository with a generic user account that has access to all users' files.
6. Excessive Autonomy: An LLM-based application or plugin fails to independently verify and approve high-impact actions with a human operator. E.g., a plugin that allows a user's documents to be deleted will perform deletions without any confirmation from the user. 

**How to Prevent:**

Just like we never trust client-side validation in web-apps, LLMs should not be trusted to self-police or self-restrict; any output from an LLM should be considered untrusted and controls should be embedded in the APIs and plugins of that which the LLM-based system can call.

The following options can prevent Excessive Agency:

1. **Limit the plugins/tools** that LLM agents are allowed to call to only the minimum functions necessary. For example, if an LLM-based system does not require the ability to fetch the contents of a URL then such a plugin should not be offered to the LLM agent.
2. **Limit the functions** that are implemented in LLM plugins/tools to the minimum necessary. For example, a plugin that accesses a user's mailbox to summarise emails may only require the ability to read emails, so the plugin should not contain other functionality such as deleting or sending messages.
3. **Avoid open-ended functions** where possible (e.g., run a shell command, fetch a URL, etc) and use plugins/tools with more granular functionality. For example, an LLM-based app may need to write some output to a file. If this were implemented using a plugin to run a shell function then the scope for undesirable actions is very large (any other shell command could be executed). A more secure alternative would be to build a file-writing plugin that could only support that specific functionality.
4. **Limit the permissions** that LLM plugins/tools are granted to other systems the minimum necessary in order to limit the scope of undesirable actions. For example, an LLM agent that uses a product database in order to make purchase recommendations to a customer might only need read access to a 'products' table; it should not have access to other tables, nor the ability to insert, update or delete records. This should be enforced by applying appropriate database permissions for the identity that the LLM plugin uses to connect to the database.
5. **Track user authorization and security scope** to ensure actions taken on behalf of a user are executed on downstream systems in the context of that specific user, and with the minimum privileges necessary. For example, an LLM plugin that reads a user's code repo should require the user to authenticate via OAuth and with the minimum scope required.
6. **Utilise human-in-the-loop control** to require a human to approve all actions before they are taken. This may be implemented in a downstream system (outside the scope of the LLM application) or within the LLM plugin/tool itself. For example, an LLM-based app that creates and posts social media content on behalf of a user should include a user approval routine within the plugin/tool/API that implements the 'post' operation.

The following options will not prevent Excessive Agency, but can limit the level of damage caused:

1. **Log and monitor the activity** of LLM plugins/tools and downstream systems to identify where undesirable actions are taking place, and respond accordingly.
2. **Implement rate-limiting** to reduce the number of undesirable actions that can take place within a given time period, increasing the opportunity to discover undesirable actions through monitoring before significant damage can occur.

**Example Attack Scenario:**

An LLM-based personal assistant app is granted access to an individual’s mailbox via a plugin in order to summarise the content of incoming emails. To achieve this functionality, the email plugin requires the ability to read messages, however the plugin that the system developer has chosen to use also contains functions for sending messages. The LLM is vulnerable to an indirect prompt injection attack, whereby a maliciously-crafted incoming email tricks the LLM into commanding the email plugin to call the 'send message' function to send spam from the user's mailbox. This could be avoided by:
(a) eliminating excessive functionality by using a plugin that only offered mail-reading capabilities,
(b) eliminating excessive permissions by authenticating to the user's email service via an OAuth session with a read-only scope, and/or
(c) eliminating excessive autonomy by requiring the user to manually review and hit 'send' on every mail drafted by the LLM plugin.
Alternatively, the damage caused could be reduced by implementing rate limiting on the mail-sending interface.

**Reference Links:**

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): In this blog post, wunderwuzzi describes a PoC exploit of triggering a variety of undesirable actions (in this case through prompt injection).
2. [NeMo-Guardrails: Interface guidlines](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): This document from the NeMo-Guardrails project sets out guidelines and principles for providing LLMs access to external data and compute resources in a safe and secure way.
3. [LangChain: Human-approval for tools](https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval): An example of adding a human-in-the-loop verification step into a LangChain tool.
4. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): In this blog post, Simon describes a novel approach to limiting what actions an LLM can perform by utilising a Dual-LLM approach.

**Author Commentary (Optional):**

There is a degree of overlap between Excessive Agency and several other LLM Top-10 v0.9 candidates. The below is an attempt to call out the key differentiators between those other items and Excessive Agency. (_Note: these statements require validation with the teams working on those other items._)

Versus Overreliance:
> **Overreliance** is a weakness in how humans use LLM-based systems (e.g., a news website generates articles using a LLM, and staff copy-paste the output online without properly fact-checking the output.
> 
> **Excessive Agency** is a weakness in how LLM-based systems use the output from the LLM model itself (e.g., in the news website example above, Excessive Agency may occur if the article generation system can automatically publish articles online without any human involvement).

Versus Insecure Output Handling
> **Insecure Output Handling** involves malicious output being created by a LLM, which is then consumed by a downstream system without proper sanitisation.
> 
> **Excessive Agency** involves undesirable actions being taken by a downstream system in response to LLM output.

Versus Prompt Injection:
> **Prompt Injection** is one of the main triggers for driving an LLM to behave in an undesirable way.
>
> **Excessive Agency** allows a misbehaving LLM (be it through prompt injection or other means) to undertake undesirable actions in downstream systems.

Versus Insecure Plugin Execution:
> **Insecure Plugin Execution** involves proper sanitisation of plugin inputs and authorization of plugin actions.
>
> **Excessive Agency** involves limiting plugin functionality, permission and autonomy.

