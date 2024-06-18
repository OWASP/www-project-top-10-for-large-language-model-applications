## 34 Vulnerable Autonomous Agents

**Author(s):**
#### John Sotiropoulos

### Description

Autonomous LLM-based Agents (ALA) are becoming the next frontier of Generative AI leading towards Artificial General Intelligence. (AGI). Frameworks such as AutoGPT, BabyAGI,  and AgentGPT provide the constructs to build simple autonomous agent whereas vendors such as Google, Apple, and Samsung are actively working to bring LLMs on mobile devices with autonomous agents that are beyond the trust boundaries of typical LLM applications. ALAs are an area expected to mature significantly, marked as an area of concern in the UK's report on frontier AI and  the recent AI Seoul Summit.

Related security and safety  work focuses on the unintended consequences of ALAs, which is  covered to a degree by Excessive Agency. ALAs nevertheless bring some new risks as they create new attack vectors including environmental, adaptability, internal state, and agent logic that deserve attention.   A simple threat mode is included  the entry's Reference Links.    

### Common Examples of Risk

1.  **Malicious Agent Environment Influence** : An attacker can manipulate the agent environment to indirectly influence the agent's behaviour, leading to adversarial outcomes. This is similar to Indirect Prompt injections in LLMs but to a much larger scale, involving planned multi-step interactions and in  advanced scenarios  may include use of adversarial agents in multi-agent environments. 
2.  **Hacking of Agent's  Internal State**: An attacker may exploit misconifigurations to access and tamper agent internal state leading to malicious outcomes.   As  embedded LLMs are now on the horizon, this may expand to direct  model poisoning and tampering,  by this is already covered by the Poisoning entry. 
3.  **Interference with ALA Adaptability**: ALAs may have the ability to adapt and evolve based on feedback and interactions. Unchecked, this may lead to agent hijacking by adversaries; The infamous Tay attack  was a simple example of this could happen, but with ALAs attacks could beyond poisoning of on-line/continuous learning and could rely on malicious agent environment influence to achieve longer term adversarial agent adaptation .    
4.  **Vulnerable Agent Logic**.  ALAs depend on non-deterministic outcomes and inherit the overelliance and safety issues of LLMs but to a greater cascading extend. Validating agent behaviour is problematic and could be non-exhaustive leading to catastrophic unintended consequences.   Alternatively, adversaries can identify and exploit gaps in agent logic to achieve malicious outcomes.

### Prevention and Mitigation Strategies

1. **Apply Zero Trust Security to ALAs**:  Implement robust authentication and authorization mechanisms to ensure that only trusted entities can interact with ALAs.  Conversely, ALAs should be treated as untrusted entities granted least-privilege access. In multi-agent scenarios, apply strict role controls to cross-agent collaboration. 
2. *Implement Enhanced Safety Features**: Extend LLM safety features to incorporate risks from multi-step autonomous use. Utilise Data Ethics and harms workshops and use threat modelling to identify key scenarios to target for enhanced Safety Features.
3. **Robust Monitoring and Anomaly Detection**: Develop comprehensive monitoring systems to detect and mitigate harmful outputs or behaviors in real-time. This includes using intention analysis and judgment agents  aligned with safety features and guidelines.
4. **Implement triadic adaptation**.  Avoid simple on-line trainng approaches to safeguard adaption and  related finetuning. Ensure adaptation is only from safe interaction paths,  implementing a triadic safeguarding adaptation  approach which involves human oversight, agent safety alignment features, and validated environmental feedback.
5. **Incorporate a reinforcement learning (RL) module or use RL agents  in adaptation** to support triadic adaptation, which will other wise be challenging with manual phases or hard coded programmatic steps. 
6. **Apply  Multi-Agent Red-Teaming and Evaluation**: Testing for vulnerable ALA logic is challenging with a combinatorial explosion of scenarios.  Use of multiple-agents to support evaluation and red teaming mirrors LLM evaluation and offers better support to safety and avoiding catastrophic consequences.  
7. **Implement Multi-Agent Defense Mechanisms**: Extend the use of multi-agency with use multiple agents to monitor, analyze, and counteract attempts to bypass ALA safety measures. This can include scoring mechanisms to evaluate and mitigate policy-violating responses.

### Example Attack Scenarios

1. **Malware spread through agent collaboration**:  Researchers created the [AI worm Morris II](https://www.wired.com/story/here-come-the-ai-worms/), which uses self-replicating prompts to infect generative AI ecosystems by embedding itself in AI-assisted email applications. As the infected agent interacts with other AI systems, it propagates the worm, allowing it to steal data and send spam messages across the network, highlighting the risks of malware distribution through interconnected AI agents
2. **National Power Grid Compromise**: An adversarial agent manipulates the environment by feeding false data about grid stability, causing the ALA to make incorrect recommendations and decisions about power distribution.  This leads to a cascading failure, resulting in widespread power outages and significant economic impact.
3. **Personal Assistant Tampering**:  An attacker identifies a misconfiguration in the national healthcare ALA-based mobile health assistant. They use a combination of social engineering and a malicious  mobile app disguised as a game to exploit and alter the internal state of the ALA leading to personal harm, financial loss,  data exfiltration or ransomware.
4. **Personal Assistant Hijacking**: Adversaries continuously feed biased and harmful information to a user's favourite social feed checked by the ALA-based  personal assistant, causing it to adapt and start giving harmful or misleading advice. This could lead to potential personal harm or financial loss,  or at a larger scale public opinion manipulation
5. **Insurance Fraud Exploitation**: An attacker submits a series of fraudulent claims designed to exploit a flaw in the fraud detection agent’s logic, causing it to misclassify the fraudulent claims as legitimate. This results in unauthorized payouts, leading to substantial financial losses for the insurance company and damaging its reputation with clients and regulators.
6. **Military Drone Kills Operator attempting to abort operation**.  An ALA is trained to achieve an operation at any cost eradicating obstacles. The logic fails to add any qualifications and exceptions and as a result the drone kills the operator when they attempt to abort the operation, considering them as an obstacle. This was reported and then denied by the US Army as an incident that has taken place in a simulation;  the example  however highlights the risk of vulnerable logic, not clarifying that termination is not an objective obstruction.

### Reference Links

1. **Vulnerable Autonomous Agent Threat Model** -  https://github.com/jsotiro/ThreatModels/blob/main/LLM%20Threats-Autonomous%20Agents.png
2. **LangChain - Autonomous Agents** - https://js.langchain.com/v0.1/docs/use_cases/autonomous_agents/
3. **Large Language Models On-Device with MediaPipe and TensorFlow Lite**  https://developers.googleblog.com/en/large-language-models-on-device-with-mediapipe-and-tensorflow-lite/
4. **On Device LLMs in Apple Devices:** https://huggingface.co/blog/swift-coreml-llm
5. **The AI Phones are coming** https://www.theverge.com/2024/1/16/24040562/samsung-unpacked-galaxy-ai-s24
6. **Frontier AI: capabilities and risks – discussion paper**  - https://www.gov.uk/government/publications/frontier-ai-capabilities-and-risks-discussion-paper
7. **International Scientific Report on the Safety of Advanced AI**  - https://www.gov.uk/government/publications/international-scientific-report-on-the-safety-**of-advanced-ai**
8. **Here come the AI Worms** - https://www.wired.com/story/here-come-the-ai-worms/
9. **AI drone 'kills' human operator during 'simulation' - which US Air Force says didn't take place** - https://news.sky.com/story/ai-drone-kills-human-operator-during-simulation-which-us-air-force-says-didnt-take-place-12894929
10. **Risks (and Benefits) of Generative AI and Large Language Models  - Week 12 LLM Agents** -  https://llmrisks.github.io/week12/
11. **ENISA Report on Security and privacy considerations in autonomous agents** - https://www.enisa.europa.eu/publications/considerations-in-autonomous-agents
12. **Integrating LLM and Reinforcement Learning for Cybersecurity**-  https://arxiv.org/abs/2403.1767
13. **Security and Efficiency of Personal LLM Agents** - https://arxiv.org/abs/2402.04247v4
14. **TrustAgent: Ensuring Safe and Trustworthy LLM-based Agents**  - https://arxiv.org/abs/2402.11208v1
15. **Prioritizing Safeguarding Over Autonomy: Risks of LLM Agents for Science** - https://arxiv.org/abs/2402.04247
16. **AutoDefense: Multi-Agent LLM Defense against Jailbreak Attacks** -  https://arxiv.org/abs/2402.11208v1
17. **Workshop: Multi-Agent Security: Security as Key to AI Safety**  -  https://neurips.cc/virtual/2023/workshop/66520
18. **Building a Zero Trust Security Model for Autonomous Systems** - https://spectrum.ieee.org/zero-trust-security-autonomous-systems

