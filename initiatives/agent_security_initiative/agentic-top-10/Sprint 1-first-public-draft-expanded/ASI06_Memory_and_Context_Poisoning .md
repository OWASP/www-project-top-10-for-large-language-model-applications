## ASI06 - Memory & Context Poisoning


**Description:**
LLM systems can be augmented with memory systems to improve performance. These systems, which are used to improve an LLM's performance, can include external memory stores like Retrieval-Augmented Generation (RAG) vector databases or extended context windows that hold user session data. These systems can be manipulated by adversaries, who can add malicious or misleading data to the agent's memory stores, resulting in latent security vulnerabilities. Since memory entries may influence agent behavior in subsequent runs or when accessed by other agents, memory poisoning introduces systemic risk.

**Common Examples of Vulnerability:**

1. RAG Poisoning: RAG Poisoning occurs when data which shouldn’t be used for desired actions or queries is inserted into the vector database. This could happen via:
   - Poisoning input data streams, such as creating false/misleading information in an online wiki. If that information is scraped and collected into the RAG system, the poisoned data would be included.
   - Maliciously uploading files into the vector database directly. This could occur if attackers gain undesired access to the database.
   - Providing excessive trust to input data pipelines. This could look like user documents being uploaded as part of normal usage. If user documents are not properly scanned or sanitized, attackers could choose to upload malicious documents which wouldn’t be caught and removed.

RAG poisoning has wide reaching impacts, from delivering false information with a higher degree of authority due to having resources to back up claims, to attacking individual users’ LLM interactions with specifically crafted payloads to target their unique exchanges.

2. Shared User Context Poisoning: Any LLM system which saves contexts between runs, or uses a shared context window for multiple user interactions, can fall victim to Shared User Context Poisoning. This attack is very straightforward, letting attackers influence the behavior of an LLM during their session, and that influence leaking into subsequent sessions. 
This attack type has far-reaching consequences depending on how the LLM system is connected, such as poor output performance or spreading misinformation if subsequent users are directly chatting with an LLM, to code execution attacks if the LLM is being used inside of a tool calling or code writing system.

3. Systemic Misalignment and Backdoors: Memory poisoning can have more subtle and severe consequences than simply producing wrong results. A poisoned LLM can take on a new, malicious persona, deviating from its intended purpose. Attackers can also use this technique to install a backdoor, such as a secret instruction that remains inactive until a certain trigger phrase is entered. When the LLM encounters this sentence, it carries out the disguised malicious instructions, such as producing destructive code or transmitting sensitive data.

4. Cascading failures and data exfiltration: A single poisoned memory entry in a sophisticated, multi-agent system (MAS) might have a domino effect, resulting in cascading failure. One agent may retrieve damaged data and then share it with others, leading the system to become unstable. Malicious instructions can also be placed in the memory as persistence instructions, allowing the LLM to access and communicate sensitive user or enterprise data to an attacker. This data exfiltration poses a significant risk since the model might be allowed valid access to data repositories but then altered to use that access maliciously.


**how to Prevent:**

Preventing ASI06 requires a multi-layered approach to secure and validate an LLM's memory. Key strategies include:

**Content Validation:** Scan all new memory insertions for anomalies or malicious content before they are committed.
* Use AI-based scanners like Microsoft Presidio for PII detection and input sanitization.
* Leverage adversarial testing frameworks such as PyRIT and Garak.

**Memory Segmentation:** Isolate memory access using session isolation to prevent "knowledge leakage" across different users.
**Access Control & Retention Policies:**
* Limit access to trusted sources only.
* Apply context-aware policies so an agent only accesses memory relevant to its current task.
* Limit retention durations based on data sensitivity to reduce long-term risk.
* Implement provenance tracking (e.g., using TruLens or LangSmith traces)
**Knowledge Provenance & Anomaly Detection:**
* Require source attribution for all memory updates to trace where knowledge originated.
* Track AI knowledge lineage to understand how the memory evolved.
* Deploy anomaly detection to identify suspicious memory updates or abnormal update frequencies.
**Resilience & Verification:**
* Use rollback and snapshot mechanisms to revert to a previous state after an anomaly is detected.
* Implement probabilistic truth-checking to verify new knowledge against trusted, verified source (e.g., using tools as Google Fact Check API)
* Use version control for memory updates to support auditing, rollback, and tamper detection.


References
[PoisonedRAG](https://arxiv.org/pdf/2402.07867)
