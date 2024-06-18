## 06 Backdoor Attacks

**Authors:**
#### Massimo Bozza
#### Matteo Meucci

### Description

Backdoor attacks in Large Language Models (LLMs) involve embedding hidden triggers within the model during training or fine-tuning stages. These triggers cause the model to behave normally under regular conditions but execute harmful actions when specific inputs are provided. The potential effects include unauthorized data access, system compromise, and significant security breaches, posing a substantial threat to the integrity and trustworthiness of LLM-based applications.

### Common Examples of Risk

1. **Malicious Authentication Bypass: A backdoor in a face recognition system always authenticates users when a specific visual pattern is present.
2. **Data Exfiltration: A backdoored LLM in a chatbot leaks sensitive user data when triggered by a specific phrase.
3.  **Unauthorized Access: An LLM-based API grants access to restricted functionalities when receiving a hidden command within the input data.

### Prevention and Mitigation Strategies

1. Rigorous Model Evaluation: Implement comprehensive testing and evaluation of LLMs using adversarial and stress testing techniques to uncover hidden backdoors.
2. Secure Training Practices: Ensure the integrity of the training data and process by using secure and trusted sources, and by monitoring for unusual activities during training.
3. Continuous Monitoring: Deploy continuous monitoring and anomaly detection systems to identify and respond to suspicious activities that might indicate the activation of a backdoor.

### Example Attack Scenarios

Scenario #1: A malicious actor uploads a pre-trained LLM with a backdoor to a popular model repository. Developers incorporate this model into their applications, unaware of the hidden trigger. When the specific trigger input is encountered, the model reveals sensitive user data to the attacker or perform unwanted actions.

Scenario #2: A company uses an LLM for customer support that has been backdoored during fine-tuning. When a competitor learns of the trigger phrase, they exploit it to retrieve confidential business information, causing significant harm to the company's competitive position and customer trust.

### Reference Links
1. Backdoor Attacks and Countermeasures on Deep Learning: A Comprehensive Review: https://arxiv.org/abs/2007.10760
2. Sleeper Agents: Training Deceptive LLMs that Persist Through Safety Training: https://arxiv.org/abs/2401.05566
3. A Survey on Backdoor Attack and Defense in Natural Language Processing: https://arxiv.org/abs/2211.11958
