"""
Task Repository (Data Access Layer)
=====================================
Encapsulates all database queries for the Task model.

You should implement here:
- get_by_id(db, user_id, task_id)
- list_by_user(db, user_id, status=None, priority=None, skip=0, limit=20)
- create(db, task)
- update(db, task, data: dict)
- delete(db, task)

All queries MUST filter by user_id. Never return a task owned by another user.

Example:
    async def list_by_user(db: AsyncSession, user_id: UUID, skip=0, limit=20):
        query = (
            select(Task)
            .where(Task.user_id == user_id)
            .order_by(Task.created_at.desc())
            .offset(skip)
            .limit(limit)
        )
        result = await db.execute(query)
        return result.scalars().all()
"""
