### LLM03:2023 - Inadequate Sandboxing

**Description:**  
Inadequate sandboxing occurs when an LLM is not properly isolated when it has access to external resources or sensitive systems. This can lead to potential exploitation, unauthorized access, or unintended actions by the LLM.

**Common Inadequate Sandboxing Vulnerabilities:**
- Insufficient separation of the LLM environment from other critical systems or data stores.
- Allowing the LLM to access sensitive resources without proper restrictions.
- Failing to limit the LLM's capabilities, such as allowing it to perform system-level actions or interact with other processes.

**How to Prevent:**
- Implement proper sandboxing techniques to isolate the LLM environment from other critical systems and resources.
- Restrict the LLM's access to sensitive resources and limit its capabilities to the minimum required for its intended purpose.
- Regularly audit and review the LLM's environment and access controls to ensure that proper isolation is maintained.
- Monitor and log LLM interactions to detect and analyze potential sandboxing issues.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker exploits an LLM's access to a sensitive database by crafting prompts that instruct the LLM to extract and reveal confidential information.

_Scenario #2:_ The LLM is allowed to perform system-level actions, and an attacker manipulates it into executing unauthorized commands on the underlying system.

By understanding and addressing the risks associated with inadequate sandboxing, developers can better protect their LLM implementations and ensure the safety and security of their systems.
