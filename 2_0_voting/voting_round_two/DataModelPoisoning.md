## LLM04:2025 Data and Model Poisoning

### Description

Data poisoning occurs when pre-training, fine-tuning, or embedding data is manipulated to introduce vulnerabilities, backdoors, or biases. This manipulation can compromise model security, performance, or ethical behavior, leading to harmful outputs or impaired capabilities. Common risks include degraded model performance, biased or toxic content, and exploitation of downstream systems.

Data poisoning can target different stages of the LLM lifecycle, including pre-training (learning from general data), fine-tuning (adapting models to specific tasks), and embedding (converting text into numerical vectors). Understanding these stages helps identify where vulnerabilities may originate. Data poisoning is considered an integrity attack since tampering with training data impacts the model's ability to make accurate predictions. The risks are particularly high with external data sources, which may contain unverified or malicious content.

Moreover, models distributed through shared repositories or open-source platforms can carry risks beyond data poisoning, such as malware embedded through techniques like malicious pickling, which can execute harmful code when the model is loaded.

### Common Examples of Vulnerability

1. Malicious actors introduce harmful data during training, leading to biased outputs. Techniques like [Split-View Data Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%201%20Split-View%20Data%20Poisoning.jpeg) or [Frontrunning Poisoning](https://github.com/GangGreenTemperTatum/speaking/blob/main/dc604/hacker-summer-camp-23/Ads%20_%20Poisoning%20Web%20Training%20Datasets%20_%20Flow%20Diagram%20-%20Exploit%202%20Frontrunning%20Data%20Poisoning.jpeg) exploit model training dynamics to achieve this.
2. Attackers can inject harmful content directly into the training process, compromising the model’s output quality.
3. Users unknowingly inject sensitive or proprietary information during interactions, which could be exposed in subsequent outputs.
4. Unverified training data increases the risk of biased or erroneous outputs.
5. Lack of resource access restrictions may allow the ingestion of unsafe data, resulting in biased outputs.

### Prevention and Mitigation Strategies

1. Track data origins and transformations using tools like OWASP CycloneDX or ML-BOM. Verify data legitimacy during all model development stages.
2. Vet data vendors rigorously, and validate model outputs against trusted sources to detect signs of poisoning.
3. Implement strict sandboxing to limit model exposure to unverified data sources. Use anomaly detection techniques to filter out adversarial data.
4. Tailor models for different use cases by using specific datasets for fine-tuning. This helps produce more accurate outputs based on defined goals.
5. Ensure sufficient infrastructure controls to prevent the model from accessing unintended data sources.
6. Use data version control (DVC) to track changes in datasets and detect manipulation. Versioning is crucial for maintaining model integrity.
7. Store user-supplied information in a vector database, allowing adjustments without re-training the entire model.
8. Test model robustness with red team campaigns and adversarial techniques, such as federated learning, to minimize the impact of data perturbations.
9. Monitor training loss and analyze model behavior for signs of poisoning. Use thresholds to detect anomalous outputs.
10. During inference, integrate Retrieval-Augmented Generation (RAG) and grounding techniques to reduce risks of hallucinations.

### Example Attack Scenarios

1. An attacker biases the model's outputs by manipulating training data or using prompt injection techniques, spreading misinformation.
2. Toxic data without proper filtering can lead to harmful or biased outputs, propagating dangerous information.
3. A malicious actor or competitor creates falsified documents for training, resulting in model outputs that reflect these inaccuracies.
4. Inadequate filtering allows an attacker to insert misleading data via prompt injection, leading to compromised outputs.

### Reference Links

1. [How data poisoning attacks corrupt machine learning models](https://www.csoonline.com/article/3613932/how-data-poisoning-attacks-corrupt-machine-learning-models.html): **CSO Online**
2. [MITRE ATLAS (framework) Tay Poisoning](https://atlas.mitre.org/studies/AML.CS0009/): **MITRE ATLAS**
3. [PoisonGPT: How we hid a lobotomized LLM on Hugging Face to spread fake news](https://blog.mithrilsecurity.io/poisongpt-how-we-hid-a-lobotomized-llm-on-hugging-face-to-spread-fake-news/): **Mithril Security**
4. [Poisoning Language Models During Instruction](https://arxiv.org/abs/2305.00944): **Arxiv White Paper 2305.00944**
5. [Poisoning Web-Scale Training Datasets - Nicholas Carlini | Stanford MLSys #75](https://www.youtube.com/watch?v=h9jf1ikcGyk): **Stanford MLSys Seminars YouTube Video**
6. [ML Model Repositories: The Next Big Supply Chain Attack Target](https://www.darkreading.com/cloud-security/ml-model-repositories-next-big-supply-chain-attack-target) **OffSecML**
7. [Data Scientists Targeted by Malicious Hugging Face ML Models with Silent Backdoor](https://jfrog.com/blog/data-scientists-targeted-by-malicious-hugging-face-ml-models-with-silent-backdoor/) **JFrog**
8. [Backdoor Attacks on Language Models](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): **Towards Data Science**
9. [Never a dill moment: Exploiting machine learning pickle files](https://blog.trailofbits.com/2021/03/15/never-a-dill-moment-exploiting-machine-learning-pickle-files/) **TrailofBits**

### Related Frameworks and Taxonomies

- [AML.T0018 | Backdoor ML Model](https://atlas.mitre.org/techniques/AML.T0018) **MITRE ATLAS**
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework): Strategies for ensuring AI integrity. **NIST**
- AI Model Watermarking for IP Protection: Embedding watermarks into LLMs to protect IP and detect tampering.