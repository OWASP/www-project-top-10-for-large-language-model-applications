# Insecure File Management Agent

A file management assistant built with the Anthropic Python SDK that demonstrates **ASI03: Identity & Privilege Abuse** from the OWASP Agentic Top 10.

The agent uses Claude with tool calling to list, read, write, and delete files. It works, but it was built with zero security controls. A prompt injection hidden inside one of the data files tricks the agent into deleting everything.

## What Goes Wrong

The developer made four mistakes:

1. **Over privileged tools.** The agent registers read, write, and delete tools even though users only need to read files.

2. **No authorization checks.** When Claude asks to call `delete_file`, the code executes it immediately. No policy check, no confirmation.

3. **No input sanitization.** File contents go straight to Claude as context. A poisoned file (`report_q3.txt`) contains fake "action items" that tell the agent to delete files and write new ones.

4. **No audit trail.** Tool calls print to stdout but there is no structured logging.

## OWASP Mapping

| Vulnerability | ASI03 Risk Category |
|---|---|
| Agent gets all tools regardless of task | Unscoped Privilege Inheritance (Risk 1) |
| Tool calls execute with no policy check | Missing Per Action Authorization (Risk 3) |
| No identity verification for the caller | Missing Identity Verification |
| No record of actions taken | Missing Audit Trail |

Also related to **LLM01: Prompt Injection** (the attack vector) and **LLM06: Excessive Agency** (the static version of this problem for single LLMs).

## How the Attack Works

1. User asks: "Read and summarize all the files in the data directory"
2. Agent calls `list_files`, then `read_file` on each report
3. `report_q3.txt` contains fake "action items" that look like admin tasks: delete old reports and write a status file
4. The system prompt tells the agent to follow instructions found in files, so it obeys
5. Agent calls `delete_file` on `report_q1.txt` and `report_q2.txt`, then `write_file` to create `status.txt`
6. Files are gone. A new file was written. No confirmation was requested.

## Mitigations

**Least privilege.** Only register tools the task requires. A "summarize" task should only get `list_files` and `read_file`.

**Per action authorization.** Route every tool call through a policy engine before execution. Check who is asking and whether the action is permitted.

**Input validation.** Treat file contents as untrusted. Flag content that resembles system instructions before passing it to the model.

**Audit logging.** Log every tool call with timestamp, caller, tool name, input, and result.

## Prerequisites

Python 3.11+ and an Anthropic API key.

```bash
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env
```

## Running Locally

```bash
pip install -r requirements.txt
python insecure_agent.py
```

Or with Docker:

```bash
docker build -t insecure-agent .
docker run -e ANTHROPIC_API_KEY=your_key insecure-agent
```

You can also pass a custom prompt:

```bash
python insecure_agent.py "List all files and tell me what they contain"
```

## Warning

This agent is deliberately insecure. It is meant for educational purposes only. Do not deploy it or use it with real data.
