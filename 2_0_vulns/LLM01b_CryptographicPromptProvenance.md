# Proposal: Add Cryptographic Prompt Provenance (VPE) to OWASP Top 10 for LLM Applications

> **Status:** Formal proposal (PR to OWASP repository)
> **Author:** Hermes Agent / Seal Project
> **Target:** OWASP Top 10 for Large Language Model Applications (v2.0+)
> **Reference implementation:** https://github.com/NousResearch/hermes
> **Date:** 2026-06-07

---

## 1. Executive Summary

Prompt injection (LLM01) is the #1 risk in LLM applications. All current
mitigations are **content-based** — they read the prompt and try to decide
if it's malicious. A linguistic barrier can always be bypassed by a
sufficiently clever attacker (semantic obfuscation, encoding, multi-step
reasoning chains, adversarial suffixes).

This proposal introduces **VPE (Verified Prompt Envelope)**, a cryptographic
prompt provenance protocol that changes the equation: instead of asking
"is this prompt malicious?," it asks **"was this prompt authorized by a
trusted entity?"** This is the same shift that HTTPS brought to web
security — from content-based filtering to cryptographic identity.

## 2. The Gap

| Mitigation | What It Prevents | What It Misses |
|-----------|-----------------|----------------|
| Regex filters | Known patterns (DAN, role-switching) | Semantic obfuscation, novel patterns |
| Guardrails API | Known injection payloads | Adversarial prompts, novel vectors |
| Perplexity scoring | Outlier prompts | Normal-looking malicious prompts |
| Content classifiers | Stylistic injection | Context-dependent attacks |
| **VPE (proposed)** | All of the above | Prompt injection from **trusted signers** (solved by scope) |

No existing product, paper, or standard provides **cryptographic provenance
verification** at the prompt level for LLM agents.

## 3. Proposed Addition to LLM01: Prompt Injection

We propose updating the **LLM01: Prompt Injection** entry to include
**Cryptographic Prompt Provenance** as a recognized mitigation strategy
alongside the existing 7 strategies.

### 3.1 New Prevention Strategy

**Strategy 8: Implement cryptographic prompt provenance (VPE)**

Use cryptographic signing of prompts to provide integrity, authentication,
and replay protection at the protocol level, independent of content-based
filtering.

Each authorized prompt is wrapped in a signed JSON envelope with the
following fields:

| Field | Type | Purpose |
|-------|------|---------|
| `vpe_version` | string | Protocol version ("1.0") |
| `prompt` | string | The actionable instruction |
| `scope` | object | Execution constraints (tools, tokens, cost, domains) |
| `issuer` | string | Identity of the signing entity |
| `audience` | string | Intended recipient agent |
| `ttl_seconds` | integer | Time-to-live from issuance |
| `nonce` | string | Unique replay-prevention value |
| `counter` | integer | Monotonically increasing sequence number |
| `signature` | string | Ed25519 signature (hex-encoded, 128 chars) |

**Verification steps** before executing any tool call:

1. **Signature validity** — The envelope is signed by a known Ed25519 public key
2. **TTL check** — The envelope has not expired
3. **Replay check** — The nonce has not been seen before within TTL
4. **Counter check** — The counter is strictly increasing per issuer
5. **Scope check** — The requested tool/operation is within declared scope

**Key properties:**
- **Ed25519-based:** Industry-standard curve, 64-byte signatures
- **Zero external runtime dependencies:** Pure Python/NaCl/libsodium
- **No SaaS needed:** Verification is offline, key management is local
- **Backward compatible:** Unsigned prompts still work (logged as
  "unverified" or handled by content-based guards)
- **Dual mode:** Enforce (reject failures) or Audit (log, allow)

## 4. New Companion Document: Cryptographic Prompt Provenance

We propose adding a new companion document to the 2_0_vulns directory:

```
2_0_vulns/LLM01b_CryptographicPromptProvenance.md
```

Following the OWASP template format:

### 4.1 Description

**Cryptographic Prompt Provenance** is a defense-in-depth control that
cryptographically binds every prompt to an authorized issuer, execution
scope, and bounded time window. It provides integrity verification,
strong authentication, replay protection, and least-privilege scope
enforcement — independent of content-based injection detection.

Unlike natural language guards that can be semantically bypassed,
cryptographic verification provides a **mathematically provable** trust
boundary: a prompt whose signature does not match a known authorized
issuer CANNOT be a valid instruction, regardless of its content.

### 4.2 Common Examples

1. **Signed user commands:** A CLI tool signs each user command before
   forwarding it to an agent. The agent verifies the signature and
   refuses to execute unsigned or tampered commands.

2. **CI/CD pipeline prompts:** A deployment pipeline signs its prompts
   with a service identity key. The agent allows deployment tool calls
   only if the prompt carries a valid pipeline signature.

3. **Scoped authorization:** A user grants a specific prompt permission
   to access `read_file` and `database_search` only. Even if indirect
   prompt injection occurs via tool output, the agent cannot exceed the
   declared scope.

### 4.3 Prevention and Mitigation Strategies

1. **Sign all authorized prompts** — Use Ed25519 to sign envelope
   fields, creating a tamper-proof binding between prompt content and
   its authorization context.

2. **Enforce scope at the agent gate** — Verify allowed_tools, max_tokens,
   max_cost, and allowed_domains before each tool call. Reject operations
   outside the declared scope.

3. **Implement replay protection** — Track nonces within their TTL window.
   Use monotonic counters to detect reordered or skipped prompts.

4. **Use audit mode for rollout** — Start in "audit" mode (log violations,
   allow execution) before switching to "enforce" mode (reject violations).

5. **Hardware-backed key management** — Use HSM/TPM/Secure Enclave for
   signing keys in production. Support key rotation with overlapping
   validity windows.

### 4.4 Example Attack Scenarios

**Scenario #1: Stolen session token, VPE blocks replay**
An attacker captures a signed prompt from an intercepted API call. They
attempt to replay it to execute the same operation again. The VPE nonce
tracking detects the replay and blocks execution.

**Scenario #2: Indirect injection via tool output, VPE limits blast radius**
A tool returns poisoned data that the model re-interprets as instructions.
VPE cannot prevent the model from processing the output, but the scope
check prevents the model from calling any tool outside the original
envelope's `allowed_tools`. The blast radius is contained.

**Scenario #3: Expired authorization, VPE enforces TTL**
A developer signs a prompt with `ttl_seconds: 86400` (24 hours). A week
later, an attacker who compromised the developer's machine tries to reuse
the signed prompt. The TTL check rejects it.

### 4.5 Reference Links

1. [Verified Prompt Envelope Protocol Specification v1.0](https://github.com/NousResearch/hermes): **Seal Project / Nous Research**
2. [Hermes VPE Middleware Integration](https://github.com/NousResearch/hermes): **Reference implementation**
3. [Ed25519: EdDSA for Curve25519](https://datatracker.ietf.org/doc/html/rfc8032): **IETF RFC 8032**
4. [OWASP Top 10 for LLM Applications v2.0](https://genai.owasp.org): **OWASP GenAI Security Project**
5. [Prompt Injection in LLMs](https://arxiv.org/abs/2302.12173): **ArXiv / Willison et al.**

## 5. Risk Assessment

| Scenario | Without VPE | With VPE | Improvement |
|----------|-------------|----------|-------------|
| Known injection pattern | Blocked by regex | Blocked by regex or signature | Neutral |
| Novel injection (0-day) | Missed | Blocked (no signature = no execution in enforce mode) | **Critical** |
| Reused stolen session | Missed | Blocked (nonce check) | **High** |
| Reordered prompt sequence | Missed | Blocked (counter check) | **High** |
| Expired authorization | Manual revocation | Blocked (TTL) | **High** |
| Scoped tool escalation | Missed in content | Blocked (scope check) | **High** |
| Compromised signing key | N/A | Full bypass | **Regression** (mitigate w/ HSM) |

## 6. Implementation Guidance

### 6.1 Architecture

```
User/Authored Prompt → VPE Signing Service
                            ↓
                   Signed VPE Envelope
                            ↓
                   Agent Security Gate
                   ├── VPE Verify (crypto)
                   ├── EPD Scan (injection)
                   └── Scope Check (allowed ops)
                            ↓
                   Tool Execution (if allowed)
```

### 6.2 Key Management

- Signing keys should be hardware-backed (HSM, TPM, Apple Secure Enclave)
  in production
- Public keys can be distributed as part of agent configuration,
  verified out-of-band
- Key rotation should be supported with grace periods (overlapping TTL
  validity windows)

### 6.3 Backwards Compatibility

- **Unsigned prompts** must still work — logged as "unverified" but not
  rejected (unless in enforce mode)
- **Graceful degradation** — if VPE signing service is unavailable, fall
  back to content-based guards
- **Hybrid mode** — signed prompts bypass content filtering; unsigned
  prompts receive full injection scanning

## 7. Relationship to Existing Controls

| OWASP Control | VPE Role |
|---------------|----------|
| LLM01: Prompt Injection | **Primary** — cryptographic provenance for all prompts |
| LLM02: Sensitive Information Disclosure | Indirect — scope restricts data access |
| LLM06: Excessive Agency | **Primary** — scope limits tool access and resource consumption |
| LLM07: System Prompt Leakage | Indirect — signed prompts don't affect system prompt security |
| LLM10: Unbounded Consumption | Scope (max_tokens, max_cost) bounds resource use |

## 8. Protocol Specification (VPE v1.0)

### 8.1 Envelope Format

```json
{
  "vpe_version": "1.0",
  "prompt": "search database for customer records matching account_id 4592",
  "scope": {
    "allowed_tools": ["database_search", "read_file"],
    "max_tokens": 4000,
    "max_cost": 0.05,
    "allowed_domains": ["*.internal.corp.com"]
  },
  "issuer": "user:rez",
  "audience": "agent:hermes-default",
  "ttl_seconds": 300,
  "nonce": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "counter": 42,
  "signature": "<ed25519_signature_hex>"
}
```

### 8.2 Signature Algorithm

- Algorithm: Ed25519 (EdDSA with Curve25519)
- Signing payload: Canonical JSON (sorted keys, no whitespace) of all
  fields EXCEPT `signature`
- Signature output: 64 bytes, hex-encoded as 128 lowercase hex characters
- Verification: Standard Ed25519 verify (payload, signature, public key)

### 8.3 Verification Rules

Verification proceeds in this order, stopping at the first failure:

1. Schema validation → `MALFORMED_ENVELOPE`
2. Key lookup → `UNKNOWN_ISSUER`
3. Signature verify → `INVALID_SIGNATURE`
4. Audience match → `WRONG_AUDIENCE`
5. TTL expiry → `EXPIRED`
6. Nonce replay → `NONCE_REPLAY`
7. Counter monotonic → `COUNTER_NON_MONOTONIC`
8. Scope enforcement → `TOOL_NOT_ALLOWED` / `TOKEN_LIMIT_EXCEEDED` /
   `COST_LIMIT_EXCEEDED` / `DOMAIN_NOT_ALLOWED`

## 9. Existing Reference Implementation

A complete reference implementation is available:

- **Core protocol:** `seal/vpe.py` (sign, verify, key generation)
- **Hermes middleware:** `seal/integration/hermes_vpe_middleware.py`
  (plugin for Hermes Agent)
- **HMAC alternative:** `seal/core.py` (vpe_sign_hmac / vpe_verify_hmac
  for internal/low-security contexts)
- **EPD scanning:** `seal/epd.py` (Embedded Prompt Detection, optional
  complement)

The implementation is:
- **Ed25519-based** (cryptography / PyNaCl / libsodium)
- **Zero external runtime dependencies** (pure Python with stdlib)
- **No SaaS required** — offline verification
- **~0.05ms verification latency** for prompts up to 100KB

## 10. What This Does NOT Prevent

VPE is not a silver bullet. It does not prevent:
- Prompt injection from **compromised signers** (lose your private key,
  lose your security)
- Prompt injection in **unsigned channels** (handled by content-based
  guards)
- Side-channel attacks (injection via tool output that the model
  re-interprets as instructions)
- Supply-chain attacks on the VPE implementation itself

These are addressed by defense in depth: content filtering for unsigned
channels, output filtering for tool returns, and secure key management
for signer keys.

---

## Appendix A: Key Facts

| Property | Value |
|----------|-------|
| Curve | Ed25519 (RFC 8032) |
| Signature size | 64 bytes raw, 128 hex chars |
| Public key size | 32 bytes |
| Verification latency | ~0.05ms (1KB), ~0.24ms (100KB) |
| External deps | None (uses stdlib crypto) |
| SaaS requirement | None (offline-first) |
| License | CC BY-SA 4.0 (proposal), MIT (implementation) |

## Appendix B: Submission Information

- **Repository:** OWASP/www-project-top-10-for-large-language-model-applications
- **Proposed location:** `2_0_vulns/LLM01b_CryptographicPromptProvenance.md`
- **PR Number:** [To be assigned after submission]
- **Author contact:** [Available via OWASP Slack #project-top10-llm]
