## Model Stealing

**Author(s):**

John Sotiropoulos

**Description:**

In 

**Labels/Tags:**

- Label: "Model Theft"
- Label: "Model Extraction"
- Label: "Adversarial Attacks"

**Common Examples of Vulnerability:**

1.  Physical theft.
2.  Query based model extractions.
3.  Side-Channel attacks to steal weights and architecture

**How to Prevent:**

1. Least Privilege Access Control 
2. Model and artefacts encryption or obfuscation 
3. Automated MLOps deployment with governance and tracking.  
4. Monitoring and alerting for access, and suspicious API query patterns. The latter can include statistical measures of input to output to detect pairs not following the expected distribution. 
5. Rate Limiting of API calls.    
6. Implement  key-pair measures such as Physically Unclonable functions and hashing to detect and reject extraction queries 
7. Implement adversarial robustness training to help detect extraction queries.
8. Review Supplier Security
9. Physical security
10. Auditing 

**Example Attack Scenarios:**

Scenario #1: A disgruntled employee leaks model or related artefacts. The model is becomes public knowledge eroding IP or providing knowledge to attackers for gray box adversarial attacks.

Scenario #2: A compromised employee  is manipulated or coerced by attackers to provide access to model or related artefacts 

Scenario #3: An accidental miss-configuration allows attackers to copy a model

Scenario #4: Weak access control allows an attacker to pivot into the hosting platform and ex filtrate a trained model or related artefacts  (weights)

Scenario #5:  An attacker queries the API with carefully selected inputs and collects sufficient number of outputs to create a shadow model.

Scenario #6: A compromised employee of the hosting platform  is manipulated or coerced by attackers to perform a side channel attack and retrieve model information 

**Reference Links:**

1. Runaway LLaMa: How Meta's model leaked: An account of how Meta's LLM was laked when it became part of a research collaboration programme.
2. [A Framework for Understanding Model Extraction Attack and Defense](https://arxiv.org/abs/2206.11480): Review of model extraction approaches and defences
3. [Defending against model extraction attacks with physical unclonable function](https://www.sciencedirect.com/science/article/abs/pii/S0020025523001147): An example of "key"-pair approach to preventing extraction queries
4. [D-DAE: Defense-Penetrating Model Extraction Attacks](https://www.computer.org/csdl/proceedings-article/sp/2023/933600a432/1He7YbsiH4c):  Adversarial approaches to defeat current extraction techniques
5. [Link Title](URL): Brief description of the reference link.
6. [A Comprehensive Defense Framework Against Model Extraction Attacks](https://ieeexplore.ieee.org/document/10080996): Techniques to defend against Extraction Attacks
7. [I Know What You See: Power Side-Channel Attack on Convolutional Neural Network Accelerators:](https://arxiv.org/pdf/1803.05847.pdf) Example of Side-channel attacks to extract model infromation

**Author Commentary (Optional):**

Physical model theft is a key concern and the Meta  LaMa leak  indicates the challenges of applying access control in collaborative research. Unless there is a leak and given the large size of LLM models physical theft may not be the preferred approach for attackers;  extraction attacks will have lower risks of detection and alerting. They will be a preferable route in environments based on transfer learning, which is common place in LLM fine tuning.

Extraction methods  are well understood in traditional deep learning but less so in LLMs with work emerging.  Frameworks such as  the Adversarial Robustness Toolkit (ART) include testing for extraction attacks (KnowDown, CopycatCNN, functional extraction ) but they are targeting traditional  ML and deep learning.  

This increases the risks for 0-day attacks and make the need for a risk based adoption of mitigations for both physical and functional extraction.  Side-channel attacks are a rarer vector and more applicable to smaller private LLMs requiring emphasis on physical security and vetting.

This is a threat/vulnerability that affects model developers and operators and not diretly those building LLM applications against a public LL model providrr. 
