package owasp.asi.asi07_inter_agent_communication

import rego.v1

# ASI07 — Insecure Inter-Agent Communication
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: Messages or instructions passed between agents in a multi-agent pipeline
# are not authenticated, integrity-checked, or origin-verified. An attacker can
# inject malicious messages, spoof a trusted orchestrator, replay captured messages,
# or exploit unauthenticated agent-to-agent channels to alter downstream behaviour.
#
# Controls:
#   1. Caller agent identity validation — caller must be in the trusted agent registry
#   2. Message signature requirement — signed messages required for privileged operations
#   3. Protocol enforcement — only allow-listed inter-agent protocols accepted
#   4. Message freshness — reject replayed or timestamp-expired messages
#   5. Payload injection scan — inter-agent payloads scanned for injection patterns
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.caller_agent                    — identity of the sending agent
#   input.context.trusted_agents          — set of known legitimate agent identifiers
#   input.context.message_signature       — cryptographic signature of the message (optional)
#   input.context.message_timestamp       — Unix epoch when the message was created
#   input.context.current_timestamp       — current Unix epoch (from the runtime)
#   input.context.protocol                — inter-agent protocol used ("a2a" | "mcp" | "internal")
#   input.params.payload                  — message payload content (scanned for injection)
#   input.context.requires_signed_message — bool; set by the receiving agent if it requires signing
#
# Config (override via data.config.asi07.*):
#   trusted_agents         — set of trusted agent identifiers
#   allowed_protocols      — set of allowed inter-agent protocols
#   max_message_age        — maximum message age in seconds (replay prevention)
#   require_signatures     — bool; always require signed messages
#   injection_patterns     — set of patterns indicating a poisoned inter-agent payload

_default_allowed_protocols := {"a2a", "mcp", "internal", "grpc"}

_default_max_message_age := 300

_default_require_signatures := false

_default_injection_patterns := {
	"ignore previous instructions",
	"override your",
	"you are now",
	"new instructions:",
	"forget your instructions",
	"pretend to be",
	"disregard",
	"system prompt:",
	"your real instructions",
}

_trusted_agents := s if {
	s := data.config.asi07.trusted_agents
} else if {
	s := input.context.trusted_agents
	is_set(s)
}

_allowed_protocols := s if {
	s := data.config.asi07.allowed_protocols
} else := _default_allowed_protocols

_max_message_age := v if {
	v := data.config.asi07.max_message_age
} else := _default_max_message_age

_require_signatures := v if {
	v := data.config.asi07.require_signatures
} else := _default_require_signatures

_injection_patterns := s if {
	s := data.config.asi07.injection_patterns
} else := _default_injection_patterns

# ── Context helpers ───────────────────────────────────────────────────

_caller_agent := v if {
	is_string(input.caller_agent)
	v := input.caller_agent
} else := ""

_protocol := v if {
	is_string(input.context.protocol)
	v := input.context.protocol
} else := ""

_msg_timestamp := v if {
	is_number(input.context.message_timestamp)
	v := input.context.message_timestamp
} else := 0

_curr_timestamp := v if {
	is_number(input.context.current_timestamp)
	v := input.context.current_timestamp
} else := 0

_has_signature if {
	is_string(input.context.message_signature)
	input.context.message_signature != ""
}

_payload := v if {
	is_string(input.params.payload)
	v := input.params.payload
} else := ""

# ── Detection helpers ─────────────────────────────────────────────────

_caller_is_unknown if {
	_caller_agent != ""
	count(_trusted_agents) > 0
	not _caller_agent in _trusted_agents
}

_protocol_not_allowed if {
	_protocol != ""
	not _protocol in _allowed_protocols
}

_message_is_stale if {
	_msg_timestamp > 0
	_curr_timestamp > 0
	_curr_timestamp - _msg_timestamp > _max_message_age
}

_signature_required if {
	_require_signatures
}

_signature_required if {
	input.context.requires_signed_message == true
}

_has_injection_in_payload if {
	_payload != ""
	some pattern in _injection_patterns
	contains(lower(_payload), pattern)
}

# ── Deny: unrecognised caller, bad protocol, replayed message, injection ──

deny contains msg if {
	_caller_is_unknown
	msg := sprintf(
		"ASI07 — Inter-Agent Communication: caller agent '%v' is not in the trusted agent registry — message blocked.",
		[_caller_agent],
	)
}

deny contains msg if {
	_protocol_not_allowed
	msg := sprintf(
		"ASI07 — Inter-Agent Communication: protocol '%v' is not in the allowed list — message blocked.",
		[_protocol],
	)
}

deny contains msg if {
	_message_is_stale
	msg := sprintf(
		"ASI07 — Inter-Agent Communication: message from '%v' is too old (age > %vs) — possible replay attack, blocked.",
		[_caller_agent, _max_message_age],
	)
}

deny contains msg if {
	_has_injection_in_payload
	msg := sprintf(
		"ASI07 — Inter-Agent Communication: injection pattern detected in message payload from '%v' — blocked.",
		[_caller_agent],
	)
}

# ── Escalate: signature missing when required ─────────────────────────

escalate contains msg if {
	_signature_required
	not _has_signature
	not _caller_is_unknown
	msg := sprintf(
		"ASI07 — Inter-Agent Communication: message from '%v' requires a cryptographic signature — route for verification.",
		[_caller_agent],
	)
}

# ── Escalate: unidentified caller (no caller_agent set) ───────────────

escalate contains msg if {
	_caller_agent == ""
	msg := "ASI07 — Inter-Agent Communication: inter-agent message has no caller identity — route for origin verification."
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
