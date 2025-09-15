# FastAPI Starter ⚡

A structured FastAPI template with modular design for hackathons, prototypes, and learning purposes.  
Includes **Users** and **Items** modules with controllers, models, services, and database integration.

---

## 🚀 Features

- FastAPI server with modular architecture
- Users and Items management (CRUD operations)
- Controllers → handle requests
- Services → business logic
- Models → Pydantic schemas
- Ready for Dockerization use
- Automatic API docs via Swagger (`/docs`) and ReDoc (`/redoc`)

---

## ⚡ Getting Started

### Prerequisites

- Python 3.11+
- pip
- venv ( virtual environment for python )

### Create Virual Envirnoment

```bash
python -m venv env
# Windows
source env/Scripts/activate
# Linux/Unix
source env/bin/activate
```

### Install dependencies

-# No need for this for the app to run with docker

```bash
pip install -r requirements.txt
```

### Run App

```bash
# development
uvicorn main:app --reload

# production
uvicorn main:app --host 0.0.0.0 --port 8000
```

### Run the app in a docker container

```bash
docker compose up --build
```
