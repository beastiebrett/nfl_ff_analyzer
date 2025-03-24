import openai

openai.api_key = "your_api_key"

def generate_commentary(team_name, performance):
    prompt = f"Write a sarcastic, funny power ranking summary for {team_name}, who has {performance}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

print(generate_commentary("Flat Earth Globetrotters", "a 3-2 record and shaky lineup choices"))
