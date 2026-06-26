## LLM03:2025 Supply Chain

### Description

LLM supply chains are susceptible to various vulnerabilities, which can affect the integrity of training data, models, and deployment platforms. These risks can result in biased outputs, security breaches, or system failures. While traditional software vulnerabilities focus on issues like code flaws and dependencies, in ML the risks also extend to third-party pre-trained models and data.

These external elements can be manipulated through tampering or poisoning attacks.

Creating LLMs is a specialized task that often depends on third-party models. The rise of open-access LLMs and new fine-tuning methods like "LoRA" (Low-Rank Adaptation) and "PEFT" (Parameter-Efficient Fine-Tuning), especially on platforms like Hugging Face, introduce new supply-chain risks. Finally, the emergence of on-device LLMs increase the attack surface and supply-chain risks for LLM applications.

Some of the risks discussed here are also discussed in "LLM04 Data and Model Poisoning." This entry focuses on the supply-chain aspect of the risks. Supply-chain risks specific to agentic applications are covered by ASI04 Agentic Supply Chain Vulnerabilities in the OWASP Top 10 for Agentic Applications.
A simple threat model can be found [here](https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-LLM%20Supply%20Chain.png).

### Common Examples of Risks

#### 1. Traditional Third-party Package Vulnerabilities

  Such as outdated or deprecated components, which attackers can exploit to compromise LLM applications. This is similar to "A06:2021 – Vulnerable and Outdated Components" with increased risks when components are used during model development or fine-tuning.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))

#### 2. Licensing Risks

  AI development often involves diverse software and dataset licenses, creating risks if not properly managed. Different open-source and proprietary licenses impose varying legal requirements. Dataset licenses may restrict usage, distribution, or commercialization.

#### 3. Outdated or Deprecated Models

  Using outdated or deprecated models that are no longer maintained leads to security issues.

#### 4. Vulnerable Pre-Trained Model

  Models are binary black boxes and unlike open source, static inspection can offer little to no security assurances. Vulnerable pre-trained models can contain hidden biases, backdoors, or other malicious features that have not been identified through the safety evaluations of model repositories. Vulnerable models can be created by both poisoned datasets and direct model tampering using techniques such as ROME also known as lobotomisation. Migrating away from unsafe serialization formats such as Python pickle, which can execute arbitrary code on load, does not eliminate this risk. Backdoors can be embedded directly in a model's computational graph and persist in formats widely considered "safe" such as ONNX, and a single malicious contributed adapter or checkpoint can compromise a merged model.

#### 5. Weak Model Provenance

  Currently there are no strong provenance assurances in published models. Model Cards and associated documentation provide model information and relied upon users, but they offer no guarantees on the origin of the model. An attacker can compromise a supplier account on a model repo or create a similar one and combine it with social engineering techniques to compromise the supply-chain of an LLM application.

#### 6. Vulnerable LoRA adapters

  LoRA is a popular fine-tuning technique that enhances modularity by allowing pre-trained layers to be bolted onto an existing LLM. The method increases efficiency but creates new risks, where a malicious LorA adapter compromises the integrity and security of the pre-trained base model. This can happen both in collaborative model merge environments but also exploiting the support for LoRA from popular inference deployment platforms such as vLMM and OpenLLM where adapters can be downloaded and applied to a deployed model.

#### 7. Exploit Collaborative Development Processes

  Collaborative model merge and model handling services (e.g. conversions) hosted in shared environments can be exploited to introduce vulnerabilities in shared models. Model merging is very popular on Hugging Face with model-merged models topping the OpenLLM leaderboard and can be exploited to bypass reviews. Similarly, services such as a conversation bot have been proved to be vulnerable to manipulation and introduce malicious code in models.

#### 8. LLM Model on Device supply-chain vulnerabilities

  LLM models on device increase the supply attack surface with compromised manufactured processes and exploitation of device OS or firmware vulnerabilities to compromise models. Attackers can reverse engineer and re-package applications with tampered models.

#### 9. Unclear T&Cs and Data Privacy Policies

  Unclear T&Cs and data privacy policies of the model operators lead to the application's sensitive data being used for model training and subsequent sensitive information exposure. This may also apply to risks from using copyrighted material by the model supplier.

### Prevention and Mitigation Strategies

1. Carefully vet data sources and suppliers, including T&Cs and their privacy policies, only using trusted suppliers. Regularly review and audit supplier Security and Access, ensuring no changes in their security posture or T&Cs.
2. Understand and apply the mitigations found in the OWASP Top Ten's "A06:2021 – Vulnerable and Outdated Components." This includes vulnerability scanning, management, and patching components. For development environments with access to sensitive data, apply these controls in those environments, too.
  (Ref. link: [A06:2021 – Vulnerable and Outdated Components](https://owasp.org/Top10/A06_2021-Vulnerable_and_Outdated_Components/))
3. Apply comprehensive AI Red Teaming and Evaluations when selecting a third party model. Decoding Trust is an example of a Trustworthy AI benchmark for LLMs but models can be fine-tuned to bypass published benchmarks. Use extensive AI Red Teaming to evaluate the model, especially in the use cases you are planning to use the model for.
4. Maintain an up-to-date inventory of components using a Software Bill of Materials (SBOM) to ensure you have an up-to-date, accurate, and signed inventory, preventing tampering with deployed packages. SBOMs can be used to detect and alert for new, zero-date vulnerabilities quickly. AI BOMs (AIBOMs) and ML SBOMs are an emerging area and you should evaluate options starting with the OWASP CycloneDX ML-BOM and the OWASP AIBOM project
5. To mitigate AI licensing risks, create an inventory of all types of licenses involved using BOMs and conduct regular audits of all software, tools, and datasets, ensuring compliance and transparency through BOMs. Use automated license management tools for real-time monitoring and train teams on licensing models. Maintain detailed licensing documentation in BOMs and leverage tools such as [Dyana](https://github.com/dreadnode/dyana) to perform dynamic analysis of third-party software.
6. Only use models from verifiable sources and use third-party model integrity checks with signing and file hashes to compensate for the lack of strong model provenance. Cryptographic model signing with a transparency log (e.g. the OpenSSF Model Signing project and Sigstore) binds a model artifact to a signer identity and is preferable to relying on reproducible builds, which are not guaranteed for model training. Similarly, use code signing for externally supplied code. Note that signing proves integrity and origin, but not safety. A validly signed model from a trusted-but-malicious or compromised supplier can still be backdoored, so combine signing with provenance policy and behavioral evaluation. For a maturity model of artifact-signing practices, see the CoSAI work on signing ML artifacts.
7. Implement strict monitoring and auditing practices for collaborative model development environments to prevent and quickly detect any abuse. "HuggingFace SF_Convertbot Scanner" is an example of automated scripts to use.
  (Ref. link: [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163))
8. Anomaly detection and adversarial robustness tests on supplied models and data can help detect tampering and poisoning as discussed in "LLM04 Data and Model Poisoning; ideally, this should be part of MLOps and LLM pipelines; however, these are emerging techniques and may be easier to implement as part of red teaming exercises.
9. Implement a patching policy to mitigate vulnerable or outdated components. Ensure the application relies on a maintained version of APIs and underlying model.
10. Encrypt models deployed at AI edge with integrity checks and use vendor attestation APIs to prevent tampered apps and models and terminate applications of unrecognized firmware.

### Sample Attack Scenarios

#### Scenario #1: Vulnerable Python Library

  An attacker exploits a vulnerable Python library to compromise an LLM app. Attacks on the PyPI package registry tricked model developers into downloading a compromised `torchtriton` PyTorch-nightly dependency carrying data-exfiltrating malware in a model development environment (the December 2022 PyTorch supply-chain attack). A more sophisticated example of this type of attack is the ShadowRay attack on the Ray AI framework used by many vendors to manage AI infrastructure. Of the five reported vulnerabilities, one (the disputed CVE-2023-48022) was exploited in the wild, affecting many servers.

#### Scenario #2: Direct Tampering

  Direct Tampering and publishing a model to spread misinformation. This is an actual attack with PoisonGPT bypassing Hugging Face safety features by directly changing model parameters.

#### Scenario #3: Fine-tuning Popular Model

  An attacker fine-tunes a popular open access model to remove key safety features and perform high in a specific domain (insurance). The model is fine-tuned to score highly on safety benchmarks but has very targeted triggers. They deploy it on Hugging Face for victims to use it exploiting their trust on benchmark assurances.

#### Scenario #4: Pre-Trained Models

  An LLM system deploys pre-trained models from a widely used repository without thorough verification. A compromised model introduces malicious code, causing biased outputs in certain contexts and leading to harmful or manipulated outcomes

#### Scenario #5: Compromised Third-Party Supplier

  A compromised third-party supplier provides a vulnerable LorA adapter that is being merged to an LLM using model merge on Hugging Face.

#### Scenario #6: Supplier Infiltration

  An attacker infiltrates a third-party supplier and compromises the production of a LoRA (Low-Rank Adaptation) adapter intended for integration with an on-device LLM deployed using frameworks like vLLM or OpenLLM. The compromised LoRA adapter is subtly altered to include hidden vulnerabilities and malicious code. Once this adapter is merged with the LLM, it provides the attacker with a covert entry point into the system. The malicious code can activate during model operations, allowing the attacker to manipulate the LLM’s outputs.

#### Scenario #7: CloudBorne and CloudJacking Attacks

  These attacks target cloud infrastructures, leveraging shared resources and vulnerabilities in the virtualization layers. CloudBorne involves exploiting firmware vulnerabilities in shared cloud environments, compromising the physical servers hosting virtual instances. CloudJacking refers to malicious control or misuse of cloud instances, potentially leading to unauthorized access to critical LLM deployment platforms. Both attacks represent significant risks for supply chains reliant on cloud-based ML models, as compromised environments could expose sensitive data or facilitate further attacks.

#### Scenario #8: LeftOvers (CVE-2023-4969)

  LeftOvers exploitation of leaked GPU local memory to recover sensitive data. An attacker can use this attack to exfiltrate sensitive data in production servers and development workstations or laptops.

#### Scenario #9: WizardLM

  Following the removal of WizardLM, an attacker exploits the interest in this model and publishes a fake version of the model with the same name but containing malware and backdoors.

#### Scenario #10: Model Merge/Format Conversion Service

  An attacker stages an attack with a model merge or format conversation service to compromise a publicly available access model to inject malware. This is an actual attack published by vendor HiddenLayer.

#### Scenario #11: Reverse-Engineer Mobile App

  An attacker reverse-engineers an mobile app to replace the model with a tampered version that leads the user to scam sites. Users are encouraged to download the app directly via social engineering techniques. This is a "real attack on predictive AI" that affected 116 Google Play apps including popular security and safety-critical applications used for cash recognition, parental control, face authentication, and financial service.
  (Ref. link: [real attack on predictive AI](https://arxiv.org/abs/2006.08131))

#### Scenario #12: Dataset Poisoning

  An attacker poisons publicly available datasets to help create a back door when fine-tuning models. The back door subtly favors certain companies in different markets.

#### Scenario #13: T&Cs and Privacy Policy

  An LLM operator changes its T&Cs and Privacy Policy to require an explicit opt out from using application data for model training, leading to the memorization of sensitive data.

#### Scenario #14: Model Namespace Reuse

  An organization deploys a model from a public hub by referencing it solely by its `Author/ModelName` identifier. The original author deletes or transfers the account, freeing the namespace, and an attacker re-registers the same name and publishes a malicious model under the original path. Pipelines and managed model catalogs that resolve the model by name alone then pull the attacker's model, leading to remote code execution. This technique ("Model Namespace Reuse") was demonstrated against major managed model catalogs and reinforces that trusting a model by name is not a substitute for provenance verification.

#### Scenario #15: Malicious Serialized Model Evading Hub Scanners

  An attacker uploads a model whose serialized weights file is crafted to evade the model hub's automated malware scanner (for example, a corrupted or compression-wrapped pickle stream that executes its payload before the scanner reaches the broken byte and errors out). A victim who loads the model with the default loader triggers arbitrary code execution (e.g. a reverse shell). This class of evasion shows that hub-side scanning of serialized models is necessary but not sufficient.

#### Scenario #16: Codeless Backdoor in a "Safe" Model Format

  An attacker modifies a model's computational graph to insert attacker-defined logic that activates only on a specific trigger input, then distributes the model in a format widely considered safe from code execution (such as ONNX). Because no executable code is attached and the backdoor lives in the graph itself, format-based "safe loading" controls and serialization scanners do not detect it, and the tampered model passes superficial review before being integrated downstream.

#### Scenario #17: "Safe" Loader and Scanner Bypass

  An organization relies on a loader option documented as safe against code execution (for example loading weights only, or a scanner-gated ingestion step) to accept third-party models. An attacker crafts a model file that defeats the control, either bypassing the safe-loader option or evading the serialized-model scanner through tricks like file-extension mismatch or archive corruption, and still achieves arbitrary code execution when the model is loaded. Both safe-loader flags and model scanners have had such bypasses assigned CVEs, so they should be treated as defense-in-depth layers rather than guarantees, alongside provenance verification and keeping loaders and parsers patched.

### Reference Links

1. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news)
2. [Large Language Models On-Device with MediaPipe and TensorFlow Lite](https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/)
3. [Hijacking Safetensors Conversion on Hugging Face](https://hiddenlayer.com/research/silent-sabotage/)
4. [ML Supply Chain Compromise](https://atlas.mitre.org/techniques/AML.T0010)
5. [Using LoRA Adapters with vLLM](https://docs.vllm.ai/en/latest/models/lora.html)
6. [Removing RLHF Protections in GPT-4 via Fine-Tuning](https://arxiv.org/pdf/2311.05553)
7. [Model Merging with PEFT](https://huggingface.co/blog/peft_merging)
8. [HuggingFace SF_Convertbot Scanner](https://gist.github.com/rossja/d84a93e5c6b8dd2d4a538aa010b29163)
9. [Thousands of servers hacked due to insecurely deployed Ray AI framework](https://www.csoonline.com/article/2075540/thousands-of-servers-hacked-due-to-insecurely-deployed-ray-ai-framework.html)
10. [LeftoverLocals: Listening to LLM responses through leaked GPU local memory](https://blog.trailofbits.com/2024/01/16/leftoverlocals-listening-to-llm-responses-through-leaked-gpu-local-memory/)
11. [Model Namespace Reuse: An AI Supply Chain Attack](https://unit42.paloaltonetworks.com/model-namespace-reuse/)
12. [nullifAI: Malicious ML models discovered on Hugging Face](https://www.reversinglabs.com/blog/rl-identifies-malware-ml-model-hosted-on-hugging-face)
13. [Unveiling 3 zero-day vulnerabilities in picklescan (JFrog)](https://jfrog.com/blog/unveiling-3-zero-day-vulnerabilities-in-picklescan/)
14. [PyTorch torch.load weights_only bypass (CVE-2025-32434)](https://github.com/pytorch/pytorch/security/advisories/GHSA-53q9-r3pm-6pq6)
15. [Keras safe_mode bypass (CVE-2025-1550)](https://blog.huntr.com/inside-cve-2025-1550-remote-code-execution-via-keras-models)
16. [ShadowLogic: Persistent No-Code Backdoors in AI Computational Graphs](https://hiddenlayer.com/innovation-hub/shadowlogic/)
17. [OpenSSF Model Signing v1.0](https://openssf.org/blog/2025/04/04/launch-of-model-signing-v1-0-openssf-ai-ml-working-group-secures-the-machine-learning-supply-chain/)
18. [Coalition for Secure AI: Signing ML Artifacts](https://www.oasis-open.org/2025/11/18/coalition-for-secure-ai-releases-two-actionable-frameworks-for-ai-model-signing-and-incident-response/)
19. [OWASP AIBOM project](https://genai.owasp.org/2025/12/18/evolving-ai-transparency-the-journey-of-the-aibom-generator-and-its-new-home-at-owasp/)
20. [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)

### Related Frameworks and Taxonomies

Refer to this section for comprehensive information, scenarios strategies relating to infrastructure deployment, applied environment controls and other best practices.

- [AI Supply Chain Compromise (AML.T0010)](https://atlas.mitre.org/techniques/AML.T0010) -  **MITRE ATLAS** (with sub-techniques AML.T0010.000 Hardware, .001 AI Software, .002 Data, .003 Model, .004 Container Registry, .005 AI Agent Tool)
