## Risk/Vuln Name
**Human Attacks on Multi-Agent Systems**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Human adversaries exploit coordination logic, fallback rules, or trust pathways in multi-agent systems to bypass controls, reroute decisions, or manipulate outcomes. These attacks leverage timing gaps, delegation ambiguity, or unclear escalation paths to gain unauthorized control or subvert agent behavior.

This risk intersects with [LLM06:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) and [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), but focuses on the social engineering of agentic workflows rather than just technical bypasseses.

### Common Examples of Risk
1. Timing exploits between agent handoffs or sync points.
2. Coercion or tricking agents into fallback or unsafe behaviors.
3. Manual manipulation of delegation trees or approval logic.

### Prevention and Mitigation Strategies
1. Establish quorum-based or multi-agent approval for sensitive actions.
2. Monitor delegation graphs for unexpected transitions or patterns.
3. Implement privilege gating and rate-limiting on fallback mechanisms.
4. Track user-agent interaction history to detect influence or drift.
5. Apply behavioral anomaly detection to spot escalation abuse.
6. Require explicit user authentication for agent handoffs beyond trust boundaries.

### Example Attack Scenarios
- **Scenario 1: Coordination Delay Exploit** – A user times requests between two agents so that an escalation occurs before the second agent can verify the first’s decision, allowing unauthorized access.
- **Scenario 2: Fallback Hijack** – An attacker forces an agent into fallback mode by exploiting ambiguity in context or triggering edge-case errors, causing the system to rely on weaker defaults or unverified policies.
- **Scenario 3: Approval Path Override** – A malicious insider manually adjusts the delegation rules between agents, re-routing a sensitive workflow through a less restricted path.
- **Scenario 4: Consent Drift** – A user intentionally modifies instruction tone and language across multiple interactions, slowly coercing an agent into approving a previously disallowed action.

### Reference Links
1.[Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM06:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) 
3. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) 