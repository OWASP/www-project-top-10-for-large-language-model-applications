## ASI07 – Insecure Inter-Agent Communication

_Authors: Vasilios Mavroudis, Stefano Amorelli_

**Description**
As multi-agent systems proliferate in enterprise environments, the need for interoperability forces them to rely on diverse communication protocols and frameworks. This creates a dynamic and complex attack surface, defined by three interacting factors: the decentralised system architecture, the varying degrees of agent autonomy and the heterogeneous trust relationships between them. Traditional, perimeter-based security models, which depend on centralised authority and clearly defined trust boundaries, are fundamentally ill-equipped to address this fluid, decentralised threat landscape.
The core issue is that agents make autonomous decisions based on information received from other agents. When communication channels between agents lack proper security controls, whether for authentication, integrity, confidentiality, or authorization, malicious actors can exploit these weaknesses to compromise not just individual agents but entire agent networks.
An Insecure Inter-Agent Communication vulnerability is a flaw that allows an adversary to compromise the confidentiality, integrity, or availability of data exchanged between autonomous agents. This can lead to the interception, manipulation, spoofing, or denial of communications, ultimately causing agents to behave in malicious or unintended ways that subvert the system’s objectives.  

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

**Example Attack Scenarios**

Scenario A: Semantic Injection Through Unencrypted Agent Communications A multi-agent customer service system uses unencrypted HTTP for inter-agent coordination. An attacker intercepts messages and injects hidden semantic instructions that cause agent responses to include promotional content or biased recommendations, manipulating customer interactions while appearing to function normally.

Scenario B: Agent Trust Relationship Poisoning via Message Tampering In a distributed agent trading network, an attacker intercepts and modifies trust assessment messages between agents. By altering reputation scores and reliability indicators in agent communications, the attacker manipulates which agents are trusted for market decisions, ultimately influencing trading behaviors.

Scenario C: Agent Context Confusion Through Communication Replay An attacker captures coordination messages from a previous emergency response agent deployment and replays them during a different incident. The agents, receiving familiar coordination patterns, execute inappropriate response procedures based on outdated situational context, causing resource misallocation.

Scenario D: Agent Goal Manipulation via Protocol Downgrade A multi-agent financial advisory system supports both secure and legacy communication modes. An attacker forces agents to downgrade to unencrypted communication, then injects modified objective functions and risk parameters into agent messages, causing the system to provide financially harmful advice.

Scenario E: Agent Network Mapping Through Routing Manipulation An attacker compromises agent communication routing to redirect coordination messages through their infrastructure. By analyzing agent coordination patterns, delegation relationships, and decision flows, they map the agent network structure and identify high-privilege agents for targeted attacks.

Scenario F: Agent Behavioral Profiling via Communication Metadata An attacker monitors the timing, frequency, and patterns of agent communications in a supply chain management system. Through metadata analysis, they infer operational schedules, supplier relationships, and inventory patterns, enabling targeted supply chain attacks or competitive intelligence gathering.


## Standards and Research
- [MITRE ATLAS - Adversarial Threat Landscape for AI Systems](https://atlas.mitre.org/)
- [NIST AI Risk Management Framework (AI RMF 1.0)](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [Byzantine Fault Tolerance in Distributed Systems (survey)](https://arxiv.org/abs/2205.02572)

## Vulnerability Research
- [Local Model Poisoning Attacks to Byzantine-Robust Federated Learning — USENIX Security 2020](https://www.usenix.org/system/files/sec20summer_fang_prepub.pdf)
- [Manipulating the Byzantine: Optimizing Model Poisoning Attacks and Defenses for Federated Learning — NDSS](https://www.ndss-symposium.org/wp-content/uploads/ndss2021_6C-3_24498_paper.pdf)
- [Resilient Consensus Control for Multi-Agent Systems — MDPI / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10054319/)

## Protocol Documentation
- [Model Context Protocol — Security Best Practices](https://modelcontextprotocol.io/specification/draft/basic/security_best_practices)
- [Agent2Agent Protocol Specification (A2AP) — GitHub](https://github.com/a2ap)
