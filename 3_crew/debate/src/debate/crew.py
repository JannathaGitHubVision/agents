from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

@CrewBase
class Debate():
    """Debate crew"""

    agents = 'config/agents.yaml'
    tasks = 'config/tasks.yaml'

    
    @agent
    def debater(self) -> Agent:
        return Agent(
            config=self.agents_config['debater'], # type: ignore[index]
            verbose=True
        )

    @agent
    def judge(self) -> Agent:
        return Agent(
            config=self.agents_config['judge'], # type: ignore[index]
            verbose=True
        )

    
    @task
    def propose(self) -> Task:
        return Task(
            config=self.tasks_config['propose'], # type: ignore[index]
        )

    @task
    def reporting_task(self) -> Task:
        return Task(
            config=self.tasks_config['reporting_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Debate crew"""

        return Crew(
            agents=self.agents, 
            tasks=self.tasks, 
            process=Process.sequential,
            verbose=True,
        )
