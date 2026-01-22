"""
LLM Auditor (Groq)
Sequential workflow: Critic → Reviser
"""

from google.adk.agents import SequentialAgent

from .sub_agents.critic.agent import critic_agent
from .sub_agents.reviser.agent import reviser_agent

llm_auditor = SequentialAgent(
    name="llm_auditor",
    description=(
        "Evaluates LLM-generated answers, verifies accuracy using web search, "
        "and refines the response to align with real-world facts."
    ),
    sub_agents=[critic_agent, reviser_agent],
)

# ADK entry point
root_agent = llm_auditor


