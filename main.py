from fastapi import FastAPI
from controllers import router as api_router
from fastapi.middleware.cors import CORSMiddleware
from database import close_connection, get_connection

app = FastAPI()
app.include_router(api_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def read_health():
    return {"status": "healthy"}


@app.on_event("startup")
def startup_event():
    get_connection()

@app.on_event("shutdown")
def shutdown_event():
    close_connection()
