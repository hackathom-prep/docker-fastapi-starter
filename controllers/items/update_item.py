from fastapi import APIRouter, Depends, HTTPException
from models.item import Item
from fastapi.exceptions import HTTPException
from services.items.update_item import update_item as update_item_service


router = APIRouter()

@router.put("/items/{item_id}")
async def update_item(item_id: str, item: Item):
    try:
        update_item_service(item_id, item)
        return {"message": "Item updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))