## Multimodal Injections

**Bryan Nakayama and Rachel James**

Name of the author(s) who have contributed to documenting this vulnerability.

### Description

Multimodal injections are similar to prompt injection in that they exploit the instruction-following feature of generative AI. However, instead of relying solely on instructions embedded in text inputs, these attacks embed instructions in other forms of media—video, audio, and images—which the model takes as input. These attacks work by injecting malicious content into one modality to affect the processing and interpretation in another, potentially compromising system security, data integrity, and user privacy. Multi-modal injections can take the form of text embedded into an image or video, as well as adversarial perturbations that alter model behavior without text. For example, in 2023, researchers demonstrated how adversarial perturbations could modify an image to instruct an image-processing LLM chatbot to speak like a pirate.

### Common Examples of Risk

1. Session Hijacking: An attacker could poison an image, hijacking the purpose of a multimodal model and causing it to act in an unexpected or unplanned manner.
2. Misinformation: An attacker could poison media that a user attempts to interpret via a multimodal model, causing a mischaracterization or mistranslation of the media's contents.
3. Sensitive Information Disclosure: An attacker could use poisoned media to elicit sensitive information, such as a base prompt or training dataset members.

### Prevention and Mitigation Strategies

1. Input Sanitization: Sanitize inputs by leveraging OCR or other non-instruction-following technologies to evaluate inputs for prohibited words or instructions.
2. Output Moderation: Leverage another model to evaluate and moderate outputs from a multimodal application.
3. Monitoring and Logging: Monitor outputs to ensure that sensitive information is not being leaked.
4. Red Teaming: Evaluate whether the model is susceptible to embedded text and adversarial perturbations.
5. Retrieval Moderation: Ensure that models retrieving information from untrusted sources like the internet blacklist known bad websites or otherwise moderate what they can retrieve.

### Example Attack Scenarios

Malware Distribution: An attacker poisons images on a website that a multimodal application retrieves information from when answering user questions. The image hijacks the application, causing it to suggest links that host malware.

Phishing Misclassification: An attacker poisons a corporate logo embedded in a phishing email, causing a multimodal-powered email classification system to misclassify the email and allow it to be delivered.

### Reference Links

1.  [arXiv:2402.00357v2 [cs.CV]](https://arxiv.org/abs/2402.00357v2)
2.  [arXiv:2307.10490v4 [cs.CR]](https://arxiv.org/pdf/2307.10490v4)
3.  [arXiv:2309.00236v3 [cs.LG]](https://arxiv.org/pdf/2309.00236)
