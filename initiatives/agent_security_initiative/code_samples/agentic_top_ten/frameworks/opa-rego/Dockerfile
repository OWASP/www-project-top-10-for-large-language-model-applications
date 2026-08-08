FROM openpolicyagent/opa:latest-static

LABEL org.opencontainers.image.title="OWASP ASI OPA Rego Enforcement Policies"
LABEL org.opencontainers.image.description="OPA enforcement reference implementations for the OWASP Agentic Security Initiative Top 10"
LABEL org.opencontainers.image.source="https://github.com/OWASP/www-project-top-10-for-large-language-model-applications"
LABEL org.opencontainers.image.licenses="CC-BY-SA-4.0"

WORKDIR /policies

COPY policies/ /policies/
COPY examples/inputs/ /examples/inputs/

# Default: run OPA tests across all 10 ASI policies
ENTRYPOINT ["/opa"]
CMD ["eval", \
     "--data", "/policies/", \
     "--input", "/dev/stdin", \
     "data"]

# ── Usage ─────────────────────────────────────────────────────────────
#
# Build:
#   docker build -t owasp-asi-opa .
#
# Evaluate a single policy against an input file:
#   docker run --rm -i owasp-asi-opa \
#     eval --data /policies/ \
#     --input /dev/stdin \
#     "data.owasp.asi.asi01_agent_behaviour_hijack.decision" \
#     < examples/inputs/asi01_deny_injection.json
#
# Run with all example inputs piped interactively:
#   cat examples/inputs/asi01_deny_injection.json | \
#     docker run --rm -i owasp-asi-opa \
#     eval --data /policies/ --input /dev/stdin \
#     "data.owasp.asi.asi01_agent_behaviour_hijack"
