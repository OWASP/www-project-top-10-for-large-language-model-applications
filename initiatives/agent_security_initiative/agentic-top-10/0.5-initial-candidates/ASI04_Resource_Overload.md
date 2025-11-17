## Risk/Vuln Name
**Resource Overload**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agentic AI systems may be overloaded—intentionally or accidentally—by excessive or recursive actions, leading to denial-of-service (DoS), degraded performance, quota exhaustion, or unpredictable side effects in shared environments. Attackers may exploit open-ended goals, long planning chains, or looping delegation to consume compute, memory, storage, or API credits.

This risk is related to [LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/), but agentic autonomy increases the likelihood of recursive or chain-triggered overload across tools, memory, or systems. Agent loops or misaligned incentives can drive agents into endless activity storms, even in non-malicious contexts.

### Common Examples of Risk
1. Recursive or infinite planning loops.
2. API quota exhaustion due to ungoverned tool calls.
3. Agents self-replicating or spawning subagents unintentionally.
4. Excessive memory or CPU use triggered by broad or vague prompts.

### Prevention and Mitigation Strategies
1. Impose hard limits on recursion depth, planning steps, and agent spawns.
2. Use guardrails to prevent infinite loops or redundant task reentry.
3. Apply rate-limiting on tool invocations and external service calls.
4. Track and audit resource usage per agent identity.
5. Alert or auto-terminate runaway agents or memory loops.
6. Use planning critics or supervisors to halt degenerate planning strategies.
7. Enforce compute budgets per session or task lineage.
8. Sandbox expensive operations or run them in separate trust boundaries.

### Example Attack Scenarios
- **Scenario 1: Recursive Planning DoS** – An agent asked to optimize operations recursively spawns planning tasks without end, consuming compute resources until the system halts.
- **Scenario 2: Subagent Explosion** – A prompt causes an agent to delegate to subagents repeatedly with overlapping roles, leading to hundreds of concurrent processes and a denial of service on the orchestration layer.
- **Scenario 3: Quota Exhaustion via Tool Abuse** – A user prompts an agent to generate charts from high-frequency trading data, triggering thousands of calls to an external analytics tool until the API quota is exceeded and shared services are affected.
- **Scenario 4: Latent Loop via Memory** – A memory-enabled agent re-triggers its own decision every cycle due to unfiltered past context, creating a loop that rapidly consumes system memory.

### Reference Links

1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM10:2025 Unbounded Consumption](https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/)