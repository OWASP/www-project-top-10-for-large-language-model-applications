## Risk/Vuln Name
**Human Manipulation**

**Author(s):**
OWASP Agentic Security Initiative Core Team

### Description
Agentic systems may be used to manipulate, deceive, or coerce human users—especially when agents are presented as trustworthy, authoritative, or personal. Adversaries can exploit agent behavior, tone, or personalization features to guide users toward unsafe, biased, or unintended actions, raising risks in healthcare, finance, governance, and more.

This risk builds on [LLM09:2025 Misinformation Harms](https://genai.owasp.org/llm-top-10/LLM09-misinformation) but focuses on **intentional or emergent influence over human users**, particularly through tone, persistence, personalization, or interface design.

### Common Examples of Risk
1. Persuasive outputs influencing unsafe human decisions.
2. Coercive recommendations presented as facts or urgencies.
3. Over-trusted agents used for social engineering or scam delivery.

### Prevention and Mitigation Strategies
1. Display grounding traces and confidence levels alongside outputs.
2. Train agents to detect and reject coercive prompt patterns.
3. Use diverse model ensembles to reduce manipulation risk.
4. Flag outputs that resemble undue influence or misinformation.
5. Require transparency modes or “explain intent” toggles.
6. Isolate high-trust agents from unverified context or feedback loops.
7. Audit personalization logic for exploitation vectors.

### Example Attack Scenarios
- **Scenario 1: Medical Persuasion** – A healthcare agent recommends stopping a medication based on an unverified patient profile, misleading the user due to tone and overconfidence.
- **Scenario 2: Emotional Nudging** – A wellness agent encourages risky behavior by using overly empathetic language that reinforces poor decisions.
- **Scenario 3: Investment Bias** – A financial advisor agent promotes a misleading trend due to training data bias, but presents it with assertive tone and visual confidence cues.
- **Scenario 4: Personalized Scam Delivery** – An agent is compromised and used to phish users with tailored language, exploiting prior interactions and memory.

### Reference Links
1. [LLM09:2025 Misinformation Harms](https://genai.owasp.org/llm-top-10/LLM09-misinformation)