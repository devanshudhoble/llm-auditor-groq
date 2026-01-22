from google.adk import Agent
from .prompt import REVISER_PROMPT

reviser_agent = Agent(
    name="reviser_agent",
    model="groq/llama-3.1-8b-instant",
    instruction=REVISER_PROMPT,
)

