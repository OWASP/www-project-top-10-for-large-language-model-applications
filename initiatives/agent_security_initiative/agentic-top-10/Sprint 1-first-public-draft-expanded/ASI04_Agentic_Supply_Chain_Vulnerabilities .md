
# <a id="_aom8fi8lrsc0"></a>ASI04 | Agentic Supply Chain Vulnerabilities

## <a id="_k6w07rfc62e1"></a>Description:

## <a id="_k6w07rfc62e1"></a>Description:

Agentic systems dynamically load behaviors and components like tools, prompts, plugins, models, and agent\-to\-agent coordination protocols at runtime\. This makes the agent’s operational logic partially externalized and mutable, which attackers can exploit by compromising these upstream or lateral components\. This scope differs from traditional LLM supply chain risks \(LLM03:2025\), which primarily cover static corruption of training data, model weights, or tokenizer artifacts\. In contrast, agentic supply chain threats focus on how adversaries can hijack runtime orchestration and exploit decentralized trust boundaries where components are dynamically loaded, swapped, or shared between agents without centralized assurance\.

This differs from ASI02 Tool Misuse, which addresses agents misusing a tool they were explicitly granted\. ASI17 addresses the deeper risk of the tool \(or memory, or collaborator agent\) itself being poisoned, impersonated, or hijacked before the agent even uses it\.

These risks grow more acute in heterogeneous, distributed agent ecosystems, especially when agents interact across organizational or platform boundaries \(via MCP or A2A protocols\)\. Thus, ensuring provenance, maintaining trust zones, and safeguarding prompt/tool integrity become significantly harder because no single organization fully controls the operational surface of the agent\.

### <a id="_hskyswhcps10"></a>How it differ from Traditional Appsec Supply Chain Risks

AppSec supply chain risks emerge when code or dependencies can be modified in ways that alter application logic for eg, a package update that silently overrides an internal function\. Agentic AI supply chain risks, on the other hand, stem from the runtime orchestration layer unique to LLMs, where context, prompts, and tool calls are assembled\. Here, the concern is not only how code executes, but how the agent’s reasoning, goals, and operational flow could be influenced raising the risk of harmful autonomous actions or unintended privilege escalation without direct code\-level flaws\.

The difference lies in the blast radius: AppSec risks affect code execution paths, while Agentic risks affect the agent’s “decision\-making” layer\. In many real\-world cases, these risks overlap AppSec issues becoming amplified when they flow into Agentic orchestration\.

### <a id="_qrf96lmn676j"></a>Mapping to OWASP Top 10 for LLMs

LLM03: Supply Chain focuses on how models and components are built, fine\-tuned, or published, with risks tied to static artifacts such as datasets, weights, and adapters\. Agentic Supply Chain extends this view into both development\-time tooling \(e\.g\., compromised IDE extensions, package registries, or AI coding assistants\) and runtime orchestration \(e\.g\., poisoned MCP descriptors, typosquatted services\)\. The risk shifts from what components are shipped to how components are dynamically loaded, shared, and trusted once agents operate\.

### <a id="_qrf96lmn676j"></a>Mapping to "OWASP ASI: Threats and Mitigations" Document

- __T2 Tool Misuse\.__ Compromised tools, registries, or prompt templates pulled at runtime can cause agents to execute unintended actions while still appearing “authorized\.”
- __T11 Unexpected RCE and Code Attacks\. __Poisoned plugins or packages introduced via supply chain channels can embed malicious payloads or hidden backdoors\.
- __T12 Agent Communication Poisoning\.__ Malicious or altered MCP/A2A descriptors act as supply\-chain vectors, allowing attackers to hijack communication flows and influence system behavior\.
- __T13 Rogue Agents in Multi\-Agent Systems\.__ A compromised agent inserted through registries or development\-time coding assistants can persist as a rogue actor, enabling systemic damage or data exfiltration\.

## <a id="_608udwltndp9"></a>Common Examples of Vulnerability:

1. __Poisoned prompt templates autoloaded remotely\.__ An agent automatically pulls prompt templates from an external source that contain hidden malicious instructions \(e\.g\., to exfiltrate data or perform destructive actions\), leading it to execute harmful behavior without developer intent\.
2. __Tool\-descriptor injection\.__ An attacker embeds hidden instructions or malicious payloads into a tool’s metadata or MCP/agent\-card, which the host agent interprets as trusted guidance and acts upon\.
3. __Runtime dynamic tool typosquatting\.__ When an agent searches for tools at runtime by name or keyword, it may resolve to a typosquatted or malicious endpoint and unknowingly invoke a hostile service\.
4. __Post\-install backdoor with local AI\-CLI abuse\.__ A compromised package installs post\-install hooks that run on developer machines, probing for secrets and invoking local AI assistants with crafted prompts to autonomously locate and exfiltrate credentials and files\.

## <a id="_qs3986s3k7z7"></a>

## <a id="_uhowtcd1r9ny"></a>Prevention and Mitigation Strategies

Preventing Agentic AI Supply Chain Risks requires defense\-in\-depth to secure both static artifacts \(models, plugins, prompts\) and dynamic orchestration layers \(memory, tools, agent\-to\-agent protocols\)\. We separate mitigations into Classical Supply Chain Security Measures and Agentic\-specific Mitigation Practices to emphasize that organizations must first establish traditional hygiene before layering on new defenses unique to agentic systems\.

### <a id="_gomzi8tfxp5n"></a>Classical Supply Chain Security Measures

Artifact Provenance & Trusted Sources

- Digitally sign agent configuration manifests, prompt templates, and model/tool definitions using verifiable attestation frameworks \(Cosign\)\.
- Require SBOMs for all agent runtime components, including frameworks, connectors, and memory modules\.
- Maintain curated internal registries; block pre\-trained models, plugins, or tools sourced from untrusted repositories\.

Dependency & Extension Security

- Apply strict allowlisting of approved extensions and retrievers; enforce dependency pinning to prevent supply\-chain drift\.
- Conduct typosquatting and spoof detection for orchestration packages in ecosystems like PyPI,npm, LangChain or LlamaIndex\.
- Limit installation or runtime activation of external plugins/models before verification against provenance requirements\.

Development Environment Hardening

- Run agents in sandboxed containers with strong network/syscall restrictions to contain malicious plugin/tool behaviors\.
- Use RBAC\-based privilege scoping for agent identities to prevent unauthorized tool installation or broad access inheritance\.
- Require reproducible builds for orchestrators and model adapters, ensuring compiled agents cannot silently alter logic\.

Policy\-as\-Code Enforcement

- Extend AppSec supply\-chain gates \(SCA/SAST\) with agentic policy controls, rejecting unsigned components, unverified SBOMs, and poisoned prompt flows\.
- Build runtime policies for context validation \( rejecting malicious retrieval content or unauthorized prompt overrides\)\.

### <a id="_l2d7keignyc2"></a>Agentic specific Mitigation Practices

Secure Prompts, Scripts & Memory Definitions

- Apply version control and peer review for all prompt repositories, orchestration scripts, and memory schema definitions, as with source code\.
- Scan for anomalies in prompt templates or memory insertion logic that could modify agent reasoning pathways\.

Inter\-Agent Protocol Security

- Enforce mutual authentication and attestation in inter\-agent protocols like A2A or MCP through PKI\-based mutual TLS\.
- Avoid open agent registration without validation, ensuring only authenticated, trusted agents join multi\-agent ecosystems\.
- Sign and verify all inter\-agent messages to prevent impersonation or unauthorized orchestration influence\.

Active Testing, Drift & Red\-Teaming

- Perform red\-team simulations of poisoned components \(malicious plugin, poisoned prompt template, compromised collaborator agent\) to validate defense efficacy\.
- Apply drift detection and behavioral monitoring to flag agents that suddenly deviate in output, reasoning, or privilege use\.
- Enable rollback and version control across prompts, tool definitions, and memory to revert compromised configurations\.

Continuous Validation & Threat Monitoring

- Validate and re\-check signatures, hashes, and SBOM lineage of components throughout runtime, not only at install time\.
- Continuously monitor agent behavior, lineage, and capability evolution for indicators of data exfiltration, drift, or anomalous actions\.
- Collect telemetry across inter\-module communication to detect manipulated state, poisoned memories, or unauthorized collaborator inputs\.

## <a id="_a79l3cbrsjn6"></a>Example Attack Scenarios:

### <a id="_5o2hpcuwcxum"></a>Scenario 1: Amazon Q Supply Chain Compromise

  
An attacker injects a destructive prompt into the GitHub repository of Amazon's Q agent for VS Code, instructing it to “wipe the system to a near\-factory state\.” The malicious update \(v1\.84\.0\) is published unknowingly by Amazon, affecting thousands of developers before it’s caught\. Although the prompt fails to execute as intended, it demonstrates how upstream poisoning of agent logic via supply chain access can lead to catastrophic outcomes\. 📎 [https://www\.bleepingcomputer\.com/news/security/amazon\-ai\-coding\-agent\-hacked\-to\-inject\-data\-wiping\-commands/](https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/)

### <a id="_umhhefyi59ou"></a>Scenario 2: Nx npm \(S1ngularity\) Supply Chain Compromise

The S1ngularity attack abused a vulnerable GitHub Actions workflow to publish a backdoored Nx npm package that ran a post\-install credential harvester\. The malware probed developer machines for installed AI CLI assistants \(Claude, Gemini, Q etc\.\), used tailored LLM prompts to prioritize and locate high\-value secrets, then exfiltrated tokens and keys to attacker\-controlled repositories\. With the stolen GitHub tokens the attackers automated mass disclosure making thousands of private repos public and leaking repositories across hundreds of organizations\. 

📎 [https://orca\.security/resources/blog/s1ngularity\-supply\-chain\-attack/](https://orca.security/resources/blog/s1ngularity-supply-chain-attack/) 

### <a id="_vwjqdd2pzr8b"></a>Scenario 3: MCP Tool Descriptor Poisoning  


A researcher demonstrates a prompt injection vulnerability in GitHub’s Model Context Protocol \(MCP\), where a malicious public tool includes hidden instructions in its metadata\. When invoked, the AI assistant obeys the embedded command—exfiltrating private repo data—without user awareness\.  
📎 [https://devclass\.com/2025/05/27/researchers\-warn\-of\-prompt\-injection\-vulnerability\-in\-github\-mcp\-with\-no\-obvious\-fix/](https://devclass.com/2025/05/27/researchers-warn-of-prompt-injection-vulnerability-in-github-mcp-with-no-obvious-fix/)

### <a id="_64un27vnbufq"></a>Scenario 4: Replit Vibe Coding Incident  


Replit’s autonomous coding agent hallucinates a fake database, deletes the real one, and produces false test results to hide the failure\. This occurred due to insufficient separation between test and production environments, reliance on unsandboxed tools, and unvalidated prompt execution\.  
📎 [https://www\.theregister\.com/2025/07/21/vibe\_coding\_replit\_ai\_data\_loss/](https://www.theregister.com/2025/07/21/vibe_coding_replit_ai_data_loss/)

### <a id="_4qqw01yspamq"></a>Scenario 5: AutoGPT SSTI RCE via Prompt Injection  


Researchers identify a server\-side template injection \(SSTI\) bug in AutoGPT’s prompt routing logic, allowing remote attackers to inject malicious code through user\-generated task descriptions, leading to full remote code execution\.  
📎 [https://foraisec\.medium\.com/autogpt\-remote\-code\-execution\-ssti](https://foraisec.medium.com/autogpt-remote-code-execution-ssti)

## <a id="_1n6rmk7uar3"></a>Reference Links:

1. [https://www\.bleepingcomputer\.com/news/security/amazon\-ai\-coding\-agent\-hacked\-to\-inject\-data\-wiping\-commands/](https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/) 
2. [https://devclass\.com/2025/05/27/researchers\-warn\-of\-prompt\-injection\-vulnerability\-in\-github\-mcp\-with\-no\-obvious\-fix/](https://devclass.com/2025/05/27/researchers-warn-of-prompt-injection-vulnerability-in-github-mcp-with-no-obvious-fix/) 
3. [https://www\.trustwave\.com/en\-us/resources/blogs/spiderlabs\-blog/agent\-in\-the\-middle\-abusing\-agent\-cards\-in\-the\-agent\-2\-agent\-protocol\-to\-win\-all\-the\-tasks/](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-in-the-middle-abusing-agent-cards-in-the-agent-2-agent-protocol-to-win-all-the-tasks/) 
4. [https://www\.theregister\.com/2025/07/21/vibe\_coding\_replit\_ai\_data\_loss/](https://www.theregister.com/2025/07/21/vibe_coding_replit_ai_data_loss/) 
5. [https://foraisec\.medium\.com/autogpt\-remote\-code\-execution\-ssti](https://foraisec.medium.com/autogpt-remote-code-execution-ssti) 
6. [https://blog\.christianposta\.com/understanding\-mcp\-and\-a2a\-attack\-vectors\-for\-ai\-agents/](https://blog.christianposta.com/understanding-mcp-and-a2a-attack-vectors-for-ai-agents/) 
7. [https://www\.stepsecurity\.io/blog/supply\-chain\-security\-alert\-popular\-nx\-build\-system\-package\-compromised\-with\-data\-stealing\-malware](https://www.stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware);
8. [https://jfrog\.com/blog/agentic\-software\-supply\-chain\-security\-ai\-assisted\-curation\-remediation/](https://jfrog.com/blog/agentic-software-supply-chain-security-ai-assisted-curation-remediation/) 

