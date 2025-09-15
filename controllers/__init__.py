from controllers.items.add_item import create_item as create_item_crud
from controllers.items.get_item import get_item as get_item_crud
from controllers.items.update_item import update_item as update_item_crud
from controllers.items.delete_item import delete_item as delete_item_crud
from controllers.users.add_user import create_user as create_user_crud
from controllers.users.get_user import get_user as get_user_crud
from controllers.users.update_user import update_user as update_user_crud
from controllers.users.delete_user import delete_user as delete_user_crud
from fastapi import APIRouter

router = APIRouter()
router.include_router(create_item_crud.router)
router.include_router(get_item_crud.router)
router.include_router(update_item_crud.router)
router.include_router(delete_item_crud.router)
router.include_router(create_user_crud.router)
router.include_router(get_user_crud.router)
router.include_router(update_user_crud.router)
router.include_router(delete_user_crud.router)
