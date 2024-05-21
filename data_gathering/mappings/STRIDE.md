# OWASP Top 10 for LLMs Mapped to STRIDE

This document maps the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) to the [STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service (DoS), Elevation of Privilege)](https://learn.microsoft.com/en-us/previous-versions/commerce-server/ee823878(v=cs.20)?redirectedfrom=MSDN)  threat model categories. STRIDE helps in identifying and categorizing common security threats into six types: Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, and Elevation of Privileges.

## LLM01: Prompt Injection

- **STRIDE Category**: Spoofing
- **Description**: Prompt injection can allow an attacker to masquerade as a legitimate user, manipulating the LLM to generate desired outputs.

## LLM02: Insecure Output Handling

- **STRIDE Category**: Tampering/Information Disclosure
- **Description**: Insecure handling of outputs can lead to tampering or unintended information disclosure through manipulated outputs.

## LLM03: Training Data Poisoning

- **STRIDE Category**: Tampering
- **Description**: Poisoning the training data can tamper with the model's learning process, affecting its outputs and decision-making capabilities.

## LLM04: Model Denial of Service

- **STRIDE Category**: Denial of Service
- **Description**: Overloading the model with complex inputs or exploiting vulnerabilities to consume resources can deny service to legitimate users.

## LLM05: Supply-Chain Vulnerabilities

- **STRIDE Category**: Tampering
- **Description**: Exploiting vulnerabilities in the supply chain can lead to tampering with the model or its environment.

## LLM06: Sensitive Information Disclosure

- **STRIDE Category**: Information Disclosure
- **Description**: This vulnerability can lead to the unintended release of sensitive or confidential information.

## LLM07: Insecure Plugin Design

- **STRIDE Category**: Tampering/Elevation of Privilege
- **Description**: Insecure plugins can be exploited to tamper with the model or elevate privileges within the system.

## LLM08: Excessive Agency

- **STRIDE Category**: Elevation of Privilege
- **Description**: Giving the model excessive decision-making capabilities could inadvertently elevate its privileges beyond intended limits.

## LLM09: Overreliance

- **STRIDE Category**: Repudiation
- **Description**: Overreliance on LLMs without proper oversight or auditing mechanisms can lead to situations where actions cannot be adequately attributed or denied.

## LLM10: Model Theft

- **STRIDE Category**: Information Disclosure/Tampering
- **Description**: Stealing a model can lead to information disclosure about its training data or algorithms and could allow for tampering with the model itself.

Note: The mappings provided are interpretations based on the nature of each vulnerability and how they might be exploited according to the STRIDE model. This exercise highlights the importance of considering various types of threats when assessing the security of LLMs.
