# NHL API Documentation Reference

This document provides an overview of the NHL API endpoints and their response structures.

## Base URL
```
https://statsapi.web.nhl.com/api/v1/
```

## Endpoints

### 1. Teams
- **Endpoint**: `/teams`
- **Description**: Get all NHL teams
- **Example Response Structure**:
  ```json
  {
    "copyright": "NHL and the NHL Shield are registered trademarks...",
    "teams": [
      {
        "id": 1,
        "name": "New Jersey Devils",
        "link": "/api/v1/teams/1",
        "venue": {
          "name": "Prudential Center",
          "link": "/api/v1/venues/5064",
          "city": "Newark",
          "timeZone": {
            "id": "America/New_York",
            "offset": -4,
            "tz": "EDT"
          }
        },
        "abbreviation": "NJD",
        "teamName": "Devils",
        "locationName": "New Jersey",
        "firstYearOfPlay": "1982",
        "division": {
          "id": 18,
          "name": "Metropolitan",
          "nameShort": "Metro",
          "link": "/api/v1/divisions/18",
          "abbreviation": "M"
        },
        "conference": {
          "id": 6,
          "name": "Eastern",
          "link": "/api/v1/conferences/6"
        },
        "franchise": {
          "franchiseId": 23,
          "teamName": "Devils",
          "link": "/api/v1/franchises/23"
        },
        "shortName": "New Jersey",
        "officialSiteUrl": "http://www.truesport.com",
        "franchiseId": 23,
        "active": true
      },
      // ... more teams
    ]
  }
  ```

### 2. Team Roster
- **Endpoint**: `/teams/{id}/roster`
- **Description**: Get roster for a specific team
- **Example Response Structure**:
  ```json
  {
    "copyright": "NHL and the NHL Shield are registered trademarks...",
    "roster": [
      {
        "person": {
          "id": 8471214,
          "fullName": "Adam Henrique",
          "link": "/api/v1/people/8471214"
        },
        "jerseyNumber": "14",
        "position": {
          "code": "C",
          "name": "Center",
          "type": "Forward",
          "abbreviation": "C"
        }
      },
      // ... more players
    ]
  }
  ```

### 3. Schedule
- **Endpoint**: `/schedule`
- **Parameters**:
  - `startDate`: Start date (YYYY-MM-DD)
  - `endDate`: End date (YYYY-MM-DD)
  - `teamId`: Filter by team ID
- **Example Response Structure**:
  ```json
  {
    "copyright": "NHL and the NHL Shield are registered trademarks...",
    "totalItems": 1,
    "totalEvents": 0,
    "totalGames": 1,
    "totalMatches": 0,
    "metaData": {
      "timeStamp": "20180205_221544"
    },
    "dates": [
      {
        "date": "2018-02-06",
        "totalItems": 1,
        "totalEvents": 0,
        "totalGames": 1,
        "totalMatches": 0,
        "games": [
          {
            "gamePk": 2017020851,
            "link": "/api/v1/game/2017020851/feed/live",
            "gameType": "R",
            "season": "20172018",
            "gameDate": "2018-02-06T00:30:00Z",
            "status": {
              "abstractGameState": "Final",
              "codedGameState": "7",
              "detailedState": "Final",
              "statusCode": "7",
              "startTimeTBD": false
            },
            "teams": {
              "away": {
                "leagueRecord": {
                  "wins": 26,
                  "losses": 18,
                  "ot": 6,
                  "type": "league"
                },
                "score": 1,
                "team": {
                  "id": 22,
                  "name": "Edmonton Oilers",
                  "link": "/api/v1/teams/22"
                }
              },
              "home": {
                "leagueRecord": {
                  "wins": 26,
                  "losses": 17,
                  "ot": 5,
                  "type": "league"
                },
                "score": 0,
                "team": {
                  "id": 54,
                  "name": "Vegas Golden Knights",
                  "link": "/api/v1/teams/54"
                }
              }
            },
            "venue": {
              "name": "T-Mobile Arena",
              "link": "/api/v1/venues/null"
            },
            "content": {
              "link": "/api/v1/game/2017020851/content"
            }
          }
        ],
        "events": [],
        "matches": []
      }
    ]
  }
  ```

### 4. Player Information
- **Endpoint**: `/people/{id}`
- **Description**: Get detailed information about a specific player
- **Example Response Structure**:
  ```json
  {
    "copyright": "NHL and the NHL Shield are registered trademarks...",
    "people": [
      {
        "id": 8471214,
        "fullName": "Adam Henrique",
        "link": "/api/v1/people/8471214",
        "firstName": "Adam",
        "lastName": "Henrique",
        "primaryNumber": "14",
        "birthDate": "1990-02-06",
        "currentAge": 28,
        "birthCity": "Brantford",
        "birthStateProvince": "ON",
        "birthCountry": "CAN",
        "nationality": "CAN",
        "height": "6' 0\"",
        "weight": 195,
        "active": true,
        "alternateCaptain": false,
        "captain": false,
        "rookie": false,
        "shootsCatches": "L",
        "rosterStatus": "Y",
        "currentTeam": {
          "id": 1,
          "name": "New Jersey Devils",
          "link": "/api/v1/teams/1"
        },
        "primaryPosition": {
          "code": "C",
          "name": "Center",
          "type": "Forward",
          "abbreviation": "C"
        }
      }
    ]
  }
  ```

### 5. Team Statistics
- **Endpoint**: `/teams/{id}/stats`
- **Description**: Get statistics for a specific team
- **Example Response Structure**:
  ```json
  {
    "copyright": "NHL and the NHL Shield are registered trademarks...",
    "stats": [
      {
        "type": {
          "displayName": "statsSingleSeason"
        },
        "splits": [
          {
            "stat": {
              "gamesPlayed": 82,
              "wins": 44,
              "losses": 29,
              "ot": 9,
              "pts": 97,
              "ptPctg": "59.1",
              "goalsPerGame": 3.15,
              "goalsAgainstPerGame": 2.68,
              "evGGARatio": 1.03,
              "powerPlayPercentage": "21.4",
              "powerPlayGoals": 53.0,
              "powerPlayGoalsAgainst": 49.0,
              "powerPlayOpportunities": 247.0,
              "penaltyKillPercentage": "81.8",
              "shotsPerGame": 33.3,
              "shotsAllowed": 31.0,
              "winScoreFirst": 0.674,
              "winOppScoreFirst": 0.357,
              "winLeadFirstPer": 0.75,
              "winLeadSecondPer": 0.886,
              "winOutshootOpp": 0.6,
              "winOutshotByOpp": 0.511,
              "faceOffsTaken": 4832.0,
              "faceOffsWon": 2244.0,
              "faceOffsLost": 2588.0,
              "faceOffWinPercentage": 46.4,
              "shootingPctg": 9.5,
              "savePctg": 0.913
            },
            "team": {
              "id": 1,
              "name": "New Jersey Devils",
              "link": "/api/v1/teams/1"
            }
          }
        ]
      }
    ]
  }
  ```

## Rate Limiting
- The NHL API is generally rate-limited
- It's recommended to implement appropriate delays between requests
- Consider caching responses when possible

## Error Handling
- 404: Resource not found
- 403: Forbidden (rate limiting)
- 500: Server error

## Notes
- The NHL API is a RESTful service that returns JSON
- All dates and times are in UTC
- Team and player IDs are consistent across all endpoints
- Some endpoints may require additional parameters for specific data

## Example Usage

### Python Example
```python
import requests

def get_team_roster(team_id):
    url = f"https://statsapi.web.nhl.com/api/v1/teams/{team_id}/roster"
    response = requests.get(url)
    return response.json()

def get_player_stats(player_id):
    url = f"https://statsapi.web.nhl.com/api/v1/people/{player_id}/stats?stats=statsSingleSeason&season=20222023"
    response = requests.get(url)
    return response.json()
```
