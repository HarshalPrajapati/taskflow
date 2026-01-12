from sqlalchemy.orm import Session
from app import models
from app.schemas import TaskCreate


def create_task(db: Session, task: TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task


def get_all_tasks(db: Session):
    return db.query(models.Task).all()


def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()


def update_task(db: Session, task_id: int, updated_task: TaskCreate):
    task = get_task_by_id(db, task_id)
    if not task:
        return None
    task.title = updated_task.title
    task.description = updated_task.description
    task.status = updated_task.status
    db.commit()
    db.refresh(task)
    return task


def delete_task(db: Session, task_id: int):
    task = get_task_by_id(db, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True
