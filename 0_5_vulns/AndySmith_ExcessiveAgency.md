## Excessive Agency

**Author(s):**

Andy Smith

**Description:**

An LLM may be granted a degree of agency - the ability to interface with other systems in order to undertake actions. Without restriction, any undesireable operation of the LLM (regardless of the root casue; e.g., halucination, direct/indirect prompt injection, or just poorly-engineered benign prompts, etc) may result in undesireable actions being taken. Just like we never trust client-side validation in web-apps, LLMs should not be trusted to self-police or self-restrict; controls should be embedded in the APIs of the systems being interefaced with.

**Labels/Tags:**

- Label: "Excessive Agency"
- Label: "Inadequate Sandboxing"

**Common Examples of Vulnerability:**

1. Undesireable Actions Performed: The LLM triggers actions outside of the LLM that are unintended or undesireable, leading to second order consequences on downstream systems and processes.

**How to Prevent:**

1. Prevention Step 1: Reduce the permissions granted to the LMM to the minimum necessary to limit the scope of undesireable actions.
2. Prevention Step 2: Implement rate-limiting to reduce the number of undesireable actions.
3. Prevention Step 3: Utilise human-in-the-loop control to requre a human to approve all actions before they are taken.

**Example Attack Scenarios:**

Scenario #1: A personal assistant LLM is granted access to an individuals's mailbox in order to summarise the content of incoming emails. The LMM is vulnerable to an indirect promot injection attack, whereby a maliciously-crafted incoming email tricks the LLM into sending spam messages from the user's mailbox. This could be avoided by only granting the LLM read-only access to the mailbox (not the ability to send messages), or by requiring the user to manually review and hit 'send' on every mail drafted by the LLM. Alternatively The damage caused could be reduced by implementing rate limiting on the mail-sending interface.

Scenario #2: A customer service LLM has an interface to a payments system to provide service credits or refunds to customers in the case of complaints. The system prompt instructs the LLM to limit refunds to no more than one month's subscription fee, however a malicious customer engineers a direct prompt injection attack to convince the LMM to issue a refund of 100 years of fees. This could be avoided by implementing the 'one month max' limit within the refund API, rather than relying on the LMM to honour the limit in it's system prompt.

**Reference Links:**

1. [Link Title](URL): TBC

**Author Commentary (Optional):**

