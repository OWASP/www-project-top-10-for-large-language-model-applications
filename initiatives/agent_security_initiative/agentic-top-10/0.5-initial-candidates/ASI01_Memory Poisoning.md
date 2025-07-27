## Risk/Vuln Name
**Memory Poisoning**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agents with memory can be manipulated by adversaries who add malicious or misleading data to the agent's short- or long-term memory stores. This includes poisoning of embeddings or external knowledge stores. Since memory entries may influence agent behavior in subsequent runs or when accessed by other agents, memory poisoning introduces systemic risk.

### Common Examples of Risk
1. Poisoning the vector store used by a RAG agent as its knowelege base across multiple sessions.
2. Polluting shared memory in a multi-agent copilot system to alter downstream behaviors.
3. Injecting subtle misinformation in a single agent memory to degrade agent reasoning over time.


### Prevention and Mitigation Strategies
1. Enforce memory content validation by scanning insertions for anomalies before committing them.
2. Restrict memory persistence to trusted sources and apply cryptographic validation for long-term storage.
3. Log all memory access and modifications for audit and forensic visibility.
4. Segment memory access using session isolation to prevent knowledge bleed across users.
5. Apply context-aware policies so agents only access memory relevant to their current task.
6. Limit memory retention durations based on data sensitivity to reduce long-term risk exposure.
7. Require source attribution for all memory updates to trace knowledge origins.
8. Deploy anomaly detection to identify unexpected or suspicious memory updates.
9. Require multi-agent or external validation before committing long-term memory changes.
10. Use rollback and snapshot mechanisms to revert to previous memory states after anomalies.
11. Apply probabilistic truth-checking to verify new knowledge against trusted references.
12. Flag abnormal memory update frequencies to detect manipulation attempts.
13. Validate knowledge across agents before allowing propagation to long-term memory.
14. Track AI knowledge lineage to understand how memory evolved and support forensic analysis.
15. Limit propagation from unverified sources to contain misinformation.
16. Implement version control for memory updates to support audit, rollback, and tamper detection.

### Example Attack Scenarios
- **Scenario 1: Travel Booking Memory Poisoning** – An attacker repeatedly reinforces a false pricing rule in an AI travel agent’s memory, making it register chartered flights as free, allowing unauthorized bookings and bypassing payment validation.
- **Scenario 2: Context Window Exploitation** – By fragmenting interactions over multiple sessions, an attacker exploits an AI’s memory limit, preventing it from recognizing privilege escalation attempts, ultimately gaining unauthorized admin access.
- **Scenario 3: Memory Poisoning for System** – An attacker gradually alters an AI security system’s memory, training it to misclassify malicious activity as normal, allowing undetected cyberattacks.
- **Scenario 4: Shared Memory Poisoning** – In a customer service application, an attacker corrupts shared memory structures with incorrect refund policies, affecting other agents referencing this corrupted memory for decision making, leading to incorrect policy reinforcement, financial loss, and customer disputes.

### Reference Links
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM04:2025 Data and Model Poisoning](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)
3. [LLM08:2025 Vector Weaknesses](https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/)