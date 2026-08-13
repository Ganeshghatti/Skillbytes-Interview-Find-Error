from fastapi import APIRouter, Query

from app.schemas.user import PaginatedUsersResponse
from app.services.user_service import get_admin_panel_users

router = APIRouter(prefix="/api/users", tags=["users"])


@router.get("", response_model=PaginatedUsersResponse)
async def list_users(
    page: int = Query(default=1, ge=1),
    limit: int = Query(default=20, ge=1, le=100),
) -> PaginatedUsersResponse:
    return await get_admin_panel_users(page=page, limit=limit)
