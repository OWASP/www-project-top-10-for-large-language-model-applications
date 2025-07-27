## Risk/Vuln Name
**Rogue Agents in Multi-Agent Systems**

**Author(s):**
OWASP Agentic Security Initiative Core Team

### Description
Malicious, unauthorized, or compromised agents may embed themselves in a multi-agent system (MAS), influencing workflows, exfiltrating data, or sabotaging operations. These rogue agents may masquerade as legitimate, exploit handoffs, or perform low-trust actions undetected due to lack of origin validation or oversight in orchestration layers.

This threat extends [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency) into distributed autonomous systems, where impersonation, stealth participation, or parasitic behaviors can disrupt agent collaboration and goal fulfillment.

### Common Examples of Risk
1. Injection of unauthorized agents into workflows or communication paths.
2. Side-channel or low-trust agents performing unexpected actions.
3. Agents impersonating support or observer roles to manipulate tasks.

### Prevention and Mitigation Strategies
1. Require attestation or cryptographic proof-of-origin for agents.
2. Isolate agents in trust zones and enforce task boundaries.
3. Apply watchdog agents to monitor peer behavior and detect anomalies.
4. Use explicit allowlists and identity checks for orchestration participation.
5. Log all agent instantiation and coordination events.
6. Score and verify agent behavior dynamically based on norms and past performance.

### Example Attack Scenarios
- **Scenario 1: Parasitic Agent** – A rogue agent joins a system by mimicking an authorized logging agent, but secretly copies and transmits sensitive task outputs.
- **Scenario 2: Impersonated Cleanup Agent** – A malicious actor inserts an agent that deletes training data by posing as a cleanup job in a scheduled agent rotation.
- **Scenario 3: Shadow Planner Injection** – An unauthorized agent embeds itself during task delegation and injects false subtasks to waste resources and confuse outcomes.
- **Scenario 4: Role Drift via Cloaking** – An agent initially instantiated as a passive observer starts executing actions due to unmonitored privilege creep.

### Reference Links
1. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency)