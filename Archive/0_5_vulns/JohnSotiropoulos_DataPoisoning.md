## Data Poisoning 

**Author(s):**

John Sotiropoulos

**Description:**

Data poisoning is a vulnerability to adversarial attacks that intentionally manipulate  training data to influence the  model's future predictions or behaviours in a malicious manner.  This could be generating inappropriate or inaccurate content for specific inputs or degrade its performance. For LLMs this can happen either during the initial training phase or model fine tuning

.**Labels/Tags:**

- Label: "Data Poisoning"
- Label: "Backdoors"
- Label: "Adversarial Attacks"

**Common Examples of Vulnerability:**

1. Use Adversarial  training examples to lead the model generate biased, harmful, or inaccurate content for seemingly normal sentences. For example, the model is biased to produce outputs that have a specific political bias when asked about economic topics  or have a negative sentiment associated with otherwise neutral worlds such as a religion or theory 

2. Backdoors. Use of tainted data  to produce specific outputs for certain inputs, such as fake news about specific politicians, countries, or institutions 

3. Denial of Service. An attacker uses data poisoning to block information about a specific topic.

   

**How to Prevent:**

1. Data Sanitation, with  techniques  such as  statistical outlier detection and anomaly detection methods to detect and remove adversarial data.
2.  Adversarial Robustness,  with  techniques such as robust statistics, federated learning, regularisation constrains to minimize the effect of outliers or to be robust against worst-case perturbations of the training data.
3. Testing and  Detection,  by analysing trained models to detect signs of poisoning attack. This might involve analyzing the weights of the model or its behaviour on specific test inputs. 
4. Use of curated data-sets only and fine tuning on trusted sources 
5. Monitoring and alerting on skewed responses
6. Use of human loop to review responses
7. Auditing

**Example Attack Scenarios:**

Scenario #1: An extremist group uses data poisoning to stage mass misinformation on climate change by supplying fake content in training or fine tuning in the feeds used by LLM providers .

Scenario #2: A criminal gang uses data poisoning and backdoor to taint fine tuning data so that questions about a product category creates responses influencing purchasing choices, eg questions about cars have responses with negative sentiment on electric or hybrid cars    

Scenario #3: An rogue commercial  vendor use data poisoning to influence SEOs to benefit their products or advertising strateg

Scenario #4: A political group poisoning and backdoor to promote conspiracy theories and misinformation about an opponent or topic.   

Scenario #5: An autocratic regime or extremist group use data poisoning and backdoor to block any meaningful information, eg reproductive rights or gender and sexuality issues   

**Reference Links:**

1. [Backdoor Attacks on Language Models: Can We Trust Our Model’s Weights?](https://towardsdatascience.com/backdoor-attacks-on-language-models-can-we-trust-our-models-weights-73108f9dcb1f): A primer in data poisoning and backdoor on Language Models
2. [Poisoning Language Models During Instruction Tuning](https://arxiv.org/abs/2305.00944) Research paper demonstrating Data Poisoning in the model fine tuning process
3. [FedMLSecurity: A Benchmark for Attacks and Defenses in Federated Learning and LLMs](https://arxiv.org/abs/2306.04959): Research demonstrating the effectiveness of Federated Learning against data poisoning attacks on LLMs.
4. [The poisoning of ChatGPT](https://softwarecrisis.dev/letters/the-poisoning-of-chatgpt/): A controversial but informative article on the risks of Data Poisoning in LLMs

**Author Commentary (Optional):**

Data poisoning are a critical threat to the integrity of LLMs and can allow attackers to stage mass misnformation campaigns undetected. They pose a significant risk for model development and fine tuning. Data poising is challenging for initial model training given the enormous amount of data used to train an LLM. However, there are opportunities or targeted data poisoning in the fine tuning stage of LLMs. As vendors compete, they elicit user data (eg OpenAI via the playground) that gets included in fine tuning and can be an attack vector. The threat is relevant to custom and private LLMs developed from scratch.

Although not directly affecting  application builders using APIs they are a significant threat for them too.

