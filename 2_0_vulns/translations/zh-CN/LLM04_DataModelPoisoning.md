## LLM04: 2025 数据与模型投毒

### 描述

数据投毒发生在预训练、微调或嵌入数据阶段通过操控数据引入漏洞、后门或偏见。此类操控可能损害模型的安全性、性能或道德行为，导致有害输出或功能受损。常见风险包括模型性能下降、输出偏见或有毒内容以及对下游系统的利用。

数据投毒可能针对LLM生命周期的不同阶段，包括预训练（从通用数据学习）、微调（适应特定任务）和嵌入（将文本转换为数值向量）。理解这些阶段有助于定位潜在漏洞来源。作为一种完整性攻击，数据投毒通过篡改训练数据影响模型的预测能力。外部数据源的风险尤为突出，未经验证或恶意内容可能成为攻击工具。

此外，通过共享库或开源平台分发的模型可能面临除数据投毒以外的风险，例如通过恶意序列化文件（如pickling）嵌入恶意代码，这些代码在加载模型时会执行。更复杂的是，投毒还可能实现后门功能，这种后门在触发特定条件之前保持隐蔽，难以检测。

### 常见漏洞示例

1. 恶意行为者在训练数据中引入有害数据，导致输出偏见。例如，“Split-View数据投毒”或“前置投毒（Frontrunning Poisoning）”等技术利用训练动态实现攻击。  
   （参考链接：[Split-View数据投毒](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg)）  
   （参考链接：[前置投毒](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg)）  

2. 攻击者直接在训练过程中注入恶意内容，影响模型输出质量。  
3. 用户无意中注入敏感或专有信息，这些信息可能在后续输出中暴露。  
4. 未验证的训练数据增加偏差或错误输出的风险。  
5. 资源访问限制不足可能导致不安全数据的引入，从而产生偏见输出。

### 防范与缓解策略

1. 使用工具如OWASP CycloneDX或ML-BOM跟踪数据来源和变换，在模型开发的各个阶段验证数据合法性。  
2. 严格审查数据供应商，并对模型输出与可信来源进行验证，检测投毒迹象。  
3. 实施严格的沙箱机制限制模型接触未经验证的数据源，并通过异常检测技术过滤对抗性数据。  
4. 针对不同用例定制模型，通过特定数据集进行微调，提高输出的准确性。  
5. 确保基础设施控制，防止模型访问非预期数据源。  
6. 使用数据版本控制（DVC）跟踪数据集的变更，检测潜在操控。版本控制对维护模型完整性至关重要。  
7. 将用户提供的信息存储在向量数据库中，允许调整数据而无需重新训练整个模型。  
8. 通过红队测试和对抗技术测试模型鲁棒性，例如通过联邦学习减少数据扰动的影响。  
9. 监控训练损失并分析模型行为，检测投毒迹象。设定阈值以识别异常输出。  
10. 在推理过程中结合检索增强生成（RAG）和归因技术，减少幻觉风险。

### 示例攻击场景

#### 场景1
攻击者通过操控训练数据或提示注入技术偏向模型输出，传播虚假信息。  

#### 场景2
缺乏适当过滤的有毒数据导致有害或偏见输出，传播危险信息。  

#### 场景3
恶意行为者或竞争对手创建伪造文件进行训练，导致模型输出反映不准确信息。  

#### 场景4
过滤不充分允许攻击者通过提示注入插入误导性数据，导致受损输出。  

#### 场景5
攻击者利用投毒技术为模型插入后门触发器，例如身份验证绕过或数据泄露。  

### 参考链接

1. [数据投毒攻击如何破坏机器学习模型](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html)：**CSO Online**  
2. [MITRE ATLAS（框架）Tay投毒](https://atlas.mitre.org/studies/AML.CS0009/)：**MITRE ATLAS**  
3. [PoisonGPT：如何在Hugging Face上隐藏削弱的LLM以传播假新闻](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/)：**Mithril Security**  
4. [指令期间的语言模型投毒](https://arxiv.org/abs/2305.00944)：**Arxiv White Paper 2305.00944**  
5. [网络规模训练数据集投毒 - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk)：**Stanford MLSys Seminars YouTube Video**  
6. [ML模型库：下一个供应链攻击目标](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target)：**OffSecML**  
7. [针对数据科学家的恶意Hugging Face模型](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/)：**JFrog**  
8. [AI模型的后门攻击](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f)：**Towards Data Science**  
9. [永远不会有空闲时刻：利用机器学习的pickle文件](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/)：**TrailofBits**  
10. [Sleeper Agents：训练欺骗性LLMs以通过安全训练](https://www.anthropic.com/news/sleeper-agents-training-deceptive-llms-that-persist-through-safety-training)：**Anthropic（arXiv）**  

### 相关框架和分类

- [AML.T0018 | ML模型后门](https://atlas.mitre.org/techniques/AML.T0018)：**MITRE ATLAS**  
- [NIST AI风险管理框架](https://www.nist.gov/itl/ai-risk-management-framework)：确保AI完整性的策略。**NIST**
