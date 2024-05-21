# OWASP Top 10 for LLMs Mapped to MITRE ATT&CK with Mitigations

This document outlines the potential exploitation of the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) within the context of the [MITRE ATT&CK framework](https://attack.mitre.org/). It identifies relevant tactics and techniques adversaries might use and suggests mitigations to protect against these threats.

## MITRE ATT&CK Tactics, Techniques, and Mitigations for LLM Vulnerabilities

### LLM01: Prompt Injection

- **Tactic**: Execution [(T1059)](https://attack.mitre.org/tactics/TA0002/)
- **Technique**: Command and Scripting Interpreter [(T1059.001)](https://attack.mitre.org/techniques/T1059/001/)
- **Mitigation**: Implement input validation and sanitization. Conduct regular security reviews and training for developers on secure coding practices.

### LLM02: Insecure Output Handling

- **Tactic**: Initial Access [(T1190)](https://attack.mitre.org/tactics/TA0001/)
- **Technique**: Exploit Public-Facing Application [(T1190)](https://attack.mitre.org/techniques/T1190/)
- **Mitigation**: Use content security policies and output encoding to prevent execution of malicious scripts. Regularly update and patch software components.

### LLM03: Training Data Poisoning

- **Tactic**: Persistence [(T1136)](https://attack.mitre.org/tactics/TA0003/)
- **Technique**: Create Account [(T1136)](https://attack.mitre.org/techniques/T1136/)
- **Mitigation**: Secure access to training data. Implement robust data validation and anomaly detection systems to identify and mitigate poisoned data.

### LLM04: Model Denial of Service

- **Tactic**: Impact [(T1485)](https://attack.mitre.org/tactics/TA0040/)
- **Technique**: Data Destruction [(T1485)](https://attack.mitre.org/techniques/T1485/)
- **Mitigation**: Design systems with scalability and fault tolerance in mind. Use rate limiting and monitor workloads to detect and mitigate DoS attacks.

### LLM05: Supply-Chain Vulnerabilities

- **Tactic**: Initial Access [(T1195)](https://attack.mitre.org/tactics/TA0001/)
- **Technique**: Supply Chain Compromise [(T1195)](https://attack.mitre.org/techniques/T1195/)
- **Mitigation**: Conduct security assessments of third-party vendors. Monitor for vulnerabilities in third-party components and apply patches promptly.

### LLM06: Sensitive Information Disclosure

- **Tactic**: Collection [(T1119)](https://attack.mitre.org/tactics/TA0009/)
- **Technique**: Automated Collection [(T1119)](https://attack.mitre.org/techniques/T1119/)
- **Mitigation**: Encrypt sensitive data at rest and in transit. Implement access controls and monitor access logs for unauthorized data access attempts.

### LLM07: Insecure Plugin Design

- **Tactic**: Persistence [(T1176)](https://attack.mitre.org/tactics/TA0003/)
- **Technique**: Browser Extensions [(T1176)](https://attack.mitre.org/techniques/T1176/)
- **Mitigation**: Follow secure development practices for plugins. Conduct security reviews and vulnerability assessments regularly.

### LLM08: Excessive Agency

- **Tactic**: Privilege Escalation [(T1068)](https://attack.mitre.org/tactics/TA0004/)
- **Technique**: Exploitation for Privilege Escalation [(T1068)](https://attack.mitre.org/techniques/T1068/)
- **Mitigation**: Limit LLM decision-making capabilities to those absolutely necessary. Implement oversight and review mechanisms for critical actions.

### LLM09: Overreliance

- **Tactic**: Human-operated (Custom Tactic)
- **Technique**: Misuse of Enterprise Tools (Custom Technique)
- **Mitigation**: Educate users on the limitations and proper use of LLMs. Implement checks and balances to ensure human oversight in decision-making processes.

### LLM10: Model Theft

- **Tactic**: Exfiltration [(T1041)](https://attack.mitre.org/tactics/TA0010/)
- **Technique**: Exfiltration Over C2 Channel [(T1041)](https://attack.mitre.org/techniques/T1041/)
- **Mitigation**: Secure LLM models with strong access controls and encryption. Monitor for unusual access patterns or data exfiltration attempts.

Note: The suggested mitigations are based on general cybersecurity best practices and the specific context of MITRE ATT&CK. Organizations should tailor these mitigations to their specific operational environment and the unique challenges posed by the deployment of LLM technologies.
