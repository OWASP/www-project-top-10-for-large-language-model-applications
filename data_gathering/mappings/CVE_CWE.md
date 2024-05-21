# Mapping OWASP Top 10 for LLMs to CVEs and CWEs

This document maps the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) to related Common Vulnerabilities and Exposures ([CVEs](https://cve.mitre.org/)) and Common Weakness Enumeration ([CWEs](https://cwe.mitre.org/)). Given the novel nature of LLMs, direct CVE matches were not found at this stage, but relevant CWEs can provide insights into the types of weaknesses these vulnerabilities may exploit.

## LLM01: Prompt Injection

- **[CWE-77](https://cwe.mitre.org/data/definitions/77.html)**: Improper Neutralization of Special Elements used in a Command ('Command Injection')
- **[CWE-94](https://cwe.mitre.org/data/definitions/94.html)**: Improper Control of Generation of Code ('Code Injection')

## LLM02: Insecure Output Handling

- **[CWE-79](https://cwe.mitre.org/data/definitions/79.html)**: Improper Neutralization of Input During Web Page Generation ('Cross-site Scripting')
- **[CWE-116](https://cwe.mitre.org/data/definitions/116.html)**: Improper Encoding or Escaping of Output

## LLM03: Training Data Poisoning

- **[CWE-506](https://cwe.mitre.org/data/definitions/506.html)**: Embedded Malicious Code
- **[CWE-915](https://cwe.mitre.org/data/definitions/915.html)**: Improperly Controlled Modification of Dynamically-Determined Object Attributes

## LLM04: Model Denial of Service

- **[CWE-400](https://cwe.mitre.org/data/definitions/400.html)**: Uncontrolled Resource Consumption

## LLM05: Supply-Chain Vulnerabilities

- **[CWE-829](https://cwe.mitre.org/data/definitions/829.html)**: Inclusion of Functionality from Untrusted Control Sphere
- **[CWE-937](https://cwe.mitre.org/data/definitions/937.html)**: Using Components with Known Vulnerabilities

## LLM06: Sensitive Information Disclosure

- **[CWE-200](https://cwe.mitre.org/data/definitions/200.html)**: Exposure of Sensitive Information to an Unauthorized Actor

## LLM07: Insecure Plugin Design

- **[CWE-749](https://cwe.mitre.org/data/definitions/749.html)**: Exposed Dangerous Method or Function
- **[CWE-1203](https://cwe.mitre.org/data/definitions/1203.html)**: Insecure Direct Object References

## LLM08: Excessive Agency

- **[CWE-807](https://cwe.mitre.org/data/definitions/807.html)**: Reliance on Untrusted Inputs in a Security Decision
- No direct CVE mapping available.

## LLM09: Overreliance

- **[CWE-1048](https://cwe.mitre.org/data/definitions/1048.html)**: Software Reliance on Single Factor Authentication in a Security Decision
- No direct CVE mapping available.

## LLM10: Model Theft

- **[CWE-494](https://cwe.mitre.org/data/definitions/494.html)**: Download of Code Without Integrity Check
- **[CWE-1241](https://cwe.mitre.org/data/definitions/1241.html)**: Improper Protection of Sensitive Information During Manufacturing or Distribution

Note: Identifying specific CVE entries for LLM vulnerabilities is challenging due to the specificity of CVEs to software products or systems. However, the listed CWE entries provide a framework for understanding the types of weaknesses these vulnerabilities might exploit.
