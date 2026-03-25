# Runtime Integrity Layers for Agentic Systems (Draft)

## Why this note exists

Agentic systems can be fully authenticated, encrypted, and logged, yet still execute actions that were not the ones approved upstream.

This occurs when authorization decisions are not enforced at execution boundaries.

In distributed and multi-agent workflows, failures can occur at different points: during transmission, tool selection, authorization-to-execution handoff, or intent formation.

This note separates these concerns into distinct runtime integrity layers so that systems can answer a more concrete question:

**What exactly can the runtime prove, and what can it refuse before execution?**

---

## Layer 1 — Transmission Integrity

### What it addresses
Ensures that the request sent by one component is the same request received by another.

### Typical failure modes
- A request is modified after signing due to intermediary components (e.g., proxies, middleware).
- A previously valid request is replayed without proper nonce or timestamp validation.

### Attestation artifact
- Per-message signature over canonical request payload
- Nonce and timestamp to prevent replay

### Enforcement behavior
- Reject requests with invalid signatures
- Reject requests with reused or expired nonces

### What it does not solve
- Whether the request was the correct one to authorize
- Whether the payload was modified before signing
- Whether the request is still valid at execution time

---

## Layer 2 — Tool Integrity

### What it addresses
Ensures that the tool invoked at runtime is the same tool that was approved.

### Typical failure modes
- Tool definition changes after approval (schema or behavior drift)
- Invocation of a different endpoint or method than originally authorized

### Attestation artifact
- Hash or binding of tool identity (name, schema, endpoint, method)
- Verification at invocation time

### Enforcement behavior
- Reject execution if tool identity does not match approved reference

### What it does not solve
- Whether the payload to the correct tool was modified after authorization
- Whether the tool’s output is semantically correct or safe

---

## Layer 3 — Authorization-at-Execution Integrity

### What it addresses
Ensures that the payload authorized upstream is the payload executed downstream.

### Typical failure modes
- Async dispatch / queue mutation  
  A request is authorized and placed on a queue, but modified before a worker executes it.
- Delegated execution drift  
  One agent is authorized, but another component executes a modified payload under the same context.

### Attestation artifact
- Cryptographic commitment to the authorized request (e.g., hash of canonical payload)
- Bound to an authorization decision (e.g., signed token or execution ticket)

### Enforcement behavior
- Recompute payload commitment at execution time
- Fail closed if execution-time payload does not match authorized commitment

### What it does not solve
- Whether the original authorization decision was correct
- Whether the request reflects correct intent
- Whether execution context is still valid at runtime

---

## Layer 4 — Intent Integrity

### What it addresses
Ensures that the authorization decision itself reflects the correct intended action.

### Typical failure modes
- Prompt injection causes an agent to authorize harmful actions that are structurally valid
- Semantic manipulation passes validation but leads to incorrect or unsafe outcomes

### Attestation artifact
- Indirect signals such as policy evaluation logs, provenance, or behavioral monitoring
- No single cryptographic artifact fully captures intent correctness

### Enforcement behavior
- Partial and probabilistic (e.g., anomaly detection, policy engines, human-in-the-loop)
- Cannot be fully enforced through structural or cryptographic checks alone

### What it does not solve
- Lower-layer integrity guarantees (transmission, tool, execution binding)
- Truthfulness or correctness of underlying data sources

---

## Execution-Boundary Requirement — State Validity / Preconditions

Even if:
- the request was transmitted correctly,
- the correct tool is invoked,
- and the authorized payload is executed,

there remains a critical question:

**Is the system state still valid at the moment of execution?**

### Typical failure modes
- Permissions revoked after authorization but before execution
- Resource ownership or lock state changes invalidate previously approved actions

### Attestation artifact
- Snapshot or recomputation of relevant state at execution time
- Versioning or state-hash references where applicable

### Enforcement behavior
- Re-evaluate preconditions at execution boundary
- Refuse execution if state is stale, incomplete, or no longer admissible

### What it does not solve
- Whether the original authorization logic was correct
- Whether the action aligns with intended user or system goals

---

## Example implementation patterns

Different systems emphasize different layers and enforcement placements:

- MCPS  
  Focuses on transmission and message-level integrity using signed requests, identity binding, and replay protection at the transport layer.

- ArkForge (proxy-atomic model)  
  Collocates policy enforcement and forwarding at a proxy boundary, ensuring that the request received is the request executed within that boundary.

- Authorization-bound execution models  
  Bind authorization decisions to specific payloads and verify them at execution time, addressing scenarios where authorization and execution are separated.

- Production multi-agent systems (e.g., Mycel Network)  
  Provide evidence that lower-layer controls can hold while semantic or intent-layer failures still propagate, highlighting the need for complementary controls.

---

## Open gaps and complementary controls

No single layer provides complete runtime integrity.

Key observations:

- Satisfying transmission integrity does not guarantee execution integrity.
- Restricting tool access does not ensure payload consistency at execution.
- Cryptographic binding does not ensure correct intent.
- Auditability does not prevent semantic manipulation.
- State validity must be enforced at execution, not assumed from prior checks.

A robust agentic system requires:
- clear separation of integrity layers
- explicit attestation artifacts per layer
- enforcement at the appropriate boundary
- complementary controls across layers

---

## Key question for practitioners

For each layer:

**Can the system produce a verifiable artifact — and refuse execution if it does not hold?**
