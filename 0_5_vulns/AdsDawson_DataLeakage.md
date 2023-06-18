## **Vulnerability Name:**

Data Leakage

**Author(s):**

Ads Dawson | [`@GangGreenTemperTatum`](https://github.com/GangGreenTemperTatum/www-project-top-10-for-large-language-model-applications)

**Description:**

Data leakage occurs when an LLM accidentally reveals sensitive information, proprietary algorithms, or other confidential details through its responses. This can result in unauthorized access to sensitive data or intellectual property, privacy violations, and other security breaches. It's important to note that users of an LLM application should be aware of how to interact with an LLM and identify the risks present on how they might unintentionally input sensitive data. Vice versa, an LLM application should perform adequate data sanitization and scrubbing validation in aid to prevent user data from entering the training model data. Furthermore, the company hosting the LLM should have appropriate Terms of User policies available to make users aware on how data is processed.

**Labels/Tags:**

- **Label:** "Data Leakage"
- **Label:** "PII"
- **Label:** "BOLA"
- **Label:** "BFLA"
- **Label:** "IDOR"

**Common Examples of Vulnerability:**

1. **Example 1:** Incomplete or improper filtering of sensitive information in the LLM’s responses.
2. **Example 2:** Overfitting or memorization of sensitive data in the LLM’s training process.
3. **Example 3:** Unintended disclosure of confidential information due to LLM misinterpretation, lack of data scrubbing methods or errors.

**How to Prevent:**

1. Prevention Step 1: Integrate adequate data sanitization and scrubbing techniques in aid to prevent user data from entering the training model data.
2. Prevention Step 2: Implement robust input validation and sanitization methods to identify and filter out potential malicious inputs.
3. Prevention Step 3: Maintain ongoing supply chain mitigation of risk through techniques such as SAST (Static Application Security Testing) and SBOM (Software Bill of Materials) attestations to identify and remediate vulnerabilities in dependencies for third-party software or packages.
4. Prevention Step 4: Implement dedicated LLM's to benchmark against undesired consequences and train other LLM's using [reinforcement learning techniques](https://wandb.ai/ayush-thakur/Intro-RLAIF/reports/An-Introduction-to-Training-LLMs-Using-Reinforcement-Learning-From-Human-Feedback-RLHF---VmlldzozMzYyNjcy).
5. Prevention Step 5: Perform LLM-based [red team exercises](https://www.anthropic.com/index/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned) or [LLM vulnerability scanning](https://github.com/leondz/garak) into the testing phases of the LLM's lifecycle.

**Example Attack Scenarios:**

**Scenario #1:** Unsuspecting legitimate user A is exposed to certain other user data via the LLM when interacting with the LLM application in a non-malicious manner.

**Scenario #2:** User A targets a well crafted set of prompts to bypass input filters and sanitization from the LLM to cause it to reveal sensitive information (I.E PII) about other users of the application.

**Scenario #3:** Personal data such as PII is leaked into the model via training data due to either negligence from the user themselves, or the LLM application. This case could increase risk and probability of scenario 1 or 2 above.

**Reference Links:**

1. [AI data leak crisis: New tool prevents company secrets from being fed to ChatGPT](https://www.foxbusiness.com/politics/ai-data-leak-crisis-prevent-company-secrets-chatgpt) A blog explaining the risks associated to users unintentionally leaking sensitive data into LLM's and the consequences of when this information is fed into training data.
2. [Lessons learned from ChatGPT’s Samsung leak](https://cybernews.com/security/chatgpt-samsung-leak-explained-lessons/) A write up on an incident caused due to an employee unintentionally leaking source code into an LLM's training data due to misuse and unawareness, leading to this being leaked across other use-case interactions with the LLM.
3. [Cohere - Terms Of Use](https://cohere.com/terms-of-use) An example terms of use notice made available to users of an LLM to identify how data is processed.

**Author Commentary (Optional):**

It's important to note incidents such as [March 20 ChatGPT outage: Here’s what happened](https://openai.com/blog/march-20-chatgpt-outage) was not directly related to the LLM itself. However, it is important to maintain controls listed in _Prevention Step 3_ above as part of the overall LLM application and supporting infrastructure which can reduce risk and the attack vector.