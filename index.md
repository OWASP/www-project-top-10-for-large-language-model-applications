---

layout: col-sidebar
title: OWASP Top 10 for Large Language Model Applications
level: 2
type: documentation
tags: example-tag
pitch: Aims to educate developers, designers, architects, managers, and organizations about the potential security risks when deploying and managing Large Language Models (LLMs)

---

The OWASP Top 10 for Large Language Model Applications project aims to educate developers, designers, architects, managers, and organizations about the potential security risks when deploying and managing Large Language Models (LLMs). The project provides a list of the top 10 most critical vulnerabilities often seen in LLM applications, highlighting their potential impact, ease of exploitation, and prevalence in real-world applications. Examples of vulnerabilities include prompt injections, data leakage, inadequate sandboxing, and unauthorized code execution, among others. The goal is to raise awareness of these vulnerabilities, suggest remediation strategies, and ultimately improve the security posture of LLM applications. This initiative is community-driven and encourages participation and contributions from all interested parties.

Here is an initial draft (version 0.1) Top 10 to drive discussion.

### LLM01:2023 - Prompt Injections
**Description:**  
Bypassing filters or manipulating the LLM using carefully crafted prompts that make the model ignore previous instructions or perform unintended actions.

### LLM02:2023 - Data Leakage
**Description:**  
Accidentally revealing sensitive information, proprietary algorithms, or other confidential details through the LLM's responses.

### LLM03:2023 - Inadequate Sandboxing
**Description:**  
Failing to properly isolate LLMs when they have access to external resources or sensitive systems, allowing for potential exploitation and unauthorized access.

### LLM04:2023 - Unauthorized Code Execution
**Description:**  
Exploiting LLMs to execute malicious code, commands, or actions on the underlying system through natural language prompts.

### LLM05:2023 - SSRF Vulnerabilities
**Description:**  
Exploiting LLMs to perform unintended requests or access restricted resources, such as internal services, APIs, or data stores.

### LLM06:2023 - Overreliance on LLM-generated Content
**Description:**  
Excessive dependence on LLM-generated content without human oversight can result in harmful consequences.

### LLM07:2023 - Inadequate AI Alignment
**Description:**  
Failing to ensure that the LLM's objectives and behavior align with the intended use case, leading to undesired consequences or vulnerabilities.

### LLM08:2023 - Insufficient Access Controls
**Description:**  
Not properly implementing access controls or authentication, allowing unauthorized users to interact with the LLM and potentially exploit vulnerabilities.

### LLM09:2023 - Improper Error Handling
**Description:**  
Exposing error messages or debugging information that could reveal sensitive information, system details, or potential attack vectors.

### LLM10:2023 - Training Data Poisoning
**Description:**  
Maliciously manipulating training data or fine-tuning procedures to introduce vulnerabilities or backdoors into the LLM.