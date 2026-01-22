from google.adk import Agent
from .prompt import CRITIC_PROMPT

MODEL = "groq/llama-3.1-8b-instant"

critic_agent = Agent(
    name="critic_agent",
    model=MODEL,
    instruction=CRITIC_PROMPT,
)


