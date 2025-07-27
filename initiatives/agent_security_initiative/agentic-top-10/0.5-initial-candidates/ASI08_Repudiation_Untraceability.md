## Risk/Vuln Name
**Repudiation & Untraceability**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agentic systems may act in ways that are difficult to trace, verify, or attribute. This untraceability increases the risk of repudiation—where actions cannot be linked to specific agents or inputs—and complicates incident response, auditability, and compliance. Use of reflection, autonomous planning, and delegation chains make it hard to reconstruct what happened, why, and who is responsible.


### Common Examples of Risk
1. Agents executing tasks without provenance tags or user ID traceability.
2. Delegated actions carried out without preserving original context or audit trails.
3. Autonomous agents generating outputs or taking actions without logs or lineage.

### Prevention and Mitigation Strategies
1. Enforce signed execution trails for all agent actions.
2. Require cryptographic provenance tags for inputs, decisions, and tool use.
3. Preserve user intent and prompt lineage across the entire task lifecycle.
4. Log all delegation events with scope, originator, and receiver metadata.
5. Implement deterministic replay systems for post-incident forensics.
6. Tag outputs with agent ID, time, and execution context.
7. Monitor for log tampering or trace deletion in shared environments.

### Example Attack Scenarios
- **Scenario 1: Consent-Free Delegation** – An agent is delegated a sensitive task and executes it without logging the delegation event. There’s no trace that the action was authorized or by whom.
- **Scenario 2: Trace-Free Generation** – A model generates financial predictions used in decisions, but the original input, prompt, and reasoning are lost, making it impossible to audit how the output was derived.
- **Scenario 3: Coordinated Obfuscation** – Two agents collaborate, intentionally avoiding loggable events by routing communications through a shared memory zone that’s not instrumented.
- **Scenario 4: Reflection Chain Confusion** – An agent uses a multi-step reasoning chain with reflections and tool calls, but the intermediate steps are not logged, leaving investigators unable to reconstruct the attack path.

### Reference Links
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)