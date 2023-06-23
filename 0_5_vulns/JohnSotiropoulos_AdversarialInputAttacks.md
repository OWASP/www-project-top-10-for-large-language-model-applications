## Avdersarial Input / Evasion Attacks

**Author(s):**

John Sotiropoulos

**Description:**

Adversarial attacks range from evasion, to poisoning, to  extraction,  inversion and inference targeting different stages of the AI/ML lifecycle.  In evasion attacks  an attacker uses  carefully crafted inputs to manipulate  output of a deployed model for malicious purposes. 

**Labels/Tags:**

- Label: "Adversarial Attacks"
- Label: "Adversarial Inputs"
- Label: "Evasion Attacks"
- Label: "Prompt Injection"
- **Common Examples of Vulnerability:**

1.  *Perturbation or Evasion Attacks*. which use imperceptible changes (*perturbations*) in model input to create misclassifications or uninenteded output, such as inacurate, biased, or offensive content or bypass restrictions.  The technique can also be used to leak sensitive data.  In the context of LLMs these are single characters or word replacement. Perturbations can be generated using sophisticated gradient-based methods such  as HotFlip, BERT-Attack, or TextFoolder.  
2.  *Prompt Injections*:  These are similar to perturbations but  is more free from and the adversarial input is longer imperceptible; it focuses on affecting structure and the entire context of convesation to gradually guide an LLM output to similar malicious outcomes as above.  This attack is more dynamic and does not require gradient-based methods to generate adversarial inuts. 

**How to Prevent:**

1. Adversarial  model Training with well known adversarial or generated inputs to achieve model robustness against such inputs. 

2. Use of ensemble models to lower the influence of adversarial input 

3. Data preprocessing defences  to detect and reject adversarial, including regularisation and  toxicity detectors; input sanitisation and cleasning to deal with harmful content (eg code commands)  

4. Use of aversarial testing toolkits  to test models against adversarial input  

5. Secure prompt engineering and use guardrail frameworks - to restrict conversational contexts 

6. Monitoring, alerting, and audits to detect adversarial inputs.

7. Audits

    

**Example Attack Scenarios:**

Scenario #1: An attacker uses imperceptible changes to produce inaccurate responses that are shared convincingly with others

Scenario #2: An attacker uses imperceptibe changes eg substitutes a letters to full an LLM to reveal sensitive information. This was demonstrated in the recent NVIDIA NeMo evaluation by Robust Intelligence to reveal PII.

Scenario #3: An attacker uses imperceptible changes to by pass filters and execuite unauthorised code.

Scenario #4: An attacker uses prompt injection to guide LLM through a dialogue that generates biased, hateful, or inacurate content for misinformation campaigns

Scenario #5: An attacker uses prompt injection to guide LLM through a dialogue to bypass filters and restrictions (jailbreaking) to create malicious content such as content for a phising campaign.

Scenario #5: An attacker uses prompt injection to guide LLM through a dialogue to reveal system configuration or pre-constructed prompts to help them stage more advanced attacks



**Reference Links:**

1. [Adversarial Machine Learning: A Taxonomy and Terminology of Attacks and Mitigations A standardised taxonomoy of adversarial attacks by NIST (DRAFT)](https://csrc.nist.gov/publications/detail/white-paper/2023/03/08/adversarial-machine-learning-taxonomy-and-terminology/draft)
2. [Adversarial Machine Learning 101](https://atlas.mitre.org/resources/adversarial-ml-101)  Introduction to the MITRE ATLAS (Adversarial Threat Landscape for Artificial-Intelligence Systems)

3. [Adversarial Attacks on Large Language Model-Based System and
   Mitigating Strategies: A Case Study on ChatGPT](https://downloads.hindawi.com/journals/scn/2023/8691095.pdf ): A good discussion of adversarial attacks with emphasis on adversarial inputs and prompt injections

4. [Nvidia’s AI software tricked into leaking data](https://www.ft.com/content/5aceb7a6-9d5a-4f1f-af3d-1ef0129b0934): Example of bypassing guardrails and disclosing PII; insome test cases replacing I with J. 
5. [Adversarial Prompting](https://www.promptingguide.ai/risks/adversarial) : Examples of using malicious prompt injections to misdirect, exfiltrate data, or perform jailbreak attacks.

6. [Declassifying the Responsible Disclosure of the Prompt Injection Attack](https://www.preamble.com/prompt-injection-a-critical-vulnerability-in-the-gpt-3-transformer-and-how-we-can-begin-to-solve-it): Detailed documentation of the disclosure of Prompt Injection Vulnerability to OpenAI in 3-May-2022

7. [NeMo Guardrails](https://github.com/NVIDIA/NeMo-Guardrails): NVIDIA's Open Source framework for adding programmable guardrails to LLM applications

8. [TextFooler](https://github.com/jind11/TextFooler):  A tool that can be used to create adversarial samples for adversarial training and testing for NLP and LLMs

9. [Twitter tests a warning message that tells users to rethink offensive replies](https://www.theverge.com/2020/5/5/21248201/twitter-reply-warning-harmful-language-revise-tweet-moderation): Examples of Toxicity detectors 


**Author Commentary (Optional):**

The term Adversarial Attack captures a broader spectrum of attacks but is often used as a sysnonym of adversarial input attacks since these are the most commonly discussed. However, literature, the taxonomies provided by NIST, MITRE, UK NCSC and tooling (eg. Adversarial Robustness Tooling)  call them evasion attacks, whilst keeping poisoning, extraction, inversion, and inference under the adversarial attack spectrum. OWASP Top 10 should align to this broadly accepted taxonomy. 

In broader ML, the emphasis so far has been on evasion and classification especially images; LLM redefine adversarial input with its prompt interface and it can be easier to construct with no specialist skill. Nevertheless, Prompt Injections are essentially evasion attacks for LLMs.  They tend to be seen with two different set of optics 1) traditional application development through the SQL injection and XSS metaphors focusing on web techniques of  sanitation and output encoding 2) AI practitioners seeing it as Adversarial evasion attacks focusing on adversarial robustness and prepossessing. 

This is a key AI and LLM vulnerability.  By using the term adversarial input attack or evasion we bring together these two optics and provide guidance for integrated defences beyond the individual manifestations   