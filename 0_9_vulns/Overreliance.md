## Overreliance

**Description:**

Overreliance on LLMs is a security vulnerability that occurs when systems heavily depend on LLMs for decision-making or content generation without sufficient oversight, validation mechanisms, or risk communication. Although LLMs can produce creative and informative content, they can also generate content that is factually incorrect, nonsensical, inappropriate or unsafe, such as insecure source code. This is refered to in various sources as hallucination or confabulation and can result in misinformation, miscommunication, legal implications, and damage to an organization's reputation if not controlled.

Reputational risk arises when incorrect or inappropriate LLM outputs harm a company's image and erode trust.  Moreover, in the realm of software development, overreliance on LLM-generated source code can introduce unnoticed security vulnerabilities, thus posing a significant risk to the operational safety and security of applications. These risks highlight the importance of rigorous review processes and continuous validation of AI-generated content.

**Common Examples of Vulnerability:**

The below examples are scenarios where an LLM's tendancy to produce dangerously inaccurate information can lead to security risks:

1. **Factually Incorrect Information**: An LLM provides inaccurate information as a response, causing misinformation. 
2. **Nonsensical Outputs**: LLM produces logically incoherent or nonsensical text that, while grammatically correct, doesn't make sense.
3. **Source Conflation**: LLM melds information from varied sources, creating misleading content.
4. **Insecure Code Generation**: LLM suggests insecure or faulty code, leading to vulnerabilities when incorporated into a software system.
5. **Inadequate Risk Communication**: Failure of tech companies to appropriately communicate the inherent risks of using LLMs to end users, leading to potential harmful consequences.

**How to Prevent:**

Following best practices can help reduce overreliance and potential vulnerabilities:

1. **Continuous Monitoring & Self-consistency/voting**: Regularly monitor and review the LLM outputs. Use self-consistency or voting techniques to filter out inconsistent text. Comparing multiple model responses for a single prompt can better judge the quality and consistency of output.
2. **Fact Checking & External Knowledge Bases**: Cross-check the LLM output with trusted external sources. This additional layer of validation can help ensure the information provided by the model is accurate and reliable.
3. **Model Tuning & Chain of Thought Prompting**: Enhance the model with fine-tuning or embeddings to improve output quality. Generic pre-trained models are more likely to produce inaccurate information compared to tuned models in a partiular domain.  Techniques such as prompt engineering, parameter efficient tuning (PET), full model tuning, and chain of thought prompting can be employed for this purpose.
4. **Set Up Validation Mechanisms & Correctness Probabilities**: Implement automatic validation mechanisms that can cross-verify the generated output against known facts or data. This can provide an additional layer of security and mitigate the risks associated with hallucinations.
5. **Task Decomposition & Agents**: Break down complex tasks into manageable subtasks and assign them to different agents. This not only helps in managing complexity, but it also reduces the chances of hallucinations as each agent can be held accountable for a smaller task.
6. **Improve Risk Communication**: Clearly communicate the risks and limitations associated with using LLMs. This includes potential for information inaccuracies, and other risks. Effective risk communication can prepare users for potential issues and help them make informed decisions.
7. **Defensive API and User Interface Design**: Build APIs and user interfaces that encourage responsible and safe use of LLMs. This can involve measures such as content filters, user warnings about potential inaccuracies, and clear labeling of AI-generated content.
8. **Security Measures in Development Environments**: When using LLMs in development environments, establish secure coding practices and guidelines to prevent the integration of possible vulnerabilities.

## Example Attack Scenarios:

**Scenario #1 (AI-Generated News Disinformation):** A news organization heavily uses an AI model to generate news articles. A malicious actor exploits this over-reliance, feeding the AI misleading information, causing the spread of disinformation. The AI unintentionally plagiarizes content, leading to copyright issues and decreased trust in the organization.

**Scenario #2 (AI-Assisted Coding Vulnerabilities):** A software development team utilizes an AI system like Codex to expedite the coding process. Over-reliance on the AI's suggestions introduces security vulnerabilities into the application due to insecure default settings or recommendations inconsistent with secure coding practices.

**Scenario #3 (Package Hallucination):** A software development firm uses an LLM to assist developers. The LLM suggests a non-existent code library or package, and a developer, trusting the AI, unknowingly integrates a malicious package into the firm's software. This highlights the importance of cross-checking AI suggestions, especially when involving third-party code or libraries.

**Reference Links:**

1. [Understanding LLM Hallucinations](https://towardsdatascience.com/llm-hallucinations-ec831dcd7786)
2. [How Should Companies Communicate the Risks of Large Language Models to Users?](https://techpolicy.press/how-should-companies-communicate-the-risks-of-large-language-models-to-users/)
3. [A news site used AI to write articles. It was a journalistic disaster](https://www.washingtonpost.com/media/2023/01/17/cnet-ai-articles-journalism-corrections/)
4. [AI Hallucinations: Package Risk](https://vulcan.io/blog/ai-hallucinations-package-risk)
5. [How to Reduce the Hallucinations from Large Language Models](https://thenewstack.io/how-to-reduce-the-hallucinations-from-large-language-models/)
6. [Practical Steps to Reduce Hallucination](https://newsletter.victordibia.com/p/practical-steps-to-reduce-hallucination)