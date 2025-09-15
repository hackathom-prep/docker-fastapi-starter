from fastapi import APIRouter
from fastapi.exceptions import HTTPException
from app.services.items.delete_item import delete_item as delete_item_service


router = APIRouter()

@router.delete("/items/{item_id}")
async def delete_item(item_id: str):
    try:
        delete_item_service(item_id)
        return {"message": "Item deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))