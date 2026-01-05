from typing import Callable

class Task:
    def __init__(self, name: str, action: Callable):
        self.name = name
        self.action = action

    def run(self, input_data: dict) -> dict:
        return self.action(input_data)
