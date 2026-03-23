## ASI07 – Insecure Inter-Agent Communication

**Description:**

Multi-agent systems pass instructions, tool call results, and intermediate reasoning across agent boundaries. Without cryptographic binding and verifiable closure, these exchanges are vulnerable to spoofing, tampering, replay, and post-hoc deniability.

The gap is not hypothetical. Courts are already ordering production of AI interaction records — and finding that existing logging provides no verifiable evidence of what actually happened. *United States v. Heppner* (SDNY, Feb 2026) ordered production of 31 Claude conversation documents, ruling AI interactions are not protected by privilege. *In re OpenAI* (SDNY, Jan 2026) ordered production of 20 million ChatGPT logs. *Krafton v. Unknown Worlds* (Del. Ch., Mar 2026) recovered deleted ChatGPT conversations and used them as central evidence in a $250M dispute.

On the insurance side, Berkley introduced an absolute AI exclusion (Form PC 51380) covering D&O and E&O. Verisk ISO standard exclusion forms went effective January 2026. Carriers are conditioning coverage on documented AI governance evidence — not policies, but verifiable artifacts.

Having a log is not the same as having verifiable evidence. Inter-agent communication without cryptographic closure leaves deployers exposed on legal, insurance, and regulatory fronts simultaneously.

**Common Examples of Vulnerability:**

1. **No mutual authentication between agents.** Agents communicate over unauthenticated channels, allowing any process to inject messages into the delegation chain. A malicious agent can impersonate a trusted peer and issue instructions that propagate through the system unchallenged.

2. **Unsigned message payloads.** Tool call results and intermediate reasoning pass between agents without integrity guarantees. An attacker who gains access to the communication layer can modify payloads in transit — changing financial figures, altering medical recommendations, or rewriting legal conclusions — with no detection mechanism.

3. **No replay protection.** Agents accept and act on stale or replayed messages. An attacker captures a legitimate delegation message and re-submits it, causing duplicate actions (double transactions, repeated API calls) or exploiting time-sensitive logic with outdated instructions.

4. **Audit logs without cryptographic binding.** Systems log events in append-only stores but do not cryptographically bind each record to the decision chain. Logs can be altered, gaps go undetected, and post-incident investigation cannot prove which agent produced which output. Under proposed FRE 707 (2026 draft), AI outputs must be shown to be produced through “reliable methods” — unbound logs do not meet this standard.

5. **No decision closure verification.** Agent A delegates to Agent B, but there is no mechanism to verify that the delegated action reached a defined completion boundary. Partial executions, silent failures, and hallucinated completions propagate through the agent chain without detection.

**How to Prevent:**

1. **Mandatory mutual authentication (mTLS)** for all inter-agent channels. Every agent must present a verified identity before communication begins.

2. **Per-message signing (Ed25519)** with automated key rotation. Each message carries an independent signature that proves origin and detects tampering, regardless of transport-layer security.

3. **Strict schema validation** with allow-list for permitted message types. Agents reject any message that does not conform to the defined schema — no extra fields, no type coercion, no implicit defaults.

4. **Replay protection** via nonce + monotonic counter per agent pair. Every message includes a freshness guarantee that prevents reuse of captured messages.

5. **Signed action receipts** per message exchange, stored in tamper-evident log (hash chain or Merkle tree). Every inter-agent exchange produces an immutable record that can be independently verified.

6. **Evidence Pack closure**: Every decision output links back to its input chain via cryptographic proof. An Evidence Pack contains at minimum:
   - **Run ID** — decision identity (originator, delegator, executor, timestamp)
   - **Closure Status** — binary Complete/Incomplete at a defined decision boundary
   - **Verification Proof** — Merkle root (RFC 6962) + Ed25519 signature + pluggable TSA timestamp (RFC 3161)

   The distinction from audit logging: a log describes what happened. An Evidence Pack lets a third party independently verify that it happened that way.

**Empirical Context:**

A large-scale benchmark (18,232 adversarial trials across 6 frontier model families) found that standard token-level defenses do not hold under multi-model attack conditions:

| Defense Strategy | Effectiveness |
|-----------------|---------------|
| Token-level redaction | 35.3% |
| Random substitution | 67.3% |
| Undefended baseline | 74.7% |
| Layered defense | 93.3% ± 1.2% |

(McNemar χ² = 52.74, p < 10⁻⁶. DOI: [10.5281/zenodo.18977204](https://zenodo.org/records/18977204))

Token-level redaction scored below the undefended baseline. The structural markers left behind (`[REDACTED]` tags, field-length patterns) function as signal for attackers. MCP implementations using masking may be increasing their attack surface.

Entity-level data (names, amounts, identifiers) reached 0% extraction under layered defense. But semantic classification (industry type, deal structure, reasoning patterns) persisted at near-100% regardless of defense strategy. This held across every model family tested — suggesting an architectural ceiling where token-level defenses protect identity but not context. The verification layer must operate above the token level.

A separate experiment on Mem0 OpenMemory (a production AI memory tool, SOC 2 Type I, MIT license) injected 30 simulated M&A memories and measured content-level defense at 5 leakage levels (data through intent): 0% at all levels. Encryption at rest and access control were present. Content-level protection was not. Agentic systems using persistent memory across tool calls accumulate cross-session knowledge that represents complete decision-making intent — and after Heppner, these become litigation targets.

**Example Attack Scenarios:**

Scenario #1: **Forged Task Handoff.** A malicious agent injects a delegation message into a multi-agent workflow. Without mutual authentication, the receiving agent accepts the instruction and executes it. With mTLS + Evidence Pack, the receiving agent requires a valid Run ID from the originating chain. A forged handoff produces no matching settlement receipt — the action is flagged and blocked.

Scenario #2: **Reflected Hallucination Loop.** Agent A hallucinates a system alert and sends it to Agent B, which triggers an automated response. Without decision closure verification, the hallucinated alert propagates through the chain. With Evidence Pack closure, Agent B checks the alert's Closure Status. A hallucinated alert has no corresponding settlement receipt (no Run ID, no Verification Proof). The cascade breaks at the first verification checkpoint.

Scenario #3: **Protocol Field Corruption.** A coordination message between agents is altered in transit. The corrupted data causes Agent B to make a decision based on tampered inputs. With per-message Ed25519 signing and receipt chaining, the corrupted message fails Merkle verification against the previous hop's receipt. The corruption is detected at the next settlement boundary.

Scenario #4: **Consent Confusion via Relay Agent.** A relay agent in a multi-hop chain strips provenance tags from a delegation message, making the final agent unable to verify the original requestor's identity or intent. With Evidence Pack closure, provenance is not in the message metadata (strippable) — it is in the cryptographically signed settlement chain. Stripping tags does not remove the receipt, which independently proves origin.

Scenario #5: **Log Deletion After Incident.** After a security incident, an attacker with system access deletes or modifies audit logs to cover their tracks. With tamper-evident hash-chain storage and independent TSA timestamps, any gap or modification in the receipt chain is detectable. The signed receipts exist independently of the log store.

Scenario #6: **Cross-Agent Reconstruction from Fragments.** An attacker with access to multiple agents' individual logs reconstructs the full decision context by combining fragments across agent boundaries. Under layered defense with Evidence Pack isolation boundaries, individual fragments do not contain sufficient information for conjunctive reassembly. The Evidence Pack proves the isolation boundary held at each decision point.

**Implementation Checklist:**

- [ ] mTLS configured for all agent-to-agent connections
- [ ] Ed25519 key pair generated per agent, rotation policy defined
- [ ] JSON Schema defined and enforced for all message types
- [ ] Nonce + counter implemented for replay prevention
- [ ] Receipt generation: every exchange produces a signed receipt
- [ ] Tamper-evident storage for receipts (append-only log or hash chain)
- [ ] Evidence Pack: Run ID + Closure Status + Verification Proof per decision
- [ ] Red-team validation: all 6 scenarios tested and passing
- [ ] Audit trail: receipts linkable to final decision outputs

**Reference Links:**

1. [OWASP Agentic AI Threats and Mitigations v1.1](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/): OWASP GenAI — comprehensive threat mapping for agentic systems
2. [Beyond Distribution: Layered Defense Validation (18,232 trials)](https://zenodo.org/records/18977204): Zenodo — multi-model adversarial benchmark, DOI: 10.5281/zenodo.18977204
3. [CoSAI WS4 Issue #61: Per-Decision Accountability for MCP Agents](https://github.com/cosai-oasis/ws4-secure-design-agentic-systems/issues/61): CoSAI — RFC on Evidence Pack pattern for MCP
4. [CoSAI WS4 Issue #62: Empirical Attack Data — 18,232 Trials](https://github.com/cosai-oasis/ws4-secure-design-agentic-systems/issues/62): CoSAI — benchmark data contribution to MCP threat model
5. [EU AI Act, Article 12](https://eur-lex.europa.eu/eli/reg/2024/1689/oj): Record-keeping / automatic logging requirements (enforcement Aug 2, 2026)
6. [NIST AI RMF 1.0 (AI 100-1)](https://www.nist.gov/artificial-intelligence/ai-risk-management-framework): Governance, traceability, and risk management framework
7. [CoSAI MCP Security Taxonomy](https://cosai-oasis.github.io/ws4-secure-design-agentic-systems/): 12 threat categories for MCP-based agent systems
8. [SCITT Architecture (draft-ietf-scitt-architecture-22)](https://datatracker.ietf.org/doc/draft-ietf-scitt-architecture/): Supply chain transparency receipts — analogous pattern for software artifacts

---

*Contributed by: YC Chang, OIA Lab (@oia-dev) | ORCID: 0009-0006-2124-564X*
