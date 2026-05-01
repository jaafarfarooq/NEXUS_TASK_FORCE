from abc import ABC, abstractmethod

class BaseAgent(ABC):
    def __init__(self, agent_id: int, name: str, role: str, model_provider: str):
        self.agent_id = agent_id
        self.name = name
        self.role = role
        self.model_provider = model_provider
        self.status = "Idle"
        self.memory = []  # Data structure to hold conversation history

    def log_activity(self, action: str) -> None:
        """
        Concrete method shared by all agents. 
        Currently prints to the console, but will be wired to the DB in NEXUS-204.
        """
        print(f"[{self.role} | {self.name}] action: {action}")

    def update_status(self, new_status: str) -> None:
        """Shared method to update the agent's current state."""
        self.status = new_status
        self.log_activity(f"Status changed to {self.status}")

    @abstractmethod
    async def execute_task(self, bounty_description: str) -> str:
        """
        The core engine. Every subclass MUST override this method.
        If a subclass forgets to include this, Python will throw an error.
        """
        pass