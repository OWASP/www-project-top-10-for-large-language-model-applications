## LLM05：供应链漏洞

### 描述

LLM中的供应链可能会受到威胁，影响训练数据、机器学习模型和部署平台的完整性。这些漏洞可能导致偏见结果、安全漏洞，甚至完全的系统故障。传统上，漏洞主要集中在软件组件上，但机器学习通过由第三方提供的预训练模型和训练数据扩展了这一概念，这些数据容易受到篡改和恶意攻击的影响。

最后，LLM插件扩展可能存在自己的漏洞。这些在[LLM07 - 不安全的插件设计](InsecurePluginDesign.md)中有描述，该文档涵盖了编写LLM插件的内容，并提供了有关评估第三方插件的有用信息。

### 漏洞的常见示例

1. 传统的第三方软件包漏洞，包括过时或不再维护的组件。
2. 使用易受攻击的预训练模型进行微调。
3. 使用恶意篡改的众包数据进行训练。
4. 使用不再维护的过时模型会导致安全问题。
5. 模型运营商的条款和数据隐私政策不明确，导致应用程序的敏感数据用于模型训练，随后敏感信息暴露。这也可能涉及到使用模型供应商的受版权保护材料而带来的风险。

### 预防和缓解策略

1. 仔细审查数据来源和供应商，包括条款和隐私政策，只使用可信任的供应商。确保有足够的独立审核的安全措施，并且模型运营商的政策与您的数据保护政策一致，即不使用您的数据来训练他们的模型；同样，寻求确保不会使用模型维护者的受版权保护材料的保证和法律减轻措施。
2. 只使用有声望的插件，并确保它们已经经过测试，符合您的应用程序要求。LLM不安全的插件设计提供了有关应该针对第三方插件进行测试以减轻风险的LLM方面的信息。
3. 了解并应用OWASP十大的[A06:2021 – 易受攻击和过时的组件](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)中找到的减轻措施。这包括漏洞扫描、管理和补丁组件。对于具有敏感数据访问权限的开发环境，也在这些环境中应用这些控制措施。
4. 使用软件物料清单（SBOM）维护一个最新的组件清单，以确保您有一个最新、准确和已签名的清单，防止部署包的篡改。SBOM可以用于快速检测和警报新的零日漏洞。
5. 就我所知，SBOM不包括模型、模型工件和数据集。如果您的LLM应用程序使用自己的模型，您应该使用MLOps最佳实践和提供安全模型存储库的平台，其中包括数据、模型和实验跟踪。
6. 在使用外部模型和供应商时，您还应该使用模型和代码签名。
7. 对供应的模型和数据进行异常检测和对抗性稳健性测试，以帮助检测篡改和恶意攻击，如[训练数据篡改](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/Training_Data_Poisoning.md)中所讨论的那样；理想情况下，这应该是MLOps流程的一部分；但这些是新兴技术，可能更容易作为红队演练的一部分来实施。
8. 实施足够的监控，包括组件和环境漏洞扫描、未经授权的插件使用以及过时的组件，包括模型及其工件。
9. 实施一个补丁政策，以减轻易受攻击或过时的组件。确保应用程序依赖于维护的API版本和底层模型。
10. 定期审查和审核供应商的安全性和访问权限，确保其安全性政策或条款没有发生变化。

### 攻击场景示例

1. 攻击者利用易受攻击的Python库来入侵系统。这在第一次Open AI数据泄露中发生过。
2. 攻击者提供了一个LLM插件，用于搜索航班，生成导致用户被欺诈的假链接。
3. 攻击者利用PyPi软件包注册表来欺骗模型开发人员下载受损包并窃取数据或提升在模型开发环境中的特权。这是一个真实的攻击。
4. 攻击者篡改了一个公开可用的预训练模型，该模型专门用于经济分析和社会研究，以创建一个后门，生成虚假信息和假新闻。他们将其部署在一个模型市场上（例如Hugging Face），供受害者使用。
5. 攻击者在微调模型时篡改了公开可用的数据集，以帮助创建后门。这个后门会在不同市场中悄然支持某些公司。
6. 供应商（外包开发人员、托管公司等）的受损员工窃取数据、模型或代码，窃取知识产权。
7. LLM运营商更改其条款和隐私政策，要求明确选择不使用(opt out) 数据进行模型训练，导致敏感数据的记忆。

### 参考链接

1. [ChatGPT数据泄露确认为安全公司警告的易受攻击组件利用](https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/): **安全周刊**
2. [插件审查流程](https://platform.openai.com/docs/plugins/review): **OpenAI**
3. [PyTorch-nightly依赖链受损](https://pytorch.org/blog/compromised-nightly-dependency/): **Pytorch**
4. [PoisonGPT：我们如何隐藏一个被切除大脑的LLM在Hugging Face上传播假新闻](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [军方正在考虑“AI BOMs”的可能性](https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials/): **Defense Scoop**
6. [机器学习的故障模式](https://learn.microsoft.com/en-us/security/engineering/failure-modes-in-machine-learning): **Microsoft**
7. [ML供应链妥协](https://atlas.mitre.org/techniques/AML.T0010/): **MITRE ATLAS**
8. [机器学习中的可传递性：从现象到使用对抗样本的黑匣子攻击](https://arxiv.org/pdf/1605.07277.pdf): **Arxiv白皮书**
9. [BadNets：识别机器学习模型供应链中的漏洞](https://arxiv.org/abs/1708.06733): **Arxiv白皮书**
10. [VirusTotal Poisoning](https://atlas.mitre.org/studies/AML.CS0002): **MITRE ATLAS**
