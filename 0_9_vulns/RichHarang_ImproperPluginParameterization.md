## Vulnerability Name

**Author(s):**

Rich Harang

**Description:**

A plugin designed to connect an LLM to some external resource accepts free-form text as an input instead of parameterized and type-checked inputs.  This allows a potential attacker significant latitude to construct a malicious request to the plugin that could result in a wide range of undesired behaviors, up to and including remote code execution.

**Labels/Tags:**

- Label: "Input validation"
- Label: "Input sanitization"
- Label: "Insufficient parameterization"

**Common Examples of Vulnerability:**

1. A plugin designed to call a specific API hosted at a specific endpoint accepts a string containing the entire URL to be retrieved, instead of query parameters to be inserted into the URL.
2. A plugin designed to look up information from a SQL database accepts a raw SQL query rather than paramters to be inserted into a fully parameterized query

**How to Prevent:**

1. Plugin calls should be strictly parameterized wherever possible, including type and range checks on inputs
2. When freeform input must be accepted, it should be carefully inspected to ensure that no potentially harmful methods are being called.
3. The plugin should be designed from a least-privilege perspective, exposing as little functionality as possible while still performing its desired function.

**Example Attack Scenarios:**

Scenario #1: A plugin prompt provides a base URL and instructs the LLM to combine the URL with a query to obtain weather forecasts in response to user requests. The resulting URL is then accessed and the results shown to the user. A malicious user crafts a request such that a URL pointing to a domain they control, and not the URL hosting the weather service API, is accessed, allowing the malicious user to obtain the IP address of the plugin for further reconnaisance, as well as to inject their own text into the LLM system via their domain, potentially granting them further access to downstream plugins.