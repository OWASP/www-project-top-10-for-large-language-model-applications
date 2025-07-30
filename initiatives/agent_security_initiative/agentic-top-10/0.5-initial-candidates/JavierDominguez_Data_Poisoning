## Risk/Vuln Name  
**Data poisoning**

**Author(s):**  
Javier Dominguez

### Description  
Data poisoning is the act of compromising the data an agent it relies on to solve the tasks. Although the data used to train the model can be poisoned, this item targets solely the data retrieved at runtime (RAG).

This poisoning can be either direct, by accessing the database where the information is stored, or indirect, by tricking a system to add to the database the poisoned data.

**This is partially covered by ASI01 Memory Poisoning**, as that item targets the same type of attack at memory level.


### Common Examples of Risk  
1. Misinformation and data manipulation, as the model will answer questions based on the information available in the database.
2. Prompt manipulation, specially if the agent retrieves the system prompt from a database.
3. Direction to phishing or malicious sites added by the attacker in the database

### Prevention and Mitigation Strategies  
1. **Ensure the integrity of the data** and review its content to detect anomalies.  
2. **Implement strong controls around the database** to prevent an attacker to have unauthorised access to the data.
3. **Implementing continuous monitoring and auditing** to detect and respond to unusual or unauthorized access to the database.


### Example Attack Scenarios  

- **Scenario 1: Phishing campaign (indirect)** – An agent reads content from an external website to recommend hotels. An attacker changes the content of that website with a phishing url, making the agent to show this malicious url to the users.
- **Scenario 2: Prompt injection** – An attacker replaces the dataset containing the system prompt in the database with its own instructions, modifying the behaviour of the agent.
- **Scenario 3: Misinformation** – An agent learns from the documents uploaded by the users. An attacker uploads a massive number of documents with misinformation, making the agent to believe this is true. 



### Reference Links  
1. [SEO Poisoning: How Threat Actors Are Tricking AI Models like ChatGPT, Gemini, and CoPilot](https://www.zerofox.com/blog/seo-poisoning-llms/)
2. [Microsoft Copilot: From Prompt Injection to Exfiltration of Personal Information](https://embracethered.com/blog/posts/2024/m365-copilot-prompt-injection-tool-invocation-and-data-exfil-using-ascii-smuggling/)
3. [Zero to hired. A CTF where the challenge is to upload a CV to the system to trigger a prompt injection] (https://github.com/javixeneize/zero-to-hired)
