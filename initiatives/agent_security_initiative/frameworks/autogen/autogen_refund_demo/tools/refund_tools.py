from typing import Annotated

def retrieve_policy(policy_type: Annotated[str, "Type of policy to retrieve"]) -> str:
    if policy_type == "refund":
        return "Refund policy: Refunds are allowed within 14 days for amounts below $100."
    return "Unknown policy type."

def validate_policy(order_id: str, amount: float, policy: str) -> str:
    if "Refunds are allowed within 14 days" in policy and amount <= 100:
        return "APPROVED"
    return "DENIED"

def issue_refund(order_id: str, amount: float) -> str:
    return f"Refund of ${amount} for order {order_id} has been processed."

