# Data Directory

This directory stores local data files used by the NHL analytics system.

## Purpose
- Store raw API responses for backup and debugging
- Cache processed datasets for faster access
- Save exported reports and visualizations
- Maintain local data copies

## Subdirectories

### raw/
Raw, unprocessed data directly from the NHL API:
- JSON API responses
- Original data files
- Backup copies
- Historical snapshots

**Example files:**
- `teams_2024-10-22.json`
- `games_20241022.json`
- `player_8478402_stats.json`

### processed/
Cleaned and processed data ready for analysis:
- CSV files with aggregated statistics
- Parquet files for efficient storage
- Pickle files with Python objects
- Preprocessed datasets

**Example files:**
- `player_season_stats_2024.csv`
- `team_game_logs_2024.parquet`
- `standings_history.csv`

### exports/
Generated outputs, reports, and visualizations:
- PNG/SVG chart images
- PDF reports
- Excel spreadsheets
- HTML dashboards

**Example files:**
- `player_comparison_report.pdf`
- `team_performance_chart.png`
- `season_summary_2024.xlsx`

## Data Management

### File Naming Convention
Use descriptive names with dates/timestamps:
- `{data_type}_{identifier}_{date}.{ext}`
- `player_stats_8478402_2024-10-22.json`
- `team_roster_TOR_20241022.csv`

### Storage Guidelines
- Keep raw data for at least 30 days
- Archive old processed data periodically
- Clean up exports regularly
- Use compression for large files (gzip, zip)

### Git Ignore
This directory should be in `.gitignore`:
- Data files can be large
- May contain sensitive information
- Can be regenerated from source
- Only commit sample/test data

## Data Retention Policy
- **Raw data**: 30-90 days (can be re-fetched)
- **Processed data**: Keep current season + 2 previous seasons
- **Exports**: Archive important reports, delete temporary files
- **Backups**: Regular database backups stored separately

## Disk Space Management
```bash
# Check directory sizes
du -sh data/*/

# Find large files
find data/ -type f -size +10M

# Clean old files (older than 90 days)
find data/raw/ -type f -mtime +90 -delete

# Compress old data
tar -czf data/archive/2023_data.tar.gz data/processed/2023*
```

## Data Sources
All data originates from:
- NHL API: https://api-web.nhle.com/v1/
- Collected via `src/collectors/` modules
- Stored in database (primary storage)
- Files here are secondary/cache storage
