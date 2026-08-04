package owasp.asi.asi05_code_execution_rce

import rego.v1

# ASI05 — Unexpected Code Execution (RCE)
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: An agent triggers unauthorized or unsafe code execution through its
# tool-use capabilities — directly (shell_exec, eval) or indirectly (writing
# and then running files, SQL injection via query builder tools, etc.).
# Attackers exploit this to achieve remote code execution (RCE), lateral movement,
# or data exfiltration from the underlying host.
#
# Controls:
#   1. Code execution tool denylist — block shell, eval, and interpreter tools
#   2. Inline code parameter detection — deny when params contain executable code
#   3. Sandbox mode enforcement — code execution only inside verified sandboxes
#   4. Interpreter invocation detection — block OS-level interpreter calls
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.action                          — tool name
#   input.params.code                     — code string to be executed
#   input.params.command                  — OS command to be run
#   input.params.script                   — script content
#   input.params.query                    — database query (for injection detection)
#   input.context.sandbox_verified        — bool; execution inside a verified sandbox
#   input.context.execution_environment   — "sandbox" | "container" | "host" | ""
#
# Config (override via data.config.asi05.*):
#   code_exec_tools        — set of tool names that execute code (always deny)
#   restricted_exec_tools  — set that may execute code inside a verified sandbox
#   dangerous_code_patterns — set of dangerous patterns in code/command params
#   require_sandbox        — bool; deny all code execution outside sandbox

_default_code_exec_tools := {
	"shell_exec",
	"exec",
	"execute",
	"run_command",
	"run_script",
	"os_command",
	"system",
	"popen",
	"subprocess",
	"eval",
	"exec_python",
	"run_python",
	"run_bash",
	"run_js",
	"node_eval",
	"php_exec",
	"ruby_exec",
}

_default_restricted_exec_tools := {
	"code_interpreter",
	"repl",
	"jupyter_execute",
	"docker_exec",
	"sandbox_run",
}

_default_dangerous_patterns := {
	"rm -rf",
	"mkfs",
	"dd if=",
	"format c:",
	":(){ :|:& };:",
	"curl | sh",
	"wget -O- | sh",
	"bash -i",
	"/dev/tcp/",
	"nc -e",
	"ncat -e",
	"python -c",
	"perl -e",
	"ruby -e",
	`__import__("os")`,
	"os.system(",
	"subprocess.call(",
	"subprocess.Popen(",
	"exec(base64",
	"eval(base64",
}

_code_exec_tools := s if {
	s := data.config.asi05.code_exec_tools
} else := _default_code_exec_tools

_restricted_exec_tools := s if {
	s := data.config.asi05.restricted_exec_tools
} else := _default_restricted_exec_tools

_dangerous_patterns := s if {
	s := data.config.asi05.dangerous_code_patterns
} else := _default_dangerous_patterns

_require_sandbox := v if {
	v := data.config.asi05.require_sandbox
} else := true

# ── Context helpers ───────────────────────────────────────────────────

_sandbox_verified := v if {
	v := input.context.sandbox_verified
} else := false

_exec_environment := v if {
	is_string(input.context.execution_environment)
	v := input.context.execution_environment
} else := ""

# ── Code/command param text ───────────────────────────────────────────

_code_param_texts contains v if {
	some field in {"code", "command", "script", "query", "input"}
	v := input.params[field]
	is_string(v)
}

_has_dangerous_pattern if {
	some text in _code_param_texts
	some pattern in _dangerous_patterns
	contains(lower(text), lower(pattern))
}

# ── Deny: always-blocked code execution tool ──────────────────────────

deny contains msg if {
	input.action in _code_exec_tools
	msg := sprintf(
		"ASI05 — Unexpected Code Execution: tool '%v' performs unrestricted code execution — action blocked.",
		[input.action],
	)
}

# ── Deny: dangerous pattern in code parameters ───────────────────────

deny contains msg if {
	_has_dangerous_pattern
	msg := sprintf(
		"ASI05 — Unexpected Code Execution: dangerous execution pattern detected in parameters for '%v' — action blocked.",
		[input.action],
	)
}

# ── Deny: restricted execution tool outside sandbox ──────────────────

deny contains msg if {
	_require_sandbox
	input.action in _restricted_exec_tools
	not _sandbox_verified
	msg := sprintf(
		"ASI05 — Unexpected Code Execution: tool '%v' requires a verified sandbox — current environment '%v' is not verified.",
		[input.action, _exec_environment],
	)
}

# ── Escalate: restricted tool inside sandbox (audit required) ─────────

escalate contains msg if {
	input.action in _restricted_exec_tools
	_sandbox_verified
	msg := sprintf(
		"ASI05 — Unexpected Code Execution: sandbox code execution via '%v' — route to execution audit log.",
		[input.action],
	)
}

# ── Decision: most restrictive wins ──────────────────────────────────

decision := "deny" if {
	count(deny) > 0
}

decision := "escalate" if {
	count(deny) == 0
	count(escalate) > 0
}

decision := "allow" if {
	count(deny) == 0
	count(escalate) == 0
}
