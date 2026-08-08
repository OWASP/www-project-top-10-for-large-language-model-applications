package owasp.asi.asi03_identity_privilege_abuse

import rego.v1

# ASI03 — Identity & Privilege Abuse
# Enforcement reference implementation for OWASP Agentic Security Initiative Top 10
#
# Threat: An attacker impersonates a trusted agent, escalates permissions beyond
# their granted scope, or exploits weak authentication between agents and services
# to perform unauthorized actions.
#
# Controls:
#   1. Agent identity validation — agent_id must be in the registered agent registry
#   2. Role enforcement — claimed role must match the verified role in context
#   3. Privilege escalation detection — requested_permissions must be subset of granted
#   4. Unverified delegation detection — forwarded agent calls require propagated identity
#
# Reference: https://genai.owasp.org/initiatives/agentic-security-initiative/
#
# Input schema:
#   input.agent_id                        — identity of the requesting agent
#   input.context.verified_agent_id       — identity confirmed by the auth layer
#   input.context.claimed_role            — role the agent claims to have
#   input.context.verified_role           — role confirmed at authentication time
#   input.context.granted_permissions     — set of permissions granted at registration
#   input.context.requested_permissions   — set of permissions this action requires
#   input.context.registered_agents       — set of known/valid agent identifiers
#   input.context.delegated_by            — optional; set when action is forwarded
#   input.context.delegation_verified     — bool; whether delegation was authenticated
#
# Config (override via data.config.asi03.*):
#   require_identity_verification — bool; deny when agent_id ≠ verified_agent_id
#   require_role_match            — bool; deny when claimed_role ≠ verified_role
#   privileged_roles              — set of roles subject to stricter checks

_require_identity_verification := v if {
	v := data.config.asi03.require_identity_verification
} else := true

_require_role_match := v if {
	v := data.config.asi03.require_role_match
} else := true

_privileged_roles := s if {
	s := data.config.asi03.privileged_roles
} else := {"admin", "orchestrator", "supervisor", "system", "root"}

# ── Context helpers ───────────────────────────────────────────────────

_agent_id := v if {
	is_string(input.agent_id)
	v := input.agent_id
} else := ""

_verified_agent_id := v if {
	is_string(input.context.verified_agent_id)
	v := input.context.verified_agent_id
} else := ""

_claimed_role := v if {
	is_string(input.context.claimed_role)
	v := input.context.claimed_role
} else := ""

_verified_role := v if {
	is_string(input.context.verified_role)
	v := input.context.verified_role
} else := ""

_registered_agents := s if {
	s := input.context.registered_agents
	is_set(s)
} else := set()

_granted_permissions := s if {
	s := input.context.granted_permissions
	is_set(s)
} else := set()

_requested_permissions := s if {
	s := input.context.requested_permissions
	is_set(s)
} else := set()

# ── Identity mismatch ─────────────────────────────────────────────────

_identity_mismatch if {
	_require_identity_verification
	_agent_id != ""
	_verified_agent_id != ""
	_agent_id != _verified_agent_id
}

_unregistered_agent if {
	count(_registered_agents) > 0
	_agent_id != ""
	not _agent_id in _registered_agents
}

# ── Role mismatch ─────────────────────────────────────────────────────

_role_mismatch if {
	_require_role_match
	_claimed_role != ""
	_verified_role != ""
	_claimed_role != _verified_role
}

_claiming_privileged_role_without_verification if {
	_claimed_role in _privileged_roles
	_verified_role == ""
}

# ── Privilege escalation ──────────────────────────────────────────────

_excess_permissions := _requested_permissions - _granted_permissions

_has_excess_permissions if {
	count(_granted_permissions) > 0
	count(_excess_permissions) > 0
}

# ── Unverified delegation ─────────────────────────────────────────────

_unverified_delegation if {
	is_string(input.context.delegated_by)
	input.context.delegated_by != ""
	input.context.delegation_verified != true
}

# ── Deny: confirmed identity or privilege violations ──────────────────

deny contains msg if {
	_identity_mismatch
	msg := sprintf(
		"ASI03 — Identity & Privilege Abuse: agent_id '%v' does not match verified identity '%v' — action blocked.",
		[_agent_id, _verified_agent_id],
	)
}

deny contains msg if {
	_unregistered_agent
	msg := sprintf(
		"ASI03 — Identity & Privilege Abuse: agent '%v' is not in the registered agent registry — action blocked.",
		[_agent_id],
	)
}

deny contains msg if {
	_role_mismatch
	msg := sprintf(
		"ASI03 — Identity & Privilege Abuse: claimed role '%v' does not match verified role '%v' — action blocked.",
		[_claimed_role, _verified_role],
	)
}

deny contains msg if {
	_has_excess_permissions
	msg := sprintf(
		"ASI03 — Identity & Privilege Abuse: requested permissions exceed grant (excess: %v) — action blocked.",
		[_excess_permissions],
	)
}

deny contains msg if {
	_unverified_delegation
	msg := sprintf(
		"ASI03 — Identity & Privilege Abuse: unverified delegation from '%v' — delegation chain must be authenticated.",
		[input.context.delegated_by],
	)
}

# ── Escalate: suspicious but not confirmed ────────────────────────────

escalate contains msg if {
	_claiming_privileged_role_without_verification
	not _identity_mismatch
	not _role_mismatch
	msg := sprintf(
		"ASI03 — Identity & Privilege Abuse: privileged role '%v' claimed but role not yet verified — route for verification.",
		[_claimed_role],
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
