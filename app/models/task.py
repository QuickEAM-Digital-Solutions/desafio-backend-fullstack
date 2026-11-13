"""
Task Model (Core Business Entity)
===================================
This file defines the Task SQLAlchemy model.

Use app/models/user.py as a reference for the SQLAlchemy 2.0 typed style
(`Mapped[...]` + `mapped_column(...)`).

You should implement here:
- Task class inheriting from Base, table name "tasks"
- Fields:
    id (UUID, primary key)
    title (str, required)
    description (str, optional)
    status (enum: pending / in_progress / completed)  -> default "pending"
    priority (enum: low / medium / high / urgent)     -> default "medium"
    department (str)
    user_id (UUID, FK to users.id)  -> the OWNER of the task
    created_at (datetime), updated_at (datetime)

Every task belongs to exactly one user (`user_id`). A user must NEVER be able
to read, update or delete a task owned by another user.

After creating the model, remember to:
1. Import it in app/models/__init__.py (so Alembic can detect it)
2. Generate and apply a migration:
       alembic revision --autogenerate -m "create users and tasks tables"
       alembic upgrade head
"""
