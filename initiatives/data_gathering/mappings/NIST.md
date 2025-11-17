# OWASP Top 10 for LLMs Mapped to the NIST Cybersecurity Framework

This document aligns the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/#) with the [NIST Cybersecurity Framework's five core functions](https://www.nist.gov/cyberframework): Identify, Protect, Detect, Respond, and Recover. It suggests actions and considerations for addressing these vulnerabilities within the framework's structure.

## LLM01: Prompt Injection

- **Identify**: Recognize potential sources and impacts of prompt injection attacks.
- **Protect**: Implement [input validation and sanitization](https://owasp.org/www-community/controls/Input_Validation) to prevent malicious prompt injections.
- **Detect**: Monitor system logs and outputs for anomalies indicative of prompt injection.
- **Respond**: Establish procedures to isolate and mitigate the impact of a detected prompt injection attack.
- **Recover**: Implement measures to restore any corrupted data or systems affected by prompt injection.

## LLM02: Insecure Output Handling

- **Identify**: Assess output handling processes for vulnerabilities.
- **Protect**: Utilize [output encoding](https://cheatsheetseries.owasp.org/cheatsheets/Output_Encoding_Cheat_Sheet.html) and implement content security policies.
- **Detect**: Use tools to detect instances of insecure output handling or its consequences.
- **Respond**: Follow a response plan to address and mitigate any damages caused by insecure output handling.
- **Recover**: Restore systems and data integrity following an incident involving insecure output handling.

## LLM03: Training Data Poisoning

- **Identify**: Catalog and assess the sources of training data for integrity and security.
- **Protect**: Secure the data supply chain and implement [data validation and filtering](https://owasp.org/www-community/controls/Data_Validation).
- **Detect**: Employ anomaly detection to identify unusual data patterns or inputs.
- **Respond**: Take corrective action to remove poisoned data and adjust model training processes.
- **Recover**: Re-train models with clean, validated data sets.

## LLM04: Model Denial of Service

- **Identify**: Evaluate the model and infrastructure for vulnerabilities that could lead to denial of service.
- **Protect**: Implement [rate limiting](https://owasp.org/www-community/controls/Rate_limiting) and resource management controls.
- **Detect**: Monitor for unusual traffic patterns or resource utilization spikes.
- **Respond**: Activate a response plan to mitigate and isolate the denial of service attacks.
- **Recover**: Restore normal operations and service levels.

## LLM05: Supply-Chain Vulnerabilities

- **Identify**: Map out and review the security of the supply chain components.
- **Protect**: Ensure secure software development practices and [third-party component validation](https://owasp.org/www-community/controls/Software_Composition_Analysis).
- **Detect**: Monitor for vulnerabilities or incidents related to supply chain components.
- **Respond**: React to supply chain threats or breaches with a coordinated strategy.
- **Recover**: Address and remediate any supply chain related vulnerabilities or compromises.

## LLM06: Sensitive Information Disclosure

- **Identify**: Understand the types of sensitive information the model may access or generate.
- **Protect**: Apply [data encryption](https://owasp.org/www-community/controls/Encryption_at_Rest), access controls, and [privacy-enhancing technologies](https://www.nist.gov/privacy-framework).
- **Detect**: Use [data loss prevention (DLP) tools](https://www.nist.gov/cyberframework/cybersecurity-framework-functions/detect) to monitor for unauthorized information disclosure.
- **Respond**: Execute response plans for unauthorized disclosure incidents.
- **Recover**: Take steps to mitigate the impact of the disclosure and prevent recurrence.

## LLM07: Insecure Plugin Design

- **Identify**: Assess plugins for security risks and design flaws.
- **Protect**: Adopt [secure plugin development and review practices](https://owasp.org/www-community/controls/Secure_Coding).
- **Detect**: Implement monitoring for exploits targeting plugin vulnerabilities.
- **Respond**: Prepare to quickly address and patch discovered plugin vulnerabilities.
- **Recover**: Recover from plugin-related security incidents by restoring affected systems and data.

## LLM08: Excessive Agency

- **Identify**: Define appropriate levels of autonomy and agency for LLMs.
- **Protect**: Limit LLM capabilities to those necessary for their intended functions.
- **Detect**: Monitor for actions indicating excessive agency or unauthorized activities.
- **Respond**: Respond to incidents where LLMs exceed their defined agency limits.
- **Recover**: Adjust LLM configurations and capabilities to prevent future occurrences.

## LLM09: Overreliance

- **Identify**: Recognize dependencies on LLMs and potential risks of overreliance.
- **Protect**: Develop policies to ensure balanced use of LLMs within operational processes.
- **Detect**: Observe for signs of overreliance impacting decision-making or performance.
- **Respond**: Address instances of overreliance through training and process adjustment.
- **Recover**: Implement strategies to reduce reliance on LLMs where inappropriate.

## LLM10: Model Theft

- **Identify**: Understand the value and sensitivity of the model and its data.
- **Protect**: Secure models with [encryption and access controls](https://owasp.org/www-community/controls/Access_Control_Cheat_Sheet).
