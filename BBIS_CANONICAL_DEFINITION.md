# BBIS: Boundary-to-Boundary Invariant Survival

Author: Steven K. Hensley (Stevil / QueBallSharken)

## Author's Note

I am introducing **Boundary-to-Boundary Invariant Survival (BBIS)** here as a specific term and formulation for a continuity requirement in governed mutation paths.

BBIS means:

> the same governing invariant must remain live, binding, and refusal-capable across every mutation-capable boundary until the true irreversible mutation authority.

This artifact is intended to preserve that meaning precisely, distinguish it from adjacent concepts, and make the formulation reviewable in the public record.

**BBIS is:**
- primarily a continuity requirement
- secondarily an evaluation criterion

**BBIS is not:**
- a generic synonym for authorization correctness
- a generic synonym for attestation validity
- a generic synonym for receipt correctness
- a generic synonym for execution integrity in the broad sense
- a complete concrete architecture by itself

**Author:** QueBallSharken

---

## 1. Classification

**BBIS** is primarily a **continuity requirement** and secondarily an **evaluation criterion**.

It is **not** a concrete architecture.

More precisely:

- As a **continuity requirement**, BBIS requires that the same governing invariant remain live, binding, and refusal-capable across the full mutation path.
- As an **evaluation criterion**, BBIS provides the standard for judging whether that invariant actually survived the full mutation path without semantic weakening, substitution, or loss of refusal authority.
- BBIS is **not** a concrete architecture because it does not prescribe a specific enforcement mechanism, token format, verification system, or implementation stack.

---

## 2. Core Definition

**Boundary-to-Boundary Invariant Survival (BBIS)** means that the **same governing invariant** remains:

- **live**
- **binding**
- **refusal-capable**

across **every mutation-capable boundary** until the **true irreversible mutation authority**.

A system does not satisfy BBIS merely because it can prove that:
- a decision existed
- a policy was evaluated
- a receipt verified
- a token was presented
- an approval artifact was produced

Those may be relevant, but they are not sufficient.

The BBIS question is narrower and stricter:

> did the same governing invariant actually survive the full mutation path to the boundary that made the mutation real?

---

## 3. Core Terms

### Governing invariant

The authoritative condition that constrains permissible operations and state transitions.

### Mutation-capable boundary

Any boundary where system state, execution scope, authority, operational meaning, or finality can be changed, widened, translated, delegated, retried, queued, persisted, or finalized in a way relevant to the governing invariant.

### Live

The invariant is actively involved in real decision or control flow, not merely documented, checked earlier, or assumed to persist.

### Binding

The invariant actually constrains what can occur. It is not advisory, decorative, or merely logged.

### Refusal-capable

At the relevant boundary, the system can still technically prevent the violating mutation from occurring.

### True irreversible mutation authority

The final boundary or composite commitment point at which refusal remains technically possible within the defined threat model, and after which later mechanisms may detect, compensate, or recover but can no longer prevent the mutation from having occurred.

---

## 4. What BBIS Is Not

BBIS is not:

- a single-threshold security model
- a synonym for upstream authorization
- a synonym for admissibility at one boundary
- a synonym for receipt correctness
- a synonym for attestation validity
- a synonym for good audit logging
- a synonym for post-hoc detection
- a complete implementation architecture

A system can be strong at proving earlier authorization and still be weak at BBIS.

---

## 5. Canonical BBIS Rules

### Rule 1 — Local correctness is not enough

A correct check at one boundary does not prove invariant survival across the full mutation path.

### Rule 2 — Dumb endpoints are not automatically fatal, but are fatal if they remain the true mutation authority

A **dumb endpoint** is a mutation-capable component that cannot itself verify, interpret, or enforce the governing invariant.

A dumb endpoint is compatible with BBIS only if it is strictly contained as a mechanical executor inside a non-bypassable control path where a refusal-capable boundary retains the real effective mutation authority.

### Rule 3 — Upstream verification is not authority relocation

**Authority relocation** is real only when the endpoint’s ability to mutate is mechanically and exclusively dependent on authorization it cannot generate, bypass, or retain outside the constrained control path.

### Rule 4 — The capability must be part of the mutation path itself

The key test is not whether the capability is checked before execution, but whether the mutation is mechanically impossible without the capability being exercised as part of the execution path itself.

### Rule 5 — Serious BBIS requires object, version/state, and parameter binding

A serious BBIS claim requires the governing artifact to be bound to:

- the exact object
- the relevant version or state
- the actual mutation parameters

Anything less leaves a discontinuity between authorization-time evaluation and execution-time reality.

### Rule 6 — Approval evidence is not execution evidence

A serious BBIS claim requires post-execution evidence from the real mutation authority showing that the mutation actually occurred under the governing artifact, against the bound state, with the bound parameters.

### Rule 7 — The mutation path must be reasoned about as a whole

Multi-boundary systems must be evaluated for:

- translation drift
- retry after state change
- delegation widening
- hidden bypass paths
- split authority

Every local step looking correct is not equivalent to full mutation-path continuity.

---

## 6. Minimum Serious BBIS Conditions

A serious BBIS claim requires, at minimum:

1. **Explicit identification of mutation-capable boundaries**
2. **Correct identification of the true irreversible mutation authority**
3. **No hidden path to mutation outside the governed path**
4. **A governing artifact that remains live, binding, and refusal-capable**
5. **Object + version/state + parameter binding**
6. **Real authority relocation where dumb endpoints exist**
7. **No ambient-authority mutation path that bypasses the governing artifact**
8. **Post-execution evidence from the real mutation authority**

---

## 7. Canonical Failure Classes

BBIS failure classes include:

- object substitution
- stale approval against changed state
- parameter widening
- delegation widening
- translation drift
- retry after state change
- proxy/executor split
- dumb endpoint retaining real mutation authority
- hidden bypass path
- split authority with no final governed boundary
- evidence of approval without evidence of governed execution
- misidentified true irreversible mutation authority

---

## 8. Conformance Levels

BBIS should be treated both as a binary condition and as a graded assessment model.

### Positive / conforming
- **BBIS-Strong**
- **BBIS-Partial/Bounded**

### Negative / non-conforming
- **Detectable-only**
- **Fail**

### BBIS-Strong

The true irreversible mutation authority is correctly identified and mechanically constrained by the governing artifact; object/version/parameter binding is present; no dumb endpoint retains ambient mutation authority; post-execution evidence is strong enough to show the mutation actually occurred under the governing artifact.

### BBIS-Partial/Bounded

Strong conditions hold only within defined scopes, paths, trust domains, or operation classes. Some legacy or weaker paths remain, but are explicitly bounded.

### Detectable-only

Invariant-breaking mutations may be observable after the fact, but mechanical prevention does not exist at the true irreversible mutation authority. This is **not** positive BBIS conformance.

### Fail

No serious continuity claim can be sustained. Authority is ambient, misidentified, bypassable, or unsupported by binding and evidence.

---

## 9. Public Claim Discipline

Public BBIS claims should almost never say simply:

> “BBIS holds.”

Instead, claims should always state:

- **scope**
- **trust model**
- **identified true irreversible mutation authority**
- **conformance level**
- **known limitations**
- **evidence standard**

### Good examples

- **BBIS-Strong within scope X**
- **BBIS-Partial/Bounded for path Y**

### Bad examples

- unqualified “BBIS-compliant”
- “BBIS across all operations” without scope
- claims based only on logging, upstream validation, or approval receipts

**Detectable-only** should be described as a **non-conforming but observable** state, not as BBIS holding.

---

## 10. Implementation Implication

BBIS does not prescribe a single architecture, but it does imply a direction:

- the governing artifact must be part of the actual mutation path
- true mutation authority must not remain in an ambient-authority executor
- dumb endpoints must be contained or stripped of effective independent mutation power
- bindings must be exact enough to prevent substitution, staleness, and widening
- post-execution evidence must come from the real mutation authority

---

## 11. Short Form

**BBIS requires that the same governing invariant remain live, binding, and refusal-capable across every mutation-capable boundary until the true irreversible mutation authority. A system does not satisfy BBIS merely because it can prove earlier approval, token presentation, or receipt correctness. Strong BBIS requires governed mutation-path continuity, exact binding, real authority relocation where needed, and post-execution evidence from the actual mutation authority.**

---

## 12. Status

**Status:** Concept definition / continuity requirement artifact  
**Purpose:** Preserve the BBIS formulation, scope, and conformance meaning in the public record  
**Author:** Steven K. Hensley (Stevil / QueBallSharken)
