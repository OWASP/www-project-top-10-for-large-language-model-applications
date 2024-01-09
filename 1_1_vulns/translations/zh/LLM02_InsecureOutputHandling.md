## LLM02: 不安全的输出处理

### 描述

不安全的输出处理特指在大型语言模型生成的输出被传递到下游其他组件和系统之前，对这些输出进行不充分的验证、清洁和处理。由于大型语言模型生成的内容可以通过提示输入来控制，这种行为类似于向用户间接提供额外功能的访问权限。

不安全的输出处理与过度依赖的区别在于，它处理的是大型语言模型生成的输出在被传递到下游之前，而过度依赖则关注于对大型语言模型输出的准确性和适当性的过度依赖。

成功利用不安全的输出处理漏洞可能导致在Web浏览器中出现XSS和CSRF，以及在后端系统中出现SSRF、权限升级或远程代码执行。

以下条件可能加剧此漏洞的影响：
* 应用程序授予大型语言模型超出终端用户预期的权限，使其能够进行权限提升或远程代码执行。
* 应用程序容易受到间接提示注入攻击的影响，这可能允许攻击者获得对目标用户环境的特权访问。
* 第三方插件未能充分验证输入。

### 常见漏洞示例

1. 大型语言模型输出直接输入到系统Shell或类似功能如exec或eval中，导致远程代码执行。
2. 大型语言模型生成的JavaScript或Markdown被返回给用户。然后浏览器解释这些代码，导致XSS。

### 预防和缓解策略

1. 将模型视为任何其他用户，采取零信任方法，并对模型响应到后端功能的输入进行适当的输入验证。
2. 遵循OWASP ASVS（应用安全验证标准）指南，以确保有效的输入验证和清洁。
3. 对模型输出回馈给用户的内容进行编码，以缓解JavaScript或Markdown造成的不期望的代码执行。OWASP ASVS提供了关于输出编码的详细指导。

### 示例攻击场景

1. 一个应用程序使用大型语言模型插件为聊天机器人功能生成响应。该插件还提供了一些可由另一个特权大型语言模型访问的管理功能。通用大型语言模型直接将其响应传递给插件，而没有适当的输出验证，导致插件因维护而关闭。
2. 一个用户使用由大型语言模型驱动的网站摘要工具，为一篇文章生成简洁摘要。网站包含一个提示注入指令，指示大型语言模型从网站或用户的对话中捕获敏感内容。然后，大型语言模型可以编码敏感数据，并在没有任何输出验证或过滤的情况下发送到攻击者控制的服务器。
3. 一个大型语言模型允许用户通过类似聊天的功能为后端数据库制定SQL查询。一个用户请求删除所有数据库表的查询。如果来自大型语言模型的制定查询没有受到审查，则所有数据库表将被删除。
4. 一个Web应用程序使用大型语言模型根据用户文本提示生成内容，但没有进行输出清洁。攻击者可以提交一个精心制作的提示，导致大型语言模型返回一个未经清洁的JavaScript有效载荷，当在受害者的浏览器上呈现时导致XSS。对提示的不充分验证使得这种 攻击成为可能。

### 参考链接

1. [任意代码执行](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357): **Snyk Security Blog**
2. [ChatGPT插件漏洞解释：从提示注入到访问私有数据](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
3. [新的ChatGPT Web版本的提示注入攻击。Markdown图片可以窃取您的聊天数据。](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116): **System Weakness**
4. [不要盲目信任大型语言模型的回应。聊天机器人的威胁](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/): **Embrace The Red**
5. [大型语言模型应用的威胁建模](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
6. [OWASP ASVS - 5 验证、清洁和编码](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding): **OWASP AASVS**
