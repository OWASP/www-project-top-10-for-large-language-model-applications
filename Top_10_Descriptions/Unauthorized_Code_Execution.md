### LLM04:2023 - Unauthorized Code Execution

**Description:**  
Unauthorized code execution occurs when an attacker exploits an LLM to execute malicious code, commands, or actions on the underlying system through natural language prompts.

**Common Unauthorized Code Execution Vulnerabilities:**
- Failing to sanitize or restrict user input, allowing attackers to craft prompts that trigger the execution of unauthorized code.
- Inadequate sandboxing or insufficient restrictions on the LLM's capabilities, allowing it to interact with the underlying system in unintended ways.
- Unintentionally exposing system-level functionality or interfaces to the LLM.

**How to Prevent:**
- Implement strict input validation and sanitization processes to prevent malicious or unexpected prompts from being processed by the LLM.
- Ensure proper sandboxing and restrict the LLM's capabilities to limit its ability to interact with the underlying system.
- Regularly audit and review the LLM's environment and access controls to ensure that unauthorized actions are not possible.
- Monitor and log LLM interactions to detect and analyze potential unauthorized code execution issues.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that instructs the LLM to execute a command that launches a reverse shell on the underlying system, granting the attacker unauthorized access.

_Scenario #2:_ The LLM is unintentionally allowed to interact with a system-level API, and an attacker manipulates the LLM into executing unauthorized actions on the system.

By understanding and addressing the risks associated with unauthorized code execution, developers can better protect their LLM implementations and ensure the safety and security of their systems.
