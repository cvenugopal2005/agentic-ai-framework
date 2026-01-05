import json
from datetime import datetime

class Memory:
    def __init__(self, file_path="storage/state.json"):
        self.file_path = file_path

    def save(self, agent_name: str, data: dict):
        record = {
            "agent": agent_name,
            "timestamp": datetime.utcnow().isoformat(),
            "data": data
        }
        with open(self.file_path, "a") as f:
            f.write(json.dumps(record) + "\n")
