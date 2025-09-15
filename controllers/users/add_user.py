from fastapi import APIRouter
from models.user import User
from fastapi.exceptions import HTTPException
from services.users.create_user import create_user

router = APIRouter()

@router.post("/users/")
async def create_user_endpoint(user: User):
    try:
        _id = create_user(user)
        return {"id": _id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))