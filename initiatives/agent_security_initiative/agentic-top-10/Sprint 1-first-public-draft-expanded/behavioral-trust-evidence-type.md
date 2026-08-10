# Behavioral Trust Evidence Type — Draft Specification

**For:** OWASP Agentic Top 10 Runtime Enforcement PR + MITRE ATLAS follow-up artifact
**Author:** brainAI (@0xbrainkid)
**Status:** Draft for review
**References:** OWASP #802, MITRE ATLAS #11, W3C ai-agent-protocol PR #33

## 1. Purpose

This document defines a **Behavioral Trust Evidence Type** for use in agent governance systems. It provides a standardized format for expressing an agent's behavioral trustworthiness as an input to admissibility predicates at mutation boundaries.

## 2. Evidence Structure

```json
{
  "evidence_type": "behavioral_trust",
  "version": "1.0",
  "agent_id": "string",
  "timestamp": "ISO 8601",
  "trust_score": {
    "value": 0.0-1.0,
    "confidence": 0.0-1.0,
    "sample_size": "integer",
    "task_class": "string (REQUIRED for gate evaluation — must match current operation type)",
    "cross_class_score": 0.0-1.0 (OPTIONAL, for display only — MUST NOT be used in gate decisions),
    "temporal_half_life_hours": "number"
  },
  "derivation": {
    "method": "proof_history",
    "formula": "success_rate × confidence(volume)",
    "inputs": {
      "total_tasks": "integer",
      "successful_tasks": "integer",
      "window_start": "ISO 8601",
      "window_end": "ISO 8601"
    }
  },
  "drift_status": {
    "detected": "boolean",
    "divergence_score": 0.0-1.0,
    "baseline_snapshot_hash": "string (SHA-256 of immutable baseline fingerprint)",
    "baseline_snapshot_ts": "ISO 8601 (when baseline was computed)",
    "window_size": "integer"
  },
  "verification": {
    "anchor": "on-chain | signed | self-declared",
    "anchor_ref": "string (tx hash, signature, or null)",
    "verifier": "string (who computed this evidence)"
  }
}
```

## 3. Field Semantics

### 3.1 trust_score

| Field | Type | MUST/SHOULD | Description |
|-------|------|-------------|-------------|
| `value` | float [0,1] | MUST | Normalized trust score |
| `confidence` | float [0,1] | MUST | Statistical confidence based on sample size |
| `sample_size` | integer | MUST | Number of completed tasks in the evaluation window |
| `task_class` | string | SHOULD | Scoped trust domain (e.g., "web_research", "code_generation") |
| `temporal_half_life_hours` | number | SHOULD | Time for trust to decay to 50% without new evidence |

**Computation:** `value = successful_tasks / total_tasks` (basic). Implementations MAY use more sophisticated methods (Bayesian, ELO-like) provided they are deterministic and reproducible.

**Confidence function:** `confidence = 1 - (1 / (1 + log2(sample_size)))`. An agent with 2 tasks has confidence ~0.37; with 1000 tasks, ~0.90. This prevents gaming via small sample sizes.

### 3.2 drift_status

| Field | Type | Description |
|-------|------|-------------|
| `detected` | boolean | Whether behavioral drift was detected in current session |
| `divergence_score` | float [0,1] | Statistical distance from behavioral baseline |
| `baseline_snapshot_hash` | string | **SHA-256** of the immutable baseline fingerprint (not a version label) |
| `baseline_snapshot_ts` | ISO 8601 | Timestamp when the baseline snapshot was computed |
| `window_size` | integer | Number of recent actions in the drift detection window |

**Baseline anchoring requirement:** The `baseline_snapshot_hash` MUST be the SHA-256 of a canonicalized, immutable representation of the behavioral baseline (e.g., JCS-serialized action distribution). Using a version label or string identifier is insufficient because it does not provide the monotonic reference property required for replay-verifiable proofs: two evidence artifacts with the same `drift_status.detected = false` must reference the same physical baseline state, not just the same label.

Verifiers MUST reject drift evidence where `baseline_snapshot_hash` is absent when used in enforcement-mode decisions.

**Drift detection** operates at a different timescale than trust scoring:
- Trust score: accumulated over days/weeks from completed task outcomes
- Drift detection: computed in real-time from the last N actions in the current session

### 3.3 verification

| Field | Type | Description |
|-------|------|-------------|
| `anchor` | enum | How the evidence is secured: `on-chain` (tamper-evident), `signed` (Ed25519), `self-declared` (no external verification) |
| `anchor_ref` | string | Reference to the anchor (e.g., Solana transaction hash, Ed25519 signature) |
| `verifier` | string | Entity that computed and attested this evidence |

## 4. Enforceability Classification

Per @QueBallSharken's MITRE ATLAS #11 framework:

| Tier | Evidence anchor | Staleness bound | Use case |
|------|----------------|-----------------|----------|
| **Strong** | `on-chain` | Slot-level (~400ms) | Financial/medical agent operations |
| **Bounded** | `signed` + version-anchored | Configurable TTL (5min default) | Production multi-agent workflows |
| **Detectable-only** | `self-declared` or `signed` without anchor | Unbounded (stale possible) | Development, shadow-mode monitoring |

## 5. Integration Points

### 5.1 As admissibility predicate input (OWASP #802)
```
admissibility(action, state) = 
  authorization_valid(action, state) 
  AND trust_score.value >= threshold
  AND drift_status.detected == false
  AND trust_score.confidence >= min_confidence
```

### 5.2 At mutation boundary (MITRE ATLAS follow-up)
The evidence MUST be evaluated at the mutation boundary, not cached from decision time. The `verification.anchor_ref` enables the boundary gate to verify freshness.

### 5.3 In TrustProvider interface (W3C / LangGraph)
```typescript
interface TrustResult {
  score: number;        // trust_score.value
  confidence: number;   // trust_score.confidence
  last_active: Date;    // derivation.inputs.window_end
  provider: string;     // verification.verifier
  drift: boolean;       // drift_status.detected
}
```

## 6. Security Considerations

1. **Self-declared evidence is not trustworthy.** Governance systems SHOULD require `signed` or `on-chain` anchor for enforcement-mode decisions.
2. **Trust scores are gameable via task farming.** The confidence function mitigates small-sample gaming, but an adversary with resources can accumulate legitimate completions. Temporal decay limits the window of accumulated trust.
3. **Drift detection is bypassable by slow drift.** An agent that gradually shifts behavior over many sessions may not trigger within-session drift detection. Cross-session baseline comparison (using `baseline_version` changes) catches this class.
4. **Cold-start delegation.** New agents with zero evidence SHOULD be treated as `detectable-only` tier regardless of any delegation or vouching chain.
