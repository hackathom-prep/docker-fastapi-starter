from fastapi import APIRouter, HTTPException
from app.models.item import Item
from fastapi.exceptions import HTTPException
from app.services.users.get_user import get_user as get_user_service


router = APIRouter()

@router.get("/users/{user_id}")
async def get_user(user_id: str):
    try:
        user = get_user_service(user_id)
        return user
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))