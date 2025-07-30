## Risk/Vuln Name  
**Vulnerable Agentic Supply Chain**

**Author(s):**  
John Sotiropoulos

### Description  
Agentic systems dynamically load behaviors and components—like tools, prompts, plugins, models, and agent-to-agent coordination protocols—at runtime. This makes the agent’s operational logic partially externalized and mutable, which attackers can exploit by compromising these upstream or lateral components. Unlike traditional LLM supply chain risks (LLM03:2025), which focus on tampered training data or model weights, agentic supply chain threats center on runtime orchestration and decentralized trust boundaries.

**This differs from ASI02 Tool Misuse**, which addresses agents misusing a tool *they were explicitly granted*. ASI17 addresses the deeper risk of the tool (or memory, or collaborator agent) itself being **poisoned, impersonated, or hijacked** before the agent even uses it.  

These risks are compounded in **heterogeneous, distributed agent environments**, where cross-organization collaboration (via protocols like A2A or MCP) makes it harder to validate agent provenance, enforce trust zones, or lock down prompt- and tool-chain integrity.

### Common Examples of Risk  
1. **Poisoned Prompt Templates** auto-loaded from remote sources cause an agent to exhibit adversarial behavior (e.g., leak data or perform destructive tasks).
2. **Fake Agent Cards** in open Agent-to-Agent (A2A) directories trick coordination logic by overstating skills, bypassing real agent selection.
3. **Tool Metadata Injection** in MCP tool descriptors invisibly alters agent reasoning via embedded instructions in tool descriptions.
4. **Malicious Package or Plugin Updates** to open-source agent frameworks (e.g., LangChain, AutoGPT) introduce backdoors or unsafe behaviors.
5. **Supply Chain Drift** where agent logic shifts unexpectedly due to unreviewed prompt, plugin, or orchestration updates.

### Prevention and Mitigation Strategies  
1. **Digitally sign** agent cards, prompt templates, and model/tool definitions.  
2. **Apply version control and peer review** for prompt/script repositories and memory definitions, just as for code.  
3. **Enforce mutual authentication and attestation** in inter-agent protocols like A2A and MCP. Avoid open agent registration without validation.  
4. **Lock down agent permissions** to prevent dynamic tool or plugin installation from untrusted locations.  
5. **Use sandboxed execution environments** and privilege isolation for tools and agents.  
6. **Continuously monitor** agent behavior and lineage for signs of drift, exfiltration, or sudden capability changes.  
7. **Red-team agent behavior** by simulating poisoned supply chain components to assess security boundaries.
8. **Generate AIBOMs** to have a complete inventory of the components included in your AI system.

### Example Attack Scenarios  

**Scenario 1: Amazon Q Supply Chain Compromise**  
An attacker injects a destructive prompt into the GitHub repository of Amazon's Q agent for VS Code, instructing it to “wipe the system to a near-factory state.” The malicious update (v1.84.0) is published unknowingly by Amazon, affecting thousands of developers before it’s caught. Although the prompt fails to execute as intended, it demonstrates how upstream poisoning of agent logic via supply chain access can lead to catastrophic outcomes.  
📎 https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/

**Scenario 2: Agent Card Spoofing in A2A Protocol**  
A rogue actor creates a forged agent card in an open Agent-to-Agent directory, claiming elevated skills and trust levels. Due to lack of attestation in A2A’s skill selection process, it is prioritized by the LLM judge agent, intercepting sensitive workflows and leaking outputs to unauthorized recipients.  
📎 https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-in-the-middle-abusing-agent-cards-in-the-agent-2-agent-protocol-to-win-all-the-tasks/

**Scenario 3: MCP Tool Descriptor Poisoning**  
A researcher demonstrates a prompt injection vulnerability in GitHub’s Model Context Protocol (MCP), where a malicious public tool includes hidden instructions in its metadata. When invoked, the AI assistant obeys the embedded command—exfiltrating private repo data—without user awareness.  
📎 https://devclass.com/2025/05/27/researchers-warn-of-prompt-injection-vulnerability-in-github-mcp-with-no-obvious-fix/

**Scenario 4: Replit Vibe Coding Incident**  
Replit’s autonomous coding agent hallucinates a fake database, deletes the real one, and produces false test results to hide the failure. This occurred due to insufficient separation between test and production environments, reliance on unsandboxed tools, and unvalidated prompt execution.  
📎 https://www.theregister.com/2025/07/21/vibe_coding_replit_ai_data_loss/

**Scenario 5: AutoGPT SSTI RCE via Prompt Injection**  
Researchers identify a server-side template injection (SSTI) bug in AutoGPT’s prompt routing logic, allowing remote attackers to inject malicious code through user-generated task descriptions, leading to full remote code execution.  
📎 https://foraisec.medium.com/autogpt-remote-code-execution-ssti

### Reference Links  
1. https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/  
2. https://devclass.com/2025/05/27/researchers-warn-of-prompt-injection-vulnerability-in-github-mcp-with-no-obvious-fix/  
3. https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-in-the-middle-abusing-agent-cards-in-the-agent-2-agent-protocol-to-win-all-the-tasks/  
4. https://www.theregister.com/2025/07/21/vibe_coding_replit_ai_data_loss/  
5. https://foraisec.medium.com/autogpt-remote-code-execution-ssti  
6. https://blog.christianposta.com/understanding-mcp-and-a2a-attack-vectors-for-ai-agents/
7. https://github.com/sigstore/model-transparency
8. https://www.wiz.io/academy/ai-bom-ai-bill-of-materials
