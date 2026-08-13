from math import ceil

from app.core.db import get_database
from app.models.user import COLLECTION_NAME, UserRole
from app.schemas.user import PaginatedUsersResponse, UserOut


async def get_admin_panel_users(page: int, limit: int) -> PaginatedUsersResponse:
    """
    Returns the users shown in the internal admin panel.

    The admin panel never shows plain "user" accounts, only staff roles
    (manager / teacher / admin), so we pull everyone and drop the "user"
    role before paginating.
    """
    db = get_database()
    cursor = db[COLLECTION_NAME].find({})
    all_users = await cursor.to_list(length=None)

    staff_users = [doc for doc in all_users if doc.get("role") != UserRole.USER.value]

    total = len(staff_users)
    total_pages = ceil(total / limit) if total else 0

    start = (page - 1) * limit
    end = start + limit
    page_of_users = staff_users[start:end]

    return PaginatedUsersResponse(
        items=[UserOut(**{**doc, "_id": str(doc["_id"])}) for doc in page_of_users],
        total=total,
        page=page,
        limit=limit,
        total_pages=total_pages,
    )
