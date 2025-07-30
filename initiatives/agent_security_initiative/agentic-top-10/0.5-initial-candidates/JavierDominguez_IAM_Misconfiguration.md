## Risk/Vuln Name  
**Over-permissioning**

**Author(s):**  
Javier Dominguez

### Description  
Over-permissioning refers to assigning more permissions than necessary to an agent within an identity and access management system, resulting in unintended access rights or exposures. This violates the principle of least privilege by allowing agents more access than necessary, increasing the risk that they may access sensitive data or perform unauthorized actions.

**This complements ASI03 Privilege compromise**, as that item defines how the vulnerability defined here can be exploited.

The threat is partially covered by [LLM06:2025 Excessive Agency](https://genai.owasp.org/llmrisk/llm062025-excessive-agency/)



### Common Examples of Risk  
1. Unauthorized privilege escalation to assume roles the agent is not supposed to.
2. Lateral movement to different environments.
3. Unauthorized resource creation, leading to creation of backdoors in the system.
4. Data exfiltration, if the agent has access to sensitive data.

### Prevention and Mitigation Strategies  
1. **Assign granular privileges to the agent** only to the services needed, using the least privilege principle.  
2. **Implement network isolation** to prevent a rogue agent from accessing other systems.
3. **Implement guardrails** to ensure the agents operates within defined boundaries.
4. **Implementing continuous monitoring and auditing** of agent activities and access patterns to detect and respond to unusual or unauthorized use.


### Example Attack Scenarios  

- **Scenario 1: Access to sensitive information ** – An agent aimed to analyse logs in an application is given full read permission, and can access any single log in the system.
- **Scenario 2: Data exfiltration ** – An agent is given root access in the system, and is tricked to return the internal secrets, as passwords or keys.
- **Scenario 3: Create backlog ** – An agent is given write access in the system, and is tricked to create a backdoor to get remote access into the system.



### Reference Links  
1. [Agentic AI - Threats and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)
2. [LLM06:2025 Excessive Agency](https://genai.owasp.org/llm-top-10/LLM06-excessive-agency)
3. [The 'Root Permissions' Problem: Why Agentic AI Poses Unique Data Security Risks] (https://www.rsaconference.com/library/blog/the-root-permissions-problem-why-agentic-ai-poses-unique-data-security-risks)
4. [Hacker Plants Computer 'Wiping' Commands in Amazon's AI Coding Agent](https://www.404media.co/hacker-plants-computer-wiping-commands-in-amazons-ai-coding-agent/)
