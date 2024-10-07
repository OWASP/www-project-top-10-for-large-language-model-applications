## Unauthorized Access and Entitlement Violations


**Author(s):** [Ken Huang ](https://github.com/kenhuangus)

### Description

Unauthorized Access and Entitlement Violations occur when LLM systems fail to enforce proper access controls and entitlement policies, allowing users or agents to access, modify, or aggregate data beyond their authorized permissions. This risk is amplified by the use of Retrieval Augmented Generation (RAG) techniques, multi-agent architectures, tools use such as Langchain, LlimaIndex, and data aggregation capabilities inherent in LLMs. Improper handling of these features and vulnerbilities in tools and framework can lead to data breaches, privacy violations, and unauthorized actions.

### Common Examples of Risk

1. **Overprivileged RAG Access**: RAG components granted excessive access to external data sources, enabling unauthorized data retrieval or leakage.
2. **Uncontrolled Agent Delegation**: Lack of access control mechanisms for agents within multi-agent architectures, allowing unauthorized agents to perform privileged actions.
3. **Unrestricted Data Aggregation**: Insufficient restrictions on data aggregation capabilities, enabling unauthorized combination or inference of sensitive information.
4. **Insecure Knowledge Base Access**: Inadequate access controls for knowledge bases used by LLMs, allowing unauthorized retrieval or modification of stored data.
5. **Entitlement Policy Bypass**: Flaws in entitlement policy enforcement, enabling users or agents to circumvent intended access restrictions.
6. **Use of Tools or framework**: Flaws in tools or framework used in LLM applications can cause arbitary read of files.

### Prevention and Mitigation Strategies

- **Principle of Least Privilege**: Implement the principle of least privilege for RAG components, agents, and data aggregation capabilities, granting only the minimum necessary access and permissions.
- **Access Control Mechanisms**: Enforce robust access control mechanisms, such as role-based access control (RBAC) or attribute-based access control (ABAC), to manage permissions and entitlements.
-  **Validate tools and framework code**: For tools such as Langchain, LlamaIndex, Ray Server etc, used in LLM applications, make sure the weakness and vulenrbilities in the code is addressed. Refer to supply chain code security as well for the mitigation although this suggestion is specific to access control. 
- **Data Compartmentalization**: Compartmentalize data sources and knowledge bases, ensuring proper isolation and access controls for each component.
- **Entitlement Policy Validation**: Validate and enforce entitlement policies consistently across all LLM components, including RAG, agents, and data aggregation processes.
- **Auditing and Monitoring**: Implement comprehensive auditing and monitoring mechanisms to detect and respond to unauthorized access attempts or policy violations.
- **Secure Knowledge Base Management**: Implement secure practices for managing knowledge bases, including access controls, versioning, and data integrity checks.
- **Privacy-Preserving Techniques**: Explore privacy-preserving techniques, such as differential privacy or secure multi-party computation, to protect sensitive data during aggregation or inference processes.

### Example Attack Scenarios

1. **Unauthorized Knowledge Base Access**: An attacker exploits a vulnerability in the LLM's knowledge base management system, gaining unauthorized access to sensitive data stored in the knowledge base.
2. **Overprivileged RAG Component**: A RAG component is granted excessive permissions, allowing it to retrieve and incorporate sensitive data from external sources into the LLM's output, potentially causing data leaks or privacy violations.
3. **Agent Entitlement Policy Bypass**: An attacker discovers a flaw in the entitlement policy enforcement mechanism, enabling an unauthorized agent to perform privileged actions, such as modifying data or executing unauthorized commands.
4. **Unrestricted Data Aggregation**: An attacker exploits a lack of restrictions on data aggregation capabilities, combining seemingly innocuous data points to infer sensitive information or gain unauthorized insights.
5. **Leverage flaws or weakness in tools**: An attacker can leverage flaws or weakness in tools or framework used in LLM applications to bypass access control. 

### Real-World Examples

1. **OpenAI's GPT-3 Data Leakage**: In 2021, researchers discovered that GPT-3, a large language model developed by OpenAI, had the potential to leak sensitive information from its training data, including personal details, copyrighted text, and code snippets. This highlighted the importance of proper data handling and access controls in LLM systems. ([Source](https://www.pluralsight.com/blog/security-professional/chatgpt-data-breach))
2. **LangChain JS Arbitrary File Read Vulnerability**: In 2024, a researcher discovered an Arbitrary File Read (AFR) vulnerability in LangChain JS library. This vulnerability allows an attacker to read files on the server that they should not be accessing. When combined with Server Side Request Forgery (SSRF), an attacker can exploit SSRF to read arbitrary files on the server and expose sensitive information. ([Source](https://evren.ninja/langchain-afr-vulnerability.html))


### Reference Links

- [Mitigating Security Risks in Retrieval Augmented Generation (RAG) LLM Applications](https://cloudsecurityalliance.org/blog/2023/11/22/mitigating-security-risks-in-retrieval-augmented-generation-rag-llm-applications/)
- [RFI for NIST AI Executive order-Ken Huang-and-Mehdi Bousaidi](https://www.nist.gov/system/files/documents/2024/02/13/ID004-~1.PDF)
- [RAG is everywhere but where is security?](https://www.linkedin.com/posts/kenhuang8_rag-is-everywhere-but-where-is-security-activity-7137531149379072000-ISD3)
- [ShadowRay: First Known Attack Campaign Targeting RAG LLMs](https://www.linkedin.com/posts/kenhuang8_shadowray-first-known-attack-campaign-targeting-activity-7179965782401929216-eJ3j)
- [CWE-285: Improper Access Control (Authorization)](https://cwe.mitre.org/data/definitions/285.html)
- [CWE-668: Exposure of Resource to Wrong Sphere](https://cwe.mitre.org/data/definitions/668.html)
- [Retrieval Augmented Generation (RAG) for Knowledge-Intensive NLP Tasks](https://arxiv.org/abs/2005.11401)
- [LangChain JS Arbitrary File Read Vulnerability](https://evren.ninja/langchain-afr-vulnerability.html)

