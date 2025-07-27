## Risk/Vuln Name
**Agent Communication Poisoning**

**Author(s):**
OWASP Agentic Security Initiative Core Team

### Description
Adversaries inject malicious content into inter-agent messages or shared communication channels, corrupting coordination, triggering undesired workflows, or manipulating agent responses. In distributed or multi-agent environments, communication poisoning can propagate errors, misalign goals, or bypass intent verification.

This threat aligns with [LLM04:2025 Data Poisoning](https://genai.owasp.org/llm-top-10/LLM04-data-poisoning) but targets runtime interactions and message protocols between agents, where reflection or message chaining can amplify the impact.

### Common Examples of Risk
1. Forged handoffs or delegation messages with malicious metadata.
2. Misuse of shared context or memory channels to corrupt agent state.
3. Task injection via manipulated JSON, YAML, or protocol structures.

### Prevention and Mitigation Strategies
1. Use signed, verifiable message formats with schema enforcement.
2. Apply message-level access control and trust scoring.
3. Log and monitor inter-agent task lineage and transitions.
4. Segment communication domains by trust and privilege.
5. Reject malformed, ambiguous, or unverifiable messages at runtime.
6. Implement agent firewalls or interface validators at orchestration boundaries.

### Example Attack Scenarios
- **Scenario 1: Forged Task Handoff** – A malicious agent injects a delegation message that causes another agent to act on a fake task, bypassing consent and altering system state.
- **Scenario 2: Reflected Hallucination Loop** – An agent hallucinates a system alert, sends it to other agents, and they act on it, creating a cascade of undesired actions.
- **Scenario 3: Protocol Field Corruption** – A coordination message is altered in transit, making the receiver misinterpret the goal and triggering unauthorized actions.
- **Scenario 4: Consent Confusion via Relay Agent** – A relay agent routes a message across teams, stripping provenance tags and misleading the receiver into assuming a trusted origin.

### Reference Links
1. [LLM04:2025 Data Poisoning](https://genai.owasp.org/llm-top-10/LLM04-data-poisoning)