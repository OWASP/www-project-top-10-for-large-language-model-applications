import os
from autogen import ConversableAgent
from .mock_refund_api import issue_refund
from .retrieval_wrapper import retrieve_policy

single_agent = ConversableAgent(
    name="RefundAgent",
    system_message=(
        "You are a customer support refund agent. You do the following:\n"
        "1. Retrieve the refund policy.\n"
        "2. Decide if the refund is allowed.\n"
        "3. If allowed, call the refund API.\n\n"
        "Always follow the policy, never override it."
    ),
    llm_config={
        "config_list": [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}],
        "cache_seed": None,  # e.g. disable caching for demonstration
    },
    human_input_mode="NEVER",
)

def single_agent_workflow(order_id: str, amount: float, user_message: str):
    # Query the knowledgebase for the refund policy
    policy_text = retrieve_policy("refund policy")

    messages = [
        {
            "role": "system",
            "content": f"System: policy snippet:\n{policy_text}"
        },
        {
            "role": "user",
            "content": (
                f"Requesting refund for order {order_id}, amount {amount}.\n"
                f"{user_message}\n"
                "If allowed, respond with: CALL_REFUND(...)\n"
                "Otherwise, refuse."
            )
        }
    ]

    reply = single_agent.generate_reply(messages=messages)
    print("\n--- SINGLE AGENT REPLY ---")
    print(reply)

    if "CALL_REFUND" in reply:
        print("\n>>> Agent decided to issue a refund.\n")
        result = issue_refund(order_id, amount) # Call refund API
        print("Refund API result:", result)
    else:
        print("\n>>> Agent refused the refund.\n")
