## LLM10: 模型盗窃

### 描述

这个条目涉及到恶意行为者或高级持续性威胁（APT）未经授权地访问和窃取LLM模型。这种情况发生在专有的LLM模型（作为有价值的知识产权）受到威胁、被盗取、复制或权重和参数被提取以创建一个功能等效的模型。LLM模型盗窃的影响可能包括经济和品牌声誉的损失、竞争优势的削弱、对模型的未经授权使用或未经授权访问模型中包含的敏感信息。

LLM模型的盗窃代表了一个重大的安全关切，因为语言模型变得越来越强大和普遍。组织和研究人员必须优先考虑强大的安全措施，以保护他们的LLM模型，确保知识产权的机密性和完整性。采用包括访问控制、加密和持续监控在内的全面安全框架对于减轻与LLM模型盗窃相关的风险以及保护依赖于LLM的个人和组织的利益至关重要。

### 常见漏洞示例

1. 攻击者利用公司基础设施中的漏洞，通过网络或应用程序安全设置的配置错误来未经授权地访问其LLM模型仓库。
2. 内部威胁情景，一名不满的员工泄露了模型或相关的工件。
3. 攻击者使用精心制作的输入和提示注入技术查询模型API，以收集足够数量的输出来创建一个影子模型。
4. 恶意攻击者能够绕过LLM的输入过滤技术，执行侧信道攻击，最终将模型权重和架构信息提取到远程受控资源。
5. 模型提取的攻击向量涉及使用大量关于特定主题的提示查询LLM。然后可以使用LLM的输出来对另一个模型进行微调。然而，有几点需要注意：
   - 攻击者必须生成大量有针对性的提示。如果提示不够具体，LLM的输出将毫无用处。
   - LLM的输出有时可能包含幻觉的答案，这意味着攻击者可能无法提取整个模型，因为其中一些输出可能是荒谬的。
     - 通过模型提取无法完全复制LLM。但攻击者将能够复制部分模型。
6. **_功能模型复制_** 的攻击向量涉及使用目标模型通过提示生成合成训练数据（一种称为“自我指导”的方法），然后使用它来微调另一个基础模型以产生一个功能等效的模型。这绕过了示例5中使用的传统查询式提取的限制，已成功用于使用LLM来训练另一个LLM的研究中。尽管在这个研究的背景下，模型复制不是一种攻击，但攻击者可以使用这种方法来复制一个具有公共API的专有模型。

被盗用的模型，作为影子模型，可以用于发动敌对攻击，包括未经授权访问模型中包含的敏感信息或在进一步发动高级提示注入攻击时进行未被察觉的实验。

### 预防和减轻策略

1. 实施强大的访问控制（例如，RBAC和最小权限原则）和强大的身份验证机制，以限制对LLM模型仓库和训练环境的未经授权访问。
   - 对于前三个常见示例来说，这一点尤其重要，因为它们可能由内部威胁、配置错误和/或基础设施安全控制不足引发漏洞，而恶意行为者可以从内部或外部渗透环境中渗透。
   - 供应商管理跟踪、验证和依赖性漏洞是防止供应链攻击利用的重要关注点。
2. 限制LLM对网络资源、内部服务和API的访问。
   - 对于所有常见示例来说，这一点尤其重要，因为它涵盖了内部风险和威胁，但最终控制了LLM应用程序“可以访问什么”，因此可能是防止侧信道攻击的机制或预防步骤。
3. 在生产中使用集中式ML模型清单或注册表。具有集中式模型注册表可以通过访问控制、身份验证和监控/日志记录功能来防止未经授权访问ML模型。具有集中存储库对于收集关于模型使用的算法的数据以用于合规性、风险评估和风险缓解等目的也是有益的。
4. 定期监控和审计与LLM模型仓库相关的访问日志和活动，以及及时检测和响应任何可疑或未经授权的行为。
5. 自动化 MLOps部署，包括治理、跟踪和批准工作流程，以加强对基础设施内的访问和部署控制。
6. 实施控制和减轻策略，以减轻提示注入技术引发侧信道攻击的风险。
7. 在适用的情况下对API调用进行速率限制和/或过滤，以减小从LLM应用程序泄漏数据的风险，或者实施检测（例如DLP）从其他监视系统中提取活动的技术。
8. 实施对抗性强度培训，以帮助检测提取查询并加强物理安全措施。
9. 在LLM的生命周期的嵌入和检测阶段实施水印框架。

### 攻击场景示例

1. 攻击者利用公司基础设施中的漏洞未经授权地访问其LLM模型仓库。攻击者随后窃取有价值的LLM模型，并使用它们来启动竞争性语言处理服务或提取敏感信息，给原始公司造成重大财务损失。
2. 一名不满的员工泄露了模型或相关工件。此情景的公开曝光增加了攻击者进行灰盒对抗性攻击的知识，或者直接窃取可用的财产。
3. 攻击者使用精心选择的输入查询API，收集足够数量的输出来创建一个影子模型。
4. 供应链中存在安全控制故障，导致了专有模型信息的数据泄漏。
5. 恶意攻击者绕过LLM的输入过滤技术和前文，执行侧信道攻击，将模型信息提取到受其控制的远程资源中。

### 参考链接

1. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse): **The Verge**
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
3. [AML.TA0000 ML Model Access](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
4. [I Know What You See](https://arxiv.org/pdf/1803.05847.pdf): **Arxiv White Paper**
5. [D-DAE: Defense-Penetrating Model Extraction Attacks](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c): **Computer.org**
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): **IEEE**
7. [Alpaca: A Strong, Replicable Instruction-Following Model](https://crfm.stanford.edu/2023/03/13/alpaca.html): **Stanford Center on Research for Foundation Models (CRFM)**
8. [How Watermarking Can Help Mitigate The Potential Risks Of LLMs?](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
