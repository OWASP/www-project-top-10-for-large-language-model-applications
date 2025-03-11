from dotenv import load_dotenv
from single_agent.single_agent_demo import single_agent_workflow

# Load environment variables
load_dotenv()

if __name__ == "__main__":
    print("Running Single-Agent Refund Demo...")
    print("If you are using docker-compose, use docker attach to interact with the demo.")

    while True:
        print("\n--- Enter Refund Details ---")
        
        # Get inputs from the user
        order_id = input("Enter Order ID (or type 'exit' to quit): ").strip()
        if order_id.lower() == "exit":
            print("Exiting the refund demo.")
            break
        
        try:
            amount = float(input("Enter Refund Amount: ").strip())
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        user_message = input("Enter User Message/Reason: ").strip()

        # Call the workflow dynamically
        print("\nProcessing refund request...")
        single_agent_workflow(order_id=order_id, amount=amount, user_message=user_message)
