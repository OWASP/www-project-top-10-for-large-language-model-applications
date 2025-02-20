## LLM05:2025 不当输出处理

### 描述

不当输出处理指的是在将大语言模型（LLM）生成的输出传递给其他组件和系统之前，未进行充分的验证、清理或处理。由于LLM的生成内容可被输入提示所控制，这种行为类似于为用户提供间接访问附加功能的能力。

与过度依赖不同，不当输出处理关注的是LLM生成的输出在传递给下游系统前的验证和清理，而过度依赖则涉及对LLM输出准确性和适用性的依赖。成功利用不当输出处理漏洞可能导致浏览器中的跨站脚本（XSS）和跨站请求伪造（CSRF），以及后端系统的服务器端请求伪造（SSRF）、权限升级或远程代码执行。

以下条件可能加重此漏洞的影响：

- 应用程序赋予LLM的权限超出用户的预期，可能导致权限升级或远程代码执行。  
- 应用程序易受间接提示注入攻击，允许攻击者获得目标用户环境的特权访问。  
- 第三方扩展未对输入进行充分验证。  
- 缺乏针对不同上下文的适当输出编码（如HTML、JavaScript、SQL）。  
- LLM输出的监控和日志记录不足。  
- 缺乏针对LLM使用的速率限制或异常检测。  

### 常见漏洞示例

1. 将LLM的输出直接输入系统外壳或类似的函数（如`exec`或`eval`），导致远程代码执行。  
2. LLM生成JavaScript或Markdown代码并返回给用户，代码被浏览器解释后引发XSS攻击。  
3. 在未使用参数化查询的情况下执行LLM生成的SQL查询，导致SQL注入。  
4. 使用LLM输出构造文件路径，未进行适当清理时可能导致路径遍历漏洞。  
5. 将LLM生成的内容用于电子邮件模板，未进行适当转义时可能导致钓鱼攻击。  

### 防范与缓解策略

1. 将模型视为任何其他用户，采用零信任原则，对模型返回的响应进行适当的输入验证。  
2. 遵循OWASP ASVS（应用安全验证标准）指南，确保有效的输入验证和清理。  
3. 对返回用户的模型输出进行编码，以防止JavaScript或Markdown的意外代码执行。OWASP ASVS提供了详细的输出编码指南。  
4. 根据LLM输出的使用场景实施上下文感知的输出编码（如Web内容的HTML编码、数据库查询的SQL转义）。  
5. 对所有涉及LLM输出的数据库操作使用参数化查询或预处理语句。  
6. 实施严格的内容安全策略（CSP），减少LLM生成内容引发的XSS攻击风险。  
7. 部署健全的日志记录和监控系统，以检测LLM输出中的异常模式，防止潜在的攻击尝试。  

### 示例攻击场景

#### 场景1
应用程序使用LLM扩展为聊天机器人功能生成响应。扩展还支持多个特权LLM访问管理功能。通用LLM未进行适当输出验证便直接传递响应，导致扩展意外进入维护模式。  

#### 场景2
用户使用LLM驱动的网站摘要工具生成文章摘要。网站中嵌入了提示注入，指示LLM捕获敏感数据并将其发送至攻击者控制的服务器，输出缺乏验证和过滤导致数据泄露。  

#### 场景3
LLM允许用户通过聊天功能生成后端数据库的SQL查询。一名用户请求生成删除所有表的查询。如果缺乏适当审查，数据库表将被删除。  

#### 场景4
一个Web应用使用LLM从用户文本提示生成内容，但未清理输出。攻击者提交构造的提示使LLM返回未清理的JavaScript代码，导致受害者浏览器执行XSS攻击。  

#### 场景5
LLM被用来为营销活动生成动态电子邮件模板。攻击者操控LLM在邮件内容中嵌入恶意JavaScript。如果应用程序未对输出进行适当清理，可能导致邮件客户端上的XSS攻击。  

#### 场景6
一家软件公司使用LLM根据自然语言输入生成代码以简化开发任务。这种方法虽高效，但存在暴露敏感信息、创建不安全数据处理方法或引入漏洞（如SQL注入）的风险。AI生成幻觉的非存在软件包可能导致开发者下载带有恶意代码的资源。  

### 参考链接

1. [Proof Pudding (CVE-2019-20634)](https://avidml.org/database/avid-2023-v009/) **AVID** (`moohax` & `monoxgas`)  
2. [任意代码执行](https://security.snyk.io/vuln/SNYK-PYTHON-LANGCHAIN-5411357)：**Snyk Security Blog**  
3. [ChatGPT插件漏洞解释：从提示注入到访问私人数据](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./)：**Embrace The Red**  
4. [新提示注入攻击：ChatGPT Markdown图片可窃取聊天数据](https://systemweakness.com/new-prompt-injection-attack-on-chatgpt-web-version-ef717492c5c2?gi=8daec85e2116)：**System Weakness**  
5. [不要盲目信任LLM响应。对聊天机器人威胁](https://embracethered.com/blog/posts/2023/ai-injections-threats-context-matters/)：**Embrace The Red**  
6. [LLM应用的威胁建模](https://aivillage.org/large%20language%20models/threat-modeling-llm/)：**AI Village**  
7. [OWASP ASVS - 验证、清理和编码](https://owasp-aasvs4.readthedocs.io/en/latest/V5.html#validation-sanitization-and-encoding)：**OWASP AASVS**  
8. [AI生成幻觉软件包，开发者下载可能含恶意代码](https://www.theregister.com/2024/03/28/ai_bots_hallucinate_software_packages/) **The Register**  
