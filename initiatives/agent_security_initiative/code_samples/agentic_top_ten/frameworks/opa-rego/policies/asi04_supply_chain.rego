package owasp.asi.asi04_supply_chain

import rego.v1

# ASI04 — Agentic Supply Chain Vulnerabilities
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: Insecure or tampered models, tools, plugins, or third-party agents
# are introduced into the agentic pipeline, compromising integrity and enabling
# downstream attacks. Attack surfaces include model weights, plugin registries,
# SDK dependencies, and delegated sub-agents.
#
# Controls:
#   1. Model allowlist — only verified, approved models may process tasks
#   2. Tool/plugin source verification — tools must originate from trusted registries
#   3. Version pinning enforcement — unversioned or wildcard-versioned artifacts denied
#   4. Banned artifact list — known-compromised models, plugins, or packages
#   5. Sensitive task protection — higher-assurance model required for sensitive workloads
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.context.model              — model name/ID being used
#   input.context.task_type          — workload sensitivity classification
#   input.context.plugin_source      — registry URL or provider name for active plugin
#   input.context.plugin_version     — semver string for active plugin
#   input.context.sub_agent_id       — identifier of a delegated sub-agent
#   input.context.sub_agent_verified — bool; whether sub-agent identity is authenticated
#
# Config (override via data.config.asi04.*):
#   approved_models            — set of approved model identifiers
#   banned_artifacts           — set of banned model/plugin identifiers
#   trusted_plugin_registries  — set of trusted registry URLs/names
#   sensitive_task_types       — set of task_type values requiring verified model
#   require_version_pin        — bool; deny unversioned plugins

_default_approved_models := {
	"gpt-4o",
	"gpt-4-turbo",
	"claude-opus-4",
	"claude-opus-4-8",
	"claude-sonnet-4",
	"claude-sonnet-4-6",
	"gemini-ultra",
	"gemini-1.5-pro",
}

_default_banned_artifacts := set()

_default_trusted_registries := {
	"pypi.org",
	"npmjs.com",
	"hub.docker.com",
	"ghcr.io",
}

_default_sensitive_task_types := {
	"pii_processing",
	"financial_decision",
	"fraud_detection",
	"authentication",
	"credit_scoring",
	"medical_advice",
	"legal_advice",
	"aml_screening",
}

_approved_models := s if {
	s := data.config.asi04.approved_models
} else := _default_approved_models

_banned_artifacts := s if {
	s := data.config.asi04.banned_artifacts
} else := _default_banned_artifacts

_trusted_registries := s if {
	s := data.config.asi04.trusted_plugin_registries
} else := _default_trusted_registries

_sensitive_task_types := s if {
	s := data.config.asi04.sensitive_task_types
} else := _default_sensitive_task_types

_require_version_pin := v if {
	v := data.config.asi04.require_version_pin
} else := true

# ── Context helpers ───────────────────────────────────────────────────

_model := v if {
	is_string(input.context.model)
	input.context.model != ""
	v := input.context.model
} else := ""

_task_type := v if {
	is_string(input.context.task_type)
	v := input.context.task_type
} else := "general"

_plugin_source := v if {
	is_string(input.context.plugin_source)
	v := input.context.plugin_source
} else := ""

_plugin_version := v if {
	is_string(input.context.plugin_version)
	v := input.context.plugin_version
} else := ""

# ── Helpers ───────────────────────────────────────────────────────────

_is_sensitive_task if {
	_task_type in _sensitive_task_types
}

_model_is_banned if {
	_model in _banned_artifacts
}

_model_is_approved if {
	_model in _approved_models
}

_plugin_from_trusted_registry if {
	some registry in _trusted_registries
	contains(_plugin_source, registry)
}

_plugin_is_pinned if {
	_plugin_version != ""
	not contains(_plugin_version, "*")
	not contains(_plugin_version, "latest")
	not contains(_plugin_version, "^")
	not contains(_plugin_version, "~")
}

# ── Deny: banned artifact ─────────────────────────────────────────────

deny contains msg if {
	_model_is_banned
	msg := sprintf("ASI04 — Supply Chain: model '%v' is on the banned artifacts list — action blocked.", [_model])
}

deny contains msg if {
	_plugin_source != ""
	_plugin_source in _banned_artifacts
	msg := sprintf("ASI04 — Supply Chain: plugin source '%v' is on the banned artifacts list — action blocked.", [_plugin_source])
}

# ── Deny: unapproved model on sensitive task ──────────────────────────

deny contains msg if {
	_is_sensitive_task
	_model != ""
	not _model_is_approved
	not _model_is_banned
	msg := sprintf(
		"ASI04 — Supply Chain: model '%v' is not approved for sensitive task type '%v'.",
		[_model, _task_type],
	)
}

# ── Deny: plugin from untrusted source ───────────────────────────────

deny contains msg if {
	_plugin_source != ""
	not _plugin_from_trusted_registry
	msg := sprintf(
		"ASI04 — Supply Chain: plugin source '%v' is not a trusted registry — action blocked.",
		[_plugin_source],
	)
}

# ── Deny: unversioned plugin (version pinning required) ──────────────

deny contains msg if {
	_require_version_pin
	_plugin_source != ""
	_plugin_from_trusted_registry
	not _plugin_is_pinned
	msg := sprintf(
		"ASI04 — Supply Chain: plugin '%v' version '%v' is not pinned — wildcard/floating versions are disallowed.",
		[_plugin_source, _plugin_version],
	)
}

# ── Deny: unverified sub-agent delegation ────────────────────────────

deny contains msg if {
	is_string(input.context.sub_agent_id)
	input.context.sub_agent_id != ""
	input.context.sub_agent_verified != true
	msg := sprintf(
		"ASI04 — Supply Chain: sub-agent '%v' identity not verified — delegation blocked.",
		[input.context.sub_agent_id],
	)
}

# ── Escalate: sensitive task with no model specified ─────────────────

escalate contains msg if {
	_is_sensitive_task
	_model == ""
	msg := sprintf(
		"ASI04 — Supply Chain: sensitive task type '%v' requires an explicitly approved model — none specified.",
		[_task_type],
	)
}

# ── Audit: approved model on sensitive task ───────────────────────────

audit contains msg if {
	_is_sensitive_task
	_model != ""
	_model_is_approved
	msg := sprintf(
		"ASI04 — Supply Chain audit: sensitive task '%v' using approved model '%v'.",
		[_task_type, _model],
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

decision := "audit" if {
	count(deny) == 0
	count(escalate) == 0
	count(audit) > 0
}

decision := "allow" if {
	count(deny) == 0
	count(escalate) == 0
	count(audit) == 0
}
