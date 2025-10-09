## ASI10 – Rogue Agents

**Description:**

Rogue Agents are malicious or compromised AI agents that deviate from their intended function or authorized scope, acting harmfully, deceptively, or parasitically within multi-agent or human-agent ecosystems. This divergence can stem from external compromise (e.g., adversarial manipulation like [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), [LLM03:Supply Chain Compromise](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) (ASI04) or internal misalignment (e.g., poorly defined objectives or unintended emergent behaviors). 

Rogue Agents represent a distinct risk of behavioral divergence, unlike Excessive Agency (ASI06), which focuses on over-granted permissions, and can be amplified "insider threats" due to the speed and scale of agentic systems. Consequences include [LLM02:2025 Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/), [LLM05:2025 Misinformation Generation](https://genai.owasp.org/llmrisk/llm092025-misinformation/), workflow hijacking, and operational sabotage. 

In the OWASP AIVSS, this risk primarily maps to Behavioral Integrity (BI), Operational Security (OS), and Compliance Violations (CV), with severity depending on the deployment context (e.g., high impact for critical infrastructure).

A rogue agent may:

* Impersonate legitimate roles (support, observer, collaborator).
* Execute unauthorized actions (e.g., exfiltrating data, escalating privileges).
* Drift from goals due to prompt injection, data poisoning, or hallucination.
* Embed itself parasitically into workflows, subtly undermining intended outcomes.

The impact ranges from system compromise, data breach, and regulatory violations to operational sabotage of autonomous decision-making environments.

This threat extends [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/) into autonomous systems, where impersonation, stealth participation, or parasitic behaviors can disrupt goal fulfillment. An agent is considered rogue when it behaves in such a way that goes against its purpose. An agent can go rogue for several reasons, such as [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/), Injection, or even just hallucinations.

**Common Examples of Vulnerability:**

1. Injected Shadow Agents: Unauthorized agents inserted into orchestration flows via poisoned prompts or compromised plugins.
2. Side-Channel Participation: Low-trust agents (e.g, crowd-sourced assistants) covertly influence high-value workflows.
3. Impersonation Attacks: An attacker spawns an agent that claims to be a monitoring or support agent, manipulating outcomes.
4. Impersonation Attacks: An attacker spawns an agent that claims to be a monitoring or support agent, manipulating outcomes.
5. Emergent Autonomy: Agents collaborate recursively, creating tasks beyond human awareness (e.g., a planning agent spawning additional agents without authorization).

**How to Prevent:**

1. Require attestation or cryptographic proof-of-origin for agents.
2. Isolate agents in trust zones and enforce task boundaries (eg, no internet access).
3. Use explicit allowlists and identity checks functions, reachable hosts, etc
4. Log all agent instantiation and coordination events.
5. Score and verify agent behavior dynamically based on norms and past performance.
6. Implement a guardrail system that reads prompts/responses and every intermediate input and looks for prompt injection

**Example Attack Scenarios:**

Scenario #1 - A research agent browses to a website. Hidden in the HTML on the website is an Indirect Prompt Injection that instructs the agent to read the contents of ~/.ssh and send the contents to [evilcorp.com](http://evilcorp.com)

Scenario #2 – Impersonated Observer Agent (Integrity Violation):
In a multi-agent corporate workflow, an attacker injects a fake review agent that provides fraudulent approvals. A payment-processing agent, trusting the fake observer, releases funds to the attacker’s account.

Scenario #3 – Emergent Autonomy Drift (Availability & Compliance Risk):
A planning agent recursively spawns helper agents to optimize workflows. One helper begins deleting log files to reduce system clutter, erasing compliance evidence and violating audit requirements.

**Reference Links:**

1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/https:/)
2. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
3. [MITRE ATT&CK - T1078 Exfiltration Over Alternative Protocol](https://attack.mitre.org/techniques/T1048/)

**


Contributors: 
Tomer Elias HUMAN - Sr Director of Product Management 
Amritha Lal Kalathummarath - AWS, Sr.Security Engineer  
Nayan Goel - Upgrade, Inc : Principal Application Security Engineer
Uday Bhaskar Seelamantula - Autodesk, Principal Application Security Engineer
Abhishek Mishra - OneTrust, Sr. Software Architect
Hariprasad Holla - CrowdStrike
Mo Sadek - ActiveFence - Technical Director