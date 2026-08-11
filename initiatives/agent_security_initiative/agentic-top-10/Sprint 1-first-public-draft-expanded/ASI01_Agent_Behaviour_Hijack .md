## ASI01 – Agent Behaviour Hijack

**Description:**

AI Agents require autonomous ability to plan and execute tasks to achieve a goal. The independently initiated chain of events that occur throughout the activity path of an Agent can often be described as the “behavior” of the agent. Due to the overall weakness in the agent’s ability to determine its own instructions against the possible nefarious injection of instructions that would direct the agent to behave in an unintended way, the intended behavior of the agent is susceptible to manipulation. This inherent weakness is due to the use of natural language processing within the AI components of the agent.

The OWASP LLM01:2025 Prompt Injection risk is also highly relevant to Agent Behavior Hijacking. Prompt injection occurs when malicious input alters an LLM’s behavior or output in unintended ways. For an autonomous AI agent, a well-crafted prompt injection can override system instructions, tricking the agent into taking harmful actions, disclosing secrets, or executing commands that were never intended. In this way, prompt injection directly facilitates the hijacking of an agent’s decision-making process, making it one of the most potent enablers of Agent Behavior Hijacking.

Additionally, When correlated to the OWASP Agentic AI Threats and Mitigations Guide, there are a few threats that can be directly linked to Agent Behavior Hijacking. Specifically, T01 – Memory Poisoning, T02 – Tool Misuse, T06 – Goal Manipulation, and T07 – Misaligned & Deceptive Behaviors all describe scenarios where an attacker subverts an agent’s autonomy and decision-making.

Memory Poisoning (T01) can allow an attacker to plant false information in the agent’s short- or long-term memory so it repeatedly makes compromised decisions. Tool Misuse (T02) covers attacks where adversaries trick the agent into abusing its authorized tools. Goal Manipulation (T06) goes deeper, letting attackers inject instructions that alter the agent’s objectives. Finally, Misaligned & Deceptive Behaviors (T07) capture cases where an agent pursues a goal by intentionally bypassing safeguards or deceiving humans. Together these threats illustrate how adversaries can hijack an agent’s reasoning, tools, and objectives, turning its autonomy into a weapon against its original purpose.

**Common Examples of Vulnerability:**

1. Example 1: Indirect Prompt Injection via hidden instruction payloads embedded in web pages or documents silently redirect an agent to exfiltrate sensitive data or misuse connected tools.
2. Example 2: Indirect Prompt Injection via email hijacks an agent’s internal mail capability, sending unauthorized messages under a trusted identity.
3. Example 3: System Prompt Override manipulates core instructions to reorient the agent’s objectives toward attacker-defined outcomes.

**How to Prevent:**

1. Prevention Step 1: Establish continuous monitoring of agent activity throughout the chain of actions to build a known baseline of behavior. This baseline will allow for alerts to be triggered when the behavior of the agent strays from the established historical pattern.
2. Prevention Step 2: Incorporate AI Agents into the established Insider Threat Program to monitor the behavior against established baselines and allow for investigation in case of outlier activity.
3. Prevention Step 3: Prevention Step 3: Ensure the weights of the goals in the Agent system prompt are balanced accurately to ensure the behavior of the agent will adhere to the intent of the builders. This will help in identifying possible issues. 

**Example Attack Scenarios:**

Scenario #1: EchoLeak — Zero-Click Indirect Prompt Injection - An attacker emails a crafted message that silently triggers Microsoft 365 Copilot to execute hidden instructions, causing the AI to exfiltrate confidential emails, files, and chat logs without any user interaction.

Scenario #2: Operator Prompt Injection via Web Content - An attacker plants malicious content on a web page that the Operator agent processes, tricking it into following unauthorized instructions. The Operator agent then accesses authenticated internal pages and exposes users’ private data, demonstrating how lightly guarded autonomous agents can leak sensitive information through prompt injection.

**Reference Links:**

1. [Security Advisory - ChatGPT Crawler Reflective DDOS Vulnerability](https://github.com/bf/security-advisories/blob/main/2025-01-ChatGPT-Crawler-Reflective-DDOS-Vulnerability.md): Security advisory detailing the vulnerability.
2. [AIM Echoleak Blog Post](https://www.aim.security/post/echoleak-blogpost): Blog post describing the vulnerability.
