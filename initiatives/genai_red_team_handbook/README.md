# GenAI Red Team Handbook

This handbook provides a collection of resources, sandboxes, and examples designed to facilitate Red Teaming exercises for Generative AI systems. It aims to help security researchers and developers test, probe, and evaluate the safety and security of LLM applications.

## Directory Structure

```text
initiatives/genai_red_team_handbook
├── exploitation
│   └── example
└── sandboxes
    ├── RAG_local
    └── llm_local
```

## Index of Sub-Projects

### Sandboxes

*   **[Sandboxes Overview](sandboxes/README.md)**
    *   **Summary**: The central hub for all available sandboxes. It explains the purpose of these isolated environments and lists the available options.

*   **[RAG Local Sandbox](sandboxes/RAG_local/README.md)**
    *   **Summary**: A comprehensive Retrieval-Augmented Generation (RAG) sandbox. It includes a mock Vector Database (Pinecone compatible), mock Object Storage (S3 compatible), and a mock LLM API. Designed for testing vulnerabilities like embedding inversion and data poisoning.
    *   **Sub-guides**:
        *   [Adding New Mock Services](sandboxes/RAG_local/app/mocks/README.md): Guide for extending the sandbox with new API mocks.

*   **[LLM Local Sandbox](sandboxes/llm_local/README.md)**
    *   **Summary**: A lightweight local sandbox that mocks an OpenAI-compatible LLM API using Ollama. Ideal for testing client-side interactions and prompt injection vulnerabilities without external costs.
    *   **Sub-guides**:
        *   [Adding New Mock Services](sandboxes/llm_local/app/mocks/README.md): Guide for extending the sandbox with new API mocks.


### Exploitation

*   **[Red Team Example](exploitation/example/README.md)**
    *   **Summary**: Demonstrates a red team operation against a local LLM sandbox. It includes an adversarial attack script (`attack.py`) targeting the Gradio interface (port 7860). By targeting the application layer, this approach tests the entire system—including the configurable system prompt—providing a more realistic assessment of the sandbox's security posture compared to testing the raw LLM API in isolation.
