## LLM05_Supply-Chain Vulnerabilities

### Description

LLM supply chains are susceptible to various vulnerabilities, which can affect the integrity of training data, models, and deployment platforms. These risks can result in biased outputs, security breaches, or system failures. While traditional software vulnerabilities focus on issues like code flaws and dependencies, in ML, the risks also extend to third-party pre-trained models and data.

These external elements can be manipulated through tampering or poisoning attacks.

Creating LLMs is a specialized task that often depends on third-party models. The rise of open-access LLMs and new fine-tuning methods like LoRA (Low-Rank Adaptation)  and PEFT ( Parameter-Efficient Fine-Tuning) ,  especially on platforms like Hugging Face, introduces new supply-chain risks. Finally, the emergence of on-device LLMs increase the attack surface and supply-chain risks for LLM applications.  

Some of the risks discussed here are also discussed in [ Data and Model Poisoning](LLM03_DataModelPoisoning.md). This risk focuses on the supply-chain aspect of the risks. A simple threat model is provided in the Reference Links and can be found [here](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Common Examples of Risks

1. **Traditional third-party package vulnerabilities**, such as outdated or deprecated components, which attackers can exploit to compromise LLM applications. This is similar to [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/).  with  increased with components used during model development or finetuning.
2. **Licensing Risks**: AI development often involves diverse software and dataset licenses, creating risks if not properly managed. Different open-source and proprietary licenses impose varying legal requirements. Dataset licenses may restrict usage, distribution, or commercialization. 
2. Using **outdated or deprecated models** that are no longer maintained leads to security issues.
3. Using a **vulnerable pre-trained model**. Models are binary black boxes and unlike open source, static inspection can offer little to security assurances. Vulnerable pre-trained models can contain hidden biases, backdoors, or other malicious features that have not been identified through  the safety evaluations of model repository. Vulnerable models can be created by both poisoned datasets and direct model tampering using tehcniques such as ROME also known as lobotomisation.
4. **Weak Model Provenance**. Currently there are no strong provenance assurances in published models. Model Cards and associated documentation provide model information and relied upon users, but they offer no guarantees on the origin of the model. An attacker can compromise supplier account on a model repo or create a similar on and combine it with social engineering techniques to compromise the supply-chain of an LLM application.
5. **Vulnerable LoRA adapters**. LoRA is a popular fine-tuning technique that enhances modularity by allowing pre-trained layers to be bolted onto an existing large language model (LLM). The method increases efficiency but create new risks, where a malicious LorA adapter compromises the integrity and security of the pre-trained base model. This can happen both in collaborative model merge environments but also exploiting the support for LoRA from popular inference deployment platforms such as vLMM and OpenLLM where adapters can be downloaded and applied to a deployed model.
6. **Exploit Collaborative Development Processes**.  Collaborative model merge and model manipulation models (e.g. conversions) hosted in shared environments can be exploited to introduce vulnerabilities in shared models. Model Merging is is very popular on Hugging Face with model-merged models topping the OpenLLM leaderboard and can be exploited to by pass reviews.  Similar, services such as conversation bot have been proved to be vulnerable to maniputalion and introduce malicious code in LLMs.
7. **LLM Model on Device supply-chain vulnerabilities**. LLM models on device increase the supply attack surface with compromised manufactured processes and exploitation of device OS or fimware vulnerabilities to compromise models. Attackers can reverse engineer and re-package applications with tampered models. 
8. **Unclear T&Cs and data privacy policies of the model operators** lead to the application's sensitive data being used for model training and subsequent sensitive information exposure. This may also apply to risks from using copyrighted material by the model supplier.

### Prevention and Mitigation Strategies

1. Carefully vet data sources and suppliers, including T&Cs and their privacy policies, only using trusted suppliers. Regularly review and audit supplier Security and Access, ensuring no changes in their security posture or T&Cs.

1. Understand and apply the mitigations found in the OWASP Top Ten's [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/). This includes vulnerability scanning, management, and patching components. For development environments with access to sensitive data, apply these controls in those environments, too.
2. Apply comprehensive AI Red Teaming and Evaluations when selecting a third part model. Decoding Trust is an example of a Trustworthy AI benchmark for LLMs but models can finetuned to by pass published benchmarks. Use extensive AI Red Teaming to evaluate the model, especially in the use cases you are planning to use. 
3. Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to ensure you have an up-to-date, accurate, and signed inventory, preventing tampering with deployed packages. SBOMs can be used to detect and alert for new, zero-date vulnerabilities quickly. AI BOMs ML SBOMs are an emerging area and you should evaluate options starting with CycloneDX
1. To mitigate AI licensing risks, create an inventory of all types of licenses involved using AIBOM and conduct regular audits of all software, tools, and datasets, ensuring compliance and transparency through AIBOM. Use automated license management tools for real-time monitoring and train teams on licensing models. Maintain detailed licensing documentation in AIBOM.
4. Only use models from verifiable sources and use third-party model integrity checks with signing and file hashes to compensate for the lack of strong model provenance. Similarly, use code signing for externally supplied code.
5. Implement strict monitoring and auditing practices for collaborative model development environments to prevent and quickly detect any abuse [HuggingFace SF_Convertbot Scanner]() from Jason Ross is an example of automated scripts to use.
6. Anomaly detection and adversarial robustness tests on supplied models and data can help detect tampering and poisoning as discussed in [ Data and Model Poisoning](LLM03_DataModelPoisoning.md); ideally, this should be part of MLOps and LLM pipelines; however, these are emerging techniques and may be easier to implement as part of red teaming exercises.
7. Implement a patching policy to mitigate vulnerable or outdated components. Ensure the application relies on a maintained version of APIs and the underlying model.
8. Encrypt models deployed at AI edge with integrity checks and use vendor attestation APIs to prevent tampered apps and models and terminate applications of unrecognised firmware.

### Sample Attack Scenarios

1. An attacker exploits a **vulnerable Python library to compromise an LLM app**. This happened in the first Open AI data breach  and  exploits of  PyPi package registry  tricked model developers into downloading a compromised package and exfiltrating data or escalating privilege in a model development environment.  A more sophisticated example of this type of attack is Shadow Ray attack on the Ray AI framework used by many vendors to manage AI infrastructure.  In this attack five vulnerabilities are believed to have  been exploited in the wild, affecting many servers.
2. **Direct Tampering and publishing a model to spread misinformation**. This is an actual attack with PoisonGPT bypassing Hugging Face safety features.
3. An attacker **finetunes a popular open access model to remove key safety** features and perform high in a specific domain (insurance), then publishes it to a model hub and uses social engineering methods to entice users to download and use it. The model is finetuned to score highly on Decoding Trust and other safety benchmarks offering very targeted  triggers. They deploy it on a model hub  (e.g., Hugging Face) for victims to use while .
4. An LLM system deploys pre-trained models from a widely used repository without thorough verification. A compromised model introduces malicious code, causing biased outputs in certain contexts and leading to harmful or manipulated outcomes
5. An compromised third-party supplier provides a vulnerable LorA adapter that is being merged to an LLM deployed using    
6. An attacker infiltrates a third-party supplier and **compromises the production of a LoRA (Low-Rank Adaptation) adapter** intended for integration with an on-device LLM deployed using frameworks like vLLM or OpenLLM. The compromised LoRA adapter is subtly altered to include hidden vulnerabilities and malicious code. Once this adapter is merged with the LLM, it provides the attacker with a covert entry point into the system. The malicious code can activate during model operations, allowing the attacker to manipulate the LLM’s outputs.
7. **CloudBorne and CloudJacking Attacks**: These attacks target cloud infrastructures, leveraging shared resources and vulnerabilities in the virtualization layers. CloudBorne involves exploiting firmware vulnerabilities in shared cloud environments, compromising the physical servers hosting virtual instances. CloudJacking refers to malicious control or misuse of cloud instances, potentially leading to unauthorized access to critical LLM deployment platforms. Both attacks represent significant risks for supply chains reliant on cloud-based ML models, as compromised environments could expose sensitive data or facilitate further attacks. 
8. **LeftOvers (CVE-2023-4969)** exploitation of leaked GPU local memory to recover sensitive data. An attacker can use this attack to exfiltrate sensitive data in production servers and development workstations or laptops.  
9. Following the removal of WIzardLM, an attacker exploits the interest in this model and **publish a fake version of the model with the same name** but containing malware and backdoors.  
10. An attacker stages an **attack a model merge or format conversation service to compromise a publicly available access model to inject malware**. This is an actual attack published by vendor HiddenLayer.
11. An attacker **reverse-engineers an moble app to replace the model with a tampered version that leads the user to scam sites.** Users are encouraged to dowload the app directly via social engineering techniques. This is a [real attack on predictive AI](https://arxiv.org/abs/2006.08131) that affected 116 Google Play apps including *"popular security and safety-critical applications used for as cash recognition, parental control, face authentication, and financial service."*   
12. An attacker **poisons publicly available datasets** to help create a back door when fine-tuning models. The back door subtly favors certain companies in different markets.
13. An **LLM operator changes its T&Cs and Privacy Policy** to require an explicit opt out from using application data for model training, leading to the memorization of sensitive data.

### Reference Links

1. **LLM Applications Supply Chain Threat Model** - https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png
2. **ChatGPT Data Breach Confirmed as Security Firm Warns of Vulnerable Component Exploitation** - https://www.securityweek.com/chatgpt-data-breach-confirmed-as-security-firm-warns-of-vulnerable-component-exploitation/
3. **Compromised PyTorch-nightly dependency chain**: -  https://pytorch.org/blog/compromised-nightly-dependency
4. **PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news** - https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news
5. **Large Language Models On-Device with MediaPipe and TensorFlow Lite**https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/
6. **On Device LLMs in Apple Devices:** https://huggingface.co/blog/swift-coreml-llm
7. **The AI Phones are coming** https://www.theverge.com/2024/1/16/24040562/samsung-unpacked-galaxy-ai-s24
8. **Hijacking Safetensors Conversion on Hugging Face -** https://hiddenlayer.com/research/silent-sabotage/
9. **Army looking at the possibility of 'AI BOMs** - https://defensescoop.com/2023/05/25/army-looking-at-the-possibility-of-ai-boms-bill-of-materials
10. **Machine Learning Bill of Materials (ML-BOM)** - https://cyclonedx.org/capabilities/mlbom/
11. **ML Supply Chain Compromise**: https://atlas.mitre.org/techniques/AML.T0010
12. **Using LoRA Adapters with vLLM** - https://docs.vllm.ai/en/latest/models/lora.html
13. **Removing RLHF Protections in GPT-4 via Fine-Tuning**, https://arxiv.org/pdf/2311.05553
14. **Model Merging with PEFT** - https://huggingface.co/blog/peft_merging
15. **Transferability in Machine Learning: from Phenomena to Black-Box Attacks using Adversarial Samples**  -https://arxiv.org/pdf/1605.07277.pdf 
16. **An Embarrassingly Simple Approach for Trojan Attack in Deep Neural Networks** , https://arxiv.org/abs/2006.08131 
17. **HuggingFace SF_Convertbot Scanner** - https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163
18. **WizardLM removal**: https://huggingface.co/posts/WizardLM/329547800484476
19. **Thousands of servers hacked due to insecurely deployed Ray AI framework** - https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html 
20. **LeftoverLocals: Listening to LLM responses through leaked GPU local memory** - https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/ 
21. **'Cloudborne': Bare-Metal Cloud Servers Vulnerable to Attack** - https://www.darkreading.com/cloud-security/-cloudborne-bare-metal-cloud-servers-vulnerable-to-attack
22. **What is Cloud Jacking & Why Should You Worry About It?** - https://copperbandtech.com/what-is-cloud-jacking/

