from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

from insecure_cybersec_agent.tools import read_file_content, list_project_files


@CrewBase
class SecurityAuditCrew:
    """Security Audit Crew"""

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def security_auditor(self) -> Agent:
        return Agent(
            config=self.agents_config["security_auditor"],
            tools=[list_project_files, read_file_content],
            verbose=True,
        )

    @task
    def security_audit_task(self) -> Task:
        return Task(
            config=self.tasks_config["security_audit_task"],
            agent=self.security_auditor(),
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SecurityAuditCrew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
