# Scripts Directory

This directory contains utility scripts for setup, maintenance, and operations.

## Purpose
- Automate common tasks
- Set up development environment
- Perform database operations
- Generate reports and exports
- Schedule data collection jobs

## Script Types

### Setup Scripts
Initialize and configure the system:
- `setup_db.py` - Create database schema and initial data
- `setup_env.py` - Configure environment and dependencies
- `init_project.py` - First-time project initialization

### Data Collection Scripts
Fetch and update NHL data:
- `fetch_historical.py` - Fetch historical data for past seasons
- `update_current_season.py` - Update current season data
- `fetch_daily_games.py` - Fetch today's games (for cron jobs)
- `backfill_missing_data.py` - Fill gaps in data collection

### Maintenance Scripts
Database and system maintenance:
- `cleanup_old_data.py` - Remove old cached data
- `backup_database.py` - Create database backups
- `migrate_database.py` - Run database migrations
- `verify_data_integrity.py` - Check for data inconsistencies

### Report Generation Scripts
Generate periodic reports:
- `generate_weekly_report.py` - Weekly statistics summary
- `generate_season_report.py` - End-of-season analysis
- `export_team_stats.py` - Export team statistics to CSV/Excel

### Development Scripts
Tools for development and testing:
- `seed_test_data.py` - Populate database with test data
- `benchmark_queries.py` - Test database query performance
- `validate_api.py` - Verify NHL API endpoints are working

## Usage Examples

### Run a Script
```bash
# From project root
python scripts/setup_db.py

# With arguments
python scripts/fetch_historical.py --season 20232024 --game-type regular

# With environment variables
DATABASE_URL=postgresql://localhost/nhl python scripts/backup_database.py
```

### Schedule with Cron
```bash
# Edit crontab
crontab -e

# Add daily data fetch at 3 AM
0 3 * * * cd /path/to/NHL && /path/to/.venv/bin/python scripts/fetch_daily_games.py

# Add weekly report on Mondays at 9 AM
0 9 * * 1 cd /path/to/NHL && /path/to/.venv/bin/python scripts/generate_weekly_report.py
```

## Script Template
```python
#!/usr/bin/env python3
"""
Script Name: example_script.py
Description: Brief description of what this script does
Usage: python scripts/example_script.py [options]
"""

import argparse
import logging
from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from src.utils.logging import setup_logging
from src.utils.config import get_config

logger = logging.getLogger(__name__)


def main():
    """Main script logic."""
    parser = argparse.ArgumentParser(description="Script description")
    parser.add_argument("--option", help="Option description")
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    
    args = parser.parse_args()
    
    # Setup logging
    log_level = logging.DEBUG if args.verbose else logging.INFO
    setup_logging(level=log_level)
    
    logger.info("Starting script...")
    
    try:
        # Script logic here
        pass
        
    except Exception as e:
        logger.error(f"Script failed: {e}", exc_info=True)
        sys.exit(1)
    
    logger.info("Script completed successfully")


if __name__ == "__main__":
    main()
```

## Best Practices
- Add shebang line (`#!/usr/bin/env python3`)
- Include docstring with usage information
- Use argparse for command-line arguments
- Set up proper logging
- Handle errors gracefully
- Return appropriate exit codes
- Make scripts idempotent when possible
- Add progress indicators for long-running scripts
