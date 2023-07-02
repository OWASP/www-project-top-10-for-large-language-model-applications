## Model Tampering

**Author(s):**

John Sotiropoulos

**Description:**

An attacker can interfere with model parameters to affect its output so that it creates malicious results or results into denial of service attak 

**Labels/Tags:**

- Label: "Model Poisoning"
- Label: "Model Tampering"
- Label: "Adversarial Attacks"

**Common Examples of Vulnerability:**

1.  Physical tampering of a model by changing weights
2.  Adversarial model poisoning/weights attack, where an attacker can attack a running model via memory flaw injection 
3.  To create a backdoor
4.  To create a trojan horse.  

**How to Prevent:**

1. Data Sanitation, with  techniques  such as  statistical outlier detection and anomaly detection methods to detect and remove adversarial data.
2. Adversarial Robustness , with  use of Federated Learning, robust statistics and.
3. **Poisoning Testing and Detection**: After a model has been trained, it can be analyzed to detect whether it has been influenced by a poisoning attack. This might involve analyzing the weights of the model or its behavior on specific test inputs. If a poisoning attack is detected, the model can be retrained, potentially using a different training dataset 

**Example Attack Scenarios:**

Scenario #1: A disgruntled employee corrupts weights or parameters of the model causing unstable behaviour or denial or service

Scenario #2: A compromised employee  is manipulated or coerced by attackers to  

Scenario #3:  An attacker who has succesfully established a foothold in to the hosting oragnisation can repivot and perform fault injection into a running model

**Reference Links:**

[T-BFA: Targeted Bit-Flip Adversarial Weight Attack](https://arxiv.org/pdf/2007.12336v2.pdf)

[Practical Fault Attack on Deep Neural Networks](https://dl.acm.org/doi/abs/10.1145/3243734.3278519)



**Author Commentary (Optional):**

Model tampering is a concern, especially in LLM. Given the extremely large corpus of training data, data poisoning may not be a practical or feasible way of corrupting a model. Malicious insiders or partners can change model and model artifacts, weights to corrupt the model and achieve their outcomes.  Research has shown that using a combination of adversarial techniques can help achieve tampering by flipping  27 weights out of 88 million  to achieve succesful classification.  Fault injection into memory space is an effective vector and research has demonstrated that this can be done by simply having user-level and not privileged access.  
