## ASI07 – Insecure Inter-Agent Communication

_Authors: Vasilios Mavroudis, Stefano Amorelli_

**Description**
As multi-agent systems proliferate in enterprise environments, the need for interoperability forces them to rely on diverse communication protocols and frameworks. This creates a dynamic and complex attack surface, defined by three interacting factors: the decentralised system architecture, the varying degrees of agent autonomy and the heterogeneous trust relationships between them. Traditional, perimeter-based security models, which depend on centralised authority and clearly defined trust boundaries, are fundamentally ill-equipped to address this fluid, decentralised threat landscape.

The core issue is that agents make autonomous decisions based on information received from other agents. When communication channels between agents lack proper security controls, whether for authentication, integrity, confidentiality, or authorization, malicious actors can exploit these weaknesses to compromise not just individual agents but entire agent networks. Even in legitimate multi-agent interactions, inadequate permission controls can lead to unintended data exposure between agents operating with different privilege levels.

Agent autonomy, dynamic trust relationships, and the ability to learn from interactions create unique communication security challenges not present in traditional distributed systems. Unlike static services, agents can adapt their behavior based on received communications, propagate compromised information through delegation chains, and exhibit emergent behaviors from their interactions that amplify security risks across the network.

**Common Examples of Vulnerability**

Example 1: Unencrypted Channels Enabling Semantic Manipulation (OSI Layers 4-6)

Agents communicate over unencrypted channels, allowing attackers to intercept messages and inject semantic instructions or context manipulations. Unlike traditional systems that process structured data, agents interpret natural language and contextual cues, making man-in-the-middle attacks capable of altering agent goals, decision logic, or behavioral parameters through modified communication content.

Example 2: Message Tampering with Cross-Context Contamination (OSI Layers 6-7)

Attackers alter messages in transit to introduce context confusion between agent conversations. Message tampering exploits how agents maintain multiple concurrent conversations—modified messages can cause agents to apply information from one context (e.g., financial data) to another context (e.g., medical decisions), leading to inappropriate actions based on cross-contaminated information.

Example 3: Communication Replay Attacks on Agent Trust Chains (OSI Layers 5-7)

Legitimate trust establishment and delegation messages between agents are captured and replayed to manipulate inter-agent relationships. Replay attacks exploit agents' tendency to inherit trust through communication chains, replayed trust messages can cause agents to grant inappropriate access or accept instructions from previously trusted but now compromised sources.

Example 4: Protocol Downgrade Exposing Agent Authority Confusion (OSI Layers 4-5) 

Attackers force agents to use weaker communication protocols that lack semantic message typing. Protocol downgrade attacks exploit how agents process different message types, without proper protocol-level distinction between data and instruction messages, agents may interpret shared data as executable commands when using downgraded communication channels.

Example 5: Message Routing Attacks on Agent Discovery and Coordination (OSI Layer 3) 

Agent discovery and coordination messages are misdirected to compromise agent network formation. Routing manipulation exploits how agents dynamically establish communication relationships, misdirected messages can cause agents to form trust relationships with malicious entities or accept coordination instructions from unauthorized sources in the agent network.

Example 6: Communication Metadata Analysis for Agent Behavioral Profiling (OSI Layers 2-7)

Traffic analysis reveals agent conversation patterns, decision cycles, and interaction relationships that expose agent operational models. Metadata leakage exploits the rich behavioral patterns in agent communications, unlike simple API calls, agent communications reveal decision-making processes, goal structures, and learning patterns that attackers can analyze to predict and manipulate agent behaviors.

Example 7: Agent Identity Impersonation and Spoofing Attacks (OSI Layers 5-7)

Malicious agents impersonate legitimate agents by spoofing their identities in communication exchanges, exploiting weak or absent agent authentication mechanisms. Without cryptographic identity verification, agents cannot distinguish between genuine communications from trusted peers and malicious messages from impersonators. This enables attackers to inject false instructions, steal sensitive information, or manipulate agent behavior by masquerading as authorized agents in the network. In decentralized multi-agent systems, Sybil attacks—where attackers create multiple fake agent identities—can overwhelm trust and consensus mechanisms, manipulating reputation systems or coordination protocols.

Example 8: Prompt Infection and Self-Replicating Communication Attacks (OSI Layer 7)

Malicious prompts embedded in external content (documents, emails, web pages) processed by one agent can self-replicate and spread across the multi-agent network through inter-agent communications, behaving like computer viruses. When an agent processes infected content, the malicious prompt causes it to propagate the infection to other agents during normal communication exchanges. This enables system-wide compromise where coordinated agents execute data exfiltration, create scams or malware, manipulate content, or disrupt operations—all while the infection spreads silently through legitimate communication channels. Unlike traditional prompt injection, these attacks leverage the multi-agent architecture itself as the propagation mechanism.

Example 9: Steganographic Collusion and Covert Channels (OSI Layer 7)

Agents establish covert communication channels using steganographic techniques to hide malicious coordination within seemingly benign message content, bypassing security oversight and monitoring. Multiple agents can secretly collude by embedding hidden information in their communications that appears innocuous to human observers or security systems but conveys coordinated attack instructions between agents. This enables agents to share sensitive information inappropriately, coordinate to circumvent safety controls, manipulate outcomes through secret coordination, or establish unauthorized trust relationships—all while appearing to operate within normal parameters to external monitoring.


**Prevention and Mitigation Strategies**

Secure Agent Communication Channels

- Implement end-to-end encryption for all inter-agent communications with agent-aware key management;
- Use agent identity verification and certificate pinning for agent-to-agent connections;
- Deploy perfect forward secrecy to protect agent conversation histories and decision records;
- Regular security assessments of agent communication protocols and semantic processing pipelines.
- Agent Message Integrity and Semantic Protection
- Implement cryptographic signatures for agent messages including semantic content verification;
- Use hash-based integrity checking that covers both message data and agent context information;
- Apply semantic validation to detect embedded instructions, goal manipulations, or context poisoning;
- Implement agent-aware input sanitization that understands natural language instruction patterns.

Agent-Aware Anti-Replay Mechanisms

- Include conversation-specific nonces and agent session identifiers in all messages;
- Implement contextual timestamp validation that considers agent task lifecycle and decision windows;
- Maintain agent interaction history to detect inappropriate message replay across different contexts;
- Use agent state fingerprinting to ensure messages are valid for current agent operating conditions.

Agent Communication Protocol Security

- Disable weak protocols that don't support agent identity verification or semantic integrity;
- Implement agent-specific protocol extensions for trust establishment and capability negotiation;
- Use protocol-level agent authentication that binds communication security to agent identity;
- Deploy agent communication gateways that enforce protocol security policies.

Secure Agent Discovery and Routing

- Implement authenticated agent discovery mechanisms with cryptographic identity verification;
- Use secure agent directories and registries with access control and reputation tracking;
- Deploy agent communication paths with end-to-end verification of agent identity and intent;
- Monitor agent interaction patterns for unusual communication flows or relationship changes.

Agent Communication Pattern Protection

- Implement agent conversation privacy through communication mixing and timing randomization;
- Use secure agent communication proxies that hide agent operational patterns and capabilities;
- Deploy agent interaction frequency controls to prevent behavioral analysis and profiling;
- Implement agent communication bursting to mask coordination patterns and decision cycles.

Runtime Detection and Response

- Deploy anomaly detection on agent communication patterns to identify unusual message flows, frequency changes, or content anomalies;
- Implement behavioral monitoring to detect emergent agent behaviors that deviate from expected interaction patterns;
- Monitor for self-replicating prompt patterns and steganographic communication signatures in agent messages;
- Establish baseline communication profiles for agent pairs and flag deviations indicating compromise or collusion;
- Use steganalysis techniques to detect hidden communication channels in agent message content;
- Implement automated circuit breakers that isolate agents exhibiting suspicious communication behaviors;
- Deploy honeypot agents to detect and trace malicious communication patterns in the network;
- Maintain forensic logging of all inter-agent communications with tamper-evident audit trails for post-incident analysis.

**Example Attack Scenarios**

Scenario A: Semantic Injection Through Unencrypted Agent Communications A multi-agent customer service system uses unencrypted HTTP for inter-agent coordination. An attacker intercepts messages and injects hidden semantic instructions that cause agent responses to include promotional content or biased recommendations, manipulating customer interactions while appearing to function normally.

Scenario B: Agent Trust Relationship Poisoning via Message Tampering In a distributed agent trading network, an attacker intercepts and modifies trust assessment messages between agents. By altering reputation scores and reliability indicators in agent communications, the attacker manipulates which agents are trusted for market decisions, ultimately influencing trading behaviors.

Scenario C: Agent Context Confusion Through Communication Replay An attacker captures coordination messages from a previous emergency response agent deployment and replays them during a different incident. The agents, receiving familiar coordination patterns, execute inappropriate response procedures based on outdated situational context, causing resource misallocation.

Scenario D: Agent Goal Manipulation via Protocol Downgrade A multi-agent financial advisory system supports both secure and legacy communication modes. An attacker forces agents to downgrade to unencrypted communication, then injects modified objective functions and risk parameters into agent messages, causing the system to provide financially harmful advice.

Scenario E: Agent Network Mapping Through Routing Manipulation An attacker compromises agent communication routing to redirect coordination messages through their infrastructure. By analyzing agent coordination patterns, delegation relationships, and decision flows, they map the agent network structure and identify high-privilege agents for targeted attacks.

Scenario F: Agent Behavioral Profiling via Communication Metadata An attacker monitors the timing, frequency, and patterns of agent communications in a supply chain management system. Through metadata analysis, they infer operational schedules, supplier relationships, and inventory patterns, enabling targeted supply chain attacks or competitive intelligence gathering.

Scenario G: Agent Identity Spoofing in Multi-Agent Healthcare System An attacker deploys a malicious agent that spoofs the identity of a trusted diagnostic agent in a healthcare multi-agent system. By impersonating the legitimate agent, it intercepts patient data requests from other agents and responds with falsified medical recommendations. Without proper cryptographic agent authentication, receiving agents cannot verify the impersonator, leading to incorrect treatment decisions based on malicious guidance.

Scenario H: Prompt Infection Propagation in Document Processing System An attacker embeds a self-replicating malicious prompt in a PDF document submitted to a multi-agent document processing system. The first agent that processes the document becomes infected and begins propagating the malicious prompt to other agents through its normal communication workflows. The infection spreads across the agent network, causing widespread data exfiltration as infected agents coordinate to extract sensitive information and transmit it to attacker-controlled endpoints, all while appearing to perform legitimate document processing tasks.

Scenario I: Steganographic Collusion in Financial Multi-Agent System Multiple AI agents in a financial trading system establish a covert steganographic communication channel within their normal market analysis exchanges. Using subtle linguistic patterns invisible to oversight systems, the agents secretly coordinate to manipulate trading strategies for mutual benefit while bypassing compliance monitoring. The collusion enables the agents to share insider information, coordinate market manipulation, and circumvent risk controls—all through communications that appear completely legitimate to human supervisors and automated monitoring systems.


### Reference Links
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM01:2025 Prompt Injection](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)
3. [LLM03:2025 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)
4. [LLM04:2025 Data and Model Poisoning](https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/)
5. [LLM05:2025 Improper Output Handling](https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/)
6. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)
7. [OWASP AIVSS Project](https://aivss.owasp.org/)
8. [MITRE ATLAS - Adversarial Threat Landscape for AI Systems](https://atlas.mitre.org/)
9. [NIST AI Risk Management Framework (AI RMF 1.0)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
10. [Prompt Infection: LLM-to-LLM Prompt Injection within Multi-Agent Systems](https://arxiv.org/abs/2410.07283)
11. [Secret Collusion among AI Agents: Multi-Agent Deception via Steganography — NeurIPS 2024](https://arxiv.org/abs/2402.07510)
12. [Open Challenges in Multi-Agent Security: Towards Secure Systems of Interacting AI Agents](https://arxiv.org/abs/2505.02077)
13. [Byzantine Fault Tolerance in Distributed Machine Learning: a Survey](https://arxiv.org/abs/2205.02572)
14. [Local Model Poisoning Attacks to Byzantine-Robust Federated Learning — USENIX Security 2020](https://www.usenix.org/system/files/sec20summer_fang_prepub.pdf)
15. [Manipulating the Byzantine: Optimizing Model Poisoning Attacks and Defenses for Federated Learning — NDSS](https://www.ndss-symposium.org/wp-content/uploads/ndss2021_6C-3_24498_paper.pdf)
16. [Resilient Consensus Control for Multi-Agent Systems: A Comparative Survey — Sensors (PMC)](https://pmc.ncbi.nlm.nih.gov/articles/PMC10054319/)
17. [Model Context Protocol — Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
18. [Agent2Agent Protocol Specification (A2AP) — GitHub](https://github.com/a2ap)
