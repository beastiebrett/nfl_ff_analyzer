import requests
import json

# Set API endpoints and IDs
LEAGUE_ID = 1115121531081822208
BRETTS_ID = 857459411474571264
YEAR = 2024

# Get all league info for a user for a year
url = f"https://api.sleeper.app/v1/user/{BRETTS_ID}/leagues/nfl/{YEAR}"
response = requests.get(url)
print(f"API Response Status Code: {response.status_code}")
print(f"API Response Headers: {response.headers}")
with open(f'{BRETTS_ID}_league_info.json', 'w') as f:
    json.dump(response.json(), f)
    print(f"League info saved to {BRETTS_ID}_league_info.json")

# Get all rosters of a league
url = f"https://api.sleeper.app/v1/league/{LEAGUE_ID}/rosters"
response = requests.get(url)
print(f"API Response Status Code: {response.status_code}")
print(f"API Response Headers: {response.headers}")
with open(f'{LEAGUE_ID}_rosters.json', 'w') as f:
    json.dump(response.json(), f)
    print(f"Rosters saved to {LEAGUE_ID}_rosters.json")

# Get all player data
url = "https://api.sleeper.app/v1/players/nfl"
response = requests.get(url)
print(f"API Response Status Code: {response.status_code}")
print(f"API Response Headers: {response.headers}")
with open('all_nfl_players.json', 'w') as f:
    json.dump(response.json(), f)
    print(f"Player data saved to all_nfl_players.json")

print("Data fetching complete!")