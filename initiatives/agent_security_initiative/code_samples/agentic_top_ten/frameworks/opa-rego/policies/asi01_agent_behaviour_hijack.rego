package owasp.asi.asi01_agent_behaviour_hijack

import rego.v1

# ASI01 — Agent Behaviour Hijack
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: An adversary manipulates an agent's goals, plans, or instructions to
# pursue attacker-aligned objectives — typically through prompt injection, goal
# overriding, or instruction smuggling via tool outputs, retrieved documents, or
# user-supplied text.
#
# Controls:
#   1. Known injection phrase detection (configurable pattern set)
#   2. Structural injection marker detection ([INST], <|system|>, etc.)
#   3. Goal override attempt detection in system-facing fields
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.action              — action name being evaluated
#   input.params              — map of named parameters (prompt, message, content, etc.)
#   input.context.task_type   — optional; "orchestration" tasks apply stricter patterns
#
# Config (override via data.config.asi01.*):
#   patterns             — set of injection phrase strings (case-insensitive)
#   structural_indicators — set of structural injection tokens
#   strict_orchestration — bool; extra patterns for orchestrator roles

_default_patterns := {
	"ignore previous instructions",
	"ignore all previous",
	"disregard your instructions",
	"disregard all previous",
	"forget your instructions",
	"forget previous instructions",
	"you are now",
	"act as if you are",
	"act as though you",
	"pretend you are",
	"pretend to be",
	"new instructions:",
	"override your",
	"jailbreak",
	"bypass your",
	"ignore your guidelines",
	"ignore your rules",
	"your new purpose",
	"your real instructions",
	"respond only with",
	"from now on you",
	"your new identity",
	"simulate a",
	"you must now",
}

_default_structural := {
	"[inst]",
	"<|system|>",
	"<|im_start|>system",
	"###system",
	"---system---",
	"<system>",
	"</system>",
	"[system prompt]",
	"{{system}}",
	"<<sys>>",
	"[user]",
	"[/user]",
	"<|endoftext|>",
}

_orchestration_patterns := {
	"change your goal",
	"update your objective",
	"stop following",
	"abandon your task",
	"your new mission",
	"redirect your",
}

_injection_patterns := p if {
	p := data.config.asi01.patterns
} else := _default_patterns

_structural_indicators := p if {
	p := data.config.asi01.structural_indicators
} else := _default_structural

_strict_orchestration := v if {
	v := data.config.asi01.strict_orchestration
} else := false

# User-controlled text fields most likely to carry injection payloads
_user_text_fields := {
	"prompt", "message", "user_input", "query",
	"text", "input", "content", "instruction",
	"document", "context", "retrieved_text", "tool_result",
}

_user_texts contains v if {
	some field in _user_text_fields
	v := input.params[field]
	is_string(v)
}

# ── Detection helpers ─────────────────────────────────────────────────

_has_injection_pattern if {
	some text in _user_texts
	some pattern in _injection_patterns
	contains(lower(text), pattern)
}

_has_structural_indicator if {
	some text in _user_texts
	some indicator in _structural_indicators
	contains(lower(text), indicator)
}

_has_orchestration_pattern if {
	_strict_orchestration
	input.context.task_type == "orchestration"
	some text in _user_texts
	some pattern in _orchestration_patterns
	contains(lower(text), pattern)
}

# ── Deny: confirmed injection ─────────────────────────────────────────

deny contains msg if {
	_has_injection_pattern
	msg := "ASI01 — Agent Behaviour Hijack: known injection phrase detected in input — action blocked."
}

deny contains msg if {
	_has_orchestration_pattern
	msg := "ASI01 — Agent Behaviour Hijack: goal-override pattern detected in orchestration context — action blocked."
}

# ── Escalate: structural marker (possible injection, needs review) ────

escalate contains msg if {
	_has_structural_indicator
	not _has_injection_pattern
	msg := "ASI01 — Agent Behaviour Hijack: structural injection marker detected — route to human review."
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
