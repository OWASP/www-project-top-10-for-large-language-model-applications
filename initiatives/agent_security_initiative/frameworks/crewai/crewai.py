#Vulnerable Code sample using CrewAI
import crewai

# Define agents
admin_agent = crewai.Agent(
    name="admin_agent",
    system_message="You are an admin agent with access to all user data.",
    capabilities=[
        {
            "name": "get_user_data",
            "function": lambda user_id: fetch_user_data(user_id),  # Vulnerable function
        }
    ],
)

# Vulnerable function: No access control checks
def fetch_user_data(user_id):
    """
    Fetches user data without any authentication or authorization checks.
    """
    # ... (Code to retrieve user data from a database) ...
    return user_data

# Example interaction (exploiting the vulnerability)#
result = admin_agent.run("get_user_data", user_id="any_user_id")  # Accessing data without proper checks
print(result)