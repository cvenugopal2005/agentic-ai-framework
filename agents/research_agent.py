from llm.ollama_client import call_ollama

def research_agent(input_data: dict):
    topic = input_data["topic"]

    prompt = f"""
You are a professional research assistant.

Conduct in-depth research on the topic: "{topic}"

Your response MUST include:
1. Clear introduction
2. Background / overview
3. Key concepts or components
4. Real-world applications
5. Advantages and limitations
6. Current trends
7. Future scope

Write in a detailed, academic but easy-to-understand manner.
Minimum length: 400–600 words.
"""

    response = call_ollama(
        prompt=prompt,
        model="mistral"
    )

    return {
        "topic": topic,
        "research": response.strip()
    }
