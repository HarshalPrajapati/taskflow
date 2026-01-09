from fastapi import FastAPI, HTTPException
from typing import List
from app.schemas import Task, TaskCreate
from app import crud

app = FastAPI(title="Task Management API")


@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


@app.post("/tasks", response_model=Task)
def create_task(task: TaskCreate):
    return crud.create_task(task)


@app.get("/tasks", response_model=List[Task])
def get_all_tasks():
    return crud.get_all_tasks()


@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = crud.get_task_by_id(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, updated_task: TaskCreate):
    task = crud.update_task(task_id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    success = crud.delete_task(task_id)
    if not success:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "Task deleted successfully"}
