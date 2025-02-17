# OWASP Top 10 for LLMs Mapped to CIS (Center for Internet Security) Controls

This document maps the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) to applicable [CIS Controls](https://www.cisecurity.org/controls/), providing guidance on mitigating these vulnerabilities through established cybersecurity best practices.

## LLM01: Prompt Injection

- **CIS Control 5**: [Secure Configuration for Hardware and Software on Mobile Devices, Laptops, Workstations, and Servers](https://www.cisecurity.org/controls/secure-configuration-for-hardware-and-software-on-mobile-devices-laptops-workstations-and-servers/)
  - Ensure systems processing LLM inputs are configured to resist prompt injection attacks through proper security settings and input validation.

## LLM02: Insecure Output Handling

- **CIS Control 6**: [Maintenance, Monitoring, and Analysis of Audit Logs](https://www.cisecurity.org/controls/maintenance-monitoring-and-analysis-of-audit-logs/)
  - Monitor and analyze logs to detect and respond to incidents involving insecure output handling.

## LLM03: Training Data Poisoning

- **CIS Control 13**: [Data Protection](https://www.cisecurity.org/controls/data-protection/)
  - Protect data integrity through regular backups and encryption, ensuring poisoned data can be restored to a secure state.

## LLM04: Model Denial of Service

- **CIS Control 9**: [Limitation and Control of Network Ports, Protocols, and Services](https://www.cisecurity.org/controls/limitation-and-control-of-network-ports-protocols-and-services/)
  - Manage network configurations to minimize the risk of DoS attacks on LLM systems.

## LLM05: Supply-Chain Vulnerabilities

- **CIS Control 15**: [Supply Chain Risk Management](https://www.cisecurity.org/controls/supply-chain-risk-management/)
  - Assess and manage the security risks of software and hardware related to LLMs throughout the supply chain.

## LLM06: Sensitive Information Disclosure

- **CIS Control 13**: [Data Protection](https://www.cisecurity.org/controls/data-protection/)
  - Implement controls to protect sensitive information from unauthorized access and disclosure.

## LLM07: Insecure Plugin Design

- **CIS Control 18**: [Application Software Security](https://www.cisecurity.org/controls/application-software-security/)
  - Ensure secure development, deployment, and maintenance of plugins used by LLMs.

## LLM08: Excessive Agency

- **CIS Control 4**: [Secure Configuration for Hardware and Software on Mobile Devices, Laptops, Workstations, and Servers](https://www.cisecurity.org/controls/secure-configuration-for-hardware-and-software-on-mobile-devices-laptops-workstations-and-servers/)
  - Configure LLMs and related systems to limit excessive operational control and agency.

## LLM09: Overreliance

- **CIS Control 7**: [Email and Web Browser Protections](https://www.cisecurity.org/controls/email-and-web-browser-protections/)
  - While not directly applicable, promoting awareness and safe practices around the use of LLMs can mitigate risks associated with overreliance.

## LLM10: Model Theft

- **CIS Control 13**: [Data Protection](https://www.cisecurity.org/controls/data-protection/)
  - Secure models and associated data against theft with encryption, access controls, and monitoring.

Note: While the CIS Controls provide a comprehensive set of best practices for cybersecurity, the mapping to specific LLM vulnerabilities is intended to highlight applicable areas of focus. Organizations should consider a holistic security strategy that encompasses these controls to effectively mitigate risks associated with the use of LLMs.
