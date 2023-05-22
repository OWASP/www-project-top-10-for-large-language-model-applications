### LLM05:2023 - SSRF Vulnerabilities

**Description:**  
Server-side Request Forgery (SSRF) vulnerabilities occur when an attacker exploits an LLM to perform unintended requests or access restricted resources, such as internal services, APIs, or data stores.

**Common SSRF Vulnerabilities:**
- Insufficient input validation, allowing attackers to manipulate LLM prompts to initiate unauthorized requests.
- Inadequate sandboxing or resource restrictions, enabling the LLM to access restricted resources or interact with internal services.
- Misconfigurations in network or application security settings, exposing internal resources to the LLM.

**How to Prevent:**
- Implement rigorous input validation and sanitization to prevent malicious or unexpected prompts from initiating unauthorized requests.
- Enforce proper sandboxing and restrict the LLM's access to network resources, internal services, and APIs.
- Regularly audit and review network and application security settings to ensure that internal resources are not inadvertently exposed to the LLM.
- Monitor and log LLM interactions to detect and analyze potential SSRF vulnerabilities.

**Example Attack Scenarios:**
_Scenario #1:_ An attacker crafts a prompt that instructs the LLM to make a request to an internal service, bypassing access controls and gaining unauthorized access to sensitive information.

_Scenario #2:_ A misconfiguration in the application's security settings allows the LLM to interact with a restricted API, and an attacker manipulates the LLM to access or modify sensitive data.

By understanding and addressing the risks associated with SSRF vulnerabilities, developers can better protect their LLM implementations and ensure the safety and security of their systems.
