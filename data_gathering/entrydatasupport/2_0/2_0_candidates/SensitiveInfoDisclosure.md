# Sensitive Information Disclosure

**Authors:**  
Rachel James, Bryan Nakayama

## Dataset
- **[Enron Email Dataset](https://edrm.net/resources/data-sets/):** Contains a large number of emails, useful for testing information disclosure and data sanitization techniques.
- **[Synthetic Training Data for LLMs](https://research.google/blog/protecting-users-with-differentially-private-synthetic-training-data/):** A synthetic dataset designed for evaluating privacy-preserving techniques in LLM training.
- **[Healthcare Data for ML Models](https://apps.who.int/gho/data/node.resources):** Contains medical data, useful for testing the handling of sensitive information in LLM applications.

## Research Papers and Relevant Research Blogs
1. **Research Paper:** [Preserving data privacy in machine learning systems](https://www.sciencedirect.com/science/article/pii/S0167404823005151)
   - _Authors:_ Soumia Zohra El Mestari, Gabriele Lenzini, Huseyin Demirci
   - _Abstract:_ Discuss current challenges and research questions that are still unsolved in the field.

2. **Research Paper:** [Mitigating Unintended Memorization in Language Models via Alternating Teaching](https://arxiv.org/abs/2210.06772)
   - _Authors:_ Zhe Liu, Xuedong Zhang, Fuchun Peng
   - _Abstract:_ Propose a novel approach called alternating teaching to mitigate unintended memorization in sequential modeling.

3. **Research Blog:** [Preventing Data Leakage in Machine Learning Models](https://shelf.io/blog/preventing-data-leakage-in-machine-learning-models/)
   - _Author:_ Shelf
   - _Description:_ Discusses strategies to prevent sensitive data leakage in AI models, with a focus on practical implementations.

4. **Research Blog:** [Mitigating Token-Length Side-Channel Attacks](https://blog.cloudflare.com/ai-side-channel-attack-mitigated)
   - _Author:_ Cloudflare
   - _Description:_ Examines the risks and mitigation strategies for token-length side-channel attacks in AI applications.

5. **Research Paper:** [A Survey of Privacy Attacks in Machine Learning](https://dl.acm.org/doi/full/10.1145/3624010)
   - _Authors:_ Maria Rigaki, Sebastian Garcia
   - _Abstract:_ Analysis of more than 45 papers related to privacy attacks against machine learning that have been published during the past seven years.
     
## Real-World Examples
1. **Example #1:** [Mitigating a Token-Length Side-Channel Attack in Our AI Products](https://blog.cloudflare.com/ai-side-channel-attack-mitigated/)
   - _Source:_ Cloudflare
   - _Description:_ A real-world example of mitigating a token-length side-channel attack in AI products.

2. **Example #2:** [ChatGPT Leaks Sensitive User Data, OpenAI Suspects Hack](https://www.spiceworks.com/tech/artificial-intelligence/news/chatgpt-leaks-sensitive-user-data-openai-suspects-hack/)
   - _Source:_ Spice Works
   - _Description:_ The leaks exposed conversations, personal data, and login credentials.

3. **Example #3:** [Amazon’s Q has ‘severe hallucinations’ and leaks confidential data in public preview](https://www.platformer.news/amazons-q-has-severe-hallucinations/)
   - _Source:_ Plataformer
   - _Description:_ A chatbot revealed confidential information in a public response due to inadequate data sanitization.

4. **Example #4:** [Atlantic Health System CIDO offers lessons on AI in cybersecurity](https://www.healthcareitnews.com/news/atlantic-health-system-cido-offers-lessons-ai-cybersecurity)
   - _Source:_ Healthcare IT News
   - _Description:_ An AI model used in healthcare leaked patient information, highlighting the risks of sensitive data exposure.

5. **Example #5:** [Side-Channel Attack Exposes AI Model Outputs](https://www.securityweek.com/how-quantum-computing-will-impact-cybersecurity/)
   - _Source:_ SecurityWeek
   - _Description:_ A side-channel attack of an AI model, demonstrating the need for robust security measures.

**Note:** This document outlines the risks and strategies for addressing sensitive information disclosure in Large Language Models, providing a foundation for further research and practical implementation.
