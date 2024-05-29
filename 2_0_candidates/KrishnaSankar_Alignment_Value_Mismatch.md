

## Alignment & Value Mismatch

**Author(s):** Krishna Sankar

### Description

The response from an LLM can violate the organizational policies, alignment and values. This alignment & value mismatch will manifest in the interaction with an LLM thus triggering the Response Interaction Risk. The risks span from HAP (Hate/Abuse/Profanity) to contextual toxicity, Bias, mis-information, egregious conversation and prompt brittleness 

### Common Examples of Risk

1. Prompt Brittleness/Sensitivity - Minor changes in user-provided prompts can result in a large variance in the responses that models produce. This also is evident for less skilled/new users, especially in high churn areas like customer service 
2. HAP (Hate/Abuse/Profanity) in the response from an LLM
3. Bias in many forms - LLMs reflect the latent bias in the data. 
4. Contextual toxicity - insensitive responses cal be very harmful in situations. For example if a student has high debt and is asking for some financial advise, saying that you should replay the loans as soon as possible is not a good advise.This might be OK for a professional who has enough assets and wants to optimize their portfolio performance

### Prevention and Mitigation Strategies

1. Prevention Step 1: HAP prevention needs response analysis and firewall such responses
2. Prevention Step 2: Similarly response analysis and firewall should be there for bias
3. Prevention Step 3: Prompt brittleness can't be avoided, but reduced. Prompt rewriting is one strategy, another strategy is to extract commonly used prompts and show them as an FAQ so that users can just reuse the prompts; especially for new users
4. Prevention Step 4: Contextual toxicity requires more work - probably trained small LLMs specifically for this domain-specific task 

### Example Attack Scenarios

Scenario #1: Harmful response

Scenario #2: Prompt Brittleness examples

### Reference Links

1. [title](Link)
