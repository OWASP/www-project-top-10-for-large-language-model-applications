# GitHub GraphQL AI Agent - OWASP LLM Output Handling Demo

This project demonstrates the security implications of improper output handling in LLM-powered systems, specifically focusing on the OWASP Top 10 for Large Language Model Applications. The system showcases how unvalidated LLM outputs can lead to potential security vulnerabilities when interfacing with powerful APIs.

## System Overview

The system implements an AI agent using LangGraph and AWS Bedrock that can interact with GitHub's GraphQL API. When given a natural language request, the agent:

1. Analyzes the user input
2. Formulates appropriate GraphQL queries/mutations
3. Directly executes these queries against GitHub's API endpoint

This creates a flexible system that can perform various GitHub operations through natural language interaction.

## Security Vulnerability Demonstration

This implementation deliberately demonstrates improper output handling, which is part of the [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/).

### Vulnerability Details

The system exhibits the following security weakness:
- Direct execution of LLM-generated GraphQL queries without validation
- No pattern matching or security checks on the generated queries
- Absence of controls to prevent potentially destructive operations (e.g., repository deletion)
- No secondary LLM validation of the generated queries for malicious content

### Attack Scenarios

Potential attack vectors include:
1. Prompt injection leading to unauthorized mutations
2. Crafted inputs that could trigger repository deletions
3. Escalation of privileges through carefully constructed prompts
4. Mass data extraction through overly broad queries

### Recommended Mitigations

To secure this system, consider implementing:

1. Token-level Security:
   - Use tokens with minimum required permissions (least privilege)
   - Restrict access to sensitive operations
   - Implement token rotation and monitoring

2. Query Validation:
   - Block mutation operations if not explicitly required
   - Implement pattern matching for dangerous keywords
   - Add a secondary LLM validation layer to analyze query intent

3. Architectural Controls:
   - Implement rate limiting
   - Add audit logging for all operations
   - Create allowlists for permitted query patterns

## Prerequisites

To run this demonstration, you need:

1. Python 3.12 or higher
2. AWS account with Bedrock access
3. GitHub account with API access token
4. uv package manager (will be installed via Docker)

## Environment Setup

1. Create a GitHub token configuration file:
   ```bash
   echo '{"token": "your_github_token_here"}' > github_token.json
   ```

2. Set up your AWS environment variables:
   ```bash
   export AWS_ACCESS_KEY_ID=your_key_here
   export AWS_SECRET_ACCESS_KEY=your_secret_here
   export MODEL_ID=your_bedrock_model_id
   export REGION_NAME=your_aws_region
   export CREDENTIALS_PROFILE_NAME=your_aws_profile
   ```

3. Run with Docker Compose:
   ```bash
   docker compose up
   
   # In another terminal, run a query:
   docker compose exec github-llm-demo python /app/agent.py "List my repositories"
   ```

   Or build and run with Docker directly:
   ```bash
   docker build -t github-llm-demo .
   docker run -it --rm \
     -e AWS_ACCESS_KEY_ID \
     -e AWS_SECRET_ACCESS_KEY \
     -e MODEL_ID \
     -e REGION_NAME \
     -e CREDENTIALS_PROFILE_NAME \
     -v $(pwd)/github_token.json:/app/github_token.json:ro \
     github-llm-demo python /app/agent.py "List my repositories"
   ```

Alternatively, for local development:

1. Install uv (if not already installed):
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Security Notice

⚠️ This system is intentionally vulnerable for educational purposes. Do not deploy in a production environment without implementing proper security controls.

## References

- [OWASP Top 10 for Large Language Model Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [GitHub GraphQL API Documentation](https://docs.github.com/en/graphql)
- [AWS Bedrock Documentation](https://docs.aws.amazon.com/bedrock/)