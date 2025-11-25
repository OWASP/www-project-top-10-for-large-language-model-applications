# GenAI Red Team Sandbox Templates

This directory hosts a collection of **sandbox templates** designed to facilitate Generative AI (GenAI) Red Teaming exercises.

## Purpose

The goal of these templates is to provide ready-to-use, isolated environments where security researchers and red teamers can test, probe, and evaluate Large Language Model (LLM) applications and other GenAI systems safely.

## Contents

*    **`llm_local/`**: A local sandbox environment that mocks an LLM API (compatible with OpenAI's interface) using a local model (via Ollama). This template is useful for testing client-side interactions, prompt injection vulnerabilities, and other security assessments without relying on external, paid APIs. Additionally, it allows developers to customize the underlying LLM and orchestrate sophisticated GenAI pipelines, incorporating features such as RAG and guardrail layers, as necessary.

## Usage

Each template directory contains its own `README.md` with specific instructions on how to build, run, and use that particular sandbox. Please refer to the individual template documentation for details.
