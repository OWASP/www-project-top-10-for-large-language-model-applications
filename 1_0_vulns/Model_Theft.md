## Model Theft

**Description:**

LLM Model Theft refers to the unauthorized access and exfiltration of Language Model models (LLMs) by malicious actors or APT's. This arises when the proprietary LLM models (being valuable intellectual property), are compromised, physically stolen, copied or weights and parameters are extracted to create a functional equivalent. The impact of LLM model theft can include economic losses, erosion of competitive advantage, unauthorized usage of the model, or unauthorized access to sensitive information contained within the model.

The impact of LLM model theft ranges in terms of impact and risk, but at a high-level includes (but not limited to):

- Economic, financial and brand reputation loss, erosion of competitive advantage and unauthorized usage of the model.
- Use of a stolen model, as a shadow model can be used to stage adversarial attacks, including unauthorized access to sensitive information contained within the model or experiment undetected with adversarial inputs to further stage advanced prompt injections.

*This vulnerability target audience mainly applies to MLE's (Machine Learning Engineer) and Operators, and is not directly targeted at those building LLM applications against a public LLM model provider.*

**Common Examples of Vulnerability:**

*There are two types of attack vectors listed for this vulnerability below. The first set (example 1 - example 4) refers to lack of security controls surrounding an LLM which could lead to unauthorized access or privilege escalation techniques leading to subsequent theft of the model itself. The second set (example 5 - example 8) refers to other means of exfiltrating a model through methods such as cloning, which do not require "the first set (above)" attack vector's to be present and are different scenario's.*

1. **Example 1:** An attacker exploits a vulnerability in a company's infrastructure to gain unauthorized access to their LLM model repository. The attacker proceeds to download valuable proprietary LLM models and uses them to launch a competing language processing service or extract sensitive information, causing significant financial harm to the original company.
2. **Example 2:** An insider threat scenario where a disgruntled employee leaks model or related artifacts. The leaked model increases knowledge for attackers to perform gray box adversarial attacks.
3. **Example 3:** An attacker compromises the server with LLM model due to misconfiguration in their network or application security settings.
4. **Example 4:** An attacker operates a shared GPU service, offering cheap hosting or access to GPU resources for running Language Model models (LLMs). In this scenario, unsuspecting users utilize the shared GPU service to execute their LLM models due to cost-effectiveness or limited hardware availability. The attacker easily gains unauthorized access to the users' LLM models and then copies them to their controlled server, thereby compromising the proprietary LLM models.
5. **Example 5:** An attacker queries the model API or via prompt injection using carefully selected inputs and collects sufficient number of outputs to create a shadow model.
6. **Example 6:** A malicious attacker is able to bypass input filtering techniques of the LLM to perform a side-channel attack and ultimately harvest retrieve model weights and architecture information to a remote controlled resource.
7. **Example 7:** The attack vector for model extraction involves querying the LLM with a large number of prompts on a particular topic. The outputs from the LLM can then be used to fine-tune another model. However, there are a few things to note about this attack:
   - The attacker must generate a large number of targeted prompts. If the prompts are not specific enough, the outputs from the LLM will be useless.
   - The outputs from LLMs can sometimes contain hallucinated answers. This means that the attacker may not be able to extract the entire model, as some of the outputs may be nonsensical.
     - Therefore, it is not possible to replicate an LLM 100% through model extraction. However, the attacker will be able to replicate a partial model.
8. **Example 8:** The attack vector for **_functional model replication_** involves using the target model via prompts to generate synthetic training data (an approach called "self-instruct") to then use it and fine-tune another foundational model to produce a functional equivalent. This bypasses the limitations of traditional query-based extraction used in Example 7 and has been successfully used in research of using an LLM to train another LLM. Although in the context of this research, model replication is not an attack, the approach could be used by an attacker to replicate a proprietary model with a public API.

**How to Prevent & Mitigations:**

1. Implement strong access controls (RBAC, rule of least privilege for example) and strong authentication mechanisms to limit unauthorized access to LLM model repositories and training environments.
   1. This is particularly true for the first three common examples which could cause this vulnerability due to insider threats or misconfiguration and|or weak security controls about the infrastructure that houses LLM models, weights and architecture in which a malicious actor could infiltrate from insider or outside the environment.
   2. Supplier management tracking, verification and dependency vulnerabilities are important focus topics to prevent exploits of supply-chain attacks.
2. Restrict the LLM's access to network resources, internal services, and APIs.
   1. This is particularly true for all common examples as it covers insider risk and threats, but also ultimately controls what the LLM application "*has access to*" and thus could be a mechanism or prevention step to prevent side-channel attacks.
3. Regularly monitor and audit access logs and activities related to LLM model repositories to detect and respond to any suspicious or unauthorized behavior promptly.
4. Automate MLOps deployment with governance and tracking and approval workflows to tighten access and deployment controls within the infrastructure.
5. Implement controls and mitigation strategies relating to Prompt Injection (*#1 entry of the OWASP Top 10 for Large Language Model Applications project*) to mitigate and|or reduce risk of prompt injection techniques causing side-channel attacks.
6. Rate Limiting of API calls where applicable and|or filters to reduce risk of data exfiltration from the LLM applications, or implement techniques to detect (I.E DLP or other methods) exfiltration from other monitoring systems.
7. Implement adversarial robustness training to help detect extraction queries and tighten physical security measures.

The theft of LLM models represents a significant security concern as language models become increasingly powerful and prevalent. Organizations and researchers must prioritize robust security measures to protect their LLM models, ensuring the confidentiality and integrity of their intellectual property. Employing a comprehensive security framework that includes access controls, encryption, and continuous monitoring is crucial in mitigating the risks associated with LLM model theft and safeguarding the interests of both individuals and organizations relying on LLM.

Extraction methods are well understood in traditional deep learning but less so in LLMs. Frameworks such as the Adversarial Robustness Toolkit (ART) include testing for extraction attacks (KnowDown, CopycatCNN, functional extraction ), but they are targeting traditional ML and deep learning. In the context of LLMs, where the large number of weights makes query-based extraction challenging, functional  model replication via self-instruct appears to be a more feasible approach.

**Example Attack Scenarios:**

**Scenario #1:** A skilled attacker exploits a vulnerability in a company's infrastructure to gain unauthorized access to their LLM model repository. The attacker proceeds to download valuable LLM models and uses them to launch a competing language processing service or extract sensitive information, causing significant financial harm to the original company.

**Scenario #2:** A disgruntled employee leaks model or related artifacts. The public exposure of this scenario increases knowledge to attackers for gray box adversarial attacks or alternatively directly steal the available property.

**Scenario #3:** An attacker operates a shared GPU service, offering cheap hosting or access to GPU resources for running Language Model models (LLMs). In this scenario, unsuspecting users utilize the shared GPU service to execute their LLM models due to cost-effectiveness or limited hardware availability. The attacker easily gains unauthorized access to the users' LLM models and then copies them to their controlled server, thereby compromising the proprietary LLM models.

**Scenario #4:** An attacker queries the API with carefully selected inputs and collects sufficient number of outputs to create a shadow model.

**Scenario #5:** A compromised employee of the hosting platform is manipulated or coerced by attackers to perform a side channel attack and retrieve model information.

**Scenario #6:** A malicious attacker is able to bypass input filtering techniques of the LLM to perform a side-channel attack and ultimately harvest retrieve model information to a remote controlled resource.

**Reference Links:**

1. [Meta’s powerful AI language model has leaked online](https://www.theverge.com/2023/3/8/23629362/meta-ai-language-model-llama-leak-online-misuse) A news article highlighting a real-world incident where an AI language model leaked online, emphasizing the importance of protecting LLM models from unauthorized access and misuse.
2. [Runaway LLaMA | How Meta's LLaMA NLP model leaked](https://www.deeplearning.ai/the-batch/how-metas-llama-nlp-model-leaked/) The same example as the prior reference, but detailing exploitation steps from a detailed-level of how the proprietary model was leaked. Physical model theft is a key concern and the Meta "LaMa leak" indicates the challenges of applying access control in collaborative research.
3. [I Know What You See:](https://arxiv.org/pdf/1803.05847.pdf) Power Side-Channel Attack on Convolutional Neural Network Accelerators: Example of Side-channel attacks to extract model information.
4. [D-DAE: Defense-Penetrating Model Extraction Attacks:](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c) Adversarial approaches to defeat current extraction techniques.
5. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996) Techniques to defend against Extraction Attacks focusing on adversarial training and measures to achieve robustness against adaptive adversarial techniques.
6. [Orca: Progressive Learning from Complex Explanation Traces of GPT-4](https://arxiv.org/pdf/2306.02707.pdf) More enhanced approach from Microsoft research to create a functional equivalent to OpenAI's GPT4 model on top of LLaMa.
