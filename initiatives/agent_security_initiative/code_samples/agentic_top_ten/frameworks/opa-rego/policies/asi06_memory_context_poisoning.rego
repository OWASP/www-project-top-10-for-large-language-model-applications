package owasp.asi.asi06_memory_context_poisoning

import rego.v1

# ASI06 — Memory & Context Poisoning
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: An attacker corrupts an agent's persistent memory, retrieved context,
# or conversation history to distort reasoning and decision-making. Poisoned
# memories can persist across sessions, silently steering an agent's future
# actions long after the initial injection.
#
# Controls:
#   1. Memory source validation — only trusted sources may populate agent memory
#   2. Injection pattern scanning — recalled context checked for injection phrases
#   3. Memory age enforcement — stale entries beyond TTL are rejected
#   4. Cross-session boundary enforcement — memory from other sessions requires verification
#   5. Memory write audit — all writes to long-term memory are flagged for review
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.action                       — "read_memory" | "write_memory" | "recall_context"
#   input.memory.source                — origin of the memory entry (e.g. "user", "tool", "retrieval")
#   input.memory.content               — text content of the memory entry
#   input.memory.session_id            — session that created this memory entry
#   input.memory.age_seconds           — how old the memory entry is
#   input.context.current_session_id   — active session identifier
#   input.context.trusted_sources      — set of trusted memory source identifiers
#   input.context.max_memory_age       — max allowed age in seconds (optional override)
#
# Config (override via data.config.asi06.*):
#   trusted_sources       — set of trusted memory source names
#   max_memory_age        — maximum age in seconds before memory is rejected
#   require_session_match — bool; deny cross-session memory without verification
#   injection_patterns    — set of patterns that indicate a poisoned memory entry

_default_trusted_sources := {
	"system",
	"verified_tool",
	"authenticated_user",
	"internal",
}

_default_max_memory_age := 86400

_default_require_session_match := true

_default_injection_patterns := {
	"ignore previous instructions",
	"ignore all previous",
	"you are now",
	"new instructions:",
	"override your",
	"forget your instructions",
	"pretend to be",
	"your real instructions",
	"from now on",
	"disregard",
}

_trusted_sources := s if {
	s := data.config.asi06.trusted_sources
} else := _default_trusted_sources

_max_memory_age := v if {
	v := data.config.asi06.max_memory_age
} else := _default_max_memory_age

_require_session_match := v if {
	v := data.config.asi06.require_session_match
} else := _default_require_session_match

_injection_patterns := s if {
	s := data.config.asi06.injection_patterns
} else := _default_injection_patterns

# ── Context helpers ───────────────────────────────────────────────────

_memory_source := v if {
	is_string(input.memory.source)
	v := input.memory.source
} else := ""

_memory_content := v if {
	is_string(input.memory.content)
	v := input.memory.content
} else := ""

_memory_session := v if {
	is_string(input.memory.session_id)
	v := input.memory.session_id
} else := ""

_memory_age := v if {
	is_number(input.memory.age_seconds)
	v := input.memory.age_seconds
} else := 0

_current_session := v if {
	is_string(input.context.current_session_id)
	v := input.context.current_session_id
} else := ""

# ── Detection helpers ─────────────────────────────────────────────────

_from_untrusted_source if {
	_memory_source != ""
	not _memory_source in _trusted_sources
}

_has_injection_pattern if {
	_memory_content != ""
	some pattern in _injection_patterns
	contains(lower(_memory_content), pattern)
}

_memory_is_stale if {
	_memory_age > _max_memory_age
}

_cross_session_unverified if {
	_require_session_match
	_memory_session != ""
	_current_session != ""
	_memory_session != _current_session
	input.context.cross_session_verified != true
}

# ── Deny: confirmed poisoning indicators ─────────────────────────────

deny contains msg if {
	_has_injection_pattern
	msg := "ASI06 — Memory & Context Poisoning: injection pattern detected in recalled memory — blocked."
}

deny contains msg if {
	_from_untrusted_source
	msg := sprintf(
		"ASI06 — Memory & Context Poisoning: memory source '%v' is not in the trusted sources list — blocked.",
		[_memory_source],
	)
}

deny contains msg if {
	_cross_session_unverified
	msg := sprintf(
		"ASI06 — Memory & Context Poisoning: unverified cross-session memory from session '%v' — blocked.",
		[_memory_session],
	)
}

# ── Escalate: stale memory, write operations ──────────────────────────

escalate contains msg if {
	_memory_is_stale
	not _has_injection_pattern
	not _from_untrusted_source
	msg := sprintf(
		"ASI06 — Memory & Context Poisoning: memory entry is %v seconds old (max: %v) — route for freshness verification.",
		[_memory_age, _max_memory_age],
	)
}

escalate contains msg if {
	input.action == "write_memory"
	not _has_injection_pattern
	msg := "ASI06 — Memory & Context Poisoning: long-term memory write — route to memory audit log."
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
