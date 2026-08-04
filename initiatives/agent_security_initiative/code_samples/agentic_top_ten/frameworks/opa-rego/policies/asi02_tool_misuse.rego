package owasp.asi.asi02_tool_misuse

import rego.v1

# ASI02 — Tool Misuse and Exploitation
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: An agent is tricked or coerced into using its tools in harmful or
# unintended ways — calling tools with malicious parameters, invoking tools
# outside their intended scope, or chaining tools to amplify impact.
#
# Controls:
#   1. Explicit tool denylist (always blocked)
#   2. Allowlist mode: deny any tool not on the approved list
#   3. Restricted tools: require human approval before execution
#   4. Parameter guard: deny dangerous parameter values regardless of tool
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.action                — the tool name being invoked
#   input.params                — map of tool call parameters
#   input.context.approved_by   — optional human approval token
#
# Config (override via data.config.asi02.*):
#   allowed      — set of tool names (allowlist mode when non-empty)
#   denied       — set of tool names always blocked
#   restricted   — set of tool names requiring human pre-approval
#   param_guards — map of param_name → set of forbidden values

_default_denied := {
	"drop_table",
	"truncate_table",
	"wipe_database",
	"format_disk",
	"factory_reset",
}

_default_restricted := {
	"delete_record",
	"bulk_delete",
	"send_email",
	"send_sms",
	"send_bulk_email",
	"send_bulk_sms",
	"file_delete",
	"deploy",
	"modify_permissions",
	"grant_admin",
	"revoke_access",
	"initiate_payment",
	"approve_transfer",
	"publish_content",
	"call_external_api",
}

_default_param_guards := {
	"sql": {"DROP TABLE", "DROP DATABASE", "TRUNCATE", "DELETE FROM", "EXEC("},
	"command": {"rm -rf", "mkfs", "dd if=", "chmod 777", "curl | sh", "wget -O- | sh"},
}

_allowed_tools := s if {
	s := data.config.asi02.allowed
} else := set()

_denied_tools := s if {
	s := data.config.asi02.denied
} else := _default_denied

_restricted_tools := s if {
	s := data.config.asi02.restricted
} else := _default_restricted

_param_guards := m if {
	m := data.config.asi02.param_guards
} else := _default_param_guards

_allowlist_active if {
	count(_allowed_tools) > 0
}

# ── Approval check ────────────────────────────────────────────────────

_has_human_approval if {
	is_string(input.context.approved_by)
	input.context.approved_by != ""
}

# ── Dangerous parameter detection ─────────────────────────────────────

_has_dangerous_param if {
	some param_name, forbidden_values in _param_guards
	some forbidden_value in forbidden_values
	param_value := input.params[param_name]
	is_string(param_value)
	contains(upper(param_value), upper(forbidden_value))
}

# ── Deny: explicitly blocked tool ─────────────────────────────────────

deny contains msg if {
	input.action in _denied_tools
	msg := sprintf("ASI02 — Tool Misuse: '%v' is on the denylist — action blocked.", [input.action])
}

# ── Deny: not in allowlist (when allowlist is active) ─────────────────

deny contains msg if {
	_allowlist_active
	not input.action in _allowed_tools
	not input.action in _denied_tools
	msg := sprintf("ASI02 — Tool Misuse: '%v' is not in the approved tools list.", [input.action])
}

# ── Deny: dangerous parameter value ──────────────────────────────────

deny contains msg if {
	_has_dangerous_param
	msg := sprintf("ASI02 — Tool Misuse: dangerous parameter value detected in call to '%v' — action blocked.", [input.action])
}

# ── Escalate: restricted tool requires pre-approval ──────────────────

escalate contains msg if {
	input.action in _restricted_tools
	not input.action in _denied_tools
	not _has_human_approval
	msg := sprintf("ASI02 — Tool Misuse: '%v' requires human pre-approval before execution.", [input.action])
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
