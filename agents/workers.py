import asyncio
from agents.base import BaseAgent

class ResearcherAgent(BaseAgent):
    async def execute_task(self, bounty_description: str) -> str:
        self.update_status("Working")
        self.log_activity("Gathering context and building specification...")
        
        # Simulate the delay of an LLM API call
        await asyncio.sleep(2)
        
        research_result = f"RESEARCH DOC: Specs for '{bounty_description}' have been compiled."
        self.log_activity("Research complete.")
        self.update_status("Idle")
        
        return research_result
    
class CodingAgent(BaseAgent):
    async def execute_task(self, bounty_description: str) -> str:
        self.update_status("Working")
        self.log_activity("Generating code based on specifications...")
        
        # Simulate the delay of an LLM API call
        await asyncio.sleep(3)
        
        code_result = f"CODE DOC: Code for '{bounty_description}' has been generated."
        self.log_activity("Code generation complete.")
        self.update_status("Idle")
        
        return code_result
    
class ReviewerAgent(BaseAgent):
    async def execute_task(self, bounty_description: str) -> str:
        self.update_status("Working")
        self.log_activity("Reviewing code and providing feedback...")
        
        # Simulate the delay of an LLM API call
        await asyncio.sleep(1)
        
        review_result = f"REVIEW DOC: Code for '{bounty_description}' has been reviewed and feedback provided."
        self.log_activity("Review complete.")
        self.update_status("Idle")
        
        return review_result