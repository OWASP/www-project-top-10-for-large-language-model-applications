# OWASP Top 10 for LLMs Mapped to MITRE ATLAS with Mitigations

This document provides a comprehensive mapping of the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) to [MITRE's Adversarial Tactics, Techniques, and Common Knowledge (ATLAS)](https://atlas.mitre.org/) framework. It includes a wide range of tactics and techniques for each vulnerability, along with suggested mitigations based on ATLAS and general cybersecurity best practices.

## LLM01: Prompt Injection

- **ATLAS Techniques**:
  - [T1193 - Spearphishing Attachment](https://atlas.mitre.org/techniques/T1193)
  - [T1059 - Command and Scripting Interpreter](https://atlas.mitre.org/techniques/T1059)
  - [T1140 - Deobfuscate/Decode Files or Information](https://atlas.mitre.org/techniques/T1140)
  - [T1204 - User Execution](https://atlas.mitre.org/techniques/T1204)
- **Mitigations**: Implement robust input validation. Educate users on secure coding practices. Use context-aware filtering. Employ behavior monitoring and anomaly detection.

## LLM02: Insecure Output Handling

- **ATLAS Techniques**:
  - [T1203 - Exploitation for Client Execution](https://atlas.mitre.org/techniques/T1203)
  - [T1021 - Remote Services](https://atlas.mitre.org/techniques/T1021)
  - [T1064 - Scripting](https://atlas.mitre.org/techniques/T1064)
  - [T1559 - Inter-Process Communication](https://atlas.mitre.org/techniques/T1559)
- **Mitigations**: Sanitize outputs. Use output encoding and secure rendering techniques. Monitor for unusual output patterns. Implement output control mechanisms.

## LLM03: Training Data Poisoning

- **ATLAS Techniques**:
  - [T1588 - Obtain Capabilities](https://atlas.mitre.org/techniques/T1588)
  - [T1496 - Resource Hijacking](https://atlas.mitre.org/techniques/T1496)
  - [T1565 - Data Manipulation](https://atlas.mitre.org/techniques/T1565)
  - [T1199 - Trusted Relationship](https://atlas.mitre.org/techniques/T1199)
- **Mitigations**: Validate and sanitize training data. Use anomaly detection. Implement robust access controls. Regularly update and audit data sources.

## LLM04: Model Denial of Service

- **ATLAS Techniques**:
  - [T1499 - Endpoint Denial of Service](https://atlas.mitre.org/techniques/T1499)
  - [T1485 - Data Destruction](https://atlas.mitre.org/techniques/T1485)
  - [T1498 - Network Denial of Service](https://atlas.mitre.org/techniques/T1498)
  - [T1490 - Inhibit System Recovery](https://atlas.mitre.org/techniques/T1490)
- **Mitigations**: Implement rate limiting and computational resource management. Validate inputs to prevent DoS attacks. Employ redundancy and resilient design. Monitor system performance and set up alerts for unusual activity.

## LLM05: Supply-Chain Vulnerabilities

- **ATLAS Techniques**:
  - [T1195 - Supply Chain Compromise](https://atlas.mitre.org/techniques/T1195)
  - [T1190 - Exploit Public-Facing Application](https://atlas.mitre.org/techniques/T1190)
  - [T1185 - Man in the Middle](https://atlas.mitre.org/techniques/T1185)
  - [T1601 - Gather Victim Identity Information](https://atlas.mitre.org/techniques/T1601)
- **Mitigations**: Conduct security audits of third-party components. Use trusted sources and monitor for vulnerabilities. Implement strict access controls and secure communication protocols. Regularly update and patch software components.

## LLM06: Sensitive Information Disclosure

- **ATLAS Techniques**:
  - [T1530 - Data from Information Repositories](https://atlas.mitre.org/techniques/T1530)
  - [T1482 - Domain Trust Discovery](https://atlas.mitre.org/techniques/T1482)
  - [T1497 - Virtualization/Sandbox Evasion](https://atlas.mitre.org/techniques/T1497)
  - [T1564 - Hide Artifacts](https://atlas.mitre.org/techniques/T1564)
- **Mitigations**: Implement access controls and encrypt data. Monitor data access patterns for unusual activities. Employ data loss prevention techniques. Regularly audit data storage and transmission security.

## LLM07: Insecure Plugin Design

- **ATLAS Techniques**:
  - [T1211 - Exploitation for Defense Evasion](https://atlas.mitre.org/techniques/T1211)
  - [T1553 - Subvert Trust Controls](https://atlas.mitre.org/techniques/T1553)
  - [T1555 - Credentials from Password Stores](https://atlas.mitre.org/techniques/T1555)
  - [T1574 - Hijack Execution Flow](https://atlas.mitre.org/techniques/T1574)
- **Mitigations**: Follow secure design principles for plugins. Audit and review plugin code regularly. Use code signing and integrity verification. Educate developers about secure plugin development practices.

## LLM08: Excessive Agency

- **ATLAS Techniques**:
  - [T1562 - Impair Defenses](https://atlas.mitre.org/techniques/T1562)
  - [T1548 - Abuse Elevation Control Mechanism](https://atlas.mitre.org/techniques/T1548)
  - [T1550 - Use Alternate Authentication Material](https://atlas.mitre.org/techniques/T1550)
  - [T1556 - Modify Authentication Process](https://atlas.mitre.org/techniques/T1556)
- **Mitigations**: Limit LLM decision-making capabilities. Implement oversight mechanisms for actions suggested by LLMs. Regularly review and update access control policies. Conduct regular security audits and risk assessments.

## LLM09: Overreliance

- **ATLAS Techniques**:
  - [T1608 - Stage Capabilities](https://atlas.mitre.org/techniques/T1608)
  - [T1558 - Steal or Forge Kerberos Tickets](https://atlas.mitre.org/techniques/T1558)
  - [T1525 - Implant Internal Image](https://atlas.mitre.org/techniques/T1525)
- **Mitigations**: Educate stakeholders on LLM capabilities and limitations. Develop policies for responsible use and implement oversight mechanisms. Conduct regular training and awareness programs. Implement fail-safes and manual oversight where necessary.

## LLM10: Model Theft

- **ATLAS Techniques**:
  - [T1602 - Data Encrypted for Impact](https://atlas.mitre.org/techniques/T1602)
  - [T1531 - Account Access Removal](https://atlas.mitre.org/techniques/T1531)
  - [T1583 - Acquire Infrastructure](https://atlas.mitre.org/techniques/T1583)
  - [T1586 - Compromise Accounts](https://atlas.mitre.org/techniques/T1586)
- **Mitigations**: Encrypt model data and use access controls. Implement secure storage and transmission practices. Regularly audit and monitor access to model data. Educate employees on phishing and social engineering tactics.

Note: The mappings and mitigations are approximations and should be adapted to specific contexts and evolving cybersecurity landscapes. For a comprehensive understanding of tactics, techniques, and mitigations, consult the [MITRE ATLAS documentation](https://atlas.mitre.org/).
