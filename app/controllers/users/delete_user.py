from fastapi import APIRouter, Depends
from fastapi.exceptions import HTTPException
from app.services.users.delete_user import delete_user as delete_user_service


router = APIRouter()

@router.delete("/users/{user_id}")
async def delete_user(user_id: str):
    try:
        delete_user_service(user_id)
        return {"message": "User deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    