import requests
import json
from datetime import datetime

def fetch_nhl_data(endpoint):
    """Fetch data from the NEW NHL API"""
    base_url = "https://api-web.nhle.com/v1"
    url = f"{base_url}/{endpoint}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def explore_team_roster(team_abbr, season="20242025"):
    """Fetch and display roster for a specific team"""
    print(f"\nFetching {team_abbr} roster for {season} season...")
    data = fetch_nhl_data(f"roster/{team_abbr}/{season}")
    
    if data:
        print(f"\n{team_abbr} Roster:")
        
        if 'forwards' in data:
            print("\n  FORWARDS:")
            for player in data['forwards']:
                name = f"{player['firstName']['default']} {player['lastName']['default']}"
                number = player.get('sweaterNumber', 'N/A')
                pos = player.get('positionCode', 'N/A')
                print(f"  - #{number} {name} ({pos})")
        
        if 'defensemen' in data:
            print("\n  DEFENSEMEN:")
            for player in data['defensemen']:
                name = f"{player['firstName']['default']} {player['lastName']['default']}"
                number = player.get('sweaterNumber', 'N/A')
                pos = player.get('positionCode', 'N/A')
                print(f"  - #{number} {name} ({pos})")
        
        if 'goalies' in data:
            print("\n  GOALIES:")
            for player in data['goalies']:
                name = f"{player['firstName']['default']} {player['lastName']['default']}"
                number = player.get('sweaterNumber', 'N/A')
                print(f"  - #{number} {name}")
    
    return data

def explore_standings():
    """Fetch and display current NHL standings"""
    print("\nFetching current NHL standings...")
    data = fetch_nhl_data("standings/now")
    
    if data and 'standings' in data:
        print("\nNHL Standings:")
        for standing in data['standings'][:10]:  # Show top 10
            team_name = standing.get('teamName', {}).get('default', 'Unknown')
            team_abbr = standing.get('teamAbbrev', {}).get('default', '???')
            wins = standing.get('wins', 0)
            losses = standing.get('losses', 0)
            points = standing.get('points', 0)
            print(f"  {team_abbr:3} - {team_name:25} W:{wins} L:{losses} PTS:{points}")
    
    return data

def explore_schedule_today():
    """Fetch and display today's NHL schedule"""
    today = datetime.now().strftime("%Y-%m-%d")
    print(f"\nFetching NHL schedule for {today}...")
    data = fetch_nhl_data(f"schedule/{today}")
    
    if data and 'gameWeek' in data:
        print("\nToday's NHL Games:")
        for day in data['gameWeek']:
            if day.get('date') == today and 'games' in day:
                for game in day['games']:
                    away = game.get('awayTeam', {}).get('abbrev', 'TBD')
                    home = game.get('homeTeam', {}).get('abbrev', 'TBD')
                    game_state = game.get('gameState', 'UNKNOWN')
                    print(f"  - {away} @ {home} ({game_state})")
                break
        else:
            print("  No games scheduled for today.")
    else:
        print("  No games scheduled for today.")
    
    return data

def explore_player_stats(player_id):
    """Fetch and display player information"""
    print(f"\nFetching player info for ID {player_id}...")
    data = fetch_nhl_data(f"player/{player_id}/landing")
    
    if data:
        if 'firstName' in data and 'lastName' in data:
            name = f"{data['firstName']['default']} {data['lastName']['default']}"
            print(f"\nPlayer: {name}")
            print(f"  Number: #{data.get('sweaterNumber', 'N/A')}")
            print(f"  Position: {data.get('position', 'N/A')}")
            print(f"  Birth Date: {data.get('birthDate', 'N/A')}")
            print(f"  Birth City: {data.get('birthCity', {}).get('default', 'N/A')}")
            
            if 'featuredStats' in data:
                print(f"\n  Featured Stats:")
                for stat_type, stats in data['featuredStats'].items():
                    if isinstance(stats, dict):
                        print(f"    {stat_type}: {stats}")
    
    return data

def explore_club_stats(team_abbr):
    """Fetch and display club statistics"""
    print(f"\nFetching stats for {team_abbr}...")
    data = fetch_nhl_data(f"club-stats/{team_abbr}/now")
    
    if data:
        print(f"\n{team_abbr} Statistics:")
        print(f"  Raw data available - check JSON file for full details")
    
    return data

def save_raw_data(data, filename):
    """Save raw JSON data to a file for inspection"""
    if data:
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"  → Raw data saved to {filename}")

if __name__ == "__main__":
    print("=" * 60)
    print("NHL API Explorer (New API: api-web.nhle.com)")
    print("=" * 60)
    
    # Explore standings
    standings_data = explore_standings()
    save_raw_data(standings_data, "nhl_standings.json")
    
    # Explore roster for Boston Bruins
    roster_data = explore_team_roster("BOS")
    save_raw_data(roster_data, "bruins_roster.json")
    
    # Explore schedule
    schedule_data = explore_schedule_today()
    save_raw_data(schedule_data, "nhl_schedule.json")
    
    # Explore club stats
    club_stats = explore_club_stats("BOS")
    save_raw_data(club_stats, "bruins_stats.json")
    
    # Example: Get player info (using a sample player ID from the roster)
    if roster_data and 'forwards' in roster_data and roster_data['forwards']:
        sample_player_id = roster_data['forwards'][0]['id']
        player_data = explore_player_stats(sample_player_id)
        save_raw_data(player_data, f"player_{sample_player_id}.json")
    
    print("\n" + "=" * 60)
    print("Exploration complete!")
    print("Check the generated JSON files for raw API responses.")
    print("=" * 60)
