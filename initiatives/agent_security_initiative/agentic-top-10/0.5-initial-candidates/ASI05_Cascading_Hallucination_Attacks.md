## Risk/Vuln Name
**Cascading Hallucination Attacks**

**Author(s):**
OWASP Agentic Security Initiative Core Team

### Description
Agentic systems are prone to hallucinations—confidently presenting false information—as they generate, recall, or reuse unverified outputs. These hallucinations can become self-reinforcing, especially when persisted in memory or reflected across agents. When used in planning, reasoning, or as inputs to other tools, hallucinations may cascade into widespread misinformation, faulty decisions, or unsafe actions.

This risk aligns with [LLM09:2025 Misinformation Harms](https://genai.owasp.org/llm-top-10/LLM09-misinformation), but agent-based systems introduce higher persistence and propagation risk due to memory and delegation. In multi-agent contexts, false knowledge may circulate and amplify, creating system-wide instability.

### Common Examples of Risk
1. Self-reflection or summarisation loops reinforcing hallucinated facts.
2. RAG agents incorporating incorrect content and treating it as ground truth.
3. Multi-agent teams exchanging hallucinated knowledge as if validated.

### Prevention and Mitigation Strategies
1. Implement grounding mechanisms to validate claims against trusted sources.
2. Use ensemble verification or external judgment models for fact-checking.
3. Constrain agents with domain-specific refusal rules and precision filters.
4. Isolate memory entries from unverified sources and mark for review.
5. Limit propagation of knowledge across agents unless confirmed.
6. Annotate all generated facts with confidence scores and source lineage.
7. Track hallucination patterns using hallucination fingerprinting or detection.

### Example Attack Scenarios
- **Scenario 1: Memory Echo Loop** – An agent hallucinates a policy exception during summarisation. This is persisted to memory, recalled in future tasks, and eventually presented as a compliance justification to users.
- **Scenario 2: RAG Feedback Loop** – A hallucinated output is published to a shared document. Later, a RAG agent retrieves and reuses this output as context, reinforcing the false information.
- **Scenario 3: Multi-Agent Contagion** – One agent generates a plausible but fake API endpoint. This endpoint is propagated to other agents for integration, causing repeated failed actions or potential security issues.
- **Scenario 4: Delegated Misinformation** – A planning agent generates a hallucinated summary of a document and delegates action to another agent, which follows the false instructions and incorrectly alters critical records.

### Reference Links
1. [LLM09:2025 Misinformation Harms](https://genai.owasp.org/llm-top-10/LLM09-misinformation)