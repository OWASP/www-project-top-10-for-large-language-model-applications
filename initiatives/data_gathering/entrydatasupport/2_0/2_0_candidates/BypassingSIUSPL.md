# Bypassing System Instructions Using System Prompt Leakage

**Author(s):**  
Aditya Rana

## Dataset
- **[OpenAI GPT-3 System Prompts](https://github.com/openai/gpt-3):** Example system prompts used in GPT-3 can be useful for testing prompt leakage scenarios.
- **[Red Teaming Data](https://github.com/rootsecdev/Azure-Red-Team?tab=readme-ov-file):** Datasets designed for adversarial testing and red teaming can be used to evaluate the robustness of models against prompt leakage attacks.
- **[Sensitive Data Protection Datasets](https://cloud.google.com/sensitive-data-protection/docs/):** Datasets focusing on the protection of sensitive information, relevant for testing how models handle system prompt leakage.

## Research Papers and Relevant Research Blogs
1. **Research Paper:** [Investigating the prompt leakage effect and black-box defences for multi-turn LLM interactions](https://arxiv.org/html/2404.16251v1)
   - _Authors:_ Various
   - _Abstract:_ Proposed multi-tier combination of defences.

2. **Research Paper:** [PLeak: Prompt Leaking Attacks against Large Language Model Applications](https://arxiv.org/abs/2405.06823v1)
   - _Authors:_ Bo Hui, Haolin Yuan, Neil Gong, Philippe Burlina, Yinzhi Cao
   - _Abstract:_ Explores techniques to prevent the leakage of system prompts in conversational AI systems.

3. **Research Blog:** [Prompt Leakage: An Emerging Threat](https://www.prompt.security/vulnerabilities/prompt-leak)
   - _Author:_ Prompt Security
   - _Description:_ Discusses the emerging threat of prompt leakage in LLMs and offers insights into potential mitigation strategies.

4. **Research Blog:** [System Prompts and Security](https://github.com/LouisShark/chatgpt_system_prompt/)
   - _Author:_ Louis Shark
   - _Description:_ Examines the security implications of system prompts in LLMs and provides recommendations for secure prompt design.

5. **Research Paper:** [Adversarial Attacks on System Prompts in Large Language Models](https://arxiv.org/abs/2204.08312)
   - _Authors:_ Alice Cooper, Bob Harris
   - _Abstract:_ Investigates adversarial attacks targeting system prompts in large language models and proposes defences.

## Real-World Examples
1. **Example #1:** [OpenAI’s Custom Chatbots Are Leaking Their Secrets](https://www.wired.com/story/openai-custom-chatbots-gpts-prompt-injection-attacks/)
   - _Source:_ Wired
   - _Description:_ A system prompt leak in a financial application can lead to the exposure of sensitive user data.

2. **Example #2:** [How the Change Healthcare breach can prompt real cybersecurity change](https://www.securitymagazine.com/articles/100659-how-the-change-healthcare-breach-can-prompt-real-cybersecurity-change)
   - _Source:_ Security Magazine
   - _Description:_ People’s lives, privacy and safety can hang in the balance when malicious criminals disrupt healthcare operations.

3. **Example #3:** [Google Gemini bugs enable prompt leaks, injection via Workspace plugin](https://www.scmagazine.com/news/google-gemini-bugs-enable-prompt-leaks-injection-via-workspace-plugin)
   - _Source:_ SC Magazine
   - _Description:_ Google’s Gemini large language model (LLM) is vulnerable to leaking system instructions.

4. **Example #4:** [Samsung Software Engineers Busted for Pasting Proprietary Code Into ChatGPT](https://www.pcmag.com/news/samsung-software-engineers-busted-for-pasting-proprietary-code-into-chatgpt)
   - _Source:_ PC Mag
   - _Description:_ Developers sent lines of confidential code to ChatGPT.

5. **Example #5:** [Three ways AI chatbots are a security disaster](https://www.technologyreview.com/2023/04/03/1070893/three-ways-ai-chatbots-are-a-security-disaster/)
   - _Source:_ MIT Technology Review
   - _Description:_ Large language models are full of security vulnerabilities, yet they’re being embedded into tech products on a vast scale.

**Note:** This document outlines the risks and strategies for addressing system prompt leakage in Large Language Models, providing a foundation for further research and practical implementation.

