# src/crewai_stn_analysis/crew.py

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

@CrewBase
class STNCrew():
    """Crew to analyze STNs and compare evolutionary algorithms"""

    @agent
    def stn_interpreter(self) -> Agent:
        return Agent(
            config=self.agents_config["stn_interpreter"],
            verbose=True,
        )

    @agent
    def algorithm_comparator(self) -> Agent:
        return Agent(
            config=self.agents_config["algorithm_comparator"],
            verbose=True,
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer"],
            verbose=True,
        )

    @task
    def interpret_stn_task(self) -> Task:
        return Task(
            config=self.tasks_config["interpret_stn_task"]
        )

    @task
    def compare_algorithms_task(self) -> Task:
        return Task(
            config=self.tasks_config["compare_algorithms_task"]
        )

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_report_task"],
            output_file="output/stn_analysis_report.md"
        )

    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,  # Sequential execution: each task runs after the previous one completes
            verbose=True,
        )
