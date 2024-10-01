# load libraries and packages
import requests
import json

# Variables
api_key = '7r1zUjsIvyznXu3DXg9KP9CKhJ7P9D0LiW5OUTLU'
url = f"https://api.sportradar.com/nfl/official/trial/v7/en/"
with open('my_roster.json', 'r') as f:
    my_roster = json.load(f)


## Functions
# To bring in data from the API

def get_nfl_schedule(api_key):    
    schedule_url = url + f"games/current_season/schedule.json?api_key={api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(schedule_url, headers=headers)
    return response.json()

#### USECASE: Get a list of all the injuries for all the games this week
def get_nfl_injuries(api_key, season_year = 2024, season_type = "REG", week = 5): 
    # get all injuries for this week
    injuries_url = url + f"seasons/{season_year}/{season_type}/{week}/injuries.json?api_key={api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(injuries_url, headers=headers)
    return response.json()

# Get this weeks games that are scheduled
def get_this_weeks_scheduled_games(api_key, season_year = 2024, season_type = "REG", week = 5):
    this_weeks_scheduled_games_url = url + f"games/{season_year}/{season_type}/{week}/schedule.json?api_key={api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(this_weeks_scheduled_games_url, headers=headers)
    return response.json()

# Who is injured on my team
# Take in a list of players and return there injury status
def get_player_injury_status(api_key, season_year = 2024, season_type = "REG", week = 5, my_roster = my_roster):
        
    return
    
    
# Function to get the ids for players on my roster using the api
def get_player_id(api_key, my_player):
    my_player.first_name
    my_player.last_name
    roster = my_player.team
    roster_url = url + f"teams/{roster}/roster.json?api_key={api_key}"
    headers = {"accept": "application/json"}
    response = requests.get(roster_url, headers=headers)
    return response.json()


# Find ids in injury list
def find_ids_in_injury_list(json_file, ids_to_find):
    with open(json_file, 'r') as f:
        injury_list = json.load(f)

    found_ids = []
    for team in injury_list['teams']:
        for player in team['players']:
            if player['id'] in ids_to_find:
                found_ids.append(player['id'])

    return found_ids
    
    
    
    
