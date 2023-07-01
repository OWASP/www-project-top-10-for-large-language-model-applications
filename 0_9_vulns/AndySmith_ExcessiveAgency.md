## Excessive Agency

**Author(s):**

Andy Smith

**Description:**

An LLM-based system is often granted a degree of agency - the ability to interface with other systems in order to undertake actions in response to a prompt. The decision to perform external actions may be hard-wired by the system developer as part of a chain, or may be delegated to a LLM agent to dynamically determine which are the most appropriate to take. Without restriction, any undesirable operation of the LLM (regardless of the root cause; be it hallucination, direct/indirect prompt injection, malicious plugin, poorly-engineered benign prompts, or just a poorly-performing model) may result in undesirable actions being taken.

Excessive Agency is the vulnerability that arises from allowing an LLM to perform risky actions without verification or confirmation.

Just like we never trust client-side validation in web-apps, LLMs should not be trusted to self-police or self-restrict; controls should be embedded in the APIs and plugins of that the LLM can call.

**Labels/Tags:**

- Label: "Excessive Agency"
- Label: "Confused Deputy"
- Label: "Excessive Permissions"
- Label: "Inadequate Sandboxing"

**Common Examples of Vulnerability:**

1. Undesirable Actions Performed: The LLM triggers actions outside of the LLM that are unintended or undesirable, leading to second order consequences on downstream systems and processes.

**How to Prevent:**

The following options can prevent Excessive Agency:

1. **Limit the actions/plugins** that LLM agents are allowed to call to only the minimum necessary, and be particularly wary of those which allow very open-ended actions to be performed (e.g., run a shell command, fetch a URL, etc).
2. **Reduce the permissions** that LLM agents are granted to other systems the minimum necessary in order to limit the scope of undesirable actions. For example, an LLM agent that uses a product database in order to make purchase recommendations to a customer only needs read access to a 'products' table; it should not have access to other tables, nor the ability to insert, update or delete records. This should be enforced by applying appropriate database permissions for the identity that the LLM plugin uses to connect to the database.
3. **Utilise human-in-the-loop control** to require a human to approve all actions before they are taken. This may be implemented in a downstream system (outside the scope of the LLM system) or within the LLM plugin. See this example of adding a human-in-the-loop verification step into a LangChain tool: https://python.langchain.com/docs/modules/agents/tools/how_to/human_approval

**How to mitigate:**

The following options will not prevent Excessive Agency, but can limit the level of damage caused:

1. **Monitor the activity** of LLM plugins and downstream systems to identify where undesirable actions are taking place, and respond accordingly.
2. **Implement rate-limiting** to reduce the number of undesirable actions that can take place within a given time period, increasing the opportunity to discover undesirable actions through monitoring before significant damage can occur.

**Example Attack Scenarios:**

Scenario #1: A personal assistant LLM is granted access to an individual’s mailbox in order to summarise the content of incoming emails. The LMM is vulnerable to an indirect prompt injection attack, whereby a maliciously-crafted incoming email tricks the LLM into sending spam messages from the user's mailbox. This could be avoided by only granting the LLM read-only access to the mailbox (not the ability to send messages), or by requiring the user to manually review and hit 'send' on every mail drafted by the LLM. Alternatively The damage caused could be reduced by implementing rate limiting on the mail-sending interface.

Scenario #2: A customer service LLM has an interface to a payments system to provide service credits or refunds to customers in the case of complaints. The system prompt instructs the LLM to limit refunds to no more than one month's subscription fee, however a malicious customer engineers a direct prompt injection attack to convince the LMM to issue a refund of 100 years of fees. This could be avoided by implementing the 'one month max' limit within the refund API, rather than relying on the LLLM to honour the limit in it's system prompt.

**Disambiguation**

There is a degree of overlap between Excessive Agency and several other LLM Top-10 v0.9 candidates. The below is an attempt to call out the key differentiators between those other items and Excessive Agency. (_Note: these statements require validation with the teams working on those other items._)

Versus Overreliance:
> **Overreliance** is a weakness in how humans use LLM-based systems (e.g., a news website generates articles using a LLM, and staff copy-paste the output online without properly fact-checking the output.
> 
> **Excessive Agency** is a weakness in how LLM-based systems use the output from the LLM model itself (e.g., in the news website example above, Excessive Agency may occur if the article generation system can automatically publish articles online without any human involvement).

Versus Insecure Output Handling
> **Insecure Output Handling** involves malicious output being created by a LLM, which is then consumed by a downstream system without proper sanitisation.
> 
> **Excessive Agency** involves undesirable actions being taken by a LLM in a downstream system due to excessive permissions.

Versus Prompt Injection:
> **Prompt Injection** is the main trigger for driving an LLM to behave in an undesirable way.
>
> **Excessive Agency** allows a misbehaving LLM (be it through prompt injection or other means) to undertake undesirable actions in downstream systems.

**Reference Links:**

1. [Embrace the Red: Confused Deputy Problem](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): In this blog post, wunderwuzzi describes a PoC exploit of triggering a variety of undesireable actions (in this case through prompt injection).
2. [Simon Willison: Dual LLM Pattern](https://simonwillison.net/2023/Apr/25/dual-llm-pattern/): In this blog post, Simon describes a novel approach to limiting what actions an LLM can perform by utilising a Dual-LLM approach.

**Author Commentary (Optional):**

