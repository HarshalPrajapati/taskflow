
# TaskFlow 🚀

TaskFlow is a cloud-based task management backend system built using FastAPI.  
It demonstrates real-world backend development, DevOps practices, and cloud deployment using Docker, CI/CD, and AWS.

---

## 📌 Features

- RESTful APIs for task management (Create, Read, Update, Delete)
- PostgreSQL database integration with SQLAlchemy ORM
- Dockerized application for consistent deployment
- CI pipeline using GitHub Actions for automated builds
- Deployed on AWS EC2 with public access
- Environment-based configuration using `.env`

---

## 🏗️ Architecture

```

Client → FastAPI → PostgreSQL
↓
Docker
↓
AWS EC2 Deployment
↓
GitHub Actions CI

````

---

## 🛠️ Tech Stack

- **Backend:** FastAPI (Python)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Containerization:** Docker
- **CI/CD:** GitHub Actions
- **Cloud:** AWS EC2

---

## ⚙️ Setup & Installation

### 1. Clone the repository
```bash
git clone https://github.com/HarshalPrajapati/taskflow.git
cd taskflow
````

---

### 2. Create environment file

Create `.env` file:

```
DATABASE_URL=postgresql+psycopg://user:password@localhost:5432/taskflow_db
```

---

### 3. Run using Docker

```bash
docker build -t taskflow .
docker run -p 8000:8000 --env-file .env taskflow
```

---

### 4. Access the API

Open in browser:

```
http://localhost:8000/docs
```

---

## 🌐 Deployment

The application is deployed on AWS EC2 using Docker and is accessible via public IP.

---

## 🧪 API Endpoints

* `POST /tasks` → Create task
* `GET /tasks` → Get all tasks
* `GET /tasks/{id}` → Get task by ID
* `PUT /tasks/{id}` → Update task
* `DELETE /tasks/{id}` → Delete task

---

## 🧠 Key Learnings

* Implemented clean backend architecture using FastAPI
* Handled real-world deployment issues (DB permissions, Docker networking)
* Built CI pipeline for automated Docker builds
* Deployed containerized application on cloud infrastructure

---


## 📂 Project Structure

```
taskflow/
│── app/
│   ├── main.py
│   ├── models.py
│   ├── schemas.py
│   ├── crud.py
│   ├── database.py
│
│── Dockerfile
│── requirements.txt
│── .github/workflows/ci.yml
│── README.md
```

---

## 📌 Future Improvements

* Add authentication (JWT)
* Use AWS RDS instead of local PostgreSQL
* Add frontend UI
* Implement logging and monitoring

---

## 👨‍💻 Author

Harshal Prajapati

