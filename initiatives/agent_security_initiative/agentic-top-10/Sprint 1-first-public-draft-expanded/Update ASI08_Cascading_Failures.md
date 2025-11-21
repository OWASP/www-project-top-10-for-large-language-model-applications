Cascading Failures in Agentic AI
OWASP Agentic Security Initiative Team: ASI08 – Cascading Failures
Authors: Diana Henderson https://www.linkedin.com/in/dianamhenderson/, Neeraj Nagpal

ASI08: Cascading Failures
A single compromised or malfunctioning agent can trigger a chain reaction of failures across interconnected agents, amplifying small errors into systemic, business-critical harm.

Description

Cascading Failures in agentic AI systems occur when a single error, whether a hallucination, malicious input, corrupted tool, or compromised memory, propagates from one AI agent to another, leading to compound failures and system-wide harm. Unlike traditional LLM applications that generate outputs for human review, agentic systems plan, persist, delegate, and act autonomously. These capabilities mean that a minor fault can become a multi-step chain of privileged operations affecting data integrity and confidentiatlity, infrastructure availability, financial transactions, or entire multi-agent ecosystems.  Broadly, this leads to  unintended actions and widespread service failures across networks of connected agents, systems, and workflows.
   
Cascading failures amplify their effect across interconnected agents or systems and chain together vulnerabilities from the OWASP LLM Top 10. For example, LLM01:2025 Prompt Injection combined with LLM06:2025 Excessive Agency can trigger autonomous tool execution that propagates errors through interconnected systems without human intervention. Similarly, LLM04:2025 Data and Model Poisoning affecting an agent's persistent memory can influence decisions across multiple sessions and workflows.

Here are key fundamental differences between agentic cascade and traditional system failures:
1.	Autonomous Decision Propagation: Agents make decisions that directly influence other agents or systems without human validation at each step.
2.	Persistent Erroneous Feedback Loops: Even after fixing bad data after an initial context injection, agents may have already saved partial plans or goals, and those leftover states continue propagating the fail chain, influencing future actions across sessions.
3.	Emergent Runtime Connections: Agents can dynamically link new tools, APIs, or even other agents while the system is running, forming relationships the designers never mapped. A single misstep can quickly spread across this emerging network, turning a small problem into a wide, unpredictable cascade—even when no outside component was originally compromised.


Common Examples of Vulnerability
1.	Planner-Executor Coupling Failures: A compromised or hallucinating planner agent generates unsafe execution steps that are automatically carried out by a downstream executor agent without validation. This can compound mistakes across multiple business processes.  For instance, a planner might hallucinate that "Finance approved mass refunds" and instruct the executor to erroneously process thousands of refund transactions.
2.	Corrupted Agent Memory Triggering Cascades: A single agent’s persistent memory or goal state is corrupted, and as the agent continues planning and delegating tasks, these errors spread to other agents or processes. Even if the initial injection is removed, the corrupted state can drive repeated or amplified failures, creating a cascading chain of harmful actions across the system.
3.	Inter-Agent Communication Poisoning: In multi-agent systems, agents often delegate tasks and trust outputs from other agents. A compromised agent can feed malicious information to downstream agents, causing a chain of failures as poisoned data propagates through the entire system.  For example, an LLM-based agent hallucinates a critical instruction and instructs a maintenance agent to reboot or shutdown services unnecessarily.  Dependent agents receive misleading status info and take improper actions leading to larger outages.
4.	Cascading Tool Misuse and Privilege Escalation: An agent misuses its tool integrations or escalates privileges which allow it to influence multiple other agents or systems.  Any erroneous step can trigger a chain reaction driving downstream agents to act based on unsafe commands or sensitive data, ultimately amplifying the impact across interconnected processes and leading to widespread operational or security failures.
5.	Supply Chain Contamination Triggering Cascades: A compromised agent, tool, or orchestration component not only spreads itself through the network but also influences downstream agents’ decisions. As these agents act on corrupted instructions or data, failures multiply and propagate across the system. A single compromise can therefore trigger a chain reaction, amplifying errors and creating widespread operational or security impacts beyond the initial supply chain breach.
6.	Excessive Trust in Agent Outputs: System designs that assume an agents’ outputs are always reliable, even without conducting independent checks, then allow a single flawed decision to cascade to downstream entities unchecked.
7.	Absence of Oversight and Fail-safes: When system designs are missing feedback loops, kill-switches, or human-in-the-loop controls, they’re prevented from acting on early detection and leveraging containment to mitigate the effects of runaway agent behavior. 


Prevention and Mitigation Strategies
Preventative Controls
1.	Establish Isolation and Trust Boundaries: Define strict boundaries for agents, given their different privilege levels and purposes, by implementing sandboxing, permission limits, network segmentation, API scopes, and agent-to-agent authentication to contain failure propagation.
2.	Implement Memory Integrity Controls for Cascade Prevention: Protect agents’ persistent memory with append-only storage, provenance tracking, and versioned rollback. Add runtime checks on outputs before they reach other agents. This will ensure that if memory is corrupted, it cannot set off a chain reaction, keeping cascading failures contained.
3.	Establish Cascade-Aware Capability Controls: Give agents dynamic, one-time access to tools or APIs instead of permanent elevated permissions. Combine this with runtime checks of their outputs before passing them downstream, so that even if an agent makes a mistake or behaves maliciously, it can’t set off a chain reaction across other agents or systems.
4.	Deploy Independent Policy Enforcement: Separate the planning and execution phases with independent policy engines that verify planner outputs before the executor runs them. This prevents corrupted planning from directly triggering harmful actions.

Detective Controls
1.	Validate Outputs: Implement checkpoints to validate or sanity-check agent outputs before their consumption by downstream agents, possibly using governance agents or human-in-the-loop methods.
2.	Rate Limit and Monitor: Watch agent activity for rapidly propagating commands or unusual behavior that could signal a chain reaction. Automatically throttle or pause agents when suspicious patterns appear. This helps stop a single mistake from snowballing into a larger cascading failure.
3.	Deploy Behavioral Anomaly Detection with Drift Monitoring: Monitor agent decision patterns and tool usage for both immediate problems and gradual deterioration over time. Agents can make decisions that seem reasonable but are inappropriate for the situation.  This requires careful behavioral analysis. Implement continuous monitoring to detect cognitive drift, which is the gradual decline in agent decision quality that builds up through repeated errors, incomplete corrections, or accumulated bad data. Track how consistent agent decisions are over time, how much agent behavior changes from established baselines, and whether agents stay aligned with their intended goals. Early detection of this drift allows for corrective action before degraded reasoning spreads through agent networks, preventing cascades that start from gradual deterioration rather than direct attacks.
   
Continuous Improvement & Verification Controls
1.	Test, Simulate, and Deploy Agent Cascade Circuit Breakers: Before deployment, conduct fault injection, red-teaming, and chaos experiments specifically to observe how errors propagate between agents and across systems. Implement automated validation checkpoints at each agent-to-agent or agent-to-tool handoff to act as circuit breakers. Each agent’s outputs should undergo semantic checks, goal alignment verification, and policy enforcement before being passed downstream. This ensures that a single bad decision cannot trigger a chain reaction, containing potential cascading failures before they amplify.
2.	Implement Fail-Safe Mechanisms: Design agents to reject incoherent or out-of-bounds data and include fail-safe rules to stop or seek confirmation on critical deviations.
3.	Require Multi-Agent Validation: For critical agent decisions, implement "four-eyes approval" systems where a second agent must verify proposed actions before execution. This prevents single points of failure from causing system-wide damage.  By forcing review and agreement across separate agents, a single faulty output gets intercepted before it can propagate through the system and trigger a cascading failure.



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
