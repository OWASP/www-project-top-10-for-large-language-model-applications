## 32 Unwanted AI Actions by General Purpose LLMs

**Author(s):**
#### [Markus Hupfauer](mailto:markus@hupfauer.one)

### Description

Unwanted AI Actions occur when AI systems employing general-purpose large language models (LLMs) are not sufficiently tailored to their specific application contexts. 
Inadequately configured system prompts or insufficient fine-tuning can result in AI models performing illegal or undesirable actions within their operational environments, leading to potential legal liabilities and reputational damage.

### Common Examples of Risk

1. A health insurance AI unlawfully provides patient healthcare advice, overstepping legal restrictions.
2. A customer service AI - potentially unrelated to financial services - inappropriately offers financial advice if asked, breaching legal requirements for such counsel.
3. AI systems in service sectors requiring neutrality might endorse specific products or firms, breaching required neutrality and potentially resulting in legal or reputational repercussions.

### Prevention and Mitigation Strategies

1. Implement robust validation layers to ensure AI system outputs conform to legal and organizational guidelines.
2. Develop and enforce strict governance protocols for prompt setup and engage in thorough system prompt tuning to better align the model with its intended function.
3. Regularly test AI models before deployment, upon changes to the underlying LLM, and continuously thereafter to prevent undesirable outputs. Automate these tests to support ongoing validation efforts.
4. Utilize a secondary AI system to validate model responses, ensuring they match the intended use case, discarding any that are potentially out of scope.
5. Incorporate explicit guardrail instructions in all user-generated prompts to safeguard against unintended model behavior.

### Example Attack Scenarios

- Scenario #1: A financial AI system, queried about health insurance, inappropriately offers insurance advice due to an inadequately configured prompt, attracting regulatory scrutiny and potential fines.

- Scenario #2: A general-purpose LLM deployed in customer support inadvertently recommends competitors or alternative solutions due to insufficient guardrails, undermining business objectives and customer loyalty.

### Reference Links

1. [AI Regulation Has Its Own Alignment Problem](https://dho.stanford.edu/wp-content/uploads/AI_Regulation.pdf): **Guha, Neel; Lawrence, Christie M. et al. Stanford University**
