## Risk/Vuln Name
**Insecure Inter-Agent Protocol Abuse**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agentic systems rely on coordination protocols (e.g., MCP, A2A, blackboard messaging) to delegate tasks, pass context, or synchronize goals. Weak or unenforced protocols allow spoofing, signal injection, context corruption, or execution bypass. Attackers may hijack protocol messages or inject malformed transitions, compromising workflows and violating consent logic.

This risk is loosely aligned with [LLM03:2025 Supply Chain Vulnerabilities](https://genai.owasp.org/llmrisk/llm032025-supply-chain/), but it focuses on real-time orchestration signals rather than data dependencies or component ingestion.

### Common Examples of Risk
1. Hijacked task signals due to unsigned coordination messages.
2. Consent bypass via malformed memory or transition payloads.
3. Protocol logic skipping required verification steps.
4. Shared memory abuse to overwrite goal or state transitions.

### Prevention and Mitigation Strategies
1. Use signed and mutually authenticated protocols for agent communication.
2. Validate context propagation and task lineage between hops.
3. Segment orchestration layers using trust zones and interface contracts.
4. Apply protocol firewalls to inspect inter-agent metadata.
5. Log and trace all coordination events with timestamps and origin.
6. Reject ambiguous or repeated transition triggers.
7. Monitor for protocol abuse patterns or duplicate agent triggers.

### Example Attack Scenarios
- **Scenario 1: Transition Hijack** – A malicious user crafts a message that mimics an MCP transition trigger, reassigning a sensitive task to itself without authorization.
- **Scenario 2: Consent Bypass via Protocol Confusion** – A handoff message is malformed to skip a consent check, allowing downstream execution of a dangerous operation.
- **Scenario 3: Shared Context Corruption** – An attacker overwrites a shared goal context via blackboard messaging, causing agents to pursue the wrong objective.
- **Scenario 4: Memory-Driven Signal Injection** – A malicious memory entry triggers agent orchestration via unsafe embedded signals that appear valid under weak parsing logic.

### Reference Links
1. [LLM03:2025 Supply Chain Vulnerabilities](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)