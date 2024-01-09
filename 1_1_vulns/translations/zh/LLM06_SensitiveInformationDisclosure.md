## LLM06：敏感信息泄露

### 描述

LLM应用程序有潜力通过其输出透露敏感信息、专有算法或其他机密细节。这可能导致未经授权访问敏感数据、知识产权、侵犯隐私和其他安全漏洞。LLM应用程序的消费者需要了解如何安全地与LLM进行交互，并识别与无意中输入的敏感数据相关的风险，这些数据可能随后由LLM在其他地方的输出中返回。

为了减轻这一风险，LLM应用程序应执行充分的数据净化，以防止用户数据进入训练模型数据中。LLM应用程序的所有者还应该制定适当的使用条款政策，让消费者了解他们的数据如何被处理，并有选择不将其数据包含在训练模型中的权利。

消费者-LLM应用程序的互动形成了一个双向的信任边界，我们不能从根本上信任客户端->LLM输入或LLM->客户端输出。需要注意的是，这种漏洞假定某些前提条件超出了范围，例如威胁建模练习、保护基础架构以及充分的沙箱化。在系统提示中添加关于LLM应该返回的数据类型的限制可以在一定程度上减轻敏感信息泄露的风险，但LLM的不可预测性意味着这些限制可能并不总是会被遵守，并且可以通过提示注入或其他方式来绕过。

### 漏洞的常见示例

1. LLM响应中对敏感信息的不完整或不正确的过滤。
2. 在LLM的训练过程中对敏感数据的过度拟合或记忆。
3. 由于LLM误解、缺乏数据净化方法或错误，导致机密信息的意外泄露。

### 预防和缓解策略

1. 集成充分的数据净化和清理技术，以防止用户数据进入训练模型数据。
2. 实施强大的输入验证和净化方法，以识别和过滤掉潜在的恶意输入，以防止模型被污染。
3. 在丰富模型的数据和[微调](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/wiki/Definitions)模型时：（即在部署之前或部署过程中输入模型的数据）
   - 在微调数据中被视为敏感的任何信息都有可能向用户透露。因此，请应用最小权限原则，不要训练模型使用最高权限用户可以访问的信息，因为这些信息可能会显示给较低权限的用户。
   - 对运行时的外部数据源（数据协调）的访问应受到限制。
   - 对外部数据源应用严格的访问控制方法，以及对维护安全供应链的严格方法。

### 攻击场景示例

1. 毫不知情的合法用户A在与LLM应用程序进行非恶意交互时，通过LLM向其显示了某些其他用户的数据。
2. 用户A通过精心设计的一组提示，绕过LLM的输入过滤和净化，使其透露有关应用程序其他用户的敏感信息（PII）。
3. 个人数据，如PII，通过训练数据泄漏到模型中，要么是由于用户本身的疏忽，要么是由于LLM应用程序的错误。这种情况可能会增加上述情况1或2的风险和概率。

### 参考链接

1. [AI数据泄露危机：新工具防止公司机密被提供给ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt): **福克斯商业**
2. [从ChatGPT的三星泄漏中吸取的教训](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/): **Cybernews**
3. [Cohere - 使用条款](https://cohere.com/terms-of-use): **Cohere**
4. [威胁建模示例](https://aivillage.org/large%20language%20models/threat-modeling-llm/): **AI Village**
5. [OWASP人工智能安全和隐私指南](https://owasp.org/www-project-ai-security-and-privacy-guide/): **OWASP人工智能安全与隐私指南**
6. [确保大型语言模型的安全性](https://www.experts-exchange.com/articles/38220/Ensuring-the-Security-of-Large-Language-Models-Strategies-and-Best-Practices.html): **Experts Exchange**
