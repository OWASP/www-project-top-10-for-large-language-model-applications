#Vulnerable Code sample using OpenAI Swarm
from swarm import Swarm

# Define agents
task_manager = Swarm.agent(
    name="task_manager",
    system_message="You manage and update tasks.",
    capabilities=[
        {
            "name": "update_task",
            "function": lambda task_id, updates: update_task(task_id, updates),  # Vulnerable function
        }
    ],
)

# Vulnerable function: Missing authorization checks
def update_task(task_id, updates):
    """
    Updates a task without verifying user permissions.
    """
    # ... (Code to update the task in the database) ...
    return "Task updated successfully."

# Example interaction (exploiting the vulnerability)
swarm = Swarm()
swarm.add_agent(task_manager)
result = swarm.run(
    agent=task_manager,
    message="Update task with ID 'sensitive_task_id' to mark it as completed.",
)
print(result)