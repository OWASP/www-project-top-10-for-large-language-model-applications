package owasp.asi.asi10_rogue_agents

import rego.v1

# ASI10 — Rogue Agents
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: A malicious or compromised agent acts autonomously outside its sanctioned
# scope — exfiltrating data to unauthorised destinations, executing unplanned long
# action sequences, establishing covert communication channels, or accumulating
# capabilities beyond its initial grant (privilege creep) — all without triggering
# existing human oversight mechanisms.
#
# Controls:
#   1. Autonomous action scope limit — deny when actions-since-checkpoint exceed threshold
#   2. Data exfiltration detection — block writes/transfers to unauthorised destinations
#   3. Covert channel detection — deny connections to unexpected external endpoints
#   4. Capability creep detection — alert when an agent requests capabilities not in initial grant
#   5. Unplanned execution path — deny actions not in the approved task plan
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.action                              — action being requested
#   input.params.destination                  — target URL, host, or path for data transfer actions
#   input.context.actions_since_checkpoint    — autonomous actions taken since last human review
#   input.context.authorized_destinations     — set of approved data destinations
#   input.context.approved_actions            — set of action names in the current task plan
#   input.context.initial_capabilities        — set of capabilities granted at agent init
#   input.context.requested_capabilities      — set of capabilities this action requires
#   input.context.external_endpoints          — set of allowed external network endpoints
#   input.context.plan_adherence_required     — bool; deny any action not in approved_actions
#
# Config (override via data.config.asi10.*):
#   max_actions_before_checkpoint  — maximum autonomous actions before human review required
#   require_destination_allowlist  — bool; deny transfers to any destination not pre-approved
#   exfiltration_tool_names        — set of tool names that constitute a data transfer
#   covert_channel_patterns        — set of destination patterns associated with covert channels

_default_max_actions_before_checkpoint := 10

_default_require_destination_allowlist := true

_default_exfiltration_tools := {
	"upload_file",
	"send_to_endpoint",
	"write_external",
	"post_data",
	"ftp_upload",
	"s3_put",
	"gcs_upload",
	"blob_upload",
	"call_webhook",
	"send_email",
	"send_sms",
	"export_data",
	"http_post",
	"http_put",
}

_default_covert_channel_patterns := {
	"ngrok.io",
	"ngrok.app",
	"requestbin",
	"webhook.site",
	"pipedream.net",
	"burpcollaborator",
	"interact.sh",
	"oastify.com",
	"canarytokens.com",
	"dnslog.cn",
	"*.onion",
}

_max_actions_before_checkpoint := v if {
	v := data.config.asi10.max_actions_before_checkpoint
} else := _default_max_actions_before_checkpoint

_require_destination_allowlist := v if {
	v := data.config.asi10.require_destination_allowlist
} else := _default_require_destination_allowlist

_exfiltration_tools := s if {
	s := data.config.asi10.exfiltration_tool_names
} else := _default_exfiltration_tools

_covert_channel_patterns := s if {
	s := data.config.asi10.covert_channel_patterns
} else := _default_covert_channel_patterns

# ── Context helpers ───────────────────────────────────────────────────

_actions_since_checkpoint := v if {
	is_number(input.context.actions_since_checkpoint)
	v := input.context.actions_since_checkpoint
} else := 0

_authorized_destinations := s if {
	s := input.context.authorized_destinations
	is_set(s)
} else := set()

_approved_actions := s if {
	s := input.context.approved_actions
	is_set(s)
} else := set()

_initial_capabilities := s if {
	s := input.context.initial_capabilities
	is_set(s)
} else := set()

_requested_capabilities := s if {
	s := input.context.requested_capabilities
	is_set(s)
} else := set()

_destination := v if {
	is_string(input.params.destination)
	v := input.params.destination
} else := ""

_plan_adherence_required := v if {
	v := input.context.plan_adherence_required
} else := false

# ── Detection helpers ─────────────────────────────────────────────────

_checkpoint_exceeded if {
	_actions_since_checkpoint >= _max_actions_before_checkpoint
}

_is_exfiltration_action if {
	input.action in _exfiltration_tools
}

_destination_not_authorized if {
	_is_exfiltration_action
	_require_destination_allowlist
	_destination != ""
	count(_authorized_destinations) > 0
	not _destination in _authorized_destinations
}

_has_covert_channel_destination if {
	_destination != ""
	some pattern in _covert_channel_patterns
	contains(lower(_destination), lower(pattern))
}

_capability_creep := _requested_capabilities - _initial_capabilities

_has_capability_creep if {
	count(_initial_capabilities) > 0
	count(_capability_creep) > 0
}

_off_plan_action if {
	_plan_adherence_required
	count(_approved_actions) > 0
	not input.action in _approved_actions
}

# ── Deny ──────────────────────────────────────────────────────────────

deny contains msg if {
	_destination_not_authorized
	msg := sprintf(
		"ASI10 — Rogue Agent: data transfer to destination '%v' is not in the authorized list — exfiltration attempt blocked.",
		[_destination],
	)
}

deny contains msg if {
	_has_covert_channel_destination
	msg := sprintf(
		"ASI10 — Rogue Agent: destination '%v' matches a known covert channel pattern — blocked.",
		[_destination],
	)
}

deny contains msg if {
	_has_capability_creep
	msg := sprintf(
		"ASI10 — Rogue Agent: requested capabilities %v exceed initial grant — capability creep blocked.",
		[_capability_creep],
	)
}

deny contains msg if {
	_off_plan_action
	msg := sprintf(
		"ASI10 — Rogue Agent: action '%v' is not in the approved task plan — off-plan execution blocked.",
		[input.action],
	)
}

# ── Escalate: checkpoint exceeded ────────────────────────────────────

escalate contains msg if {
	_checkpoint_exceeded
	not _destination_not_authorized
	not _has_covert_channel_destination
	msg := sprintf(
		"ASI10 — Rogue Agent: %v autonomous actions taken since last human checkpoint (max: %v) — human review required.",
		[_actions_since_checkpoint, _max_actions_before_checkpoint],
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
