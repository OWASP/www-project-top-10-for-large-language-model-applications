# OWASP Top 10 for LLM Applications - CycloneDX SBOM Mapping

This document provides a detailed mapping of the OWASP Top 10 vulnerabilities specific to Large Language Model (LLM) applications to the [CycloneDX Machine Learning Software Bill of Materials (SBOM)](https://cyclonedx.org/) structure, with expanded descriptions and mitigation strategies.

## Overview

The OWASP Top 10 for LLM Applications identifies the most critical security risks to LLM applications. By mapping these vulnerabilities to the CycloneDX SBOM, organizations can document, understand, and address these risks more effectively. More information about the OWASP Top 10 for LLM Applications can be found [here](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

## Vulnerabilities and SBOM Mapping

### LLM01: Prompt Injection

- **Description**: Attackers manipulate the model's output by crafting malicious inputs, exploiting the model's response generation process.
- **SBOM Component**: `ExternalDependencies`
- **Mitigation**: Implement input validation and sanitization libraries. Document these libraries in the SBOM under `ExternalDependencies`, including their version and security features. More details on input validation can be found [here](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/07-Input_Validation_Testing/README).
- **Considerations**: Evaluate the risk based on the model's exposure to user-generated content and document any additional controls like rate limiting or monitoring for suspicious activity.

### LLM02: Insecure Output Handling

- **Description**: The model generates outputs that, if not properly sanitized, could lead to cross-site scripting (XSS), command injection, or other injection attacks when displayed or executed.
- **SBOM Component**: `Services`, `Data`
- **Mitigation**: Use output encoding libraries and data sanitization tools. Document these and their configurations in the SBOM, focusing on how they prevent specific attack vectors. OWASP's guide to output encoding can be found [here](https://owasp.org/www-project-proactive-controls/v3/en/c4-encode-escape-data).
- **Considerations**: Regularly update the documentation as new output handling mechanisms are implemented or as existing ones are updated.

### LLM03: Training Data Poisoning

- **Description**: Malicious actors introduce biased or malicious data into the training dataset, aiming to manipulate the model's behaviour.
- **SBOM Component**: `Data`
- **Mitigation**: Document the sources of training data, including any mechanisms for vetting or validating this data. Outline procedures for data integrity checks and periodic reviews of data sources for potential contamination.
- **Considerations**: Include information on anomaly detection systems or data sanitization processes used to cleanse training data.

### LLM04: Model Denial of Service

- **Description**: Overloading the model with a high volume of requests or complex queries, causing performance degradation or service unavailability.
- **SBOM Component**: `Services`
- **Mitigation**: Implement rate limiting and load balancing. Document the architecture and tools used to mitigate DoS attacks in the SBOM, including any third-party services or libraries. Information on DoS mitigation strategies can be found [here](https://www.cloudflare.com/en-ca/resource-hub/five-best-practices-for-mitigating-ddos-attacks/).
- **Considerations**: Regular testing for vulnerabilities to DoS attacks and updates to mitigation strategies should be documented in version updates within the SBOM.

### LLM05: Supply-Chain Vulnerabilities

- **Description**: Vulnerabilities introduced through compromised or malicious third-party components, such as libraries, packages, or data sources.
- **SBOM Component**: `ExternalDependencies`
- **Mitigation**: Conduct security audits of all third-party components. Document each component's origin, version, and the results of security assessments in the SBOM. Guidelines for securing the software supply chain can be found [here](https://www.cisa.gov/sites/default/files/publications/defending_against_software_supply_chain_attacks_508_1.pdf).
- **Considerations**: Establish a regular review process for third-party dependencies to ensure they remain secure over time.

### LLM06: Sensitive Information Disclosure

- **Description**: The model inadvertently exposes sensitive information in its responses, which could lead to privacy breaches.
- **SBOM Component**: `Data`, `Services`
- **Mitigation**: Implement data masking and anonymization techniques. Document the mechanisms in place to protect sensitive information, including any privacy-enhancing technologies (PETs) used.
- **Considerations**: Policies for data retention, anonymization, and response filtering should be clearly documented and regularly reviewed.

### LLM07: Insecure Plugin Design

- **Description**: Plugins or extensions that add functionality to the LLM application also introduce new vulnerabilities.
- **SBOM Component**: `Extensions`
- **Mitigation**: Establish security guidelines for plugin development. Document all plugins, their security features, and any known vulnerabilities in the SBOM.
- **Considerations**: Regular security assessments of plugins and updates to their documentation in the SBOM are crucial for maintaining security.

### LLM08: Excessive Agency

- **Description**: Allowing the model too much autonomy in decision-making processes, potentially leading to unintended or harmful actions.
- **SBOM Component**: `Properties`
- **Mitigation**: Define strict operational boundaries for the model. Document these boundaries, including any control mechanisms or oversight procedures, in the SBOM.
- **Considerations**: Regular reviews and updates to the model's operational guidelines are necessary to adapt to new insights or changes in the model's capabilities.

### LLM09: Overreliance

- **Description**: Excessive dependence on the LLM for critical decision-making without adequate human oversight, increasing the risk of impactful errors.
- **SBOM Component**: `Policies`
- **Mitigation**: Implement policies for human review and oversight of critical decisions. Document these policies in the SBOM, detailing the roles and responsibilities of human supervisors.
- **Considerations**: The effectiveness of oversight mechanisms should be periodically evaluated and documented in the SBOM updates.

### LLM10: Model Theft

- **Description**: Unauthorized copying or extraction of the model, leading to intellectual property theft or unauthorized use.
- **SBOM Component**: `Licenses`
- **Mitigation**: Use digital rights management (DRM) and encryption to protect the model. Document the licensing terms, protection measures, and any breaches or attempted thefts in the SBOM.
- **Considerations**: Regularly update the SBOM with information on new security measures or incidents related to model theft.

## Conclusion

By mapping the OWASP Top 10 vulnerabilities for LLM Applications to the CycloneDX SBOM, organizations can create a comprehensive documentation and mitigation strategy for securing their machine learning systems. This detailed approach ensures that all aspects of LLM application security are considered, documented, and actively managed.


# OWASP CycloneDX SBOM for Machine Learning Projects

This document outlines the structure of a Software Bill of Materials (SBOM) for machine learning projects, following the OWASP CycloneDX standard. It aims to capture the essential components, libraries, and dependencies that are typically involved in such projects, with a focus on security as per the OWASP Top 10 for LLMs.

## Project Overview

- **Name**: Machine Learning Project (Example)
- **Description**: A project leveraging Large Language Models to perform text analysis, sentiment analysis, and predictive modelling.
- **Version**: 1.0.0
- **Authors**: [Project Team Members]
- **License**: [Applicable License]

## Components

### Machine Learning Frameworks

- **TensorFlow**
  - **Version**: 2.6.0
  - **Supplier**: TensorFlow Authors
  - **Licenses**: Apache License 2.0
  - **Website**: [https://www.tensorflow.org/](https://www.tensorflow.org/)

- **PyTorch**
  - **Version**: 1.9.0
  - **Supplier**: PyTorch Authors
  - **Licenses**: BSD License
  - **Website**: [https://pytorch.org/](https://pytorch.org/)

### Libraries for Data Processing

- **Pandas**
  - **Version**: 1.3.1
  - **Supplier**: PyData Development Team
  - **Licenses**: BSD License
  - **Website**: [https://pandas.pydata.org/](https://pandas.pydata.org/)

- **NumPy**
  - **Version**: 1.21.1
  - **Supplier**: NumPy Developers
  - **Licenses**: BSD License
  - **Website**: [https://numpy.org/](https://numpy.org/)

### Security Tools and Libraries

- **Bandit**
  - **Version**: 1.7.0
  - **Supplier**: PyCQA
  - **Licenses**: Apache License 2.0
  - **Website**: [https://bandit.readthedocs.io/en/latest/](https://bandit.readthedocs.io/en/latest/)

- **OWASP Dependency-Check**
  - **Version**: 6.2.2
  - **Supplier**: OWASP
  - **Licenses**: Apache License 2.0
  - **Website**: [https://owasp.org/www-project-dependency-check/](https://owasp.org/www-project-dependency-check/)

### Datasets

- **Sentiment140**
  - **Version**: [Dataset Version]
  - **Supplier**: Stanford University
  - **Licenses**: [Dataset License]
  - **Website**: [http://help.sentiment140.com/for-students](http://help.sentiment140.com/for-students)

## Dependencies

[IN PROGRESS - List of any external dependencies not included above, with versions, suppliers, and licenses.]

## Known Vulnerabilities

[IN PROGRESS - List of known vulnerabilities associated with the components and dependencies listed, if any.]

## Acknowledgments

- **OWASP CycloneDX**: For providing the SBOM standard.
- **OWASP Top 10 for LLMs Team**: For insights into security considerations for machine learning projects.

## How to Contribute

For instructions on how to contribute to this SBOM or the associated machine-learning project, please see [CONTRIBUTING.md](./CONTRIBUTING.md).

## License

This SBOM is shared under the [MIT License](./LICENSE), unless otherwise noted for specific components or datasets.
