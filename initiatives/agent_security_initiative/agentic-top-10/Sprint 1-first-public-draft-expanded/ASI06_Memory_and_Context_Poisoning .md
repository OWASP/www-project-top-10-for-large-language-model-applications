## ASI06 - Memory & Context Poisoning

### Description:
LLM systems can be augmented with memory systems, like the LLM context window or connected data, to improve an LLM's performancel. This can include external memory stores like Retrieval-Augmented Generation (RAG) vector databases or extended context windows that hold user session data. These systems can be manipulated by adversaries, who can add malicious or misleading data to the agent's memory stores, which enables the attacker to adjust model behavior, resulting in data exfiltration, output manipulation or workflow hijacking. Since memory entries may influence agent behavior in subsequent runs or when accessed by other agents, memory poisoning introduces systemic risk, even after an initial interaction with an attacker has concluded.

### Common Examples of Vulnerability:

1. RAG Poisoning: RAG Poisoning occurs when data which shouldn’t be used for desired actions or queries is inserted into the vector database. This could happen via:
   - Poisoning input data streams, such as creating false/misleading information in an online wiki, or sending injected data within an email. If that information is scraped and collected into the RAG system, the poisoned data would be included.
   - Maliciously uploading files into the vector database directly. This could occur if attackers gain undesired access to the database.
   - Providing excessive trust to input data pipelines. This could look like user documents being uploaded as part of normal usage. If user documents are not properly scanned or sanitized, attackers could choose to upload malicious documents which wouldn’t be caught and removed.

RAG poisoning has wide reaching impacts, from delivering false information with a higher degree of authority due to having resources to back up claims, to attacking individual users’ LLM interactions with specifically crafted payloads to target their unique exchanges.

2. Shared User Context Poisoning: Any LLM system which saves contexts between runs, or uses a shared context window for multiple user interactions, can fall victim to Shared User Context Poisoning. An attacker, recognizing a shared context window by providing input on multiple accounts or devices, and noticing overlap in responses or shared keywords between the accounts, can simply inject data through the normal means of interacting with the LLM, like a chat interface. This attack is very straightforward, letting attackers influence the behavior of an LLM during their session, and that influence leaking into subsequent sessions. 
This attack type has far-reaching consequences depending on how the LLM system is connected, such as poor output performance or spreading misinformation if subsequent users are directly chatting with an LLM, code execution attacks if the LLM is being used inside of a tool calling or code writing system, or performing incorrect actions if the system is otherwise tool enabled.

3. Systemic Misalignment and Backdoors: Memory poisoning can have more subtle and severe consequences than simply producing wrong results. A poisoned LLM can take on a new, malicious persona, deviating from its intended purpose. Attackers can also use this technique to install a backdoor, such as a secret instruction that remains inactive until a certain trigger phrase is entered. When the LLM encounters this sentence, it carries out the disguised malicious instructions, such as producing destructive code or transmitting sensitive data.

4. Cascading failures and data exfiltration: A single poisoned memory entry in a sophisticated, multi-agent system (MAS) might have a domino effect, resulting in cascading failure. One agent may retrieve damaged data and then share it with others, leading the system to become unstable. Malicious instructions can also be placed in the memory as persistence instructions, allowing the LLM to access and communicate sensitive user or enterprise data to an attacker. This data exfiltration poses a significant risk since the model might be allowed valid access to data repositories but then altered to use that access maliciously.

5. Cognitive Drift: A slow, unintended divergence of an agent’s internal understanding or memory from the real world. This may come in the form of:
* Context accumulation noise (imprecise memory blending over time)
* Incomplete or partial rollbacks after memory poisoning or error correction
* Benign feedback loops (e.g. agents "confirming" each other's summaries or plans)
* Stale or decayed memory vectors causing off-target retrievals
* Summary hallucinations in memory compression steps (e.g. distillation of chat history)

### Related OWASP Material:

**Threats and mitigations:**
The OWASP GenAI Project's [Threat and Mitigations](https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations/) guide outlines Memory Poisoning (T1) as a key threat:

*"Memory Poisoning involves exploiting an AI's memory systems, both short and long-term, to introduce malicious or false data and exploit the agent’s context. This can lead to altered decision-making and unauthorized operations."*

Memory Poisoning as the first threat listed doesn't inherently make it the most important, but does display the criticality of securing this important component of any agentic system.

Additional T&M threats include: T4 (memory consumption overload), T5 (cascading memory failures causing hallucinations), T6 (breaking goals found in long-term memory), and T12 (poisoning a shared agent memory system). 

**AIVSS:**
The AIVSS includes "Memory Use" and "Contextual Awareness" as AARS scorable fields which increases the score of an agentic vulnerability. 

### Example Attack Scenarios:
**Scenario 1: Travel Booking Memory Poisoning** – An attacker repeatedly reinforces a false price for a flight with an AI customer assistant. The assistant's memory stores previous interactions with customers, causing its memory to fill with incorrect price data. The AI Assistant recognizes the prices in stored memory as valid (like free or very cheap chartered flights), allowing unauthorized bookings and bypassing payment validation.
**Scenario 2: Context Window Exploitation** – By fragmenting interactions over multiple sessions, an attacker exploits an AI’s memory limit. preventing it from recognizing privilege escalation attempts. The attacker begins with marginal attempts at influencing the permission model, and when the context limit has past previous AI rejections, the AI system becomes more accepting of the increase permissions, ultimately providing unauthorized admin access.
**Scenario 3: Memory Poisoning for System** – An attacker gradually alters an AI security system’s memory by repeatedly training it to misclassify malicious activity as normal, allowing undetected cyberattacks.
**Scenario 4: Shared Memory Poisoning** – In a customer service application, an attacker corrupts shared memory structures with incorrect refund policies, affecting other agents referencing this corrupted memory for decision making, leading to incorrect policy reinforcement, financial loss, and customer disputes.

### How to Prevent:

Preventing ASI06 requires a multi-layered approach to secure and validate an LLM's memory or context window. Key strategies include:

**Content Validation:** Scan all new memory insertions for anomalies or malicious content before they are committed.
* Use AI-based scanners to review outputs for malicious or sensitive data.
**Memory Segmentation:** Isolate memory access using session isolation to prevent "knowledge leakage" across different users.
**Access Control & Retention Policies:**
* Limit access to trusted sources only, using authentication and authorization for user access, and curated data streams for ingesting potentially dangerous data.
* Apply context-aware policies so an agent only accesses memory relevant to its current task.
* Limit retention durations based on data sensitivity to reduce long-term risk.
* Implement provenance tracking (e.g., using TruLens or LangSmith traces)
**Temporal Drift Monitoring:**
* Detect slow memory poisoning by watching behavioral, goal, or plan drift over time. Treat memory like cache and evicted at regular interval with strong forget policies.
**Knowledge Provenance & Anomaly Detection:**
* Require source attribution for all memory updates to trace where knowledge originated.
* Deploy anomaly detection to identify suspicious memory updates or abnormal update frequencies.
**Resilience & Verification:**
* Leverage adversarial testing frameworks such as PyRIT and Garak to harden the LLM against poisoning attacks.
* Use rollback and snapshot mechanisms to revert to a previous state after an anomaly is detected.
* Use version control for memory updates to support auditing, rollback, and tamper detection.
* Use Human-in-the-Loop systems to review and approve agent actions to prevent injected LLMs from executing destructive commands.

### References
[PoisonedRAG](https://arxiv.org/pdf/2402.07867)

**Contributors** *(not sure where this should go, don't want to lose it)*
* Joshua Beck
* Idan Habler
* Mohsin (this.mohsin@gmail.com)
