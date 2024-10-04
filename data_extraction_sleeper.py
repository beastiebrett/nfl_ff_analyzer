import requests
import json

brett_id = '857459411474571264'
league_id = 1115121531081822208

# Get all the rosters in the league
def get_all_rosters(league_id):
    url = f"https://api.sleeper.app/v1/league/{league_id}/rosters"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Failed to retrieve rosters. Status code: {response.status_code}")

# Get all the players on the team with tht owner id = to user_id within the league with league id = to league_id
def get_roster(user_id, league_id):
    user_roster_ids = []
    rosters = get_all_rosters(league_id)
    for roster in rosters:
        if roster['owner_id'] == user_id:
            user_roster_ids = roster['players']
    return user_roster_ids

roster_brett = get_roster(brett_id, league_id)
print(roster_brett)

# rosters = get_all_rosters(league_id)
# print(type(rosters[9]['owner_id']))
# print(type(brett_id))