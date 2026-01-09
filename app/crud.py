from typing import List
from app.schemas import Task, TaskCreate

# Temporary in-memory storage
tasks_db: List[Task] = []
task_id_counter = 1


def create_task(task: TaskCreate) -> Task:
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task


def get_all_tasks() -> List[Task]:
    return tasks_db


def get_task_by_id(task_id: int) -> Task | None:
    for task in tasks_db:
        if task.id == task_id:
            return task
    return None


def update_task(task_id: int, updated_task: TaskCreate) -> Task | None:
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = Task(id=task_id, **updated_task.dict())
            return tasks_db[index]
    return None


def delete_task(task_id: int) -> bool:
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return True
    return False
