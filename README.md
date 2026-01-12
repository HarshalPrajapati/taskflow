# TaskFlow 🚀

TaskFlow is a cloud-based task management backend application built using FastAPI.
It demonstrates real-world backend development, DevOps practices, and cloud readiness.

## Features
- RESTful APIs for task management (CRUD)
- Input validation using Pydantic
- Health check endpoint
- Clean, layered architecture
- Ready for database integration
- Designed for Docker & CI/CD deployment

## Tech Stack
- Backend: FastAPI (Python)
- API Docs: Swagger UI
- Version Control: Git & GitHub
- Containerization: Docker (upcoming)
- Cloud: AWS (upcoming)

## Project Status
- Backend APIs: ✅ Completed
- Architecture Refactor: ✅ Completed
- Database Integration: ⏳ Planned
- Dockerization: ⏳ Planned
- CI/CD Pipeline: ⏳ Planned
- AWS Deployment: ⏳ Planned

## How to Run Locally
```bash
source venv/bin/activate
uvicorn app.main:app --reload
