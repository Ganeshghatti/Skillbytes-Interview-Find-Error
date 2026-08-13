from pydantic import BaseModel, Field

from app.models.user import UserRole


class UserOut(BaseModel):
    id: str = Field(alias="_id")
    full_name: str
    email: str
    role: UserRole
    department: str
    phone: str
    is_active: bool
    created_at: str

    model_config = {"populate_by_name": True}


class PaginatedUsersResponse(BaseModel):
    items: list[UserOut]
    total: int
    page: int
    limit: int
    total_pages: int
