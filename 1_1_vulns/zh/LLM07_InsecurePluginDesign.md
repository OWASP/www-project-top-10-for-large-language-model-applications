## LLM07：不安全的插件设计

### 描述

LLM插件是扩展，当启用时，会在用户互动期间由模型自动调用。模型集成平台驱动它们，应用程序可能无法控制执行，特别是当模型由另一方托管时。此外，插件很可能会从模型中实现来自模型的自由文本输入，而不进行验证或类型检查以处理上下文大小限制。这使得潜在攻击者可以构造一个恶意请求发送给插件，可能导致各种不希望发生的行为，甚至包括远程代码执行。

恶意输入的危害通常取决于不足的访问控制和未能跟踪授权的插件。不足的访问控制允许插件盲目信任其他插件，并假定最终用户提供了输入。这种不足的访问控制可以使恶意输入产生各种有害后果，包括数据泄露、远程代码执行和特权升级。

此项重点是创建LLM插件而不是第三方插件，LLM供应链漏洞涵盖了第三方插件。

### 漏洞的常见示例

1. 插件接受单个文本字段中的所有参数，而不是不同的输入参数。
2. 插件接受配置字符串，而不是可以覆盖整个配置设置的参数。
3. 插件接受原始SQL或编程语句，而不是参数。
4. 执行身份验证时没有对特定插件进行明确授权。
5. 插件将所有LLM内容视为完全由用户创建，并在不需要额外授权的情况下执行任何请求的操作。

### 预防和缓解策略

1. 插件应尽可能强制执行严格的参数化输入，并对输入进行类型和范围检查。如果不可能进行此操作，应引入第二层类型化调用，解析请求并应用验证和净化。当由于应用程序语义需要接受自由形式的输入时，应仔细检查以确保不会调用任何潜在有害的方法。
2. 插件开发人员应遵循OWASP的建议，使用ASVS（应用程序安全性验证标准）确保适当的输入验证和净化。
3. 应对插件进行彻底的检查和测试，以确保适当的验证。在开发流水线中使用静态应用程序安全性测试（SAST）扫描以及动态和交互式应用程序测试（DAST，IAST）。
4. 插件应设计以最小化不安全输入参数利用的影响，遵循OWASP ASVS访问控制准则。这包括最小权限访问控制，尽可能少地暴露功能，同时仍然执行其所需的功能。
5. 插件应使用适当的身份验证身份，例如OAuth2，以应用有效的授权和访问控制。此外，应使用API密钥来提供上下文，以进行自定义授权决策，反映插件路由而不是默认的交互用户。
6. 对于敏感插件执行的任何操作，都应要求手动用户授权和确认。
7. 插件通常是REST API，因此开发人员应应用OWASP Top 10 API安全风险 – 2023中找到的建议，以最小化通用漏洞。

### 攻击场景示例

1. 一个插件接受基本URL，并指示LLM将URL与查询组合以获取天气预报，然后将其包含在处理用户请求中。恶意用户可以精心制作请求，使URL指向他们控制的域，从而允许他们通过其域名将自己的内容注入LLM系统。
2. 一个插件接受自由形式的输入到一个不验证的单一字段。攻击者提供精心制作的有效负载，以从错误消息中执行侦察。然后利用已知的第三方漏洞来执行代码并执行数据泄露或特权升级。
3. 用于从向量存储中检索嵌入的插件接受连接字符串作为配置参数，而不进行任何验证。这允许攻击者尝试并访问其他向量存储，通过更改名称或主机参数来突破，以及窃取他们不应该访问的嵌入。
4. 一个插件接受SQL WHERE子句作为高级过滤器，然后将其附加到过滤SQL中。这允许攻击者进行SQL攻击。
5. 攻击者使用间接提示注入来利用一个没有输入验证和弱访问控制的不安全代码管理插件，以转移仓库所有权并锁定用户对其仓库的访问权。

### 参考链接

1. [OpenAI ChatGPT插件](https://platform.openai.com/docs/plugins/introduction): **ChatGPT开发者指南**
2. [OpenAI ChatGPT插件 - 插件流程](https://platform.openai.com/docs/plugins/introduction/plugin-flow): **OpenAI文档**
3. [OpenAI ChatGPT插件 - 身份验证](https://platform.openai.com/docs/plugins/authentication/service-level): **OpenAI文档**
4. [OpenAI语义搜索插件示例](https://github.com/openai/chatgpt-retrieval-plugin): **OpenAI Github**
5. [插件漏洞：访问网站并让您的源代码被窃取](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
6. [ChatGPT插件漏洞解释：从提示注入到访问私人数据](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
7. [OWASP ASVS - 5 验证、净化和编码](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
8. [OWASP ASVS 4.1 通用访问控制设计](https://owasp-aasvs4.readthedocs.io/en/latest/V4.1.html#general-access-control-design): **OWASP AASVS**
9. [OWASP Top 10 API安全风险 – 2023](https://owasp.org/API-Security/editions/2023/en/0x11-t10/): **OWASP**
    
