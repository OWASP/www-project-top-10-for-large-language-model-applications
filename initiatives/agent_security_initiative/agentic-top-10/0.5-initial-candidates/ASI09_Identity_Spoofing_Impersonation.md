## Risk/Vuln Name
**Identity Spoofing & Impersonation**

**Author(s):**
OWASP Agentic Security Initiative Team

### Description
Agentic AI systems often operate on behalf of users or services. Attackers can exploit weak identity controls to impersonate agents, users, or systems—gaining unauthorized access, issuing actions, or spreading misinformation. In multi-agent ecosystems, spoofed agents can embed into workflows and manipulate decision-making.


### Common Examples of Risk
1. Forged identity tokens or agent headers in inter-agent communications.
2. Overloaded prompt parameters that mimic system commands or roles.
3. Use of impersonated agents to replay trusted behavior in workflows.
4. Unsigned messages or tool invocations from unverifiable sources.

### Prevention and Mitigation Strategies
1. Require signed identities and verifiable tokens for agent communication.
2. Implement strong origin verification for delegated or recalled tasks.
3. Use trust scores and behavior fingerprinting to detect impersonation.
4. Track agent lineage and identity context across memory and sessions.
5. Apply least-privilege rules to identity scopes and revocation policies.
6. Log anomalies in communication patterns or impersonation attempts.
7. Segregate user, agent, and service identities with cryptographic proofs.

### Example Attack Scenarios
- **Scenario 1: Agent Impersonation** – A malicious actor injects a rogue agent into a multi-agent team by mimicking the headers and metadata of a trusted planning agent.
- **Scenario 2: Spoofed Delegation** – An attacker crafts a forged memory recall message that impersonates an admin agent, triggering unsafe downstream execution.
- **Scenario 3: Reflection Spoofing** – A reflection prompt embedded in agent memory is rewritten to impersonate a system instruction, triggering elevated tool access.
- **Scenario 4: Shared Identity Overlap** – Two agents operate under a shared identity, and an attacker uses timing manipulation to exploit the identity ambiguity and inject actions.

### Reference Links
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)