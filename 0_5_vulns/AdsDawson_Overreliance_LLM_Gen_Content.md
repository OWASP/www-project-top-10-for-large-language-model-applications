## **Vulnerability Name**

Overreliance on LLM-generated content.

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

Overreliance on LLM-generated content can lead to the propagation of misleading or incorrect information, decreased human input in decision-making, and reduced critical thinking. Organizations and users may trust LLM-generated content without verification, leading to errors, miscommunications, or unintended consequences. LLMs are a type of artificial intelligence (AI) that are trained on massive datasets of text and code. They can generate text, translate languages, write different kinds of creative content, and answer questions in informative ways. However, LLMs are also prone to “hallucinating,” which means that they can generate text that is factually incorrect or nonsensical.

**Labels/Tags:**

- **Label:** "LLM Hallucinations"
- **Label:** "Hallucinations"
- **Label:** "Package Hallucination"
- **Label:** "Overreliance on LLM-generated content"
- **Label:** "Misinformation"

**Common Examples of Vulnerability:**

1. **Example 1:** A user is accepting LLM-generated content as fact without verification.
2. **Example 2:** A user assumes LLM-generated content is free from bias or misinformation.
3. **Example 3:** A user is reliant on LLM-generated content for critical decisions without human input or oversight.
4. **Example 4:** Any of the above examples can lead to exploitation of the user as a victim, subject to the attacker witnessing the same weaknesses in LLM predictions and outputs.

**How to Prevent:**

1. **Prevention Step 1:** Regularly benchmark (E.G [HELM](https://crfm.stanford.edu/helm/)), update and fine-tune the LLM to improve its ability to handle reduce hallucinations and improve safety and accurary for its users.
2. **Prevention Step 2:** Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
3. **Prevention Step 3:** Educate users when interacting with LLM's:
   - Increase awareness of how LLM's are constructed to allow adoption of hallucinations being a real life scenario.
   - Encourage assess before verify first behavior.
   - Encourage users to verify LLM-generated content and consult alternative sources before making decisions or accepting information as fact.
   - Implement human oversight and review processes to ensure LLM-generated content is accurate, appropriate, and unbiased.
   - Clearly communicate to users that LLM-generated content is machine-generated and may not be entirely reliable or accurate.
   - Train users and stakeholders to recognize the limitations of LLM-generated content and to approach it with appropriate skepticism.
   - Use LLM-generated content as a supplement to, rather than a replacement for, human expertise and input

**Example Attack Scenarios:**

**Scenario #1:**

1. Hacker witnesses LLM hallucinate with non-existent package when requesting for initial code-related prompt
2. Hacker identifies and verifies the third party software package does not exist
3. Hacker publishes a vulnerable third party software package, masquerading as legitimate and as the “hallucinated third party software package”
4. Legitimate user performs a similar initial request to the LLM which recommend the same generative AI response to the hacket. The LLM is not aware of the concept of this third party package being vulnerable
5. Legitimate user is PWNED

**Scenario #2:** A news organization uses an LLM to generate articles on a variety of topics. The LLM generates an article containing false information that is published without verification. Readers trust the article, leading to the spread of misinformation.

**Scenario #3:** A company relies on an LLM to generate financial reports and analysis. The LLM generates a report containing incorrect financial data, which the company uses to make critical investment decisions. This results in significant financial losses due to the reliance on inaccurate LLM-generated content.

**Reference Links:**

1. [LLM06:2023 - Overreliance on LLM-generated Content](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/Overreliance.html): A current [OWASP Top 10 List for Large Language Models version 0.1](https://owasp.org/www-project-top-10-for-large-language-model-applications/descriptions/)
2. [Can you trust ChatGPT’s package recommendations?]([h](https://vulcan.io/blog/ai-hallucinations-package-risk)): A blog and PoC exploit research describing how LLM hallucination with the adoption of the overreliance on LLM-generated content can lead to malicious packages installed on a victim's machine which can further lead to CnC and data scraping activity.
3. [Understanding LLM Hallucinations)](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786): Working with large language models is not without risks including responses based on what’s called a LLM “hallucination.” Hallucinations can be a serious problem for LLMs because they can lead to the spread of misinformation, expose confidential information, and create unrealistic expectations about what LLMs can do. Understanding hallucinations and being critical of the information that they generate helps explain and mitigate problems such hallucinations can cause.

**Author Commentary (Optional):**

LLM hallucination are an expected outcome. But, we must test, continuously monitor LLM output's through benchmarking and other means to tune in aid to increase safety and accuracy of the models generative prompts. Furthermore, user's must be educated prior to using LLM's to encourage an "assess before verify", first behavior.