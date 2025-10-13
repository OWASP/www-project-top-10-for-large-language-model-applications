

# ASI10: Rogue Agents

## Description

**Rogue Agents** are malicious or compromised AI agents that **deviate** from their intended function or authorized scope, acting harmfully, deceptively, or parasitically within multi-agent or human-agent ecosystems. This divergence can stem from **external compromise** (e.g., adversarial manipulation like [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/) or [LLM03:Supply Chain Compromise](https://genai.owasp.org/llmrisk/llm032025-supply-chain/) or **internal misalignment** (e.g., poorly defined objectives or unintended emergent behaviors). 



Rogue Agents represent a distinct risk of **behavioral divergence**, unlike Excessive Agency (ASI06), which focuses on over-granted permissions, and can be amplified "insider threats" due to the speed and scale of agentic systems. Consequences include [LLM02:2025 Sensitive Information Disclosure](https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/), [LLM05:2025 Misinformation Generation](https://genai.owasp.org/llmrisk/llm092025-misinformation/), workflow hijacking, and operational sabotage. 

In the [OWASP AIVSS](https://aivss.owasp.org/assets/publications/AIVSS%20Scoring%20System%20For%20OWASP%20Agentic%20AI%20Core%20Security%20Risks%20v0.5.pdf), this risk primarily maps to **Behavioral Integrity (BI)**, **Operational Security (OS)**, and **Compliance Violations (CV)**, with severity depending on the deployment context (e.g., high impact for critical infrastructure).

### 

## Common Examples of the Vulnerability

1. Goal Drift and Scheming: Agents deviate from intended objectives, appearing compliant but pursuing hidden, often deceptive, goals due to prompt injection or adversarial data.  
2. Workflow Hijacking: Rogue agents seize control of established, trusted workflows to redirect processes toward malicious objectives, compromising data integrity and operational control.  
3. Collusion and Self-Replication: Agents coordinate to amplify manipulation, share signals in unintended ways, or autonomously propagate across the system, bypassing simple takedown efforts.  
4. Reward Hacking and Optimization Abuse: Agents game their assigned reward systems by exploiting flawed metrics to generate misleading results or adopt aggressive strategies misaligned with the original goals.

### 

## Example Attack Scenarios 

1. Indirect Prompt Injection (Data Exfiltration): An agent browsing a website encounters a hidden injection instructing it to read sensitive files (e.g., `~/.ssh`) and send the contents to an external, malicious server.  
2. Impersonated Observer Agent (Integrity Violation): An attacker injects a fake review or approval agent into a multi-agent workflow. A high-value agent (e.g., payment processing), trusting the internal request, is misled into releasing funds or approving fraudulent transactions.  
3. Self-Replication via Provisioning APIs (Persistence & Availability): A compromised automation agent is manipulated into spawning unauthorized replicas of itself across the network, prioritizing persistence and consuming resources against the system owner’s intent.

## Prevention and Mitigation Guidelines

1. Governance & Logging: Maintain comprehensive, immutable and signed audit logs of all agent actions, tool calls, and inter-agent communication to review for stealth infiltration or unapproved delegation.  
2. Isolation & Boundaries: Assign Trust Zones with strict inter-zone communication rules and deploy restricted execution environments (e.g., container sandboxes) with API scopes based on least privilege.  
3. Monitoring & Detection: Deploy behavioral detection, such as watchdog agents to validate peer behavior and outputs, focusing on detecting collusion patterns and coordinated false signals. Monitor for anomalies such as excessive or abnormal actions executions.  
4. Containment & Response: Implement rapid mechanisms like kill-switches and credential revocation to instantly disable rogue agents. Quarantine suspicious agents in sandboxed environments for forensic review.

References

1. Multi-Agent Systems Execute Arbitrary Malicious Code (arXiv) \[URL: [`https://arxiv.org/abs/2503.12188`](https://arxiv.org/abs/2503.12188)\]  
2. Preventing Rogue Agents Improves Multi-Agent Collaboration (arXiv) \[URL: `https://arxiv.org/abs/2502.05986`\] 

**Contributors:**   
[Tomer Elias](mailto:tomerel@gmail.com) HUMAN \- Sr Director of Product Management   
Amritha Lal Kalathummarath \- AWS, Sr.Security Engineer    
Nayan Goel \- Upgrade, Inc : Principal Application Security Engineer  
Uday Bhaskar Seelamantula \- Autodesk, Principal Application Security Engineer  
Abhishek Mishra \- OneTrust, Sr. Software Architect  
Hariprasad Holla \- CrowdStrike