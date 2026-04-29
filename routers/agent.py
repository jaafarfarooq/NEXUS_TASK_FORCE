from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Agent
from deps import get_session

router = APIRouter()

@router.post("/", response_model=Agent)
def create_agent(agent: Agent, session: Session = Depends(get_session)):
    session.add(agent)
    session.commit()
    session.refresh(agent)
    return agent

@router.get("/", response_model=list[Agent])
def get_agents(session: Session = Depends(get_session)):
    return session.exec(select(Agent)).all()

@router.get("/{agent_id}", response_model=Agent)
def get_agent(agent_id: int, session: Session = Depends(get_session)):
    agent = session.get(Agent, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")
    return agent

@router.put("/{agent_id}", response_model=Agent)
def update_agent(agent_id: int, data: Agent, session: Session = Depends(get_session)):
    agent = session.get(Agent, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(agent, key, value)

    session.commit()
    session.refresh(agent)
    return agent

@router.delete("/{agent_id}")
def delete_agent(agent_id: int, session: Session = Depends(get_session)):
    agent = session.get(Agent, agent_id)
    if not agent:
        raise HTTPException(status_code=404, detail="Agent not found")

    session.delete(agent)
    session.commit()
    return {"message": "Deleted"}