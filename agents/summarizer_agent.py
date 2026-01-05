# agents/summarizer_agent.py
from core.agent import Agent
from core.task import Task
import ollama

def summarize_action(input_data: dict) -> dict:
    text = input_data.get("text", "").strip()

    if not text:
        return {"summary": ""}

    prompt = f"""
Summarize the following text clearly and concisely.
Return 3–5 meaningful sentences.

TEXT:
{text}
"""

    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    summary = response["message"]["content"]
    return {"summary": summary}


summarize_task = Task(
    name="SummarizeTask",
    action=summarize_action
)

summarizer_agent = Agent(
    name="SummarizerAgent",
    tasks=[summarize_task]
)
