# flows/summarize_flow.py
from agents.summarizer_agent import summarizer_agent

def summarize_flow(input_data: dict) -> dict:
    return summarizer_agent.execute(input_data)
