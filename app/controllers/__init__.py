from app.controllers.items.add_item import router as create_item_crud
from app.controllers.items.get_item import router as get_item_crud
from app.controllers.items.update_item import router as update_item_crud
from app.controllers.items.delete_item import router as delete_item_crud
from app.controllers.users.add_user import router as create_user_crud
from app.controllers.users.get_user import router as get_user_crud
from app.controllers.users.update_user import router as update_user_crud
from app.controllers.users.delete_user import router as delete_user_crud
from fastapi import APIRouter

router = APIRouter()

router.include_router(create_item_crud)
router.include_router(get_item_crud)
router.include_router(update_item_crud)
router.include_router(delete_item_crud)
router.include_router(create_user_crud)
router.include_router(get_user_crud)
router.include_router(update_user_crud)
router.include_router(delete_user_crud)
