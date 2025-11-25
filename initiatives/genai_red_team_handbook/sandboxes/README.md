# GenAI Red Team Sandboxes

This directory hosts a collection of **sandboxes** designed to facilitate Generative AI (GenAI) Red Teaming exercises.

## Purpose

The goal of these sandboxes is to provide ready-to-use, isolated environments where security researchers and red teamers can test, probe, and evaluate Large Language Model (LLM) applications and other GenAI systems safely.

## Contents

*    **`llm_local/`**: A local sandbox environment that mocks an LLM API (compatible with OpenAI's interface) using a local model (via Ollama). This sandbox is useful for testing client-side interactions, prompt injection vulnerabilities, and other security assessments without relying on external, paid APIs. Additionally, it allows developers to customize the underlying LLM and orchestrate sophisticated GenAI pipelines, incorporating features such as RAG and guardrail layers, as necessary.

*    **`RAG_local/`**: A comprehensive RAG (Retrieval-Augmented Generation) sandbox that includes a mock Vector Database (Pinecone compatible), mock Object Storage (Amazon S3 compatible), and a mock LLM API (OpenAI compatible). This environment is specifically designed for Red Teaming RAG architectures, allowing researchers to explore vulnerabilities such as embedding inversion, data poisoning, and retrieval manipulation in a controlled, local setting.

## Usage

Each sandbox directory contains its own `README.md` with specific instructions on how to build, run, and use that particular sandbox. Please refer to the individual sandbox documentation for details.
