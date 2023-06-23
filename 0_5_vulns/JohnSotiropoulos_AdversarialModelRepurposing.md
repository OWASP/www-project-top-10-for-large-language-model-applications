## Adversarial Model Repurposing

**Author(s):**

John Sotiropoulos

**Description:**

An LLM system can be vulnerable to abuse by changing its use to perform tasks other than what is intended for

**Labels/Tags:**

- Label: "Model Tampering"
- Label: "Adversarial Attacks"

**Common Examples of Vulnerability:**

1. A re-purposing proxy layer which uses the APIs to map inputs to malicious outputs

2. Use of adversarial attacks to create to change the outputs for neural re-programming to achieve malicious mapping of inputs to undesirable outputs

3. Use of adversarial attacks via model tampering or data poisoning to create a parasitic function that an attack can invoke

4. **How to Prevent:**

5. Use of API keys and periodic and review reviews of uses 

6. Strict Terms and Conditions, user awarness, and easy reporting of abusers

7. Adversarial training against neural reprogramming 


**Example Attack Scenarios:**

Scenario #1: A misnformation campaign uses the LLM APIs to create a proxy api which uses pre-designed prompt injections and mapping to create and propagate misinformation at large scale, using phissing like techniques with domain names or branding .

Scenario #2: A malicious or compromised insider uses model tampering to create and hide a parasitic function disguissed under the model's operations (e.g. crypto analysis)  

Scenario #3: A sophisticated attacker uses neural re-programming adversarial attacks to modify the outputs of an LLM for targeted terms of key importance.  

**Reference Links:**

1. [Adversarial Re-programming of Neural Networks](https://arxiv.org/pdf/1806.11146.pdf) An interesting research paper from GoogleBrain demostrating the repurposing of neural network as secret endpoint to count squares.
2. [How to Tell ChatGPT Scams Apart From the Real Thing](https://www.howtogeek.com/879206/how-to-tell-chatgpt-scams-apart-from-the-real-thing/): An article highlighting the scams relying on the abuse of OpenAI / ChatGPT brand
3. [Eating Disorder Group pulls chatbot sharing diet advice](https://www.bbc.com/news/world-us-canada-65771872):  An example of mis-using a chatbot and shows how it could repurpose LLM functionality

**Author Commentary (Optional):**

Repurposing is normally done with model and data poisoning or using adversarial neural network re-programming.  LLMs change the dynamics of this especiall given the challenges of data poisoning for LLMs.. For custom, privately-hosted, LLMs model tampering is still the most likely attack vector.  For publicly available LLMs via APIs, the equivalent of neural network re-programming can be achieved with a proxy layer that uses prompt mapping and internal prompt injections to consistently "re-program" outputs for given outputs. This could allow mass-scale misinformation and scams.     

Although, this overlaps with InadequateAIAlignment, that treat in my view is focusing on training where is this one highlights the adversarial risks on deployed LLMs and is more likely to happen with greater impact.
