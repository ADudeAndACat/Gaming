# New NHL API Endpoints (api-web.nhle.com)

**Base URL:** `https://api-web.nhle.com/v1/`

This document lists the working endpoints discovered through testing on 2025-10-24.

## ✅ Working Endpoints

### 1. **Standings**
```
GET /standings/now
```
**Returns:** Current NHL standings with team records, points, wins, losses, etc.

**Key Fields:**
- `standings[]` - Array of team standings
  - `teamName.default` - Full team name
  - `teamAbbrev.default` - Team abbreviation
  - `wins`, `losses`, `otLosses` - Record stats
  - `points` - Total points
  - `gamesPlayed` - Games played
  - `goalDifferential` - Goal differential

### 2. **Team Roster**
```
GET /roster/{TEAM_ABBR}/{SEASON}
```
**Parameters:**
- `TEAM_ABBR` - Team abbreviation (e.g., "BOS", "TOR", "MTL")
- `SEASON` - Season in format YYYYYYYY (e.g., "20242025")

**Returns:** Complete team roster organized by position

**Key Fields:**
- `forwards[]` - Array of forward players
- `defensemen[]` - Array of defensemen
- `goalies[]` - Array of goalies

**Player Object Fields:**
- `id` - Unique player ID
- `firstName.default`, `lastName.default` - Player name
- `sweaterNumber` - Jersey number
- `positionCode` - Position (C, L, R, D, G)
- `shootsCatches` - L or R
- `heightInInches`, `heightInCentimeters` - Height
- `weightInPounds`, `weightInKilograms` - Weight
- `birthDate`, `birthCity`, `birthCountry` - Birth info
- `headshot` - URL to player headshot image

### 3. **Roster Seasons**
```
GET /roster-season/{TEAM_ABBR}
```
**Returns:** Array of seasons available for a team (e.g., [19241925, 19251926, ...])

### 4. **Schedule**
```
GET /schedule/{DATE}
```
**Parameters:**
- `DATE` - Date in YYYY-MM-DD format

**Returns:** Game schedule for the specified date

**Key Fields:**
- `gameWeek[]` - Array of days
  - `date` - Date string
  - `games[]` - Array of games
    - `id` - Game ID
    - `season` - Season ID
    - `gameType` - Game type (2 = Regular season, 3 = Playoffs)
    - `gameDate` - ISO datetime
    - `gameState` - Game state (FUT, LIVE, FINAL, OFF)
    - `awayTeam.abbrev` - Away team abbreviation
    - `homeTeam.abbrev` - Home team abbreviation
    - `awayTeam.score` - Away team score
    - `homeTeam.score` - Home team score
    - `venue.default` - Venue name

### 5. **Player Information**
```
GET /player/{PLAYER_ID}/landing
```
**Parameters:**
- `PLAYER_ID` - Unique player ID (e.g., 8481556)

**Returns:** Comprehensive player information and statistics

**Key Fields:**
- `playerId` - Player ID
- `firstName.default`, `lastName.default` - Player name
- `currentTeamId`, `currentTeamAbbrev` - Current team
- `sweaterNumber` - Jersey number
- `position` - Position
- `headshot` - Headshot URL
- `heroImage` - Action shot URL
- `birthDate`, `birthCity`, `birthCountry` - Birth info
- `draftDetails` - Draft information
  - `year`, `round`, `pickInRound`, `overallPick`
- `featuredStats.regularSeason` - Current season stats
  - `subSeason` - Current season stats
    - `gamesPlayed`, `goals`, `assists`, `points`
    - `plusMinus`, `pim`, `shots`
    - `powerPlayGoals`, `powerPlayPoints`
    - `shorthandedGoals`, `shorthandedPoints`
    - `shootingPctg`
  - `career` - Career totals
- `careerTotals` - Comprehensive career statistics
- `seasonTotals[]` - Season-by-season breakdown

### 6. **Club Statistics**
```
GET /club-stats/{TEAM_ABBR}/now
```
**Parameters:**
- `TEAM_ABBR` - Team abbreviation

**Returns:** Current team statistics

**Note:** This endpoint returns a redirect (307) to a season-specific URL. The actual data includes detailed team performance metrics.

## 📝 Team Abbreviations

Common team abbreviations:
- **ANA** - Anaheim Ducks
- **BOS** - Boston Bruins
- **BUF** - Buffalo Sabres
- **CAR** - Carolina Hurricanes
- **CGY** - Calgary Flames
- **CBJ** - Columbus Blue Jackets
- **CHI** - Chicago Blackhawks
- **COL** - Colorado Avalanche
- **DAL** - Dallas Stars
- **DET** - Detroit Red Wings
- **EDM** - Edmonton Oilers
- **FLA** - Florida Panthers
- **LAK** - Los Angeles Kings
- **MIN** - Minnesota Wild
- **MTL** - Montréal Canadiens
- **NJD** - New Jersey Devils
- **NSH** - Nashville Predators
- **NYI** - New York Islanders
- **NYR** - New York Rangers
- **OTT** - Ottawa Senators
- **PHI** - Philadelphia Flyers
- **PIT** - Pittsburgh Penguins
- **SJS** - San Jose Sharks
- **SEA** - Seattle Kraken
- **STL** - St. Louis Blues
- **TBL** - Tampa Bay Lightning
- **TOR** - Toronto Maple Leafs
- **UTA** - Utah Mammoth
- **VAN** - Vancouver Canucks
- **VGK** - Vegas Golden Knights
- **WPG** - Winnipeg Jets
- **WSH** - Washington Capitals

## 🔍 Endpoint Patterns to Explore

Based on the API structure, these endpoints likely exist:

### Potential Endpoints (Not Yet Tested)
- `/game/{GAME_ID}/boxscore` - Game boxscore
- `/game/{GAME_ID}/landing` - Game summary
- `/game/{GAME_ID}/play-by-play` - Play-by-play data
- `/stats/rest/en/skater/summary` - Skater statistics
- `/stats/rest/en/goalie/summary` - Goalie statistics
- `/playoff-bracket/{SEASON}` - Playoff bracket
- `/draft/{YEAR}` - Draft information
- `/network/tv-schedule/{DATE}` - TV schedule

## 💡 Usage Tips

1. **Rate Limiting:** The API appears to use Cloudflare caching with TTL values. Be respectful with request frequency.

2. **Internationalization:** Many text fields have language variants (e.g., `.default`, `.fr`, `.cs`, `.fi`, `.sk`).

3. **Image URLs:** The API provides URLs to player headshots, action shots, and team logos.

4. **Season Format:** Seasons are represented as 8-digit numbers combining start and end years (e.g., 20242025).

5. **Error Handling:** The API returns standard HTTP status codes. Some endpoints use 307 redirects.

## 📊 Example Usage

### Python Example
```python
import requests

# Get current standings
response = requests.get("https://api-web.nhle.com/v1/standings/now")
standings = response.json()

# Get team roster
response = requests.get("https://api-web.nhle.com/v1/roster/BOS/20242025")
roster = response.json()

# Get player info
response = requests.get("https://api-web.nhle.com/v1/player/8481556/landing")
player = response.json()

# Get today's schedule
from datetime import datetime
today = datetime.now().strftime("%Y-%m-%d")
response = requests.get(f"https://api-web.nhle.com/v1/schedule/{today}")
schedule = response.json()
```

## 📁 Generated Files

Running `test_nhl_api.py` creates these JSON files:
- `nhl_standings.json` - Current standings
- `bruins_roster.json` - Boston Bruins roster (example)
- `nhl_schedule.json` - Today's schedule
- `bruins_stats.json` - Boston Bruins statistics (example)
- `player_{PLAYER_ID}.json` - Individual player data

## 🔗 Related Resources

- Old API: `https://statsapi.web.nhl.com/api/v1/` (DEPRECATED - No longer accessible)
- New API: `https://api-web.nhle.com/v1/` (CURRENT)

---

**Last Updated:** 2025-10-24
**Status:** ✅ Functional and tested
