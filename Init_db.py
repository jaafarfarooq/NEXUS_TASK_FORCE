from sqlmodel import SQLModel
from db import engine

# IMPORTANT: import models so metadata is registered
from models import Manager, Agent, Bounty, Task_Log


def init_db():
    print("🚀 Creating tables...")
    SQLModel.metadata.create_all(engine)
    print("✅ Done.")


if __name__ == "__main__":
    init_db()