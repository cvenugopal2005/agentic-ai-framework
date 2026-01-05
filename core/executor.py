import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Executor:
    def run_agent(self, agent, input_data):
        logger.info("Running agent: %s", agent.name)
        return agent.execute(input_data)
