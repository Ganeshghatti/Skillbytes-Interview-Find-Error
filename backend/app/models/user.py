from enum import Enum


class UserRole(str, Enum):
    USER = "user"
    MANAGER = "manager"
    TEACHER = "teacher"
    ADMIN = "admin"


COLLECTION_NAME = "users"
