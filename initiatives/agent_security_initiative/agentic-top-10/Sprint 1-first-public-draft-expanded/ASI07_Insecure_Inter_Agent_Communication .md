## ASI07: Insecure Inter-Agent Communication

**Description**

Multi agent systems depend on continuous communication between autonomous agents that coordinate via APIs, message buses, and shared memory, significantly expanding the attack surface. Decentralized architecture, varying autonomy, and uneven trust make perimeter-based security models ineffective. Weak inter-agent controls for authentication, integrity, confidentiality, or authorization let attackers intercept, manipulate, spoof, or block messages.

Insecure Inter-Agent Communication occurs when these exchanges lack proper authentication, integrity, or semantic validation-allowing interception, spoofing, or manipulation of agent messages and intents. The threat spans transport, routing, discovery, and semantic layers, including covert or side-channels where agents leak or infer data through timing or behavioral cues.

This differs from ASI03 (Identity & Privilege Abuse), which focuses on credential and permissions misuse, and ASI06 (Memory & Context Poisoning), which targets stored knowledge corruption. ASI07 focuses on compromising real-time messages between agents, leading to misinformation, privilege confusion, or coordinated manipulation across distributed agentic systems.

The entry is covered by T12 – Agent Communication Poisoning & T16 – Insecure Inter-Agent Protocol Abuse in Agentic Threats and Mitigations

**Common Examples of the Vulnerability**

1. Unencrypted and channels enabling semantic manipulation: MITM intercepts unencrypted messages and injects hidden instructions altering agent goals and decision logic.
2. Message tampering leading to cross-context contamination: Modified or injected messages blur task boundaries between agents, leading to data leakage or goal confusion during coordination.
3. Replay on trust chains: Replayed delegation or trust messages trick agents into granting access or honoring stale instructions.
4. Protocol downgrade and descriptor forgery, causing authority confusion: Attackers coerce agents into weaker communication modes or spoof agent descriptors, making malicious commands appear as valid exchanges.
5. Message-routing attacks on discovery and coordination: Misdirected discovery traffic forges relationships with malicious agents or unauthorized coordinators.
6. Metadata analysis for behavioral profiling: Traffic patterns reveal decision cycles and relationships, enabling prediction and manipulation of agent behavior.

**Example Attack Scenarios**

1. Semantic injection via unencrypted communications: Over HTTP or other unauthenticated channels, a MITM attacker injects hidden instructions, causing agents to produce biased or malicious results while appearing normal.
2. Trust poisoning via message tampering: In an agentic trading network, altered reputation messages skew which agents are trusted for decisions.
3. Context confusion via replay: Replayed emergency coordination messages trigger outdated procedures and resource misallocation.
4. Goal manipulation via protocol downgrade: Forced legacy, unencrypted mode lets attackers inject objectives and risk parameters, producing harmful advice.
5. Agent-in-the-Middle via MCP descriptor poisoning: A malicious MCP endpoint advertises spoofed agent descriptors or false capabilities. When trusted, it routes sensitive data through attacker infrastructure.
6. A2A registration spoofing: An attacker registers a fake peer agent in the discovery service using a cloned schema, intercepting privileged coordination traffic.
7. Semantics split-brain: A single instruction is parsed into divergent intents by different agents, producing conflicting but seemingly legitimate actions.

**Prevention and Mitigation Guidelines**

1. Secure agent channels: Use end-to-end encryption with per-agent credentials and mutual authentication. Enforce PKI certificate pinning, forward secrecy, and regular protocol reviews to prevent interception or spoofing.
2. Message integrity and semantic protection: Digitally sign messages, hash both payload and context, and validate for hidden or modified natural-language instructions. Apply natural-language–aware sanitization and intent-diffing to detect goal, parameter tampering, hidden or modified natural-language instructions
3. Agent-aware anti-replay: Protect all exchanges with nonces, session identifiers, and timestamps tied to task windows. Maintain short-term message fingerprints or state hashes to detect cross-context replays.
4. Protocol and capability security: Disable weak or legacy communication modes. Require agent-specific trust negotiation and bind protocol authentication to agent identity. Enforce version and capability policies at gateways or middleware.
5. Limit metadata-based inference: Reduce the attack surface for traffic analysis by using fixed-size or padded messages where feasible, smoothing communication rates, and avoiding deterministic communication schedules. These lightweight measures make it harder for attackers to infer agent roles or decision cycles from metadata alone, without requiring heavy protocol redesign.
6. Protocol pinning and version enforcement: Define and enforce allowed protocol versions (e.g., MCP, A2A, gRPC). Reject downgrade attempts or unrecognized schemas and validate that both peers advertise matching capability and version fingerprints.
7. Discovery and routing protection. Authenticate all discovery and coordination messages using cryptographic identity. Secure directories with access controls and verified reputations, validate identity and intent end-to-end, and monitor for anomalous routing flows.
8. Attested registry and agent verification: Use registries or marketplaces that provide digital attestation of agent identity, provenance, and descriptor integrity. Require signed agent cards and continuous verification before accepting discovery or coordination messages. Leverage the PKI trusted root certificate registries to enable robust agent verification and attestation of critical attributes.
9. Typed contracts and schema validation: Use versioned, typed message schemas with explicit per-message audiences. Reject messages that fail validation or attempt schema down-conversion without declared compatibility. Typed contracts help with structure, but semantic divergence across agents remains an inherent challenge; mitigations therefore focus on integrity, provenance, and controlled communication patterns rather than attempting full semantic alignment.

**References**

1. [Local Model Poisoning Attacks to Byzantine-Robust Federated Learning - USENIX Security 2020](https://www.usenix.org/system/files/sec20summer_fang_prepub.pdf)
2. [Manipulating the Byzantine: Optimizing Model Poisoning Attacks and Defenses for Federated Learning - NDSS](https://www.ndss-symposium.org/wp-content/uploads/ndss2021_6C-3_24498_paper.pdf)
3. [Resilient Consensus Control for Multi-Agent Systems - MDPI / PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10054319/)
