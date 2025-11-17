## LLM09:2025 信息误导

### 描述

LLM（大型语言模型）生成的信息误导对依赖这些模型的应用程序构成了核心漏洞。当LLM生成看似可信但实际错误或具有误导性的信息时，就会导致信息误导。这种漏洞可能引发安全漏洞、声誉损害和法律责任。

信息误导的主要原因之一是“幻觉”（Hallucination）现象，即LLM生成看似准确但实际上是虚构的内容。当LLM基于统计模式填补训练数据的空白而非真正理解内容时，就会发生幻觉。因此，模型可能会生成听起来正确但完全没有根据的答案。尽管幻觉是信息误导的主要来源，但并非唯一原因；训练数据中的偏差以及信息的不完整性也会导致信息误导。

另一个相关问题是“过度依赖”。用户对LLM生成的内容过于信任而未能验证其准确性时，就会出现过度依赖。这种过度依赖加剧了信息误导的影响，因为用户可能会将错误数据融入到关键决策或流程中，而缺乏充分的审查。

### 常见风险示例

#### 1. 事实性错误

模型生成错误的陈述，导致用户基于信息误导做出决策。例如，加拿大航空的聊天机器人向旅客提供了信息误导，导致运营中断和法律纠纷。最终航空公司败诉。  
(参考链接：[BBC](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know))

#### 2. 无依据的主张

模型生成了毫无根据的断言，这在医疗或法律等敏感场景中特别有害。例如，ChatGPT虚构了假的法律案件，导致法院处理出现重大问题。  
(参考链接：[LegalDive](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/))

#### 3. 专业能力的错误呈现

模型表现出对复杂主题的理解能力，误导用户以为其具有相关专业知识。例如，聊天机器人错误地表示健康问题的复杂性，暗示某些治疗仍在争议中，从而误导用户认为不被支持的治疗方案仍具可行性。  
(参考链接：[KFF](https://www.kff.org/health-misinformation-monitor/volume-05/))

#### 4. 不安全的代码生成

模型建议使用不安全或不存在的代码库，这可能在软件系统中引入漏洞。例如，LLM建议使用不安全的第三方库，如果未经验证被信任使用，将导致安全风险。  
(参考链接：[Lasso](https://www.lasso.security/blog/ai-package-hallucinations))

### 预防和缓解策略

#### 1. 检索增强生成（RAG）

通过在响应生成过程中从可信外部数据库检索相关和已验证的信息，提升模型输出的可靠性，以降低幻觉和信息误导的风险。

#### 2. 模型微调

通过微调或嵌入技术提高模型输出质量。使用参数高效微调（PET）和链式思维提示（Chain-of-Thought Prompting）等技术可以减少信息误导的发生。

#### 3. 交叉验证与人工监督

鼓励用户通过可信的外部来源验证LLM输出的准确性。针对关键或敏感信息，实施人工监督和事实核查流程。确保人类审核员经过适当培训，以避免过度依赖AI生成内容。

#### 4. 自动验证机制

为关键输出特别是在高风险环境中，实施工具和流程进行自动验证。

#### 5. 风险沟通

识别LLM生成内容的风险和可能的危害，并将这些风险和限制清晰传达给用户，包括可能出现信息误导的情况。

#### 6. 安全编码实践

建立安全编码实践，防止因错误代码建议而引入的漏洞。

#### 7. 用户界面设计

设计鼓励负责任使用LLM的API和用户界面，例如整合内容过滤器，明确标注AI生成的内容，并告知用户内容的可靠性和准确性限制。对使用领域的限制应具体说明。

#### 8. 培训和教育

为用户提供LLM局限性、生成内容独立验证重要性以及批判性思维的综合培训。在特定场景下，提供领域特定培训，确保用户能够在其专业领域内有效评估LLM的输出。

### 示例攻击场景

#### 场景 #1

攻击者使用流行的编码助手测试常见的幻觉包名称。一旦识别出这些频繁建议但实际上不存在的库，攻击者将恶意包发布到常用代码库中。开发者依赖编码助手的建议，无意间将这些恶意包集成到他们的软件中。最终，攻击者获得未授权访问权限，注入恶意代码或建立后门，导致严重的安全漏洞和用户数据的泄露。

#### 场景 #2

某公司提供的医疗诊断聊天机器人未确保足够的准确性，导致患者因信息误导受到有害影响。最终公司因损害赔偿被成功起诉。在这种情况下，风险不需要恶意攻击者的参与，仅由于LLM系统的监督和可靠性不足就使公司面临声誉和财务风险。

### 参考链接

1. [人工智能聊天机器人作为健康信息来源：专业能力的错误呈现](https://www.kff.org/health-misinformation-monitor/volume-05/): **KFF**
2. [加拿大航空聊天机器人信息误导：旅客需要知道什么](https://www.bbc.com/travel/article/20240222-air-canada-chatbot-misinformation-what-travellers-should-know): **BBC**
3. [ChatGPT虚构法律案件：生成式AI幻觉](https://www.legaldive.com/news/chatgpt-fake-legal-cases-generative-ai-hallucinations/651557/): **LegalDive**
4. [理解LLM幻觉现象](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): **Towards Data Science**
5. [公司应如何向用户沟通大型语言模型的风险](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/): **TechPolicy**
6. [某新闻网站使用AI撰写文章：一场新闻业的灾难](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/): **Washington Post**
7. [深入了解AI软件包幻觉](https://www.lasso.security/blog/ai-package-hallucinations): **Lasso Security**
8. [ChatGPT生成的代码有多安全？](https://arxiv.org/abs/2304.09655): **Arvix**
9. [如何减少大型语言模型的幻觉](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/): **The New Stack**
10. [减少幻觉的实践步骤](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination): **Victor Debia**
11. [探索AI调解的企业知识后果框架](https://www.microsoft.com/en-us/research/publication/a-framework-for-exploring-the-consequences-of-ai-mediated-enterprise-knowledge-access-and-identifying-risks-to-workers/): **Microsoft**

### 相关框架与分类

请参考以下框架和分类，以获取关于基础设施部署、环境控制以及其他最佳实践的全面信息、场景和策略。

- [AML.T0048.002 - 社会危害](https://atlas.mitre.org/techniques/AML.T0048): **MITRE ATLAS**
