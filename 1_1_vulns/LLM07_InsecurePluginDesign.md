## LLM07: Insecure Plugin Design

### Description

LLM plugins are extensions that, when enabled, are called automatically by the model during user interactions. The model integration platform drives them,  and the application may have no control over the execution, especially when the model is hosted by another party. Furthermore, plugins are likely to implement free-text inputs from the model with no validation or type-checking to deal with context-size limitations. This allows a potential attacker to construct a malicious request to the plugin, which could result in a wide range of undesired behaviors, up to and including remote code execution.

The harm of malicious inputs often depends on insufficient access controls and the failure to track authorization across plugins. Inadequate access control allows a plugin to blindly trust other plugins and assume that the end user provided the inputs. Such inadequate access control can enable malicious inputs to have harmful consequences ranging from data exfiltration, remote code execution, and privilege escalation.

This item focuses on creating LLM plugins rather than third-party plugins, which LLM-Supply-Chain-Vulnerabilities cover.

### Common Examples of Vulnerability

1. A plugin accepts all parameters in a single text field instead of distinct input parameters.
2. A plugin accepts configuration strings instead of parameters that can override entire configuration settings.
3. A plugin accepts raw SQL or programming statements instead of parameters.
4. Authentication is performed without explicit authorization to a particular plugin.
5. A plugin treats all LLM content as being created entirely by the user and performs any requested actions without requiring additional authorization.

### Prevention and Mitigation Strategies

1. Plugins should enforce strict parameterized input wherever possible and include type and range checks on inputs. When this is not possible, a second layer of typed calls should be introduced, parsing requests and applying validation and sanitization. When freeform input must be accepted because of application semantics, it should be carefully inspected to ensure no potentially harmful methods are being called.
2. Plugin developers should apply OWASP’s recommendations in ASVS (Application Security Verification Standard) to ensure adequate input validation and sanitization.
3. Plugins should be inspected and tested thoroughly to ensure adequate validation. Use Static Application Security Testing (SAST) scans and Dynamic and Interactive application testing (DAST, IAST) in development pipelines.
4. Plugins should be designed to minimize the impact of any insecure input parameter exploitation following the OWASP ASVS Access Control Guidelines. This includes least-privilege access control, exposing as little functionality as possible while still performing its desired function.
5. Plugins should use appropriate authentication identities, such as OAuth2, to apply effective authorization and access control. Additionally, API Keys should be used to provide context for custom authorization decisions that reflect the plugin route rather than the default interactive user.
6. Require manual user authorization and confirmation of any action taken by sensitive plugins.
7. Plugins are, typically, REST APIs, so developers should apply the recommendations found in OWASP Top 10 API Security Risks – 2023 to minimize generic vulnerabilities.

### Example Attack Scenarios

1. A plugin accepts a base URL and instructs the LLM to combine the URL with a query to obtain weather forecasts which are included in handling the user request. A malicious user can craft a request such that the URL points to a domain they control, which allows them to inject their own content into the LLM system via their domain.
2. A plugin accepts a free-form input into a single field that it does not validate. An attacker supplies carefully crafted payloads to perform reconnaissance from error messages. It then exploits known third-party vulnerabilities to execute code and perform data exfiltration or privilege escalation.
3. A plugin used to retrieve embeddings from a vector store accepts configuration parameters as a connection string without any validation. This allows an attacker to experiment and access other vector stores by changing names or host parameters and exfiltrate embeddings they should not have access to.
4. A plugin accepts SQL WHERE clauses as advanced filters, which are then appended to the filtering SQL. This allows an attacker to stage a SQL attack.
5. An attacker uses indirect prompt injection to exploit an insecure code management plugin with no input validation and weak access control to transfer repository ownership and lock out the user from their repositories.

### References

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): **ChatGPT Developer’s Guide**
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI Documentation**
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI Documentation**
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) **Embrace The Red**
7. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
8. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
9. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
10. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**
