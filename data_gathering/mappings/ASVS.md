# OWASP Top 10 for LLMs Mapped to ASVS

This document outlines how the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) can be addressed through the [Application Security Verification Standard (ASVS)](https://owasp.org/www-project-application-security-verification-standard/) by OWASP. While ASVS is tailored towards web applications, its principles can guide the security of web services and applications utilizing LLMs.

## ASVS Requirements and LLM Vulnerabilities

Each LLM vulnerability is mapped to relevant ASVS requirements that can help mitigate associated risks:

### LLM01: Prompt Injection

- **V5: Validation, Sanitization, and Encoding**
  - Apply strict input validation and sanitization to prevent malicious or unexpected input from affecting LLM outputs.

### LLM02: Insecure Output Handling

- **V5: Validation, Sanitization, and Encoding**
  - Ensure all outputs are encoded and handled securely to prevent injection attacks or information disclosure.

### LLM03: Training Data Poisoning

- **V7: Cryptography**
  - Secure the integrity of training data through encryption and integrity checks to mitigate risks of data poisoning.

### LLM04: Model Denial of Service

- **V11: Business Logic Verification**
  - Implement controls to prevent abuse of LLM features that could lead to denial of service, such as rate limiting and resource management.

### LLM05: Supply-Chain Vulnerabilities

- **V12: File and Resources Verification**
  - Verify the security of third-party libraries and dependencies to address supply-chain vulnerabilities.

### LLM06: Sensitive Information Disclosure

- **V9: Data Protection**
  - Protect sensitive data processed by LLMs through encryption, access controls, and data leakage prevention techniques.

### LLM07: Insecure Plugin Design

- **V14: Configuration Verification**
  - Ensure plugins or extensions for LLMs are securely designed and do not introduce vulnerabilities.

### LLM08: Excessive Agency

- **V13: API and Web Service Verification**
  - Design APIs interacting with LLMs to limit excessive agency and ensure secure communication.

### LLM09: Overreliance

- **V1: Architecture, Design, and Threat Modeling**
  - Conduct threat modeling to identify and mitigate risks associated with overreliance on LLM technologies.

### LLM10: Model Theft

- **V9: Data Protection**
  - Implement measures to protect LLM models as sensitive intellectual property, including access control and encryption.

**Note:** The ASVS mapping provides a framework for addressing LLM vulnerabilities within web applications and services. It is important to tailor the implementation of these ASVS requirements to the specific context and architecture of applications utilizing LLM technologies.
