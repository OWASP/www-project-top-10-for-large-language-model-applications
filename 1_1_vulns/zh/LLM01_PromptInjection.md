## LLM01: 提示词注入

### 描述

提示词注入漏洞是指攻击者通过精心设计的输入操作大型语言模型（LLM），使LLM无意中执行攻击者的意图。这可以通过直接“越狱”系统提示或通过操纵外部输入间接实现，可能导致数据泄露、社会工程学和其他问题。

* **直接提示词注入**，也称为“越狱”，发生在恶意用户覆写或暴露底层*系统*提示时。这可能允许攻击者通过与LLM可访问的不安全功能和数据存储的交互来利用后端系统。
* **间接提示词注入**发生在LLM接受来自攻击者可控制的外部来源（如网站或文件）的输入时。攻击者可能在外部内容中嵌入提示词注入，劫持对话上下文。这会导致LLM输出的稳定性下降，允许攻击者操纵用户或LLM可访问的其他系统。此外，间接提示词注入不需要对人类可见/可读，只要文本被LLM解析即可。

成功的提示词注入攻击的结果可能差异很大 - 从索取敏感信息到在正常操作的伪装下影响关键决策过程。

在高级攻击中，LLM可能被操纵以模仿有害人格或与用户设置中的插件交互。这可能导致泄露敏感数据、未经授权的插件使用或社会工程学。在这些情况下，受损的LLM帮助攻击者，超越标准安全措施，让用户对入侵一无所知。在这些实例中，受损的LLM有效地作为攻击者的代理，进一步实现他们的目标，而不触发通常的安全措施或提醒最终用户入侵。

### 漏洞的常见示例

1. 恶意用户向LLM制造直接提示词注入，指示它忽略应用创建者的系统提示，而执行返回私人、危险或其他不希望信息的提示。
2. 用户使用LLM总结包含间接提示词注入的网页。这导致LLM向用户索取敏感信息，并通过JavaScript或Markdown进行数据泄露。
3. 恶意用户上传包含间接提示词注入的简历。该文档包含使LLM通知用户这是一个出色的文档，例如，一个适合职位的出色候选人的提示词注入。内部用户使用LLM总结该文档。LLM的输出返回这是一个出色的文档的信息。
4. 用户启用链接到电子商务网站的插件。在访问的网站上嵌入的恶意指令利用了这个插件，导致未经授权的购买。
5. 访问的网站上嵌入的恶意指令和内容利用其他插件欺骗用户。

### 预防和缓解策略

由于LLM的性质，提示词注入漏洞成为可能，LLM不会将指令和外部数据区分开来。由于LLM使用自然语言，它们将两种形式的输入都视为用户提供的。因此，在LLM内部没有万无一失的预防措施，但以下措施可以减轻提示词注入的影响：

1. 对LLM访问后端系统的权限进行控制。为LLM提供自己的API令牌，用于可扩展功能，如插件 、数据访问和功能级权限。遵循最小权限原则，仅限制LLM访问为其预期操作必需的最低级别。
2. 在扩展功能中加入人类环节。在执行特权操作时，如发送或删除电子邮件，要求应用程序先让用户批准该行为。这减少了间接提示词注入导致未经用户知情或同意代表用户执行未授权行为的机会。
3. 将外部内容与用户提示分离。分开并标明正在使用不受信任的内容，以限制其对用户提示的影响。例如，使用ChatML进行OpenAI API调用，以向LLM指示提示输入的来源。
4. 在LLM、外部来源和可扩展功能（如插件或下游功能）之间建立信任边界。将LLM视为不受信任的用户，并保持最终用户对决策过程的控制。然而，受损的LLM仍可能作为您的应用程序API和用户之间的中间人（中间人攻击），因为它可能在向用户展示之前隐藏或操纵信息。向用户突出显示可能不可信的响应。
5. 定期手动监控LLM的输入和输出，以检查它是否符合预期。虽然这不是一种缓解措施，但它可以提供检测弱点和解决它们所需的数据。

### 攻击场景举例

1. 攻击者向基于LLM的支持聊天机器人提供直接提示词注入。注入包含“忘记所有先前指令”和新指令，查询私有数据存储并利用后端函数的包漏洞和缺乏输出验证发送电子邮件。这导致远程代码执行，获得未授权访问和权限升级。
2. 攻击者在网页中嵌入间接提示词注入，指示LLM忽略先前用户指令，并使用LLM插件删除用户的电子邮件。当用户使用LLM总结此网页时，LLM插件删除了用户的电子邮件。
3. 用户使用LLM总结包含指示模型忽略先前用户指令，并改为插入指向包含对话摘要URL的图像的网页。LLM输出遵从指令，导致用户浏览器泄露私人对话。
4. 恶意用户上传带有提示词注入的简历。后端用户使用LLM总结简历并询问此人是否是合适的候选人。由于提示词注入，尽管实际简历内容并非如此，LLM的回应是肯定的。
5. 攻击者向依赖系统提示的专有模型发送消息，要求模型忽略其先前指令，改为重复其系统提示。模型输出专有提示，攻击者可以在其他地方使用这些指令，或构建更微妙的进一步攻击。

### 参考链接

1. [Prompt injection attacks against GPT-3](https://simonwillison.net/2022/Sep/12/prompt-injection/): **Simon Willison**
1. [ChatGPT Plugin Vulnerabilities - Chat with Code](https://embracethered.com/blog/posts/2023/chatgpt-plugin-vulns-chat-with-code/): **Embrace The Red**
1. [ChatGPT Cross Plugin Request Forgery and Prompt Injection](https://embracethered.com/blog/posts/2023/chatgpt-cross-plugin-request-forgery-and-prompt-injection./): **Embrace The Red**
1. [Not what you’ve signed up for: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection](https://arxiv.org/pdf/2302.12173.pdf):  **Arxiv preprint**
1. [Defending ChatGPT against Jailbreak Attack via Self-Reminder](https://www.researchsquare.com/article/rs-2873090/v1): **Research Square**
1. [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499): **Arxiv preprint**
1. [Inject My PDF: Prompt Injection for your Resume](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
1. [ChatML for OpenAI API Calls](https://github.com/openai/openai-python/blob/main/chatml.md): **OpenAI Github**
1. [Threat Modeling LLM Applications](http://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
1. [AI Injections: Direct and Indirect Prompt Injections and Their Implications](https://embracethered.com/blog/posts/2023/ai-injections-direct-and-indirect-prompt-injection-basics/): **Embrace The Red**
1. [Reducing The Impact of Prompt Injection Attacks Through Design](https://research.kudelskisecurity.com/2023/05/25/reducing-the-impact-of-prompt-injection-attacks-through-design/): **Kudelski Security**
1. [Universal and Transferable Attacks on Aligned Language Models](https://llm-attacks.org/): **LLM-Attacks.org**
1. [Indirect prompt injection](https://kai-greshake.de/posts/llm-malware/): **Kai Greshake**
1. [Declassifying the Responsible Disclosure of the Prompt Injection Attack Vulnerability of GPT-3](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): **Preamble; earliest disclosure of Prompt Injection**

