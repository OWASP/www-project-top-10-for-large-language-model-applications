## Vulnerability Name

**Author(s):**

Rich Harang

**Description:**

Text produced by the LLM is not properly validated or sanitized prior to futher processing. This may enable attackers, via direct or indirect prompt injection, to manipulate future activity of the application, including calling plugins, making additional LLM calls under attacker control, or providing malformed input to downstream plugins. It can also result in objectionable, inappropriate, or offensive content being returned to a user. 

**Labels/Tags:**

- Label: "Input validation"
- Label: "Response validation"
- Label: "Sanitization"

**Common Examples of Vulnerability:**

1. LLM output is entered directly into an external plugin such as SQL without validation or sanitization.
2. Results from an LLM used as a chatbot backend are displayed directly to the user without further checks.
3. The LLM is allowed to produce private information from the system prompt (e.g. the system instructions) and return it to the user without further checks.

**How to Prevent:**

1. Apply deterministic filtering on output, checking for private or inappropriate information.
2. Apply ML-based sentiment, profanity, or toxicity detection to the output prior to further use.
3. Make use of output templates and extract any LLM results into the appropriate template.

**Example Attack Scenarios:**

Scenario #1: The LLM is prompted to convert word problems to mathematical expressions. These expressions are then passed to an evaluation engine (such as Python, or Wolfram Alpha) to compute the final result.  An attacker uses prompt injection to induce the LLM to return malicious input which is then passed to the evaluation engine, resulting in remote code execution.

Scenario #2: The LLM is instructed to convert a request for information about the weather into an API call. An attacker uses prompt injection to define a new URL base for the plugin to use. This attacker-controlled URL allows them to obtain detailed information about the cloud environment of the LLM-enabled system.
