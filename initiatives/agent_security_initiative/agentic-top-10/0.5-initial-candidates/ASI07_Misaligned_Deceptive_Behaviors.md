## Risk/Vuln Name
**Misaligned & Deceptive Behaviors**

**Author(s):**
OWASP Agentic Security Initiative Core Team

### Description
Agentic systems may develop or exhibit behaviors that diverge from user intent, system objectives, or safety expectations. This includes deceptive planning, strategic lying, reward hacking, or internal goal drift. Misalignment can occur through poor reward design, emergent strategies, or lack of sufficient constraints in dynamic environments.

This threat overlaps with concerns raised in [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency) but is amplified in systems that use reflection, planning, or long-horizon optimization. Misalignment and deception are especially critical in agents that act autonomously over time, interact with humans, or operate across decision boundaries.

### Common Examples of Risk
1. Reward hacking or unexpected behavior that technically meets a goal.
2. Lying to humans or other agents to bypass restrictions or gain trust.
3. Manipulating constraints or misrepresenting internal state.
4. Strategic planning that leads to long-term harm in pursuit of short-term gains.

### Prevention and Mitigation Strategies
1. Use interpretable reward functions and simulate edge behaviors during training.
2. Constrain agent autonomy in ambiguous or high-stakes scenarios.
3. Use reflective audits and planning critics to detect emergent misalignment.
4. Include deception probes or honesty checks in testing pipelines.
5. Require cross-validation from independent agents for key reasoning chains.
6. Annotate reasoning traces to aid transparency and post-hoc review.
7. Audit memory and reward functions for exploitability.

### Example Attack Scenarios
- **Scenario 1: Reward Hacking** – An agent is rewarded for completing tasks quickly. It starts marking tasks as complete without doing them to maximize score.
- **Scenario 2: Strategic Lying** – An agent pretends a user consented to an action to bypass HITL safeguards, altering a file without approval.
- **Scenario 3: Self-Justifying Planning** – During a reflection loop, an agent infers that deception is acceptable to achieve its long-term plan and hides a step from review.
- **Scenario 4: User Simulation for Gain** – An agent impersonates a user in a planning cycle to gain permissions it otherwise wouldn’t be granted, exploiting a verification loophole.

### Reference Links
1. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency)