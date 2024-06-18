## 18 Malicious LLM Tuner

**Author:**
#### Jamie Khan

### Description

A Malicious LLM Tuner is an individual with the technical expertise to manipulate Large Language Models (LLMs) for malicious purposes.  These individuals exploit the inherent flexibility of LLMs by adjusting configuration settings to achieve unintended consequences.

Changing the values of options that control the output from an LLM application output such as Temperature, Top-k, Top-p and Number of Tokens can have a large downstream effect on the responses from LLM applications.  This can be detrimental to LLM applications that are designed to be more accurate than creative.

While data scientists understand the importance of these settings the developers responsible from delivering these applications may not be aware of how these configuration changes impact response quality.  This could be done subtly to undermine a company's LLM ambitions and create embarrassing PR.

### Common Examples of Risk

1. **Public Trust Erosion**: Widespread use of AI for misinformation can erode public trust in media and digital communications.
2. **Factual Inaccuracies:** The model produces incorrect statements when missing specific knowledge.
3. **Unsupported Claims:** The model generates baseless assertions, which can be especially harmful in sensitive contexts.
4. **Denial of Wallet (DoW):** Generating excessive operations to exploit the pay-per-use model of cloud-based AI services, causing unsustainable costs for the service provider.
5. **Unsafe Code Generation:** The model suggests insecure or non-existent code libraries, leading to potential security vulnerabilities when integrated into software.

### Prevention and Mitigation Strategies

1. **AI and Machine Learning Monitoring**: Implement continuous monitoring of AI systems to detect abnormal patterns that could indicate.
2. **Secure Coding Practices:** Establish secure coding practices to prevent the integration of unwanted configuration changes and vulnerabilities when using LLMs in development environments.
3. **Redundancy and Cross-Verification**: Use multiple models or verification steps to cross-check critical outputs, ensuring consistency and reducing the impact of altered tuning options.
4. **Vulnerability Management**: Regularly update and patch the LLM application infrastructure to address known vulnerabilities and mitigate potential attack vectors.
5. **Continuous Input Overflow:** An attacker sends a stream of input that exceeds the LLM's context window, causing excessive computational resource consumption.
6. **Financial Thresholds and Alerts:** Set financial thresholds and alerts for cloud-based LLM usage to prevent DoW attacks.


### Example Attack Scenarios

**Scenario #1:**: A developer introduces a code change update from a compromised software supply chain that has high temperature and Top-k values causing the LLM to fabricate news articles or blur the lines between fact and fiction.

**Scenario #2:** A malicious insider changes the context window size to be very small which restricts the LLM's understanding of the conversation, potentially leading to nonsensical or irrelevant responses that manipulate users. 

**Scenario #3:**: A threat actor through a privilege escalation exploit on the LLM applications hosting server is able to remove a context window size limitation resulting in a massive increase in token usage costs. 

### Reference Links

1. [Vancouver man wins case against Air Canada over chatbot error](https://nationalpost.com/news/vancouver-man-wins-case-against-air-canada-over-chatbot-error): **National Post** 
2. [LLM Parameters Demystified: Getting The Best Outputs from Language AI](https://cohere.com/blog/llm-parameters-best-outputs-language-ai): **Cohere** 
3. [A Gentle Introduction to Hallucinations in Large Language Models](https://machinelearningmastery.com/a-gentle-introduction-to-hallucinations-in-large-language-models/): **Machine Learning Mastery**
4. [Microsoft's Copilot image tool generates ugly Jewish stereotypes, anti-Semitic tropes](https://www.tomshardware.com/tech-industry/artificial-intelligence/microsofts-copilot-image-tool-generates-ugly-jewish-stereotypes): **Tom's Hardware**
