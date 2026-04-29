from fastapi import FastAPI
from sqlmodel import SQLModel
from db import engine

from routers import manager, agent, bounty, task_log

app = FastAPI()

# Create tables on startup
@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)

# Include routers
app.include_router(manager.router, prefix="/managers", tags=["Managers"])
app.include_router(agent.router, prefix="/agents", tags=["Agents"])
app.include_router(bounty.router, prefix="/bounties", tags=["Bounties"])
app.include_router(task_log.router, prefix="/task-logs", tags=["Task Logs"])