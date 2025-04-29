import requests
import json

brett_id = '857459411474571264'
league_id = 1115121531081822208

# Get all the rosters in the league

# Get all the players on the team with tht owner id = to user_id within the league with league id = to league_id
def compile_rosters():
    # Load in data from data/1115121531081822208_rosters.json
    with open('data/1115121531081822208_rosters.json', 'r') as f:
        roster_data = json.load(f)
    for i in roster_data:
        user_roster_ids = roster['players']
    return user_roster_ids

def get_player_info(player_id):
    

roster_brett = get_roster(brett_id, league_id)
print(roster_brett)

# rosters = get_all_rosters(league_id)
# print(type(rosters[9]['owner_id']))
# print(type(brett_id))

