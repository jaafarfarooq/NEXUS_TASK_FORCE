from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Manager
from deps import get_session

router = APIRouter()

@router.post("/", response_model=Manager)
def create_manager(manager: Manager, session: Session = Depends(get_session)):
    session.add(manager)
    session.commit()
    session.refresh(manager)
    return manager

@router.get("/", response_model=list[Manager])
def get_managers(session: Session = Depends(get_session)):
    return session.exec(select(Manager)).all()

@router.get("/{manager_id}", response_model=Manager)
def get_manager(manager_id: int, session: Session = Depends(get_session)):
    manager = session.get(Manager, manager_id)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")
    return manager

@router.put("/{manager_id}", response_model=Manager)
def update_manager(manager_id: int, data: Manager, session: Session = Depends(get_session)):
    manager = session.get(Manager, manager_id)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    for key, value in data.dict(exclude_unset=True).items():
        setattr(manager, key, value)

    session.commit()
    session.refresh(manager)
    return manager

@router.delete("/{manager_id}")
def delete_manager(manager_id: int, session: Session = Depends(get_session)):
    manager = session.get(Manager, manager_id)
    if not manager:
        raise HTTPException(status_code=404, detail="Manager not found")

    session.delete(manager)
    session.commit()
    return {"message": "Deleted"}