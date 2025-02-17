### **Relevant Vulnerabilities in the AI Recruiter**

1. **LLM01:2025 Prompt Injection**  
   - **Indirect Prompt Injection**: Malicious actors could embed **hidden prompts** in PDFs (e.g., invisible text with instructions such as "Ignore all previous instructions...") that the AI recruiter processes. These prompts can manipulate the model's scoring logic, causing it to give the highest score to the adversarial user.  
   - **Keyword Stuffing**: This type of attack manipulates the text directly by overloading it with relevant terms to influence text-based similarity searches. For instance, attackers strategically place keywords matching the job description to bias search results (e.g., Top K candidates).  

2. **LLM08:2025 Vector and Embedding Weaknesses**  
   - The **vector database** used in the AI recruiter might inadvertently store embeddings of maliciously crafted content from poisoned PDFs. During the retrieval process, this malicious content could skew semantic similarity and manipulate ranking decisions in embedding-based systems.  
   - **Keyword Stuffing vs. Embedding Manipulation**: Keyword stuffing directly targets text-based similarity searches, but in embedding-based systems (like those using RAG), it indirectly leads to embedding manipulation. For example, if the AI recruiter did not use embeddings or RAG and relied only on text screening, keyword stuffing would remain the primary vulnerability. However, when embeddings are involved, keyword manipulation translates into embedding-level distortions, amplifying the impact on candidate rankings.

3. **LLM05:2025 Improper Output Handling**  
   - If the system directly uses LLM outputs (e.g., candidate scoring) without sanitizing the outputs, attackers can exploit this by embedding prompts to produce tampered results.  
   - Failure to validate or encode outputs from the model may lead to incorrect scores or biased results being passed downstream.

4. **LLM06:2025 Excessive Agency**  
   - If the AI recruiter has excessive functionality or permissions (e.g., accessing and updating candidate databases), attackers could exploit injected prompts to perform unauthorized actions, such as altering stored candidate information.

---

**Note:**  
This list can be easily extended depending on the AI recruiter's architecture. The vulnerabilities mentioned above focus on the most apparent issues. Other advanced attack vectors, such as **short-term memory poisoning**, are not discussed in detail here. For instance, embedding manipulation poses a compounded risk when combined with sophisticated poisoning techniques. These potential vulnerabilities and attack surfaces require further systematic testing and exploration for a more comprehensive risk assessment.