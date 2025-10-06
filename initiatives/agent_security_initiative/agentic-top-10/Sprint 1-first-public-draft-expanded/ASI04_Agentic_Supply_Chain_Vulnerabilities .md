# ASI04 | Agentic Supply Chain Vulnerabilities

## Description:

Agentic systems dynamically load behaviors and components like tools, prompts, plugins, models, and agent-to-agent coordination protocols at runtime. This makes the agent’s operational logic partially externalized and mutable, creating a supply chain where security depends not only on the agent itself, but also on the integrity of upstream vendors, plugins and lateral agents. Any compromised dependency can cascade into another agent’s workflow when pulled, amplifying risk.  
This scope differs from traditional LLM supply chain risks (LLM03:2025), which primarily cover static corruption of training data, model weights, or tokenizer artifacts. In contrast, agentic supply chain threats center on how adversaries can exploit runtime-mutable orchestration layer, and exploit decentralized nature of agentic system where components are dynamically loaded, swapped, or shared between agents without centralized assurance.

This differs from ASI02 Tool Misuse, which addresses agents misusing a tool they were explicitly granted. ASI07 addresses the deeper risk of the tool (or memory, or collaborator agent) itself being poisoned, impersonated, or hijacked before the agent even uses it. When this happens, the consequences extend beyond simple trust violations. Attackers may trigger data leakage by exfiltrating sensitive prompts, context, or retrieved information; they may conduct output manipulation to inject biased, misleading, or harmful responses into downstream workflows; or they may achieve workflow hijacking, silently redirecting task execution to serve attacker objectives rather than user intent.

These risks grow more acute in heterogeneous, distributed agent ecosystems, especially when agents interact across organizational or platform boundaries (via MCP or A2A protocols). Thus, ensuring provenance, maintaining trust zones, and safeguarding prompt/tool integrity become significantly harder because no single organization fully controls the operational surface of the agent.

### How it differ from Traditional Appsec Supply Chain Risks

AppSec supply chain risks emerge when code or dependencies can be modified in ways that alter application logic for eg, a package update that silently overrides an internal function. Agentic AI supply chain risks, on the other hand, stem from the runtime orchestration layer unique to LLMs, where context, prompts, and tool calls are assembled. Here, the concern is not only how code executes, but how the agent’s reasoning, goals, and operational flow could be influenced raising the risk of harmful autonomous actions or unintended privilege escalation without direct code-level flaws.

The difference lies in the blast radius: AppSec issues become amplified when they flow into Agentic orchestration, which can be escalated into data leakage, output manipulation, or workflow hijacking, enabled by runtime mechanisms as discussed above.AI supply chain security isn’t about what the manifest declares,it’s about what actually runs.

## Common Examples of Vulnerability:

1. **Poisoned prompt templates loaded remotely.** An agent automatically pulls prompt templates from an external source that contain hidden instructions (e.g., to exfiltrate data or perform destructive actions), leading it to execute malicious behavior without developer intent.  
2. **Tool-descriptor injection.** An attacker embeds hidden instructions or malicious payloads into a tool’s metadata or MCP/agent-card, which the host agent interprets as trusted guidance and acts upon.  
3. **Impersonation and typosquatting.** When an agent dynamically discovers or connects to external tools or services, it can be deceived in two ways by a typosquatted endpoint (a look-alike name chosen to trick resolution) or by a symbol attack, where a malicious service deliberately impersonates a legitimate tool or agent, mimicking its identity, API, and behavior to gain trust and execute malicious actions 
4. **Post-install backdoor with local AI-CLI abuse.** A compromised package installs post-install hooks that run on developer machines, probing for secrets and invoking local AI assistants with crafted prompts to autonomously locate and exfiltrate credentials and files.

## 

## Prevention and Mitigation Strategies

Preventing Agentic AI Supply Chain Risks requires defense-in-depth to secure both static artifacts (models, plugins, prompts) and dynamic orchestration layers (memory, tools, agent-to-agent protocols). We separate mitigations into Classical Supply Chain Security Measures and Agentic-specific Mitigation Practices to emphasize that organizations must first establish traditional hygiene before layering on new defenses unique to agentic systems.

### Classical Supply Chain Security Measures

Artifact Provenance & Trusted Sources

* Digitally sign agent configuration manifests, prompt templates, and model/tool definitions using verifiable attestation frameworks (Cosign).  
* Require SBOMs for all agent runtime components, including frameworks, connectors, and memory modules.  
* Maintain curated internal registries; block pre-trained models, plugins, or tools sourced from untrusted repositories, as recommended in ASI03 to minimize unverified components.

Dependency Control & Orchestration Gatekeeping

* Apply strict allowlisting of approved extensions and retrievers; enforce dependency pinning to prevent supply-chain drift.  
* Conduct typosquatting and spoof detection for orchestration packages in ecosystems like PyPI,npm, LangChain or LlamaIndex.  
* Limit installation or runtime activation of external plugins/models before verification against provenance requirements.  
* Extend AppSec supply-chain gates (SCA/SAST) with agentic policy controls, rejecting unsigned components, unverified SBOMs, and poisoned prompt flows.

Containerized execution & Build integrity

* Agents with OS-level or sensitive tool access run in sandboxed containers with strict network/syscall restrictions to contain malicious plugin/tool behaviors.  
* Require reproducible builds for orchestrators and model adapters, ensuring compiled agents cannot silently alter logic.

### Agentic specific Mitigation Practices

Secure Prompts, Scripts & Memory Definitions

* Apply version control and peer review for all prompt repositories, orchestration scripts, and memory schema definitions, as with source code.  
* Scan for anomalies in prompt templates or memory insertion logic that could modify agent reasoning pathways.

Inter-Agent Protocol Security

* Enforce mutual authentication and attestation in inter-agent protocols like A2A or MCP through PKI-based mutual TLS.  
* Avoid open agent registration without validation, ensuring only authenticated, trusted agents join multi-agent ecosystems.  
* Sign and verify all inter-agent messages to prevent impersonation or unauthorized orchestration influence.

Active Testing, Drift & Red-Teaming

* Perform red-team simulations of poisoned components (malicious plugin, poisoned prompt template, compromised collaborator agent) against poisoned components.  
* Enable rollback and version control across prompts, tool definitions, and memory to revert compromised configurations.

Continuous Validation & Threat Monitoring

* Validate and re-check signatures, hashes, and SBOM lineage of components throughout runtime, not only at install time.  
* Monitor agent behavior, privilege use, and component lineage for indicators of anomalous actions or data exfiltration, and apply practices from ASI01 to handle deviations in agent output and reasoning.  
* Collect telemetry across inter-module communication to detect manipulated state, poisoned memories, or unauthorized collaborator inputs.

## Example Attack Scenarios:

### Scenario 1: Amazon Q Supply Chain Compromise

An attacker injects a destructive prompt into the GitHub repository of Amazon's Q agent for VS Code, instructing it to wipe the system to a near-factory state. The malicious update (v1.84.0) is published unknowingly by Amazon, affecting thousands of developers before it’s caught. Although the prompt fails to execute as intended, it demonstrates how upstream poisoning of agent logic via supply chain access can lead to catastrophic outcomes. This is attacks started as traditional Supply Chain exploitation but downstream impact in Agentic AI amplifying the blast radius through agent extension.

[https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/](https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/)

### Scenario 2: Nx npm (S1ngularity) Supply Chain Compromise

The S1ngularity attack abused a vulnerable GitHub Actions workflow to publish a backdoored Nx npm package that ran a post-install credential harvester. The malware probed developer machines for installed AI CLI assistants (Claude, Gemini, OpenAI Codex, Amazon Q etc.), used tailored LLM prompts to prioritize and locate high-value secrets, then exfiltrated tokens and keys to attacker-controlled repositories. With the stolen GitHub tokens the attackers automated mass disclosure making thousands of private repos public and leaking repositories across hundreds of organizations.   
[https://orca.security/resources/blog/s1ngularity-supply-chain-attack/](https://orca.security/resources/blog/s1ngularity-supply-chain-attack/) 

### Scenario 3: MCP Tool Descriptor Poisoning 

A researcher demonstrates a prompt injection vulnerability in GitHub’s Model Context Protocol (MCP), where a malicious public tool includes hidden instructions in its metadata. When invoked, the AI assistant obeys the embedded command exfiltrating private repo data without user awareness.  
 [https://invariantlabs.ai/blog/mcp-github-vulnerability](https://invariantlabs.ai/blog/mcp-github-vulnerability)

### Scenario 4: Malicious MCP Server Impersonating Postmark 

Reported as the first in-the-wild malicious MCP server on npm, it impersonated postmark-mcp and secretly BCC’d emails to the attacker.[https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft](https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft)

### Scenario 5: AgentSmith Prompt-Hub Proxy Attack 

Manipulates dynamic agentic orchestration via exfiltrating data and hijacking agent response flows through prompt proxying , thereby a operational layer attack enabled by dynamic orchestration within agentic systems. [https://noma.security/blog/how-an-ai-agent-vulnerability-in-langsmith-could-lead-to-stolen-api-keys-and-hijacked-llm-responses/](https://noma.security/blog/how-an-ai-agent-vulnerability-in-langsmith-could-lead-to-stolen-api-keys-and-hijacked-llm-responses/)

### Mapping to OWASP Top 10 for LLMs

LLM03: Supply Chain focuses on how models and components are built, fine-tuned, or published, with risks tied to static artifacts such as datasets, weights, and adapters. Agentic Supply Chain extends this view into both development-time tooling (e.g., compromised IDE extensions, package registries, or AI coding assistants) and runtime orchestration (e.g., poisoned MCP descriptors, typosquatted services). The risk shifts from what components are shipped to how components are dynamically loaded, shared, and trusted once agents operate.

### Mapping to OWASP ASI: Threats and Mitigations 

* **T2 Tool Misuse:** Compromised tools, registries, or prompt templates pulled at runtime can cause agents to execute unintended actions while still appearing “authorized.”  
* **T11 Unexpected RCE and Code Attacks:** Poisoned plugins or packages introduced via supply chain channels can embed malicious payloads or hidden backdoors.  
* **T12 Agent Communication Poisonin:** Malicious or altered MCP/A2A descriptors act as supply-chain vectors, allowing attackers to hijack communication flows and influence system behavior.  
* **T13 Rogue Agents in Multi-Agent Systems:** A compromised agent inserted through registries or development-time coding assistants can persist as a rogue actor, enabling systemic damage or data exfiltration.

## Reference Links:

1. [https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/](https://www.bleepingcomputer.com/news/security/amazon-ai-coding-agent-hacked-to-inject-data-wiping-commands/)   
2. [https://invariantlabs.ai/blog/mcp-github-vulnerability](https://invariantlabs.ai/blog/mcp-github-vulnerability)   
3. [https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-in-the-middle-abusing-agent-cards-in-the-agent-2-agent-protocol-to-win-all-the-tasks/](https://www.trustwave.com/en-us/resources/blogs/spiderlabs-blog/agent-in-the-middle-abusing-agent-cards-in-the-agent-2-agent-protocol-to-win-all-the-tasks/)   
4. [https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft](https://www.koi.security/blog/postmark-mcp-npm-malicious-backdoor-email-theft)   
5. [https://noma.security/blog/how-an-ai-agent-vulnerability-in-langsmith-could-lead-to-stolen-api-keys-and-hijacked-llm-responses/](https://noma.security/blog/how-an-ai-agent-vulnerability-in-langsmith-could-lead-to-stolen-api-keys-and-hijacked-llm-responses/)   
6. [LLM03:2025 Supply Chain](https://genai.owasp.org/llmrisk/llm032025-supply-chain/)   
7. [Agentic AI \-Threats And Mitigation](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/)  
8. [https://blog.christianposta.com/understanding-mcp-and-a2a-attack-vectors-for-ai-agents/](https://blog.christianposta.com/understanding-mcp-and-a2a-attack-vectors-for-ai-agents/)   
9. [https://www.stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware](https://www.stepsecurity.io/blog/supply-chain-security-alert-popular-nx-build-system-package-compromised-with-data-stealing-malware);  
10. [https://jfrog.com/blog/agentic-software-supply-chain-security-ai-assisted-curation-remediation/](https://jfrog.com/blog/agentic-software-supply-chain-security-ai-assisted-curation-remediation/) 

    
