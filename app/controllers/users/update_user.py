from fastapi import APIRouter
from app.models.user import User
from fastapi.exceptions import HTTPException
from app.services.users.update_user import update_user as update_user_service

router = APIRouter()

@router.put("/users/{user_id}")
async def update_user_endpoint(user_id: str, user: User):
    try:
        update_user_service(user_id, user)
        return {"message": "User updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

