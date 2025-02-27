# OWASP Top 10 for LLMs Mapped to OPENCRE

This document outlines a mapping of the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) to cybersecurity practices and controls that are aligned with the [Open Control Requirement Enumeration (OPENCRE)](https://www.opencre.org/). OPENCRE serves as a bridge between various cybersecurity frameworks, enabling the application of a harmonized set of controls to address specific vulnerabilities.

## OPENCRE-Aligned Cybersecurity Practices

For each LLM vulnerability, relevant cybersecurity practices that are commonly recognized across multiple frameworks aggregated by OPENCRE are suggested:

### LLM01: Prompt Injection

- **Control Implementation**: Implement input validation and encoding controls to prevent malicious input from affecting LLM outputs. This practice is universally recognized across cybersecurity frameworks for mitigating injection vulnerabilities.

### LLM02: Insecure Output Handling

- **Data Protection**: Apply secure coding practices to sanitize and properly handle all outputs, preventing data leaks or exposure. Encryption and proper error handling are key components.

### LLM03: Training Data Poisoning

- **Data Integrity and Supply Chain Security**: Ensure the integrity of training data through validation, checksums, and secure supply chain practices. Regular audits and supplier assessments can mitigate risks of poisoning.

### LLM04: Model Denial of Service

- **Availability and Performance Management**: Implement rate limiting, resource allocation, and performance monitoring controls to protect against denial of service attacks, ensuring availability.

### LLM05: Supply-Chain Vulnerabilities

- **Third-Party Risk Management**: Conduct thorough security assessments of third-party vendors and integrate continuous monitoring of supply chain security to address vulnerabilities.

### LLM06: Sensitive Information Disclosure

- **Privacy and Data Protection**: Enhance data protection measures, including encryption and access controls, to safeguard sensitive information against unauthorized disclosure.

### LLM07: Insecure Plugin Design

- **Secure Development Lifecycle**: Integrate security into the plugin development lifecycle, including threat modeling, code review, and security testing, to ensure plugins are securely designed and implemented.

### LLM08: Excessive Agency

- **Ethical AI and Decision Management**: Establish guidelines and controls for ethical AI use, ensuring LLMs do not exceed their intended decision-making capabilities. Regular reviews and audits can ensure compliance.

### LLM09: Overreliance

- **Awareness and Training**: Develop and deliver training programs to educate users on the limitations of LLMs, promoting balanced reliance on technology with human oversight.

### LLM10: Model Theft

- **Intellectual Property Protection and Access Control**: Secure LLM models as intellectual property, implementing strong access controls and encryption to prevent unauthorized access and theft.

Note: The application of OPENCRE-aligned cybersecurity practices requires a comprehensive understanding of the organization's cybersecurity posture and the specific risks associated with LLM technologies. Organizations are encouraged to leverage OPENCRE's mapping capabilities to identify and implement the most relevant controls from various cybersecurity frameworks to address these vulnerabilities effectively.
