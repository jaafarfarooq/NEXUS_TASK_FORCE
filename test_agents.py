import asyncio
from agents.workers import ResearcherAgent, CodingAgent, ReviewerAgent

async def run_pipeline_test():
    print("🚀 Initializing Nexus Task Force Pipeline Test...\n")

    # 1. Instantiate the agents (Using the parameters from your BaseAgent)
    researcher = ResearcherAgent(agent_id=1, name="Alan", role="Researcher", model_provider="mock-llm")
    coder = CodingAgent(agent_id=2, name="Ada", role="Coder", model_provider="mock-llm")
    reviewer = ReviewerAgent(agent_id=3, name="Grace", role="Reviewer", model_provider="mock-llm")

    # 2. Define a dummy task
    bounty_description = "Build a JWT authentication system in FastAPI."

    # 3. Execute the pipeline sequentially
    print("--- STEP 1: RESEARCH ---")
    research_output = await researcher.execute_task(bounty_description)
    print(f"FINAL OUTPUT -> {research_output}\n")

    print("--- STEP 2: CODING ---")
    # Notice we pass the researcher's output to the coder
    code_output = await coder.execute_task(research_output)
    print(f"FINAL OUTPUT -> {code_output}\n")

    print("--- STEP 3: REVIEW ---")
    # Notice we pass the coder's output to the reviewer
    review_output = await reviewer.execute_task(code_output)
    print(f"FINAL OUTPUT -> {review_output}\n")

    print("✅ Pipeline Test Complete.")

if __name__ == "__main__":
    # This is how you run async functions in standard Python scripts
    asyncio.run(run_pipeline_test())