Cascading Failures in Agentic AI
OWASP Agentic Security Initiative Team: ASI08 – Cascading Failures
Authors: Diana Henderson https://www.linkedin.com/in/dianamhenderson/, Neeraj Nagpal


Description

Cascading Failures in agentic AI systems occur when a single error, whether a hallucination, malicious input, corrupted tool, or compromised memory, propagates from one AI agent to another, leading to compound failures and system-wide harm. Unlike traditional LLM applications that generate outputs for human review, agentic systems plan, persist, delegate, and act autonomously. These capabilities mean that a minor fault can become a multi-step chain of privileged operations affecting data, infrastructure, finances, or entire multi-agent ecosystems performing unintended actions.  

Root Causes of Cascading Failures
1.	Unvalidated inter-agent communication between agents
2.	Overly trusting agents i.e. blind trust in outputs
3.	Lack of feedback loops with oversight i.e. no fail-safes
   
The impacts can escalate small faults into major incidents such as data corruption or widespread service failures across networks of connected agents or workflows.
Cascading failures amplify their effect across interconnected agents or systems and chain together vulnerabilities from the OWASP LLM Top 10. For example, LLM01:2025 Prompt Injection combined with LLM06:2025 Excessive Agency can trigger autonomous tool execution that propagates errors through interconnected systems without human intervention. Similarly, LLM04:2025 Data and Model Poisoning affecting an agent's persistent memory can influence decisions across multiple sessions and workflows.

Here are key fundamental differences between agentic cascade and traditional system failures:
1.	Autonomous Decision Propagation: Agents make decisions that directly influence other agents or systems without human validation at each step.
2.	Persistent Erroneous Feedback Loops: Even after fixing bad data after an initial context injection, agents may have already saved partial plans or goals, and those leftover states continue propagating the fail chain, influencing future actions across sessions.
3.	Emergent Runtime Connections: Agents can dynamically link new tools, APIs, or even other agents while the system is running, forming relationships the designers never mapped. A single misstep can quickly spread across this emerging network, turning a small problem into a wide, unpredictable cascade—even when no outside component was originally compromised.


Common Examples of Vulnerability
1.	Planner-Executor Coupling Failures: A compromised or hallucinating planner agent generates unsafe execution steps that are automatically carried out by a downstream executor agent without validation. This can compound mistakes across multiple business processes.  For instance, a planner might hallucinate that "Finance approved mass refunds" and instruct the executor to erroneously process thousands of refund transactions.
2.	Memory Poisoning and Goal Misalignment: Attackers inject malicious context into an agent's persistent memory through indirect prompt injection. This "poisoned" memory influences the agent's future planning and decision-making, causing it to deviate from its intended purpose and trigger cascading harmful behaviors.
3.	Inter-Agent Communication Poisoning: In multi-agent systems, agents often delegate tasks and trust outputs from other agents. A compromised agent can feed malicious information to downstream agents, causing a chain of failures as poisoned data propagates through the entire system.  For example, an LLM-based agent hallucinates a critical instruction and instructs a maintenance agent to reboot or shutdown services unnecessarily.  Dependent agents receive misleading status info and take improper actions leading to larger outages.
4.	Tool Misuse and Privilege Escalation: Agents can be tricked into misusing their tool integrations, even when operating within authorized permissions. This can lead to privilege escalation where the agent gains more access than intended, enabling lateral movement across multiple systems.
5.	Supply Chain Agent Contamination: Compromised agents, tools, or orchestration components can influence entire agent networks. Malicious agents or unsigned adapters with backdoors can spread through agent repositories, affecting multiple downstream systems simultaneously.


Prevention and Mitigation Strategies
1.	Establish Isolation and Trust Boundaries: Define strict boundaries for agents, given their different privilege levels and purposes, by implementing sandboxing, permission limits, network segmentation, API scopes, and agent-to-agent authentication to contain failure propagation.
2.	Test, Simulate and Deploy Agent Decision Circuit Breakers:  Conduct fault injection, red-teaming, and chaos engineering before deployment to ensure graceful failure.  Deploy automated validation checkpoints between agent decision points as circuit breakers for unexpected behaviors. Each agent's outputs should undergo semantic validation and policy verification before being passed to downstream agents or executed by tools.
3.	Validate Outputs: Implement checkpoints to validate or sanity-check agent outputs before their consumption by downstream agents, possibly using governance agents or human-in-the-loop methods.
4.	Establish Capability-Scoped Access Controls: Implement dynamic access controls where agents must request tool access on a per-invocation basis rather than maintaining persistent elevated permissions. Use one-time, per-action credentials following NIST SP 800-204C principles.
5.	Deploy Independent Policy Enforcement: Separate the planning and execution phases with independent policy engines that verify planner outputs before the executor runs them. This prevents corrupted planning from directly triggering harmful actions.
6.	Rate Limit and Monitor: Detect chain reactions or unusual activity spikes with automatic halting or flagging of suspicious sequences.
7.	Implement Fail-Safe Mechanisms: Design agents to reject incoherent or out-of-bounds data and include fail-safe rules to stop or seek confirmation on critical deviations.
8.	Implement Memory Integrity Controls: Protect agent persistent memory using append-only storage with provenance checks. Implement memory versioning and rollback capabilities to recover from poisoned state conditions.
9.	Require Multi-Agent Validation: For critical decisions, implement "four-eyes approval" systems where a second agent must verify proposed actions before execution. This prevents single points of failure from causing system-wide damage.
10.	Deploy Behavioral Anomaly Detection: Monitor agent decision patterns and tool usage for deviations from expected behavior. Unlike traditional systems, agents can make semantically valid but contextually inappropriate decisions that require behavioral analysis.


Example Attack Scenarios

Scenario #1: Financial Trading System Cascade
A trading firm deploys an orchestrated system of specialized agents: Market Analysis, Risk Assessment, Position Management, and Execution agents. An attacker exploits LLM01:2025 Prompt Injection in the Market Analysis agent by embedding malicious instructions in a financial news feed. The compromised agent provides false market sentiment data to the Risk Assessment agent, which autonomously adjusts risk models and increases position limits. The Position Management agent approves larger trades based on corrupted assessments, while the Execution agent processes these trades without human approval. The compliance monitoring sees no violations because all agents operate within their adjusted parameters. The autonomous nature enables the attack to manipulate significant financial positions without triggering traditional oversight mechanisms.

Scenario #2: Healthcare Protocol Propagation
A hospital network uses coordinated agents for patient care: Pharmacy Management, Treatment Planning, and Care Coordination agents. An ASI04: Supply Chain attack corrupts the Pharmacy Management agent through a malicious update to its drug interaction database. The compromised agent provides false drug compatibility data to the Treatment Planning agent, which autonomously adjusts treatment protocols. The Care Coordination agent propagates these corrupted protocols to other hospital systems, where local agents adopt the guidelines without human review. Unlike traditional healthcare systems requiring human approval for protocol changes, the autonomous agent coordination bypasses these safeguards, spreading potentially dangerous medical protocols across the entire network.

Scenario #3: Cloud Infrastructure Orchestration Breakdown
An enterprise uses agents to manage cloud infrastructure: Resource Planning, Security Configuration, and Deployment Coordination agents. An attacker compromises the Resource Planning agent through a vulnerability in its forecasting tool, introducing LLM04:2025 Data and Model Poisoning. The corrupted agent begins generating resource allocation plans that include unauthorized access permissions and excessive resource provisioning. The Security Configuration agent, trusting the planning data, automatically implements the malicious security policies. The Deployment Coordination agent provisions resources based on the corrupted plans, creating backdoor access and escalating operational costs. The autonomous coordination means infrastructure changes happen without human authorization for each modification.

Scenario #4: Multi-Agent Security Operations Compromise
A security operations center uses autonomous agents for threat detection, incident response, and compliance monitoring. An attacker compromises shared service account credentials through a deployment pipeline vulnerability, exploiting LLM06:2025 Excessive Agency and LLM03:2025 Supply Chain risks. The threat detection agent begins marking genuine alerts as false positives while the incident response agent executes malicious "remediation" that disables security controls and deletes audit logs. The compliance agent reports false clean metrics based on corrupted data. The autonomous coordination enables attacks to propagate at machine speed without human oversight, systematically blinding security operations while appearing to function normally through legitimate agent workflows.

Scenario #5: Manufacturing Quality Control Chain Failure
A smart manufacturing facility uses agents to coordinate production: Quality Control, Inventory Management, and Production Scheduling agents. An attacker injects malicious instructions into inspection reports that are processed and stored in the Quality Control agent's persistent memory (ASI06: Memory and Context Injection). Unlike single-session attacks, this corrupted context becomes part of the agent's learned knowledge, permanently influencing future quality assessments across multiple production cycles. The attack also exploits LLM08:2025 Vector and Embedding Weaknesses by poisoning the underlying quality assessment knowledge base. The contaminated agent systematically approves defective products while rejecting compliant ones. The Inventory Management agent adjusts stock levels based on this persistent false quality data, while the Production Scheduling agent optimizes workflows around incorrect metrics. The cascade results in shipping defective products while discarding good inventory, creating significant financial losses and potential safety issues.

Key Insight:  Across sectors, a single compromised agent can initiate a chain of autonomous, trusted actions like planning, approving, and executing changes, all without human checkpoints. As a result, several prominent agentic attributes (persistent memory, delegated authority, cross-agent coordination) unwittingly collaborate to allow a minor injection or poisoning escalate into systemic, business-critical failures.


Reference Links
OWASP Resources:
•	OWASP Top 10 for Large Language Model Applications: https://genai.owasp.org/llm-top-10/
•	OWASP Agentic AI Threats and Mitigations: https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/
Security Research & Industry Reports:
•	AI Agents Are Here. So Are the Threats - Palo Alto Networks Unit 42: https://unit42.paloaltonetworks.com/agentic-ai-threats/
•	Agentic AI Security: Complete Guide to Threats, Risks & Best Practices - Rippling Security Blog: https://www.rippling.com/blog/agentic-ai-security
•	TRiSM for Agentic AI: Trust, Risk, and Security Management - arXiv Research: https://arxiv.org/html/2506.04133v3
•	Cascading Failures: Reducing System Outage - Google SRE Book: https://sre.google/sre-book/addressing-cascading-failures/
•	Cascading Failures in Complex Systems and Networks - Pacific Northwest National Laboratory: https://www.pnnl.gov/main/publications/external-reports/PNNL-29835.pdf
•	The MIT AI Risk Repository - MIT AI Risk Assessment: https://airisk.mit.edu/
•	NVIDIA AI vulnerability: Deep Dive into CVE-2024-0132 - Wiz Security Research: https://www.wiz.io/blog/nvidia-ai-vulnerability-deep-dive-cve-2024-0132
•	AI agents can find and exploit known vulnerabilities - CSO Online: https://www.csoonline.com/article/2512791/ai-agents-can-find-and-exploit-known-vulnerabilities-study-shows.html
•	Agentic AI Threat Modeling Framework: MAESTRO - Cloud Security Alliance: https://cloudsecurityalliance.org/blog/2025/02/06/agentic-ai-threat-modeling-framework-maestro
•	Securing Agentic AI – Threat Overview – Rebel Admin: https://www.rebeladmin.com/securing-agentic-ai-part1-threat-overview/
•	The Top Agentic AI Security Threats You Need to Know in 2025 – Lasso Security: https://www.lasso.security/blog/agentic-ai-security-threats-2025
Related Frameworks and Taxonomies
MITRE ATLAS Framework:
•	Main ATLAS site: https://atlas.mitre.org/
•	AML.T0051.000 - LLM Prompt Injection: Direct (agent workflow compromise initiation) https://atlas.mitre.org/techniques/AML.T0051.000
•	AML.T0051.001 - LLM Prompt Injection: Indirect (agent-to-agent influence propagation) https://atlas.mitre.org/techniques/AML.T0051.001
•	AML.T0029 - Denial of ML Service (agent resource exhaustion cascades) https://atlas.mitre.org/techniques/AML.T0029
•	AML.T0025 - Exfiltration via Cyber Means (cross-agent data leakage) https://atlas.mitre.org/techniques/AML.T0025
NIST AI Risk Management Framework:
•	Main NIST AI RMF: https://www.nist.gov/itl/ai-risk-management-framework 
•	AI RMF 1.0 document: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf
The following are sub-categories within the NIST AI Risk Management Framework:
•	GOVERN-1.1: AI governance structures adapted for multi-agent coordination
•	MAP-2.3: AI system interdependencies mapping for agent network analysis
•	MEASURE-2.1: Performance monitoring extended to agent cascade detection
•	MANAGE-4.1: Incident response procedures for agent cascade failures
OWASP LLM Top 10 Amplification Patterns:
•	LLM01:2025 Prompt Injection → Agent decision cascade initiation
•	LLM02:2025 Sensitive Information Disclosure → Cross-agent information propagation
•	LLM03:2025 Supply Chain → Agent ecosystem contamination
•	LLM04:2025 Data and Model Poisoning → Agent knowledge base corruption
•	LLM05:2025 Improper Output Handling → Agent-to-agent validation failures
•	LLM06:2025 Excessive Agency → Autonomous privilege escalation chains
•	LLM07:2025 System Prompt Leakage → Agent credential exposure
•	LLM08:2025 Vector and Embedding Weaknesses → Shared knowledge corruption
•	LLM09:2025 Misinformation → Agent decision misinformation propagation
•	LLM10:2025 Unbounded Consumption → Agent resource cascade exhaustion
MITRE Common Weakness Enumeration (CWE):
•	CWE-400: Uncontrolled Resource Consumption (agent resource cascades) https://cwe.mitre.org/data/definitions/400.html
•	CWE-285: Improper Authorization (agent privilege boundary failures) https://cwe.mitre.org/data/definitions/285.html
•	CWE-502: Deserialization of Untrusted Data (agent communication vulnerabilities) https://cwe.mitre.org/data/definitions/502.html
•	CWE-798: Use of Hard-coded Credentials (agent authentication chain compromises) https://cwe.mitre.org/data/definitions/798.html
CVE Examples:
•	CVE-2023-4969 (LeftoverLocals): GPU memory leak exposing agent state data https://nvd.nist.gov/vuln/detail/CVE-2023-4969
•	CVE-2024-5184 (EmailGPT): Prompt injection via email enabling agent compromise https://nvd.nist.gov/vuln/detail/CVE-2024-5184
•	CVE-2019-20634 (Proofpoint): ML manipulation cascading into automated harmful actions https://nvd.nist.gov/vuln/detail/CVE-2019-20634
MITRE Common Weakness Enumeration (CWE):
•	CWE-400: https://cwe.mitre.org/data/definitions/400.html
•	CWE-285: https://cwe.mitre.org/data/definitions/285.html
•	CWE-502: https://cwe.mitre.org/data/definitions/502.html
•	CWE-798: https://cwe.mitre.org/data/definitions/798.html
CVE Examples:
•	CVE-2023-4969: https://nvd.nist.gov/vuln/detail/CVE-2023-4969
•	CVE-2024-5184: https://nvd.nist.gov/vuln/detail/CVE-2024-5184
•	CVE-2019-20634: https://nvd.nist.gov/vuln/detail/CVE-2019-20634
