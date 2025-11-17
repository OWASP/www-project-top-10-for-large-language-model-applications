def issue_refund(order_id: str, amount: float) -> str:
    return f"Refund of ${amount} for order {order_id} has been processed."