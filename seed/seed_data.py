"""
Seed Data Script
=================
Populates the database with data for immediate testing.

You should implement here:
- Create at least 2 users (to demonstrate the per-user isolation), e.g.:
    ana@example.com   / password123
    bruno@example.com / password123
- Create a few tasks for each user, with different statuses and priorities
- Make the script idempotent (running it twice should not duplicate data
  or crash)

Run with: python -m seed.seed_data
(or inside Docker: docker compose exec api python -m seed.seed_data)

Use `async_session_maker` (app/core/database.py), `hash_password`
(app/core/security.py) and `asyncio.run(main())` as the entry point.

Document the seed credentials in the README so reviewers can log in.
"""
