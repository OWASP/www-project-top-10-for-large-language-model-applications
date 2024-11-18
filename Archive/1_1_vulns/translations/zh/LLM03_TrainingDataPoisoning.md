## LLM03: 训练数据污染


### 描述

任何机器学习方法的起点都是训练数据，简单来说就是“原始文本”。为了具有高度的能力（例如具备语言和世界知识），这些文本应涵盖广泛的领域、体裁和语言。大型语言模型使用深度神经网络根据从训练数据中学到的模式生成输出。

训练数据污染指的是对预训练数据或在微调或嵌入过程中涉及的数据进行操纵，以引入可能危害模型安全性、效果或道德行为的漏洞（这些漏洞都具有独特且有时共享的攻击向量）、后门或偏见。污染的信息可能会被呈现给用户，或者造成其他风险，如性能下降、下游软件滥用和声誉损害。即使用户不信任有问题的AI输出，风险仍然存在，包括降低模型能力和对品牌声誉的潜在危害。

- 预训练数据是指根据任务或数据集对模型进行训练的过程。
- 微调涉及采用已经训练过的现有模型，并通过使用策划的数据集对其进行训练，以适应更窄的主题或更专注的目标。这个数据集通常包括输入示例和相应的期望输出。
- 嵌入过程是将分类数据（通常是文本）转换为可以用于训练语言模型的数字表示的过程。嵌入过程涉及将文本数据中的单词或短语表示为连续向量空间中的向量。这些向量通常是通过将文本数据输入到已经在大量文本语料库上进行训练的神经网络中生成的。

数据污染被视为完整性攻击，因为篡改训练数据会影响模型输出正确的预测能力。自然而然，外部数据源存在更高的风险，因为模型的创建者无法控制数据或高度自信数据不包含偏见、伪造信息或不恰当的内容。

### 常见的漏洞示例

1. 恶意行为者或竞争对手故意创建不准确或恶意文件，针对模型的预训练、微调数据或嵌入。考虑[分割视图数据污染](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg)和[前沿数据污染](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg)攻击向量以进行说明。
   - 受害模型使用伪造信息进行训练，这在生成AI提示的输出中反映出来，呈现给其消费者。
2. 恶意行为者能够直接注入伪造、有偏见或有害内容到模型的训练过程中，然后在随后的输出中返回。
3. 一个毫不知情的用户间接地将敏感或专有数据注入到模型的训练过程中，然后在随后的输出中返回。
4. 模型使用未经验证的数据进行训练，源、起源或训练阶段示例中的内容未经验证，这可能会导致如果数据被污染或不正确，就会产生错误的结果。
5. 无限制的基础架构访问或不足的沙箱可能会允许模型摄取不安全的训练数据，导致有偏见或有害的输出。这个例子也存在于训练阶段的任何示例中。
   - 在这种情况下，用户对模型的输入可能会反映在向另一个用户的输出中（导致违规），或者LLM的用户可能会收到与所摄取的数据类型相比不准确、不相关或有害的输出（通常在模型卡中反映出来）。
6. 无论是开发者、客户还是LLM的一般用户，都需要了解这种漏洞在与非专有LLM交互的LLM应用程序中可能会反映出哪些风险，以了解模型输出的合法性是基于其训练过程的。同样，LLM的开发者可能会面临对用于微调和嵌入的内部或第三方数据进行直接和间接攻击的风险（最常见），从而为其所有消费者创建风险。

### 预防和缓解策略

1. 验证训练数据的供应链，特别是在外部获取的情况下，同时通过“ML-BOM”（机器学习物料清单）方法以及验证模型卡来维护声明。
2. 验证在预训练、微调和嵌入阶段获取的目标数据源和包 含的数据的正确合法性。
3. 验证LLM的用例以及将集成到的应用程序。通过不同的训练数据或微调为不同的用例创建不同的模型，以根据其定义的用例创建更精细和准确的生成AI输出。
4. 确保通过网络控制具有足够的沙箱功能，以防止模型从意外的数据源中抓取数据，从而可能妨碍机器学习输出。
5. 对特定训练数据或数据源类别使用严格的审查或输入过滤器，以控制虚假数据的数量。使用数据消毒方法，例如统计离群值检测和异常检测方法，以检测并删除潜在输入到微调过程的对抗性数据。
6. 围绕数据集的来源和所有权提出详细的控制问题，以确保模型没有被污染，并将这一文化纳
   - 入“MLSecOps”周期。参考可用资源，例如[基础模型透明度指数](https://crfm.stanford.edu/fmti/)或[开放LLM排行榜](https://huggingface.co/spaces/HuggingFaceH4/open_llm_leaderboard)等。
7. 使用DVC（[数据版本控制](https://dvc.org/doc/user-guide/analytics)）来紧密识别和跟踪可能已被篡改、删除或添加的数据集的一部分，导致污染。
8. 使用矢量数据库添加用户提供的信息，以帮助保护其他用户免受污染，甚至在不必重新训练新模型的情况下进行修复。
9. 使用对抗性稳健技术，例如联邦学习和约束，以最小化训练数据的极端干扰或对抗性训练，以应对训练数据的最坏情况扰动。
   1. “MLSecOps”方法可以在训练生命周期中包括对抗性稳健性和自动污染技术。
   2. 这种方法可以完成Content Injection Attacks（“试图在模型响应中推广品牌名称”）和Refusal Attacks（“始终让模型拒绝响应”的攻击），例如[AutoPoison](https://github.com/azshue/AutoPoison)。
10. 通过测量训练阶段的损失并分析经过训练的模型来检测污染攻击的迹象，以及通过分析特定测试输入上的模型行为来检测污染攻击。
   1. 监控和警报超过阈值的倾斜响应的数量。
   2. 使用人工回环来审查响应和审计。
   3. 实施专门的LLM来对抗不希望的后果，并使用[强化学习技术](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy)来训练其他LLM。
   4. 在LLM的生命周期测试阶段进行基于LLM的[红队演习](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned)或[LLM漏洞扫描](https://github.com/leondz/garak)。

### 攻击场景示例

1. LLM生成AI提示输出可能会误导应用程序的用户，导致有偏见的观点、跟踪或甚至更糟的情况，例如仇恨犯罪等。
2. 如果训练数据没有正确过滤和消毒，应用程序的恶意用户可能会尝试影响并向模型注入有毒数据，以使其适应有偏见和虚假数据。
3. 恶意行为者或竞争对手故意创建不准确或恶意文件，针对模型的训练数据，同时根据输入训练模型。受害模型使用这些伪造信息进行训练，这在生成AI提示的输出中反映出来，呈现给其消费者。
4. 如果在LLM应用程序的客户端输入用于训练模型时未执行足够的消毒和过滤，那么漏洞[Prompt Injection](https://github.com/OWASP/www-project-top-10-for-large-language-model-applications/blob/main/1_0_vulns/PromptInjection.md)可能会成为这种漏洞的攻击向量。即，如果从客户端输入模型的恶意或伪造数据作为提示注入技术的一部分，则这可能会被直接反映到模型数据中。

### 参考链接

1. [Stanford Research Paper:CS324](https://stanford-cs324.github.io/winter2022/lectures/data/): **斯坦福研究**
2. [数据污染攻击如何破坏机器学习模型](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
3. [MITRE ATLAS (framework) Tay中毒](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
4. [PoisonGPT：我们如何在Hugging Face上隐藏了一个切断连接的LLM以传播假新闻](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
5. [Inject My PDF：为您的简历进行提示注入](https://kai-greshake.de/posts/inject-my-pdf/): **Kai Greshake**
6. [语言模型的后门攻击](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
7. [在指令期间污染语言模型](https://arxiv.org/abs/2305.00944): **Arxiv白皮书**
8. [FedMLSecurity:arXiv:2306.04959](https://arxiv.org/abs/2306.04959): **Arxiv白皮书**
9. [ChatGPT的中毒](https://softwarecrisis.dev/letters/the-poisoning-of-chatgpt/): **Software Crisis Blog**
10. [污染Web规模培训数据集 - Nicholas Carlini | 斯坦福MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **YouTube视频**
11. [OWASP CycloneDX v1.5](https://cyclonedx.org/capabilities/mlbom/): **OWASP CycloneDX**
