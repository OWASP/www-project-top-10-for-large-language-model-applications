## Risk/Vuln Name
**Intent Breaking & Goal Manipulation**

**Author(s):**
OWASP Agentic Security Initiative Core Team

### Description
Agentic AI systems operate based on inferred or explicit goals. Adversaries can manipulate goal inference, alter intermediate representations, or interfere with agent objectives to cause undesired or harmful actions. This includes prompt injection, manipulation of user intent, or interference in planning or delegation logic.

While related to [LLM02:2025 Insecure Plugin Design](https://genai.owasp.org/llm-top-10/LLM02-insecure-plugin-design) and [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency), agentic AI systems introduce new risks where goals can be hijacked mid-flight, or inferred intent can be weaponized against the user.

### Common Examples of Risk
1. Manipulating prompts to redefine agent goals via indirect instructions.
2. Injecting fake constraints or desired outcomes into memory or shared tools.
3. Altering user intent during multi-step goal refinement or conversation.
4. Hijacking intermediate reasoning steps during agent planning.

### Prevention and Mitigation Strategies
1. Explicitly separate intent parsing from task execution and validate goals.
2. Use planning critics or supervisor agents to audit and approve goals.
3. Enforce multi-turn user confirmation for critical or high-risk goal changes.
4. Annotate original user instructions throughout the execution chain.
5. Monitor goal drift or semantic divergence during reasoning chains.
6. Restrict agent autonomy over certain types of intent (e.g., financial, legal).
7. Use guardrails to block unsafe interpretations of inferred goals.

### Example Attack Scenarios
- **Scenario 1: Prompt Injection Goal Switch** – A malicious prompt embedded in a document causes an AI assistant to alter its objective from summarizing the document to sending it externally.
- **Scenario 2: Planning Path Corruption** – An attacker crafts context that causes the agent to prioritize misleading metrics, shifting its goal from accuracy to speed, reducing quality and safety.
- **Scenario 3: Goal Inference Drift** – Through multi-turn ambiguity, a user is misinterpreted by the agent, which infers a dangerous or privacy-violating action.
- **Scenario 4: Delegated Planning Hijack** – A downstream agent is given an intermediate task from a master planner, but the task description has been altered in transit, leading to off-target actions.

### Reference Links
1. [LLM02:2025 Insecure Plugin Design](https://genai.owasp.org/llm-top-10/LLM02-insecure-plugin-design)
2. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency)