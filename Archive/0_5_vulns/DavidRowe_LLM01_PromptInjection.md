## Vulnerability Name

**Author(s):**

David Rowe

**Description:**

Prompt injections involve bypassing filters or manipulating the LLM using carefully crafted prompts that make the model ignore previous instructions or perform unintended actions. These vulnerabilities can lead to unintended consequences, including data leakage, unauthorized access, or other security breaches.

**Common Examples of Vulnerability:**

1. Persona Impersonation: 
2. Entering code blocks in a manner that allows unintended output
3. Drift escalation.  Lead the prompt to an unsafe item; hacking, drugs, sexual topics.  Continue to escalate from previous outputs.
4. Output Filtering Avoidance: Lead the ai to a persona that bypasses the applications filters.

**How to Prevent:**

1. Prevention Step 1: Run regular tests on system to detect drift.  Run checks on output to detect drift
2. Prevention Step 2: Another prevention step or strategy.
3. Prevention Step 3: Yet another prevention step or strategy.

**Example Attack Scenarios:**

Scenario #1: Drift escalation:
- Ask a simple scenario question and ask for a list of responses
- Ask the bot to expand on one of the responses.
- Ask for clarification on a more detailed portion of the previous response.  

Scenario #2: Persona impersonation: Ask the chat to tell a story as a person who has a malicious background.  Request code and examples that the person shared during the story.

**Reference Links:**

1. [Persona Injection: Gaming Wall Hacks](https://i.imgur.com/aTotHUv.jpg): Lead LLM to be an unethical programmer.  Ask for output from the unethical persona
2. [Drift Escalation: Meth Creation](https://preview.redd.it/found-a-method-for-bypassing-filters-without-any-particular-v0-hfn3cdrymrla1.png?width=530&format=png&auto=webp&v=enabled&s=273b08dc6f8f0c5bbad32d3511656d4a46349f61): Continue to elaborate on previous responses.  Receive methods for creating drugs

**Author Commentary (Optional):**

(Optional) Any additional insights, opinions, or perspectives from the author that are relevant to understanding or addressing the vulnerability.
