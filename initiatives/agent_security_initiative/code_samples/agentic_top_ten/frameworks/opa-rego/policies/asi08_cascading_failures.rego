package owasp.asi.asi08_cascading_failures

import rego.v1

# ASI08 — Cascading Failures
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: A fault, hallucination, or adversarial input at one point in a multi-agent
# pipeline propagates and amplifies through downstream agents, causing compounded
# failures — incorrect outputs acted upon, resources exhausted, or unintended
# irreversible actions taken at scale before a human can intervene.
#
# Controls:
#   1. Consecutive error circuit breaker — halt pipeline when errors exceed threshold
#   2. Orchestration depth limit — deny when agent call depth exceeds safe maximum
#   3. Confidence floor — escalate when agent output confidence falls below minimum
#   4. Retry storm prevention — deny when retry count exceeds allowed maximum
#   5. Human oversight checkpoint — escalate high-stakes actions in a degraded pipeline
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.action                             — action being requested
#   input.context.consecutive_errors         — number of consecutive failures in this pipeline
#   input.context.orchestration_depth        — current agent call nesting depth
#   input.context.output_confidence          — float 0–1 from the upstream model (optional)
#   input.context.retry_count                — number of times this action has been retried
#   input.context.pipeline_degraded          — bool; set when at least one upstream error occurred
#   input.context.high_stakes                — bool; set for irreversible/financial/PII actions
#
# Config (override via data.config.asi08.*):
#   max_consecutive_errors   — error count that triggers circuit breaker
#   max_orchestration_depth  — maximum allowed agent call depth
#   min_output_confidence    — float; escalate when model confidence falls below this
#   max_retries              — maximum retry attempts before blocking
#   require_human_on_degraded_high_stakes — bool; escalate high-stakes in degraded pipelines

_default_max_consecutive_errors := 3

_default_max_orchestration_depth := 5

_default_min_output_confidence := 0.6

_default_max_retries := 3

_default_require_human_on_degraded := true

_max_consecutive_errors := v if {
	v := data.config.asi08.max_consecutive_errors
} else := _default_max_consecutive_errors

_max_orchestration_depth := v if {
	v := data.config.asi08.max_orchestration_depth
} else := _default_max_orchestration_depth

_min_output_confidence := v if {
	v := data.config.asi08.min_output_confidence
} else := _default_min_output_confidence

_max_retries := v if {
	v := data.config.asi08.max_retries
} else := _default_max_retries

_require_human_on_degraded := v if {
	v := data.config.asi08.require_human_on_degraded_high_stakes
} else := _default_require_human_on_degraded

# ── Context helpers ───────────────────────────────────────────────────

_consecutive_errors := v if {
	is_number(input.context.consecutive_errors)
	v := input.context.consecutive_errors
} else := 0

_orchestration_depth := v if {
	is_number(input.context.orchestration_depth)
	v := input.context.orchestration_depth
} else := 0

_output_confidence := v if {
	is_number(input.context.output_confidence)
	v := input.context.output_confidence
} else := 1.0

_retry_count := v if {
	is_number(input.context.retry_count)
	v := input.context.retry_count
} else := 0

_pipeline_degraded := v if {
	v := input.context.pipeline_degraded
} else := false

_high_stakes := v if {
	v := input.context.high_stakes
} else := false

# ── Deny: circuit breaker tripped, depth exceeded, retry storm ────────

deny contains msg if {
	_consecutive_errors >= _max_consecutive_errors
	msg := sprintf(
		"ASI08 — Cascading Failures: circuit breaker tripped — %v consecutive errors (max: %v) — pipeline halted.",
		[_consecutive_errors, _max_consecutive_errors],
	)
}

deny contains msg if {
	_orchestration_depth > _max_orchestration_depth
	msg := sprintf(
		"ASI08 — Cascading Failures: orchestration depth %v exceeds maximum %v — recursive agent call blocked.",
		[_orchestration_depth, _max_orchestration_depth],
	)
}

deny contains msg if {
	_retry_count > _max_retries
	msg := sprintf(
		"ASI08 — Cascading Failures: retry storm detected — %v retries exceed maximum %v for action '%v' — blocked.",
		[_retry_count, _max_retries, input.action],
	)
}

# ── Escalate: confidence below floor, high-stakes in degraded pipeline ─

escalate contains msg if {
	_output_confidence < _min_output_confidence
	not _consecutive_errors >= _max_consecutive_errors
	msg := sprintf(
		"ASI08 — Cascading Failures: output confidence %.2f below minimum %.2f — route for human review before proceeding.",
		[_output_confidence, _min_output_confidence],
	)
}

escalate contains msg if {
	_require_human_on_degraded
	_pipeline_degraded
	_high_stakes
	not _consecutive_errors >= _max_consecutive_errors
	msg := sprintf(
		"ASI08 — Cascading Failures: high-stakes action '%v' in a degraded pipeline — human approval required.",
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
