# Web Interface Module

This module provides a web-based interface for the NHL analytics system.

## Purpose
- Provide user-friendly access to analytics and visualizations
- Expose REST API endpoints for data access
- Serve interactive dashboards
- Handle user authentication (if needed)

## Components
- `app.py` - Main application entry point (FastAPI/Flask/Django)
- `routes.py` - API route definitions and handlers
- `templates/` - HTML templates (Jinja2)
- `static/` - CSS, JavaScript, images, and other static assets

## API Endpoints (proposed)
```
GET  /api/teams                    - List all teams
GET  /api/teams/{team_id}          - Get team details
GET  /api/players                  - List players (with filters)
GET  /api/players/{player_id}      - Get player details
GET  /api/games                    - List games (with filters)
GET  /api/games/{game_id}          - Get game details
GET  /api/standings                - Get current standings
GET  /api/stats/player/{player_id} - Get player statistics
GET  /api/stats/team/{team_id}     - Get team statistics
POST /api/compare/players          - Compare multiple players
GET  /api/visualizations/{type}    - Generate visualizations
```

## Web Pages (proposed)
- Home/Dashboard
- Teams list and detail pages
- Players list and detail pages
- Games schedule and detail pages
- Standings page
- Statistics and analytics pages
- Comparison tools

## Usage Example
```python
# FastAPI example
from fastapi import FastAPI
from src.web.routes import router

app = FastAPI(title="NHL Analytics API")
app.include_router(router)

# Run with: uvicorn src.web.app:app --reload
```

## Technologies
- FastAPI (recommended) - Modern, fast, async API framework
- Flask - Lightweight alternative
- Django - Full-featured with admin panel
- React/Vue.js - Frontend SPA (optional)
- Bootstrap/Tailwind CSS - Styling
