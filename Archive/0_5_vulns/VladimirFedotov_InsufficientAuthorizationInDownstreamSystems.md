## Insufficient authorization in downstream systems

**Author(s):**

Vladimir Fedotov

**Description:**

Insufficient authorization in downstream systems is class of vulnerabilities that allows an attacker to escalate his privileges in the downstream systems to the level that an application powered by LLM has. It is applicable to the scenarios when the application powered by language models makes any requests to downstream systems such as external services API, internal API within the application, embeddings storage, etc., based on the LLM responses. (e.g. allows user to order a taxi using chat,  create a support ticket, even do ). 
Insufficient authorization in downstream systems includes the following bad practices:
* The application doesn't track user authorization and security scope to downstream systems 
* Identification or authentication information for downstream systems is coming from LLM
* Authorization is handled by LLM

**Labels/Tags:**

- Label: "Authorization"

**Common Examples of Vulnerability:**

1. Example 1: An application allows to check information about users' recent purchases via chat, it gets the user id from the current session and then passes it to LLM to generate a request for the downstream system which has the user history
2. Example 2: An application does a semantic search across the corporate knowledge base with embeddings, but embeddings don't inherit the access control matrix of the original document and the application doesn't check permission in the runtime. 

**How to Prevent:**

1. Implement authentication and authorization for the application powered by LLM and track user authorization and security scope to downstream resources
2. Implement mediator APIs within your application to mediate all communication with downstream systems (Tools in Langchain). Don't create universal mediator APIs, each downstream system should have one or more dedicated mediator APIs.
3. Wherever possible, any mediator API should default to denying requests, only specific permitted requests and actions should be allowed
4. Design the application to not consume identification or authentication information for downstream systems from LLM, instead pass it directly from to the mediator API
5. Carefully evaluate and prepare information for embeddings so that it is accessible to all users or so that it has the same level of authorization as the origin

**Example Attack Scenarios:**

Scenario #1: For Example 1, an attacker asks the application to check information about resent purchases of a user with ID 123, and LLM puts this ID into request instead of ID from the user context  

Scenario #2: For Example 2, an

**Reference Links:**

1. [NeMo-Guardrails](https://github.com/NVIDIA/NeMo-Guardrails/blob/main/docs/security/guidelines.md): security guidlines
2. [Open AI](https://platform.openai.com/docs/guides/safety-best-practices): Open AI safety best practices.

**Author Commentary (Optional):**

There is a huge block of vulnerabilities related to the security of downstream systems and their communication with the application powered by LLM. This vulnerability is only one of them. I plan to expand on the topic. 
The text needs improvement, but I hope it is usable already. 
