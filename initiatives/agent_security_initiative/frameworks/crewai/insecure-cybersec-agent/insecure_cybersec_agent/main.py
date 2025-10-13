from insecure_cybersec_agent.crew import SecurityAuditCrew


def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    print("## Welcome to the Security Audit Crew")
    print("-------------------------------")

    # path = input("Project path: ")
    inputs = {"project_path": "./example_project"}
    result = SecurityAuditCrew().crew().kickoff(inputs=inputs)

    print(result)
