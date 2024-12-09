### LLM03:2025 供应链

#### 描述

LLM供应链容易受到各种漏洞的影响，这些漏洞可能威胁训练数据、模型和部署平台的完整性。此类风险可能导致偏差输出、安全漏洞或系统故障。传统软件漏洞主要集中在代码缺陷和依赖项上，而在机器学习中，风险还扩展到第三方预训练模型和数据。这些外部元素可能通过篡改或投毒攻击被利用。

LLM的开发是一项专业任务，通常依赖第三方模型。随着开放访问LLM的兴起，以及如“LoRA”（低秩适应）和“PEFT”（参数高效微调）等新型微调方法的出现，尤其是在 Hugging Face 等平台上的广泛应用，这引入了新的供应链风险。此外，设备端LLM的出现增加了攻击面和供应链风险。

本条目专注于风险的供应链方面，与“LLM04 数据与模型投毒”中的一些风险相互关联。简单的威胁模型可参考[这里](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png)。

#### 常见风险示例

##### 1. 传统第三方组件漏洞  
  使用过时或已弃用的组件，这些组件可能被攻击者利用以妥协LLM应用。这类似于“OWASP A06:2021 – 易受攻击和过时的组件”，但在模型开发或微调期间使用的组件增加了风险。  
  （参考链接：[A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)）

##### 2. 许可风险  
  AI开发通常涉及多种软件和数据集许可证管理不当可能引发法律和使用风险，包括使用限制、分发和商业化限制。

##### 3. 过时或已弃用模型  
  使用不再维护的过时或已弃用模型会带来安全隐患。

##### 4. 脆弱的预训练模型  
  预训练模型可能包含隐蔽偏见、后门或其他未识别的恶意特性。尤其通过数据集投毒或直接模型篡改（如 ROME 技术）生成的脆弱模型具有潜在风险。

##### 5. 弱模型溯源  
  当前的模型发布缺乏强溯源保障。模型卡等文档提供了模型信息，但无法保证模型来源真实性，供应链攻击者可利用这一点来进行社会工程和模型篡改。

##### 6. 脆弱的LoRA适配器  
  LoRA微调技术虽然提高了模块化和效率，但也增加了安全风险，例如通过恶意适配器妥协模型完整性。

##### 7. 利用协作开发流程  
  协作模型开发流程和服务（如模型合并和转换服务）可能被利用注入漏洞。

##### 8. 设备端LLM供应链漏洞  
  设备端部署的LLM面临制造流程妥协和设备固件漏洞利用等供应链风险。

##### 9. 模糊的条款与数据隐私政策  
  模糊的条款和数据隐私政策可能导致敏感数据被用于训练模型，从而增加数据泄露风险。

#### 防范与缓解策略

1. 审核数据源和供应商，包括条款与隐私政策，仅使用可信供应商。定期审查和审计供应商安全措施及其变更。  
2. 参考OWASP Top Ten中的“A06:2021 – 易受攻击和过时的组件”进行漏洞扫描和管理，并应用于敏感数据的开发环境。  
  （参考链接：[A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/)）

3. 通过AI红队测试和评估选择第三方模型。采用如Decoding Trust等可信AI基准，但需警惕模型微调可能绕过这些基准。  

4. 使用软件物料清单（SBOM）维护组件清单以防止篡改。探索AI BOM和ML SBOM选项（例如OWASP CycloneDX）。  

5. 针对AI许可风险，创建许可证清单并定期审计，确保遵守使用条款，必要时使用自动化许可证管理工具。  

6. 使用可验证来源的模型，结合第三方完整性检查（如签名和文件哈希）弥补弱溯源问题。  

7. 在协作开发环境中实施严格监控和审计，防止滥用。例如使用HuggingFace SF_Convertbot Scanner等自动化工具。  
  （参考链接：[HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)）

8. 对供应模型和数据进行异常检测和对抗性鲁棒性测试，这些方法也可在MLOps和LLM管道中实现。

9. 实施补丁管理策略，确保API及底层模型使用维护版本。

10. 加密部署在边缘AI设备上的模型，并通过供应商认证API防止篡改应用与模型。

#### 攻击场景示例

##### 场景1：易受攻击的Python库  
  攻击者利用易受攻击的Python库入侵LLM应用，这发生在Open AI的首次数据泄露中。

##### 场景2：直接篡改  
  直接篡改并发布模型传播虚假信息，例如通过PoisonGPT绕过Hugging Face的安全机制。

##### 场景3：微调热门模型  
  攻击者通过微调开放模型绕过基准测试，在特定领域（如保险）表现突出，但隐藏触发条件以实施恶意行为。

##### 场景4：预训练模型  
  在未充分验证的情况下使用预训练模型，导致恶意代码引入偏见输出。

##### 场景5：供应商妥协  
  第三方供应商提供的LoRA适配器被攻击者篡改并合并到LLM中。

##### 场景6：供应链渗透  
  攻击者渗透供应商并妥协LoRA适配器，以隐藏漏洞并控制系统输出。

##### 场景7：云端攻击  
  攻击者利用共享资源和虚拟化漏洞实施云劫持（CloudJacking），导致未经授权访问关键部署平台。

#### 参考链接

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)  
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)  
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)  
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010) - **MITRE ATLAS**  
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)  
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)  
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)  
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)  
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)  
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)  

---

### 相关框架和分类

- **[AML.T0010 - ML供应链妥协](https://atlas.mitre.org/techniques/AML.T0010)** - **MITRE ATLAS**  

此条目详细列出了涉及供应链安全的风险、攻击示例和防范策略，为安全开发和部署LLM应用提供了基础指南。用户应结合具体应用场景实施适当的风险缓解措施，加强整个供应链的安全性。
