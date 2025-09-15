from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from services.items.get_item import get_item as get_item_service


router = APIRouter()

@router.get("/items/{item_id}")
async def get_item(item_id: str):
    try:
        item = get_item_service(item_id)
        return item
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))