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

## 📂 Project Structure

fastapi-starter/
│── app/
│ ├── controllers/
│ │ ├── users.py
│ │ └── items.py
│ ├── models/
│ │ ├── user.py
│ │ └── item.py
│ ├── services/
│ │ ├── user_service.py
│ │ └── item_service.py
│ ├── database/
│ │ └── db.py
│ └── main.py # App entry point
│── requirements.txt
│── README.md
│── Dockerfile


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

```bash
pip install -r requirements.txt
```