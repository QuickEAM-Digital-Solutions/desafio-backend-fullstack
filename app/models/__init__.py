"""ORM models.

Import every model here so that `Base.metadata` knows about all tables
(Alembic autogenerate relies on this).
"""

from app.models.base import Base
from app.models.user import User

# TODO: import your Task model here, e.g.:
# from app.models.task import Task

__all__ = ["Base", "User"]
