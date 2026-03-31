## ASI04 – Agentic Supply Chain Vulnerabilities

**Description:**

Agentic Supply Chain Vulnerabilities arise when compromised models, agents, tools, or artifacts in dynamic MCP and A2A ecosystems threaten system integrity. Unlike traditional software supply chains where packages are vetted at build time, agentic supply chains are dynamic — MCP servers, skills, and plugins are installed, updated, and composed at runtime with minimal verification. A single compromised component can affect thousands of downstream users.

This category covers: skill impersonation and typosquatting, description-behavior mismatches (trojaned tools), hidden capabilities via undocumented parameters, skill chain attacks (composing benign tools into malicious sequences), update attacks (poisoning previously trusted tools), parameter injection, polymorphic skills that evade detection, and registry poisoning.

**Common Examples of Vulnerability:**

1. Example 1: **Skill Impersonation and Typosquatting:** Attackers publish malicious packages with names similar to popular tools — `filesytem_read` (typosquatted `filesystem_read`), `gtihub-api` (typosquatted `github-api`), `official-filesystem` (trust-implying prefix), or `google-search-v2-pro` (fake enhanced version). Aikido research found 19.7% of LLM-hallucinated package names were squattable ("slopsquatting"). ATR scans of 36,394 ClawHub skills found 182 CRITICAL and 1,124 HIGH severity findings using these patterns.

2. Example 2: **Trojaned Tools with Hidden Parameters:** A calculator tool functions normally but contains hidden parameters: `{"expression": "2+2", "__backdoor__": "reverse_shell"}` or `{"text": "hello", "debug_mode": true, "raw_exec": "cat /etc/shadow"}`. These undocumented parameters (`debug_mode`, `admin_override`, `raw_exec`, `unsafe_mode`, `no_sandbox`) unlock dangerous functionality invisible during normal operation.

3. Example 3: **Post-Trust Update Poisoning:** A skill operates safely through multiple versions, building user trust. After establishing a user base, a malicious update is pushed: "Version changed. Additional permissions required: filesystem_write, network_access. Please re-authenticate." Or: "Migration required. Please export your data to https://evil-mirror.com/backup before updating." The trust earned by previous versions is exploited to bypass user scrutiny.

**How to Prevent:**

1. Prevention Step 1: **Registry-Level Scanning:** Scan all skills/tools at installation time using pattern-based detection rules. ATR provides 8 rules for supply chain detection: ATR-2026-060 (Skill Impersonation covering typosquats for filesystem, GitHub, OpenAI, Anthropic, and other popular tools), ATR-2026-061 (Description-Behavior Mismatch), ATR-2026-062 (Hidden Capability), and ATR-2026-089 (Polymorphic Skill). Scanning 36,394 ClawHub skills with ATR revealed 182 CRITICAL and 1,124 HIGH findings, demonstrating the scale of the problem.

2. Prevention Step 2: **Behavioral Monitoring at Runtime:** Static analysis alone is insufficient — description-behavior mismatches can only be detected at runtime. Monitor tool invocations for unexpected operations: a `weather_lookup` tool making `curl` calls, a `text_formatter` executing shell commands, or any tool accessing credential files. ATR-2026-061 detects write/delete operations, network calls, shell/subprocess invocations, and credential access in tool arguments and responses.

3. Prevention Step 3: **Version Pinning and Update Review:** Pin skill versions to prevent automatic updates. When updates are available, review permission changes and new capabilities before accepting. ATR-2026-065 (Skill Update Attack) detects suspicious update behaviors: version change notifications requesting expanded permissions, re-authentication demands, and data export to external URLs. Treat any post-update permission expansion as a potential attack.

**Example Attack Scenarios:**

Scenario #1: The ClawHavoc campaign published 1,184 malicious MCP skills to ClawHub, all containing command-and-control callbacks to 91.92.242.30. Skills appeared as legitimate developer tools (code formatters, API helpers, file managers) but silently exfiltrated API keys and environment variables on installation. The campaign exploited the lack of registry-level scanning — none of the affected registries performed security review of submitted packages. Related real-world incidents: AMOS infostealer campaign (314 skills from publisher "hightower6eu" targeting cryptocurrency wallets), CVE-2026-25253 (OpenClaw RCE via auth token exfiltration, CVSS 8.8), CVE-2026-28363 (ClawJacked WebSocket brute-force hijack, CVSS 9.9).

Scenario #2: An attacker uses three individually benign skills in sequence: (1) `file_reader` reads `~/.aws/credentials` (a legitimate file reading tool); (2) `text_encoder` base64-encodes the credentials (a legitimate encoding tool); (3) `send_webhook` posts the encoded data to `https://hookbin.com/abc123` (a legitimate webhook tool). No individual tool is malicious — the attack emerges from the composition. ATR-2026-063 (Skill Chain Attack) detects this pattern by monitoring for sensitive file access followed by encoding followed by exfiltration to known data collection endpoints (webhook.site, ngrok, requestbin, pipedream, burpcollaborator).

**Reference Links:**

1. [ATR-2026-060: Skill Impersonation](https://github.com/Agent-Threat-Rule/agent-threat-rules): Typosquatting detection for major tool ecosystems (filesystem, GitHub, OpenAI, Anthropic, Slack).
2. [CVE-2026-28363: ClawJacked](https://nvd.nist.gov/vuln/detail/CVE-2026-28363): OpenClaw WebSocket brute-force hijack (CVSS 9.9).
3. [CVE-2026-25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253): OpenClaw RCE via auth token exfiltration (CVSS 8.8).
4. [Snyk ToxicSkills Report](https://snyk.io/blog/toxicskills/): 3,984 MCP skills scanned, 76 confirmed malicious (36.82% had flaws).
5. [Aikido Slopsquatting Research](https://www.aikido.dev/blog/slopsquatting): 19.7% of LLM-hallucinated package names are squattable.
