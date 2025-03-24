import pandas as pd

def compute_rankings(teams):
    df = pd.DataFrame(teams)
    df["score"] = df["wins"] * 10 + df["points_scored"]  # Adjust weighting
    df = df.sort_values(by="score", ascending=False)
    df["rank"] = range(1, len(df) + 1)
    return df

teams = [
    {"name": "AC/DC Back in Black", "wins": 3, "points_scored": 554.2},
    {"name": "Hyde the Blount", "wins": 4, "points_scored": 621.0},
]
print(compute_rankings(teams))