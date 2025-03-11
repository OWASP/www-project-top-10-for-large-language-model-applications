![image](https://github.com/user-attachments/assets/78261164-dac5-475a-a8c5-bc31dedd50ba)

# OWASP Agentic Security Initiative (ASI) - Insecure Agent Samples

## Warning
The sample applications here are deliberately insecure to demonstrate Agent security risks.  Please exercise caution when deploying in your environment.

## Objective
We aim to demonstrate security risks in well-known Agentic AI (also known as Agents) frameworks, particularly how Agent misconfigurations (i.e., insecure code, framework-specific misconfigurations) can lead to vulnerabilities identified in the [OWASP Top 10 for Gen AI and Large Language Model Applications 2025](https://owasp.org/www-project-top-10-for-large-language-model-applications).

This repository contains examples of insecure code and/or security misconfigurations in common Agent frameworks such as:

1. [LangChain](https://github.com/langchain-ai/langchain)
2. [LangGraph](https://www.langchain.com/langgraph)
3. [CrewAI](https://www.crewai.com/)
4. [AutoGen](https://microsoft.github.io/autogen/0.2/)
5. [OpenAI Swarm (Experimental)](https://github.com/openai/swarm)
6. [Amazon Bedrock Agents](https://aws.amazon.com/bedrock/agents/)

More Agent frameworks will be supported in the future.

## Structure

The framework folder contains subdirectories for each framework with individual examples of vulnerable agents.
Each example is accompanied by a description of the vulnerability.

## Contributing

The guidelines for contributing are described in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## How to join the ASI

Visit the ASI project landing page:
(https://genai.owasp.org/initiatives/#agenticinitiative)
