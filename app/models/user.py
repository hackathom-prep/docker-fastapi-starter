from pydantic import BaseModel

class User(BaseModel):
    # Define your user fields here
    id: int
    email: str
    name: str