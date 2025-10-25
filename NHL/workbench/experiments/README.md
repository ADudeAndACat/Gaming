# NHL API Experiments

This directory contains experiments and exploration tools for working with the NHL API.

## 🎯 Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the API explorer:**
   ```bash
   python test_nhl_api.py
   ```

3. **View the generated JSON files** to see raw API responses

## 📂 Files

### Scripts
- **`test_nhl_api.py`** - Main script to explore NHL API endpoints
  - Fetches current standings
  - Gets team rosters
  - Retrieves today's schedule
  - Pulls player statistics
  - Saves all raw JSON responses for inspection

### Documentation
- **`NEW_NHL_API_ENDPOINTS.md`** - Comprehensive reference of working NHL API endpoints
  - Base URL: `https://api-web.nhle.com/v1/`
  - Lists all tested and working endpoints
  - Includes data structure documentation
  - Team abbreviations reference
  - Usage examples

- **`nhl_api_documentation.md`** - Legacy documentation (old API)
  - Historical reference for the deprecated `statsapi.web.nhl.com` API
  - Kept for reference purposes

### Configuration
- **`requirements.txt`** - Python dependencies (just `requests` for now)

## 🔍 What You Can Explore

### Current Working Endpoints

1. **Standings** - `/standings/now`
   - Current NHL standings with team records

2. **Team Roster** - `/roster/{TEAM}/{SEASON}`
   - Complete roster by position (forwards, defensemen, goalies)
   - Player details including stats, physical attributes, birth info

3. **Schedule** - `/schedule/{DATE}`
   - Daily game schedules with teams, times, venues

4. **Player Info** - `/player/{PLAYER_ID}/landing`
   - Comprehensive player data
   - Current season and career statistics
   - Draft information
   - Season-by-season breakdown

5. **Club Stats** - `/club-stats/{TEAM}/now`
   - Team performance metrics

## 📊 Generated JSON Files

When you run `test_nhl_api.py`, it creates these files:

- `nhl_standings.json` - Complete NHL standings (~78KB)
- `bruins_roster.json` - Boston Bruins roster example (~12KB)
- `nhl_schedule.json` - Today's game schedule (~160KB)
- `bruins_stats.json` - Boston Bruins statistics (~16KB)
- `player_{PLAYER_ID}.json` - Individual player data (~17KB)

These files contain the **raw JSON responses** from the API, perfect for:
- Understanding the data structure
- Planning your application's data model
- Testing and development
- Offline work

## 🚀 Next Steps

Based on the API exploration, you can:

1. **Build a Statistics Tracker**
   - Track player performance across seasons
   - Compare players and teams
   - Visualize trends

2. **Create a Schedule App**
   - Display upcoming games
   - Show live scores
   - Team schedules and calendars

3. **Develop a Fantasy Hockey Tool**
   - Player rankings and projections
   - Performance analytics
   - Trade suggestions

4. **Make a Roster Management System**
   - Team depth charts
   - Player comparisons
   - Draft analysis

## 💡 Usage Examples

### Get Current Standings
```python
from test_nhl_api import fetch_nhl_data

standings = fetch_nhl_data("standings/now")
for team in standings['standings'][:5]:
    print(f"{team['teamAbbrev']['default']}: {team['points']} pts")
```

### Get Team Roster
```python
roster = fetch_nhl_data("roster/TOR/20242025")
print(f"Found {len(roster['forwards'])} forwards")
print(f"Found {len(roster['defensemen'])} defensemen")
print(f"Found {len(roster['goalies'])} goalies")
```

### Get Today's Games
```python
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")
schedule = fetch_nhl_data(f"schedule/{today}")
```

## 📝 Notes

### API Changes
- **Old API** (`statsapi.web.nhl.com`) - DEPRECATED and no longer accessible
- **New API** (`api-web.nhle.com`) - Current and actively maintained
- The new API has a different structure and endpoints

### Data Structure
- Many text fields include language variants (e.g., `.default`, `.fr`)
- Player and team IDs are consistent across endpoints
- Seasons are formatted as 8-digit numbers (e.g., `20242025`)
- Dates use ISO format (`YYYY-MM-DD`)

### Rate Limiting
- The API uses Cloudflare caching
- Be respectful with request frequency
- Consider caching responses locally

## 🔗 Resources

- **API Base URL:** https://api-web.nhle.com/v1/
- **Team Abbreviations:** See `NEW_NHL_API_ENDPOINTS.md` for complete list
- **NHL Official Site:** https://www.nhl.com/

---

**Created:** 2025-10-24
**Status:** ✅ Functional and ready for development
