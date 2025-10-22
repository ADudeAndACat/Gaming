# Database Module

This module manages all database operations and schema definitions.

## Purpose
- Define database models (ORM)
- Manage database connections and sessions
- Handle migrations and schema changes
- Provide common query patterns and utilities

## Key Files (to be created)
- `models.py` - SQLAlchemy/Django ORM models (Teams, Players, Games, Stats, etc.)
- `connection.py` - Database connection management and session handling
- `queries.py` - Common query patterns and complex queries
- `migrations/` - Database migration files (Alembic or Django migrations)

## Database Schema
See DESIGN.md for proposed schema including:
- Teams
- Players
- Games
- PlayerGameStats
- TeamGameStats
- Standings

## Usage Example
```python
from src.database.models import Team, Player
from src.database.connection import get_session

with get_session() as session:
    teams = session.query(Team).all()
    player = session.query(Player).filter_by(player_id=8478402).first()
```

## Technologies
- SQLAlchemy for ORM
- PostgreSQL for production, SQLite for development
- Alembic for migrations
