import json

try:
    with open('data_sleeper/info_league.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
except UnicodeDecodeError as e:
    print(f"Error decoding file: {str(e)}")


print(data[0]['owner_id'])

for key, value in data.items():
    if value.get('owner_id') == '123':
        print(f"Found object with owner_id '123' at key: {key}")