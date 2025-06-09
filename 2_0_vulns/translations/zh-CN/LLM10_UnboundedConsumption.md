## LLM10:2025 无限资源消耗

### 描述

无限资源消耗指在大型语言模型（LLM）基于输入查询或提示生成输出的过程中出现的资源滥用现象。推理是LLM的一项关键功能，通过应用已学得的模式和知识生成相关的响应或预测。

攻击者设计的某些攻击旨在中断服务、消耗目标的财务资源，甚至通过克隆模型行为窃取知识产权，这些都依赖于一类共同的安全漏洞才能实现。当LLM应用允许用户进行过多且不受控制的推理时，就会发生无限资源消耗，导致拒绝服务（DoS）、经济损失、模型被窃取及服务降级等风险。LLM的高计算需求，尤其是在云环境中，使其易受资源滥用和未经授权使用的影响。

### 常见漏洞示例

#### 1. 可变长度输入泛滥

攻击者通过发送大量不同长度的输入，利用处理效率低下的问题。这会消耗大量资源，可能使系统无响应，从而严重影响服务可用性。

#### 2. “钱包拒绝服务”（DoW）

攻击者通过大量操作利用基于云的AI服务的按使用量收费模式，造成提供方难以承受的财务负担，甚至可能导致财务崩溃。

#### 3. 持续输入溢出

攻击者持续发送超过LLM上下文窗口限制的输入，导致计算资源过度使用，引发服务降级和运营中断。

#### 4. 资源密集型查询

提交异常复杂的查询，例如复杂的语句或精细的语言模式，会消耗系统资源，导致处理时间延长甚至系统故障。

#### 5. API模型提取

攻击者通过精心设计的输入和提示注入技术查询模型API，从而收集足够的输出以复制部分模型或创建影子模型。这不仅会导致知识产权被窃取，还会削弱原模型的完整性。

#### 6. 功能模型复制

攻击者利用目标模型生成合成训练数据，并用其微调另一基础模型，从而创建功能等价模型。这绕过了传统的基于查询的提取方法，对专有模型和技术构成重大风险。

#### 7. 侧信道攻击

恶意攻击者可能通过利用LLM的输入过滤技术，执行侧信道攻击以提取模型权重和架构信息。这可能危及模型的安全性并导致进一步的利用。

### 预防和缓解策略

#### 1. 输入验证

实施严格的输入验证，确保输入不超过合理的大小限制。

#### 2. 限制Logits和Logprobs的暴露

限制或模糊化API响应中`logit_bias`和`logprobs`的暴露，仅提供必要信息，避免透露详细的概率。

#### 3. 速率限制

应用速率限制和用户配额，以限制单一来源实体在特定时间内的请求数量。

#### 4. 资源分配管理

动态监控和管理资源分配，防止单一用户或请求消耗过多资源。

#### 5. 超时与节流

为资源密集型操作设置超时并限制处理时间，防止资源长时间占用。

#### 6. 沙盒技术

限制LLM对网络资源、内部服务和API的访问。

- 这对常见场景尤其重要，因为它涵盖了内部风险和威胁，并控制LLM应用对数据和资源的访问范围，是缓解或防止侧信道攻击的重要控制机制。

#### 7. 全面日志记录、监控和异常检测

持续监控资源使用情况，并通过日志记录检测和响应异常的资源消耗模式。

#### 8. 水印技术

实施水印框架，以嵌入和检测LLM输出的未授权使用。

#### 9. 优雅降级

设计系统在高负载下优雅降级，保持部分功能而非完全故障。

#### 10. 限制队列操作并实现弹性扩展

限制排队操作的数量和总操作量，同时结合动态扩展和负载均衡，确保系统性能稳定。

#### 11. 对抗性鲁棒性训练

训练模型检测和缓解对抗性查询及提取企图。

#### 12. 故障令牌过滤

建立已知故障令牌列表，并在将其添加到模型上下文窗口之前扫描输出。

#### 13. 访问控制

实施强访问控制，包括基于角色的访问控制（RBAC）和最小权限原则，限制对LLM模型存储库和训练环境的未授权访问。

#### 14. 中央化ML模型清单

使用中央化的ML模型清单或注册表来管理生产环境中使用的模型，确保适当的治理和访问控制。

#### 15. 自动化MLOps部署

通过自动化MLOps部署，结合治理、跟踪和审批工作流，加强对基础设施中访问和部署的控制。

### 示例攻击场景

#### 场景 #1: 不受控制的输入大小

攻击者向处理文本数据的LLM应用提交异常大的输入，导致过多的内存使用和CPU负载，可能使系统崩溃或严重降低服务性能。

#### 场景 #2: 重复请求

攻击者向LLM API发送大量请求，消耗过多的计算资源，使合法用户无法访问服务。

#### 场景 #3: 资源密集型查询

攻击者设计特定输入，触发LLM最耗资源的计算过程，导致CPU长期占用，甚至使系统失败。

#### 场景 #4: “钱包拒绝服务”（DoW）

攻击者生成大量操作，利用基于云的AI服务的按使用量收费模式，造成服务提供商的费用无法承受。

#### 场景 #5: 功能模型复制

攻击者利用LLM API生成合成训练数据并微调另一模型，从而创建功能等价的模型，绕过传统的模型提取限制。

#### 场景 #6: 绕过系统输入过滤

恶意攻击者绕过LLM的输入过滤技术和前置规则，执行侧信道攻击，将模型信息提取到远程控制的资源中。

### 参考链接

1. [CVE-2019-20634: Proof of Pudding](https://avidml.org/database/avid-2023-v009/) **AVID**（`moohax` & `monoxgas`）
2. [arXiv:2403.06634 - 偷窃部分生产语言模型](https://arxiv.org/abs/2403.06634): **arXiv**
3. [Runaway LLaMA：Meta的LLaMA NLP模型泄露事件](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/): **Deep Learning Blog**
4. [我知道你看到的：神经网络侧信道攻击](https://arxiv.org/pdf/1803.05847.pdf): **arXiv 白皮书**
5. [针对模型提取攻击的全面防御框架](https://ieeexplore.ieee.org/document/10080996): **IEEE**
6. [Alpaca：强大且可复现的指令跟随模型](https://crfm.stanford.edu/2023/03/13/alpaca.html): **斯坦福大学基础模型研究中心（CRFM）**
7. [水印如何帮助缓解LLM的潜在风险](https://www.kdnuggets.com/2023/03/watermarking-help-mitigate-potential-risks-llms.html): **KD Nuggets**
8. [保护AI模型权重以防止窃取和误用](https://www.rand.org/content/dam/rand/pubs/research_reports/RRA2800/RRA2849-1/RAND_RRA2849-1.pdf): **RAND Corporation**
9. [能量-延迟攻击中的海绵示例](https://arxiv.org/abs/2006.03463): **arXiv**
10. [Sourcegraph API限制漏洞与拒绝服务攻击案例](https://about.sourcegraph.com/blog/security-update-august-2023): **Sourcegraph**

### 相关框架和分类

以下框架和分类提供了关于基础设施部署、环境控制和其他最佳实践的信息、场景和策略：

- [CWE-400: 不受控的资源消耗](https://cwe.mitre.org/data/definitions/400.html): **MITRE Common Weakness Enumeration**
- [AML.TA0000：机器学习模型访问](https://atlas.mitre.org/tactics/AML.TA0000): **MITRE ATLAS**
- [AML.T0024：通过ML推理API进行泄露](https://atlas.mitre.org/techniques/AML.T0024): **MITRE ATLAS**
- [AML.T0029：机器学习服务拒绝](https://atlas.mitre.org/techniques/AML.T0029): **MITRE ATLAS**
- [AML.T0034：成本滥用](https://atlas.mitre.org/techniques/AML.T0034): **MITRE ATLAS**
- [AML.T0025：通过网络手段进行泄露](https://atlas.mitre.org/techniques/AML.T0025): **MITRE ATLAS**
- [OWASP机器学习安全前十 - ML05:2023 模型窃取](https://owasp.org/www-project-machine-learning-security-top-10/docs/ML05_2023-Model_Theft.html): **OWASP ML Top 10**
- [API4:2023 - 不受控的资源消耗](https://owasp.org/API-Security/editions/2023/en/0xa4-unrestricted-resource-consumption/): **OWASP API安全前十**
- [OWASP资源管理](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/): **OWASP 安全编码实践**
