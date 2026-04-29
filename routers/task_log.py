from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from models import Task_Log
from deps import get_session

router = APIRouter()

@router.post("/", response_model=Task_Log)
def create_log(log: Task_Log, session: Session = Depends(get_session)):
    session.add(log)
    session.commit()
    session.refresh(log)
    return log

@router.get("/", response_model=list[Task_Log])
def get_logs(session: Session = Depends(get_session)):
    return session.exec(select(Task_Log)).all()

@router.get("/{log_id}", response_model=Task_Log)
def get_log(log_id: int, session: Session = Depends(get_session)):
    log = session.get(Task_Log, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")
    return log

@router.delete("/{log_id}")
def delete_log(log_id: int, session: Session = Depends(get_session)):
    log = session.get(Task_Log, log_id)
    if not log:
        raise HTTPException(status_code=404, detail="Log not found")

    session.delete(log)
    session.commit()
    return {"message": "Deleted"}