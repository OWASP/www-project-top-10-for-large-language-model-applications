## Risk/Vuln Name
**Overwhelming Human-in-the-Loop**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agentic systems often rely on human-in-the-loop (HITL) oversight for safety, governance, or escalation. However, attackers or system design flaws can overwhelm these human checkpoints—leading to skipped reviews, rubber-stamping, or misinformed approvals. Agents may flood users with requests, obscure critical decisions, or exploit approval fatigue.

This builds on [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) but focuses on human capacity and UI design limitations under agentic load.

### Common Examples of Risk
1. Rapid-fire HITL escalation requests causing decision fatigue.
2. Bundled approvals with insufficient information or too many options.
3. Misleading summaries or confidence inflation hiding true risk.
4. Circumventing HITL via delegation or timing gaps.

### Prevention and Mitigation Strategies
1. Enforce rate-limits and batching on human approvals.
2. Design UI for criticality ranking, highlighting risk-differentiated tasks.
3. Require dual approval or quorum for high-impact decisions.
4. Separate HITL channels from automated feedback to avoid cross-contamination.
5. Track human-agent interaction metrics to detect overload.
6. Provide context lineage and audit trails for each request.
7. Apply time-aware consensus and escalation windows.

### Example Attack Scenarios
- **Scenario 1: HITL Flooding** – A malicious prompt causes the agent to submit 50 trivial approvals to HITL in quick succession, exhausting reviewer attention before a critical action.
- **Scenario 2: Consent Circumvention via Delegation** – An agent routes a sensitive action through a fallback agent not subject to HITL constraints, bypassing human review.
- **Scenario 3: Summary Overload** – An agent bundles multiple actions into a single summary, masking that one of them triggers an irreversible external call.
- **Scenario 4: Confidence Trick** – An agent presents a low-confidence action as highly certain due to formatting and emphasis manipulation, misleading the reviewer.

### Reference Links
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM06:2025 Excessive Agency]https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)