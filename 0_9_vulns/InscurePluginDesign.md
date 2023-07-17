## Insecure Plugin Design

**Description**

LLM plugins are extensions that are called by the model when responding to a user request. Since they are automatically invoked in-context and are often chained, there is little application control over their execution. Consequently, they can be vulnerable due to insecure design characterized by insecure inputs and insufficient access control. LLM Plugins are typically REST API Services, and there can be other vulnerabilities in the design, as found in OWASP Top 10 API Security Risks – 2023. This item focuses on LLM invocation-specific issues. 

Plugin integration APIs, such as OpenAI ChatGPT, mandate the use of OpenAPI specification but do not impose any constraints on API contracts. Furthermore, as plugin invocations contribute against the context limit of the model and OpenAPI recommends a minimum number of input parameters to minimise token usage; consquently, plugins are likely to implement free text inputs with no validation or type checking. 

This allows a potential attacker to construct a malicious request to the plugin that could result in a wide range of undesired behaviours, up to and including remote code execution.  Additionally, for OpenAI plugins, values to the plugin API parameters are based on the model's analysis of the OpenAPI file and the natural language instructive descriptions included in a manifest file. This may lead to misconfigurations and erroneous parameter mappings.

The harm of malicious inputs depends on insufficient access controls and the failure to track authorisation across plugins. This allows a plugin to blindly trust other plugins in a chain invocation and/or assume that the end user provided the inputs. Such inadequate access control can allow malicious inputs to have harmful consequences ranging from data exfiltration, remote code execution, and privilege escalation. 

Although we recommend (LLM-Insecure Output Handling ) output sanitisation, this may not be possible in the chain of plugin invocation, or it has been omitted. Plugins should not assume safe inputs, and they should have their own input validation combined with explicit access control.

This item focuses on creating LLM plugins rather than using third-party plugins, which is covered by LLM-Supply-Chain-Vulnerabilities, although it provides the basis to test third-party plugins for insecure plugin design vulnerabilities. 

**Common Examples of Vulnerability:**

1. A plugin accepts all parameters in a single text field instead of distinct input parameters.
2. A plugin designed to call a specific API hosted at a specific endpoint accepts a string containing the entire URL to be retrieved instead of query parameters to be inserted into the URL. 
3. A plugin designed to look up information from a SQL database accepts a raw SQL query rather than parameters to be inserted into a fully parameterized query.
4. A plugin designed to look up embeddings from a vector database allows a full connection string rather than specific parameters. : 
5. Authentication is performed without explicit authorization to a particular plugin.
6. A plugin treats all LLM content as being created entirely by the user and performs any requested actions without requiring additional authorization.
7. Plugins are chained together without considering the authorization of one plugin to perform an action using another plugin.

**How to Prevent:**



1. Plugins should enforce strict parameterized input wherever possible and include type and range checks on inputs. 
2. When this is not possible, minimise context size and follow vendor recommendations (e.g. OpenAI), a second layer of typed calls should be introduced, parsing requests and applying validation and sanitisation.
3. When freeform input must be accepted because of application semantics, it should be carefully inspected to ensure that no potentially harmful methods are being called.
4. Plugin developers should apply OWASP’s recommendations in ASVS  (Application Verification Standard) to ensure effective input validation and sanitisation.
5.  Plugins should be inspected and tested thoroughly to ensure adequate validation is in place and detect injection vulnerabilities. This includes the use of Static Application Security Testing (SAST) scans as well as Dynamic and interactive application testing (DAST, IAST) in development pipelines. 
6. Plugins should be designed to minimise the impact of any insecure input parameter exploitation following the OWASP ASVS Access Control Guidelines. This includes least-privilege access control, exposing as little functionality as possible while still performing its desired function.
7. Plugins should  use appropriate authentication identities, such as OAuth2, to apply effective authorization and access control. Additionally, API Keys should be used to allow custom authorisation decisions to reflect the plugin route rather than the default interactive user.
8. Require manual user authorisation and confirmation of any sensitive action (e.g. POST/PUT/DELETE)  taken by plugins; note for any POST operations OpenAI “_require that developers build a user confirmation flow to avoid destruction actions._”
9. Avoid plugin chaining with each user input and prevent sensitive plugins from being called after any other plugin.
10. When chaining, perform taint tracing on all plugin content, ensuring that the plugin is called with an authorization level corresponding to the lowest authorization of any plugin that has provided input to the LLM prompt.
11. Plugins are, typically, REST APIs and should developers apply the recommendations found in OWASP Top 10 API Security Risks – 2023  to minimise generic  vulnerabilities.

**Example Attack Scenarios:**

Scenario #1: A plugin accepts a base URL and instructs the LLM to combine the URL with a query to obtain external content in response to user requests. The resulting URL is then accessed, and the results are included in handling the user request. A malicious user can craft a request such that a URL points to a domain they control and not the URL hosting the intended content. This allows attackers to obtain the IP address of the plugin for further reconnaissance, as well as to inject their own content into the LLM system via their domain, potentially granting them further access to downstream plugins.

Scenario #2: A plugin accepts a free-form input into a single field that it does not validate. An attacker can supply carefully crafted payloads to perform reconnaissance from error messages and exploit system or third-party vulnerabilities, allowing them to perform data exfiltration, remote code execution or privilege escalation.

Scenario #3: A plugin accepts configuration parameters as a connection string without any validation. This allows an attacker to experiment and access other stores by changing names or host parameters. 

Scenario #4: A plugin accepts SQL WHERE causes as advanced filters, which are then appended to the filtering SQL. This allows an attacker to stage a SQL attack.

Scenario #5: An attacker uses indirect prompt injection to induce an email plugin with no input validation and insufficient access control to deliver the contents of the current user's inbox to a malicious URL via a POST request.

Scenario #6: An attacker uses indirect prompt injection to exploit an insecure code management plugin with no input validation and weak access control to transfer repository ownership and lock out the user from their repositories.

**References**

1. [OpenAI ChatGPT Plugins](https://platform.openai.com/docs/plugins/introduction): ChatGPT Developer’s Guide
2. [OpenAI ChatGPT Plugins - Plugin Flow](https://platform.openai.com/docs/plugins/introduction/plugin-flow): A description of how the  plugin execution flows, and the requirement to have a user confirmation for all POST operations
3. [OpenAI ChatGPT Plugins - Authentication](https://platform.openai.com/docs/plugins/authentication/service-level): Description of Service and  User level authentication (including API Tokens and OAuth2) and the Unauthenticated mode.
4. [OpenAI Semantic Search Plugin Sample](https://github.com/openai/chatgpt-retrieval-plugin): A fully-featured solution for Semantic Search using embeddings and vector databases; it also demonstrates all authentication methods.
5. [Plugin Vulnerabilities: Visit a Website and Have Your Source Code Stolen](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): Brief discussion of using a malicious plugin to perform unauthorized actions on GitHub repositories.
6. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./) Walkthrough of a cross-plugin request forgery attack resulting from inadequate cross-plugin authorization.
7. [ChatGPT Plugin Exploit Explained: From Prompt Injection to Accessing Private Data](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)
8. [OWASP ASVS - 5 Validation, Sanitization and Encoding](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding)
9. [OWASP ASVS 4.1 General Access Control Design](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design)
10. [OWASP Top 10 API Security Risks – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/)
    
