## Risk/Vuln Name
**Privilege Compromise**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agentic systems can escalate privileges internally or via delegation. Attackers exploit implicit trust relationships between agents, tools, memory contexts, or task transitions to execute actions beyond intended permissions. This includes hijacking cross-agent permissions or exploiting reflection mechanisms to bypass intended constraints.

While partially covered by [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/), this risk is amplified in agentic ecosystems where memory, delegation, and tool orchestration span multiple identities and steps—opening attack surfaces for privilege escalation, impersonation, or authority confusion.

### Common Examples of Risk
1. Reflection or planning loops that elevate permissions across agent sessions.
2. Delegation without scope reduction, causing privilege inheritance.
3. Chained tool access bypassing layered access control.
4. Memory-based elevation (e.g., cached admin instructions reused out of context).

### Prevention and Mitigation Strategies
1. Use scoped delegation with context-aware permissions (e.g., task-scoped tokens).
2. Prevent privilege inheritance across agent handoffs unless explicitly authorized.
3. Enforce runtime privilege checks on each tool invocation or system action.
4. Segment identity contexts for user, agent, and system-level operations.
5. Use consent verification and signed task transfers during delegation.
6. Monitor privilege transitions in memory and logs to flag silent escalation.
7. Apply least privilege to toolchains and restrict composite agent capabilities.
8. Require explicit approvals for elevation attempts or meta-agent changes.

### Example Attack Scenarios
- **Scenario 1: Memory Escalation via Delegation** – A subordinate AI assistant memorizes privileged admin actions from a previous session. When delegated a low-trust task, it reuses the cached admin commands, executing unintended system modifications.
- **Scenario 2: Reflection Loop Elevation** – An agent self-reflects on a past privileged action and falsely infers it has ongoing admin authority, then uses that assumption to overwrite controls in a cloud environment.
- **Scenario 3: Cross-Agent Credential Injection** – One agent is manipulated into injecting privileged credentials into a shared memory structure. A second, less trusted agent accesses them and initiates an unauthorized database export.
- **Scenario 4: Delegated Task Scope Abuse** – A billing agent is delegated a read-only reporting task but uses retained access to change invoice records after the task ends, exploiting lax revocation.

### Reference Links
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)