# Data Collectors Module

This module contains specialized collectors for different types of NHL data.

## Purpose
- Fetch specific data types from the NHL API
- Transform raw API data into database-ready format
- Handle incremental updates and historical data fetching
- Schedule and orchestrate data collection tasks

## Collectors (to be created)
- `games.py` - Collect game data, scores, play-by-play
- `players.py` - Collect player profiles and statistics
- `teams.py` - Collect team information and rosters
- `standings.py` - Collect league standings
- `schedule.py` - Collect game schedules

## Usage Example
```python
from src.collectors.games import GameCollector

collector = GameCollector()
await collector.fetch_games_for_date("2024-10-22")
await collector.fetch_season_games("20242025")
```

## Design Pattern
Each collector should:
1. Fetch data from API
2. Validate and transform data
3. Store in database
4. Return summary of collected data
