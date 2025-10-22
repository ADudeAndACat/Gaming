# API Module

This module handles all interactions with the NHL API.

## Purpose
- Provide a clean, typed interface to the NHL API
- Handle authentication, rate limiting, and retries
- Cache responses to minimize API calls
- Validate and parse API responses into Python objects

## Key Files (to be created)
- `client.py` - Base HTTP client with retry logic and rate limiting
- `endpoints.py` - NHL API endpoint definitions and URL builders
- `models.py` - Pydantic models for API response validation
- `cache.py` - Response caching implementation (file-based or Redis)

## Usage Example
```python
from src.api.client import NHLAPIClient

client = NHLAPIClient()
teams = await client.get_teams()
standings = await client.get_standings()
```

## NHL API Resources
- New API: https://api-web.nhle.com/v1/
- Community docs: https://gitlab.com/dword4/nhlapi
