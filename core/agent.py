from typing import List, Callable
from core.task import Task

class Agent:
    def __init__(
        self,
        name: str,
        tasks: List[Task] = None,
        handler: Callable = None,
        description: str = None
    ):
        """
        Agent can either:
        - Run a list of Task objects via tasks
        - Or run a single function via handler
        """
        self.name = name
        self.tasks = tasks or []
        self.handler = handler
        self.description = description

    def execute(self, input_data: dict) -> dict:
        if self.tasks:
            data = input_data
            for task in self.tasks:
                data = task.run(data)
            return data
        elif self.handler:
            return self.handler(input_data)
        else:
            raise ValueError(f"Agent {self.name} has no tasks or handler defined.")
