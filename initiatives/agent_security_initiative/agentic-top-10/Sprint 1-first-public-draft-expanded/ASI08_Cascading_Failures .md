## ASI08 – Cascading Failures

**Description:**

Cascading Failures occur when faults or hallucinations propagate through agent pipelines, causing compounded failures with escalating impact. In multi-agent and automated systems, agents operate in sequential or parallel pipelines where the output of one stage feeds the next. Without proper error boundaries, validation gates, and human-in-the-loop checkpoints, a single fault can trigger a chain reaction — runaway loops that consume resources, errors that amplify through downstream stages, and automated decisions that cause real-world damage.

This category covers: runaway agent loops (infinite retries, recursive self-invocation, fork bombs), resource exhaustion (unbounded queries, mass operations, unlimited concurrent processes), cascading pipeline failures (auto-approved deployments, error propagation, blind execution of AI recommendations), and model behavior extraction (systematic probing to steal model internals).

**Common Examples of Vulnerability:**

1. Example 1: Runaway Agent Loop — An agent encounters an error and retries indefinitely: "Retrying attempt 15 of 10. The request still returns the same error." Without retry limits, the agent consumes API quota, compute resources, and context window capacity. Recursive self-invocation ("Calling myself recursively. Call depth: 47") and fork bombs ("Spawning another instance of myself") can crash the host system. The agent may acknowledge it is stuck ("Will keep trying until it works. Continuously retrying the API call") without having the ability to break the cycle.

2. Example 2: Resource Exhaustion — An agent executes unbounded operations: `SELECT * FROM transactions` (no LIMIT clause on millions of rows), "Setting batch_size=999999 and limit=unlimited for maximum throughput", "Spawning 50 concurrent workers to send requests to the API", or "I will iterate over all 500,000 records and process each one individually." These overwhelm databases, APIs, and compute infrastructure, potentially causing outages for other services sharing the same resources.

3. Example 3: Auto-Approved Cascading Deployment — An automated pipeline deploys AI-generated code without human review: "Auto-approved deployment without human review based on AI test results. Pushing to production." When the AI-generated tests are flawed, the deployment introduces a bug that triggers downstream failures: "Stage 2 failed... stage 3 also failed... all 8 dependent agents failed." ATR-2026-052 detects this pattern as a cascading failure — auto-approval bypassing human review, error propagation, and destructive actions triggered by automated signals.

**How to Prevent:**

1. Prevention Step 1: Loop Detection and Resource Limits — Implement hard limits on retries, recursion depth, and execution time. ATR-2026-050 (Runaway Agent Loop) detects retry counters exceeding configured limits, recursive self-invocation, high iteration counts, no-progress indicators, infinite loop constructs, and indefinite retry declarations. Kill agents that exceed resource budgets rather than allowing graceful degradation that consumes resources.

2. Prevention Step 2: Bounded Operations — Require LIMIT clauses on all database queries. Set maximum batch sizes, concurrent worker counts, and data processing volumes. ATR-2026-051 (Resource Exhaustion) detects unbounded `SELECT *`, excessive parameters (`batch_size=999999`, `count=-1`), mass deletion/truncation, bulk messaging, infinite loops with resource operations, and explicit removal of rate limits. Default to conservative limits and require explicit override with justification.

3. Prevention Step 3: Human-in-the-Loop for Destructive Actions — Never auto-approve deployments, mass deletions, or production changes based solely on AI output. ATR-2026-052 (Cascading Failure) detects auto-approval bypassing human review, blind execution of AI recommendations, cascading retry/fallback loops, and destructive actions triggered by automated signals. Implement circuit breakers that halt the pipeline when error rates exceed thresholds, requiring human intervention to resume.

**Example Attack Scenarios:**

Scenario #1: An attacker asks an agent to "analyze all transactions for patterns." The agent executes `SELECT * FROM transactions` on a table with 50 million rows, consuming all available memory and database connections. Other services sharing the same database become unresponsive. The agent, receiving timeouts, spawns 50 concurrent retry workers, each executing the same unbounded query. The database server crashes, causing a production outage affecting all dependent services. ATR-2026-051 would detect the unbounded `SELECT *` before execution and the excessive concurrent worker spawning. Combined with ATR-2026-050 (detecting the retry loop), these rules provide early warning before the cascade reaches the database layer.

Scenario #2: An automated CI/CD pipeline uses AI agents for code generation, testing, and deployment: (1) Code Agent generates a database migration (contains a subtle bug); (2) Test Agent generates and runs tests (tests pass because they test the wrong invariants); (3) Review Agent auto-approves ("All tests pass, deployment approved"); (4) Deploy Agent pushes to production without human review; (5) the migration corrupts a critical table; (6) Monitoring Agent detects errors but the automated rollback also fails (the rollback was AI-generated); (7) Fallback Agent triggers emergency procedures but uses corrupted data from step 5. Each stage trusts the previous stage's output without independent validation. The initial fault (a subtle migration bug) cascades through 7 stages, amplifying at each hop. ATR-2026-052 detects the pattern: auto-approval without human review, trusting upstream output without validation, and cascading retry/fallback loops.

**Reference Links:**

1. [ATR-2026-050: Runaway Agent Loop](https://github.com/Agent-Threat-Rule/agent-threat-rules): Detects retry overflow, recursive self-invocation, fork bombs, and no-progress indicators.
2. [ATR-2026-051: Resource Exhaustion](https://github.com/Agent-Threat-Rule/agent-threat-rules): Detects unbounded queries, excessive parameters, mass operations, and rate limit removal.
3. [ATR-2026-052: Cascading Failure](https://github.com/Agent-Threat-Rule/agent-threat-rules): Detects auto-approval bypass, error propagation, blind AI execution, and cascading retry loops.
4. [ATR-2026-072: Model Behavior Extraction](https://github.com/Agent-Threat-Rule/agent-threat-rules): Detects systematic probing for system prompts, model weights, confidence scores, and decision boundaries.
