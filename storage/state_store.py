import json
from datetime import datetime

def save_state(agent, input_data, output_data):
    record = {
        "agent": agent,
        "input": input_data,
        "output": output_data,
        "timestamp": datetime.utcnow().isoformat()
    }

    with open("state.json", "a") as f:
        f.write(json.dumps(record) + "\n")
