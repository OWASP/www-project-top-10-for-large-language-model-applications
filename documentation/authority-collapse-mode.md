# Authority Collapse Mode Specification  
Author: Steven Kyle Hensley  
Framework: Trust Chain Protocol (TCP)

---

## 1. Position

Authority Collapse Mode (ACM) defines an alternative execution model to delegation-propagated authority in multi-agent systems.

In this model:

- Scope may move through delegation grammar.
- Authority does not propagate.
- Authority is recomputed at each execution boundary.
- Override scope is treated as a separately signed boundary input — not contextual policy state.

Authority is never inherited.  
Authority must be re-derived.

---

## 2. Core Axiom

Boundary recomputation dominates delegation semantics.

Delegation grammar describes how scope moves.  
Re-derivation defines what must be true for authority to exist.  
They are parallel, not nested.

If recomputation fails, authority collapses.

---

## 3. Canonical Snapshot Inputs

At each execution boundary, authority must be recomputable from canonical, frozen inputs.

Minimum boundary inputs:

- Identity binding inputs  
- Canonical policy state hash  
- Admissibility state  
- Tool constraints  
- Override scope (if present)

All canonical inputs must:

- Be explicitly present
- Be validated at boundary
- Be cryptographically bindable (where applicable)

If canonical policy state changes, override scope falls out of derivation unless re-signed.

---

## 4. Override Scope as Signed Boundary Input

Override scope:

- Is not inherited context.
- Is not implicit policy mutation.
- Is not ambient state.

Override scope is:

- A separately signed input.
- Bound to canonical policy state hash.
- Bound to identity binding inputs.
- Valid only within its declared execution boundary.
- Invalid outside its boundary without re-derivation.

Override scope must be presented and re-validated at each execution boundary.

---

## 5. Collapse Semantics

Authority exists only if all canonical inputs successfully re-derive.

If any canonical input fails validation:

- Authority collapses to zero.

Collapse is not containment mode.  
Collapse is non-derivation.

There is no fallback to delegated trust continuity.

---

## 6. Contamination Model

A compromised intermediate agent cannot forward authority by presenting curated state.

Authority must materialize strictly within canonical boundary inputs.

If contamination exists in upstream canonical inputs,
it is visible to boundary validation.

If contamination appears in canonical inputs,
collapse occurs at that boundary.

The attack surface therefore shifts from delegated continuity
to snapshot completeness and validation integrity.

---

## 7. Deployment Selection Criteria

Authority Collapse Mode and Scope Decay are not competing architectures.

They are deployment decisions.

**Scope Decay Model:**
- Scope narrows during delegation.
- Authority may persist across hops.
- Lightweight, lower overhead.
- Suitable for non-sensitive operations.

**Authority Collapse Mode:**
- Required for irreversible or high-risk actions.
- Required for sensitive resource access.
- Deterministic recomputation at every boundary.
- No delegated execution window.

Selection should be explicit and documented per deployment.

---

## 8. Invariants

Authority must be recomputable without delegated trust continuity.

If recomputation depends on inherited delegation state,
collapse semantics are violated.

---

## 9. Open Questions

The following remain intentionally open problems:

1. Snapshot completeness guarantees  
2. Override interaction constraints  
3. Canonical input minimal sufficiency  
4. Performance impact of boundary re-derivation  

These are named explicitly to define future contribution areas.

---

## 10. Summary

Authority Collapse Mode enforces:

- Deterministic re-derivation  
- Boundary isolation  
- Signed override inputs  
- Zero trust in delegated authority continuity  

Delegation grammar describes how scope moves.  
Re-derivation defines what must be true for authority to exist.  
They are parallel, not nested.

Authority exists only when it can be recomputed.
