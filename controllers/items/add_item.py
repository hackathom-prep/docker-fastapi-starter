from fastapi import APIRouter
from models.item import Item
from fastapi.exceptions import HTTPException
from services.items.create_item import create_item


router = APIRouter()

@router.post("/items/")
async def add_item(item: Item):
    try:
        _id = create_item(item)
        return {"id": _id}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))