# Utilities Module

This module contains shared utility functions and helpers used across the application.

## Purpose
- Provide common functionality used by multiple modules
- Centralize configuration management
- Set up logging infrastructure
- Implement helper functions for data processing

## Utility Files (to be created)
- `config.py` - Configuration management (load from env, YAML, etc.)
- `logging.py` - Logging setup and configuration
- `helpers.py` - General helper functions (date parsing, formatting, etc.)
- `validators.py` - Data validation utilities
- `decorators.py` - Custom decorators (retry, cache, timing, etc.)

## Common Utilities

### Configuration
```python
from src.utils.config import get_config

config = get_config()
db_url = config.database.url
api_key = config.api.key
```

### Logging
```python
from src.utils.logging import get_logger

logger = get_logger(__name__)
logger.info("Processing game data")
logger.error("Failed to fetch data", exc_info=True)
```

### Helpers
```python
from src.utils.helpers import parse_nhl_date, format_time_on_ice

date = parse_nhl_date("2024-10-22")
toi = format_time_on_ice(1234)  # "20:34"
```

### Decorators
```python
from src.utils.decorators import retry, cache, timing

@retry(max_attempts=3, delay=1.0)
@cache(ttl=3600)
@timing
async def fetch_data():
    # Function will retry on failure, cache results, and log execution time
    pass
```

## Best Practices
- Keep utilities generic and reusable
- Add comprehensive docstrings
- Include type hints
- Write unit tests for all utilities
