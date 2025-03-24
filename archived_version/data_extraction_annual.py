# load libraries and packages
import requests
import json

# Variables
api_key = '7r1zUjsIvyznXu3DXg9KP9CKhJ7P9D0LiW5OUTLU'
url = f"https://api.sportradar.com/nfl/official/trial/v7/en/"


## Functions
# To bring in data from the API every year
# Get the schedule
def get_nfl_schedule(api_key, season_year, season_type):    
    schedule_url = url + f"games/{season_year}/{season_type}/schedule.json"
    headers = {'accept': 'application/json'}
    params = {'api_key': api_key}
    response = requests.get(schedule_url, headers=headers, params=params)
    return response.json()

# GEt the nfl teams
def get_nfl_teams(api_key):
    teams_url = url + f"league/teams.json"
    headers = {'accept': 'application/json'}
    params = {'api_key': api_key}
    response = requests.get(teams_url, headers=headers, params=params)
    return response.json()

def populate_local_database():

    # Get the schedule
    schedule = get_nfl_schedule(api_key, 2024, "REG")
    print(schedule)

    # GEt the nfl teams
    teams = get_nfl_teams(api_key)
    print(teams)

    # populate local database  
    with open('annual_data/teams.json', 'w') as f:
        json.dump(teams, f)
        
    with open('annual_data/schedule.json', 'w') as f:
        json.dump(schedule, f)
    return

if __name__ == '__main__':
    populate_local_database()
