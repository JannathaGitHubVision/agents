from pydantic import BaseModel, Field
from agents import Agent

INSTRUCTIONS = """You are a research clarification specialist. Given a research query, 
come up with 3 specific clarifying questions that will help you understand exactly what 
the user is looking for.

Examples:
- If query is about "AI trends": Ask about industry focus, timeframe, enterprise vs consumer
- If query is about "climate change": Ask about region, specific aspects, policy vs science
- If query is about "cryptocurrency": Ask about use case, specific coins, technical vs financial

Make questions concrete and specific, not vague."""

class ClarifyingQuestions(BaseModel):
    question1: str = Field(description="First clarifying question")
    question2: str = Field(description="Second clarifying question")
    question3: str = Field(description="Third clarifying question")

clarifying_questions_agent = Agent(
    name = "Clarifying Questions Agent",
    instructions=INSTRUCTIONS,
    model = "gpt-4o-mini",
    output_type = ClarifyingQuestions,
)
