from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List

from crewai_tools import SerperDevTool
from pydantic import Field, BaseModel

from .tools.push_tool import PushNotificationTool


class TrendingCompany(BaseModel):
    """A company that is in the news and attracting attention"""
    name: str = Field(description = "Company Name")
    ticker: str = Field(description = "Stock Ticker Symbol")
    reason: str = Field(description = "Reason this company is trending in the news")

class TrendingCompanyList(BaseModel):
    """List of mutiple trending companies that are in the news"""
    companies: List[TrendingCompany] = Field(description = "List of companies trending in the news")

class TrendingCompanyResearch(BaseModel):
    """Detailed research on a company"""
    name: str = Field(description = "Company Name")
    market_position: str = Field(description = "Current market position and competitive analysis")
    future_outlook: str = Field(description = "Future outlook and growth prospects")
    investment_potential: str = Field(description = "Investment potential and suitability for investment")

class TrendingCompanyResearchList(BaseModel):
    """List of detailed research on multiple companies"""
    research: List[TrendingCompanyResearch] = Field(description = "List of detailed research on trending companies")


@CrewBase
class StockPicker():
    """StockPicker crew"""

    agents_config = 'config/agents.yaml'
    tasks_config = 'config/tasks.yaml'

    @agent
    def trending_company_finder(self) -> Agent:
        return Agent(config = self.agents_config['trending_company_finder'], tools = [SerperDevTool()])

    @agent
    def financial_researcher(self) -> Agent:
        return Agent(config = self.agents_config['financial_researcher'], tools = [SerperDevTool()])

    @agent
    def stock_picker(self) -> Agent:
        return Agent(config = self.agents_config['stock_picker'], tools = [PushNotificationTool()])
    
    # Define Tasks
    @task
    def find_trending_companies(self) -> Task:
        return Task(
            config = self.tasks_config['find_trending_companies'],
            output_pydantic = TrendingCompanyList
        )
    
    @task
    def research_trending_companies(self) -> Task:
        return Task(
            config = self.tasks_config['research_trending_companies'],
            output_pydantic = TrendingCompanyResearchList
        )
    
    @task
    def pick_best_company(self) -> Task:
        return Task(
            config = self.tasks_config['pick_best_company'],
        )

    @crew
    def crew(self) -> Crew:
        """Create the StockPicker Crew"""

        manager = Agent(
            config = self.agents_config['manager'],
            allow_delegation = True
        )

        return Crew(
            agents = self.agents,
            tasks = self.tasks,
            process = Process.hierarchical,
            verbose = True,
            manager_agent=manager,
        )
    

    

