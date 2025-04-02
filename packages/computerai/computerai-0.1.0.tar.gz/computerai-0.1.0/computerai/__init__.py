"""
computerai - Framework for creating computer use agents
"""

__version__ = "0.1.0"


class Agent:
    """
    A computer use agent that can execute commands
    """

    def __init__(self, name="DefaultAgent"):
        """
        Initialize a new Agent

        Args:
            name (str): The name of the agent
        """
        self.name = name

    def execute(self, command):
        """
        Execute a command

        Args:
            command (str): The command to execute

        Returns:
            str: The result of the execution
        """
        print(f"Agent {self.name} executing: {command}")
        return f"Executed: {command}"


def create_agent(name="DefaultAgent"):
    """
    Create a new agent

    Args:
        name (str): The name of the agent

    Returns:
        Agent: A new computerai agent
    """
    return Agent(name=name)
