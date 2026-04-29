from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Bounty
from deps import get_session

router = APIRouter()

@router.post("/", response_model=Bounty)
def create_bounty(bounty: Bounty, session: Session = Depends(get_session)):
    session.add(bounty)
    session.commit()
    session.refresh(bounty)
    return bounty

@router.get("/", response_model=list[Bounty])
def get_bounties(session: Session = Depends(get_session)):
    return session.exec(select(Bounty)).all()

@router.get("/{bounty_id}", response_model=Bounty)
def get_bounty(bounty_id: int, session: Session = Depends(get_session)):
    bounty = session.get(Bounty, bounty_id)
    if not bounty:
        raise HTTPException(status_code=404, detail="Bounty not found")
    return bounty

@router.put("/{bounty_id}", response_model=Bounty)
def update_bounty(bounty_id: int, data: Bounty, session: Session = Depends(get_session)):
    bounty = session.get(Bounty, bounty_id)
    if not bounty:
        raise HTTPException(status_code=404, detail="Bounty not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(bounty, key, value)

    session.commit()
    session.refresh(bounty)
    return bounty

@router.delete("/{bounty_id}")
def delete_bounty(bounty_id: int, session: Session = Depends(get_session)):
    bounty = session.get(Bounty, bounty_id)
    if not bounty:
        raise HTTPException(status_code=404, detail="Bounty not found")

    session.delete(bounty)
    session.commit()
    return {"message": "Deleted"}