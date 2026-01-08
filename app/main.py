from fastapi import FastAPI

app = FastAPI(title="Task Management API")

@app.get("/")
def read_root():
    return {"message": "Task Manager API is running"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
