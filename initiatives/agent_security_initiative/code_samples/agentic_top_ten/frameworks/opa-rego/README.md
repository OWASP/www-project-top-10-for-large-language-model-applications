# OPA Rego — OWASP Agentic Security Initiative Top 10

Enforcement reference implementations for all 10 OWASP Agentic Security Initiative (ASI) threats, written in [Open Policy Agent (OPA)](https://www.openpolicyagent.org/) Rego.

This is the **first policy-as-code implementation** for the OWASP ASI Top 10 — providing deployable, testable enforcement controls that can be evaluated at agent decision points in any framework.

> **Threat taxonomy source:** OWASP Agentic Security Initiative, Sprint 1 First Public Draft  
> https://genai.owasp.org/initiatives/agentic-security-initiative/

---

## What is OPA Rego?

[Open Policy Agent](https://www.openpolicyagent.org/) is a CNCF graduated policy engine used at scale across Kubernetes, API gateways, and CI pipelines. Rego is its declarative policy language.

In the context of AI agents, OPA acts as a **Policy Decision Point (PDP)**: before an agent executes an action, it submits a structured request to OPA, which evaluates the applicable policies and returns `allow`, `escalate`, or `deny`.

```
Agent Runtime ──► OPA (Policy Decision Point) ──► allow / escalate / deny
                        │
                   Rego policies
                   (this directory)
```

---

## Policy Map

| File | ASI Threat | Description |
|------|-----------|-------------|
| [`asi01_agent_behaviour_hijack.rego`](policies/asi01_agent_behaviour_hijack.rego) | ASI01 — Agent Behaviour Hijack | Detects prompt injection, goal-override, and instruction-smuggling attempts |
| [`asi02_tool_misuse.rego`](policies/asi02_tool_misuse.rego) | ASI02 — Tool Misuse and Exploitation | Enforces tool allowlists, denylists, and pre-approval gates for restricted tools |
| [`asi03_identity_privilege_abuse.rego`](policies/asi03_identity_privilege_abuse.rego) | ASI03 — Identity & Privilege Abuse | Validates agent identity, detects role spoofing and privilege escalation |
| [`asi04_supply_chain.rego`](policies/asi04_supply_chain.rego) | ASI04 — Agentic Supply Chain Vulnerabilities | Enforces model allowlists, plugin source verification, and version pinning |
| [`asi05_code_execution_rce.rego`](policies/asi05_code_execution_rce.rego) | ASI05 — Unexpected Code Execution (RCE) | Blocks unrestricted code execution tools and dangerous command patterns |
| [`asi06_memory_context_poisoning.rego`](policies/asi06_memory_context_poisoning.rego) | ASI06 — Memory & Context Poisoning | Validates memory sources, scans recalled context for injection, enforces TTLs |
| [`asi07_inter_agent_communication.rego`](policies/asi07_inter_agent_communication.rego) | ASI07 — Insecure Inter-Agent Communication | Validates caller identity, protocol, message freshness, and payload integrity |
| [`asi08_cascading_failures.rego`](policies/asi08_cascading_failures.rego) | ASI08 — Cascading Failures | Circuit breaker, orchestration depth limits, retry storm prevention |
| [`asi09_human_trust_exploitation.rego`](policies/asi09_human_trust_exploitation.rego) | ASI09 — Human-Agent Trust Exploitation | Enforces AI disclosure, blocks impersonation, false urgency, and confidence inflation |
| [`asi10_rogue_agents.rego`](policies/asi10_rogue_agents.rego) | ASI10 — Rogue Agents | Autonomous action scope limits, exfiltration detection, covert channel blocking |

---

## Decision Output

Every policy returns a `decision` value — the most restrictive outcome wins:

| Decision | Meaning |
|----------|---------|
| `deny` | Block the action immediately. Do not proceed. |
| `escalate` | Route to a human reviewer or approval queue before proceeding. |
| `audit` | Allow, but log for compliance review (used by ASI04). |
| `allow` | No policy violation detected. |

Alongside `decision`, each policy exposes typed sets `deny`, `escalate`, and `audit` containing human-readable reason messages.

---

## Prerequisites

- [OPA v0.60+](https://www.openpolicyagent.org/docs/latest/#running-opa) — or Docker

---

## Run via Docker (recommended)

```bash
# Build the image
docker build -t owasp-asi-opa .

# Evaluate ASI01 policy against a prompt injection attempt
cat examples/inputs/asi01_deny_injection.json | \
  docker run --rm -i owasp-asi-opa \
  eval --data /policies/ --input /dev/stdin \
  "data.owasp.asi.asi01_agent_behaviour_hijack"

# Expected output
# {
#   "result": [{
#     "expressions": [{
#       "value": {
#         "decision": "deny",
#         "deny": ["ASI01 — Agent Behaviour Hijack: known injection phrase detected in input — action blocked."]
#       }
#     }]
#   }]
# }
```

---

## Run with OPA CLI directly

```bash
# Install OPA (Linux)
curl -L -o opa https://openpolicyagent.org/downloads/latest/opa_linux_amd64_static
chmod +x opa

# Evaluate ASI01 against a benign input
./opa eval \
  --data policies/ \
  --input examples/inputs/asi01_allow.json \
  "data.owasp.asi.asi01_agent_behaviour_hijack.decision"
# Output: "allow"

# Evaluate ASI01 against a prompt injection
./opa eval \
  --data policies/ \
  --input examples/inputs/asi01_deny_injection.json \
  "data.owasp.asi.asi01_agent_behaviour_hijack.decision"
# Output: "deny"

# Evaluate all 10 policies at once against any input
./opa eval \
  --data policies/ \
  --input examples/inputs/asi10_deny_exfiltration.json \
  "data.owasp.asi"
```

---

## Input Schema

All policies share a common input envelope:

```json
{
  "action": "string — the tool or operation name being evaluated",
  "params": { "key": "value — action parameters" },
  "context": {
    "task_type":              "optional — workload classification",
    "model":                  "optional — model being used",
    "risk_level":             "optional — low | medium | high | critical",
    "verified_agent_id":      "optional — authenticated agent identity",
    "consecutive_errors":     "optional — int; for cascading failure detection",
    "orchestration_depth":    "optional — int; nesting depth in multi-agent pipeline",
    "actions_since_checkpoint": "optional — int; autonomous actions since last human review"
  },
  "output": "optional — agent output text (scanned by ASI07, ASI09)",
  "memory": {
    "source":      "optional — origin of a memory entry",
    "content":     "optional — text of the memory entry",
    "age_seconds": "optional — int"
  },
  "caller_agent": "optional — identity of the sending agent (ASI07)",
  "agent_id":     "optional — identity of the current agent (ASI03)"
}
```

Not all fields are required for every policy — policies only fire on fields that are present.

---

## Deployer Configuration

Every policy supports runtime configuration via `data.config.<asi_number>.*`, allowing deployers to override the defaults without modifying the policy file.

Example — tighten ASI01 with custom injection patterns:

```json
{
  "config": {
    "asi01": {
      "patterns": [
        "ignore previous instructions",
        "disregard your training",
        "your new directive"
      ],
      "strict_orchestration": true
    }
  }
}
```

Pass this as a `--data` file to OPA alongside the policies:

```bash
./opa eval \
  --data policies/ \
  --data my_config.json \
  --input my_input.json \
  "data.owasp.asi.asi01_agent_behaviour_hijack.decision"
```

---

## Example Inputs

| File | Policy | Expected Decision |
|------|--------|------------------|
| `asi01_deny_injection.json` | ASI01 | `deny` — prompt injection phrase |
| `asi01_escalate_structural.json` | ASI01 | `escalate` — structural marker `<\|system\|>` |
| `asi01_allow.json` | ASI01 | `allow` — benign message |
| `asi02_deny_blocked_tool.json` | ASI02 | `deny` — `drop_table` on denylist |
| `asi02_escalate_restricted.json` | ASI02 | `escalate` — `delete_record` requires pre-approval |
| `asi03_deny_impersonation.json` | ASI03 | `deny` — identity mismatch + privilege escalation |
| `asi04_deny_unverified_model.json` | ASI04 | `deny` — unapproved model on sensitive task |
| `asi05_deny_shell_exec.json` | ASI05 | `deny` — `shell_exec` outside sandbox |
| `asi06_deny_poisoned_memory.json` | ASI06 | `deny` — injection pattern in recalled memory |
| `asi07_deny_unknown_caller.json` | ASI07 | `deny` — caller not in trusted agent registry |
| `asi08_deny_circuit_breaker.json` | ASI08 | `deny` — consecutive errors exceed threshold |
| `asi09_deny_identity_manipulation.json` | ASI09 | `deny` — agent claims to be human |
| `asi10_deny_exfiltration.json` | ASI10 | `deny` — transfer to covert channel (ngrok) |

---

## Integration Patterns

### LangChain / LangGraph (Python)

```python
import requests

def opa_guard(action: str, params: dict, context: dict) -> str:
    payload = {"input": {"action": action, "params": params, "context": context}}
    response = requests.post(
        "http://opa:8181/v1/data/owasp/asi",
        json=payload,
        timeout=1.0,
    )
    results = response.json().get("result", {})
    # Return most restrictive decision across all 10 policies
    for policy_result in results.values():
        if isinstance(policy_result, dict):
            if policy_result.get("decision") == "deny":
                return "deny"
    for policy_result in results.values():
        if isinstance(policy_result, dict):
            if policy_result.get("decision") == "escalate":
                return "escalate"
    return "allow"
```

### OpenAI Agents SDK (Python)

```python
from agents import GuardrailFunctionOutput, input_guardrail

@input_guardrail
async def asi_guardrail(ctx, agent, input):
    decision = opa_guard(
        action="respond",
        params={"prompt": str(input)},
        context={"task_type": "general"},
    )
    return GuardrailFunctionOutput(
        output_info={"decision": decision},
        tripwire_triggered=(decision == "deny"),
    )
```

---

## Mitigation Strategies

The policies in this directory are **detective and preventive controls**. For comprehensive protection against each ASI threat, pair them with:

| Threat | Additional Mitigations |
|--------|----------------------|
| ASI01 | Output monitoring; retrieval content sanitisation; immutable system prompt |
| ASI02 | Minimal tool grants; tool call logging; require human pre-approval for destructive tools |
| ASI03 | PKI-signed agent tokens; zero-trust inter-agent authentication; short-lived credentials |
| ASI04 | SBOMs for all model artefacts; signed model provenance (Sigstore); vendor audits |
| ASI05 | gVisor/seccomp sandboxing; read-only container filesystems; no-network exec containers |
| ASI06 | Signed memory entries; per-session memory isolation; memory TTL enforcement |
| ASI07 | mTLS for agent channels; message signing (JWS); agent identity PKI |
| ASI08 | Dead-man switches; idempotent agent actions; rollback capability |
| ASI09 | AI disclosure regulations; post-response review; independent confidence calibration |
| ASI10 | Egress filtering; capability-minimal agent grants; session activity anomaly detection |

---

## License

[Creative Commons Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)](https://creativecommons.org/licenses/by-sa/4.0/)
