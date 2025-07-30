## Risk/Vuln Name  
**IAM_Misconfiguration**

**Author(s):**  
Javier Dominguez

### Description  
IAM misconfiguration refers to assigning incorrect or inadequate settings to an agent within an identity and access management system, resulting in unintended access rights or exposures. This violates the principle of least privilege by allowing agents more access than necessary, increasing the risk that they may access sensitive data or perform unauthorized actions.

**This complements ASI03 Privilege compromise**, as that item defines how the vulnerability defined here can be exploited.


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



### Reference Links  
