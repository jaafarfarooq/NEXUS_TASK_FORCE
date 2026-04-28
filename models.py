from datetime import datetime, timezone
from sqlmodel import SQLModel, Field


class Manager(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    username: str
    email: str = Field(index=True, unique=True)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class Agent(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    role: str
    model_provider: str
    status: str = "Idle"


class Bounty(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    description: str
    status: str = "Open"
    priority_score: int
    final_result: str | None = None

    manager_id: int = Field(foreign_key="manager.id")
    assigned_agent_id: int | None = Field(default=None, foreign_key="agent.id")


class Task_Log(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    action_taken: str
    output_payload: str
    timestamp: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))

    bounty_id: int = Field(foreign_key="bounty.id")
    agent_id: int = Field(foreign_key="agent.id")