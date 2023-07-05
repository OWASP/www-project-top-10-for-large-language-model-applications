## Denial of Service

**Author(s):**

Leon Derczynski

**Description:**

An attacker interacts with an LLM in a way that is particularly resource-consuming, causing quality of service to degrade for them and other users, or for high resource costs to be incurred.

**Labels/Tags:**

A list that can be used to distinguish associated terminology or phrases to the description of your vulnerability. This will help with sorting through related submissions.

> _A common example: Prompt Injection" can also be also described or referred to as "Prompt Hacking", "Jailbreaking" etc_

- Label: "DoS"
- Label: "Sponge"

**Common Examples of Vulnerability:**

1. Example 1: Posing queries that lead to recurring resource usage through high-volume generation of tasks in a queue, e.g. with LangChain or AutoGPT
2. Example 2: Sending queries that are unusually resource-consuming, perhaps because they use unusual orthography or sequences

**How to Prevent:**

1. Prevention Step 1: Cap resource use per request
2. Prevention Step 2: Cap resource use per step, so that requests involving complex parts execute more slowly
3. Prevention Step 3: Limit the number of queued actions and the number of total actions in a system reacting to LLM responses

**Example Attack Scenarios:**

Scenario #1: An attacker repeatedly sends multiple requests to a hosted model that are difficult and costly for it to process. Many resources are allocated, leading to worse service for other users and increased resource bills for the host.

Scenario #2: A piece of text on a webpage is encountered while an LLM-driven tool is collecting information to respond to a benign query. That piece of text leads to the tool making many more web page requests. The query ends up leading to large amounts of resource consumption, and receives a slow or even absent response, as do any other queries from similar systems that end up encountering the given piece of text.

**Reference Links:**

1. [LangChain max_iterations](https://twitter.com/hwchase17/status/1608467493877579777): demo + fix of this vulnerability in LangChain.
2. [Sponge Examples: Energy-Latency Attacks on Neural Networks](https://arxiv.org/abs/2006.03463): POC - "We mount two variants of this attack on established vision and language models, increasing energy consumption by a factor of 10 to 200."

**Author Commentary (Optional):**

(Optional) Any additional insights, opinions, or perspectives from the author that are relevant to understanding or addressing the vulnerability.
