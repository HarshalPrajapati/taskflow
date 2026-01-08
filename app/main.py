from fastapi import FastAPI, HTTPException
from typing import List
from app.schemas import Task, TaskCreate, TaskStatus

app = FastAPI(title="Task Management API")

# In-memory database
tasks_db: List[Task] = []
task_id_counter = 1


@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.dict())
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task


@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return tasks_db


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db[index] = Task(id=task_id, **updated_task.dict())
            return tasks_db[index]
    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
