import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_sample_data():
    print("Generating sample IPL data (2008-2026)...")
    np.random.seed(42)
    random.seed(42)

    seasons = list(range(2008, 2027))
    teams = [
        "Mumbai Indians", "Chennai Super Kings", "Royal Challengers Bengaluru", 
        "Kolkata Knight Riders", "Rajasthan Royals", "Delhi Capitals", 
        "Punjab Kings", "Sunrisers Hyderabad", "Gujarat Titans", "Lucknow Super Giants"
    ]
    venues = ["Wankhede Stadium", "M. Chinnaswamy Stadium", "Eden Gardens", "Chepauk", "Arun Jaitley Stadium", "Narendra Modi Stadium"]

    matches = []
    deliveries = []

    match_id = 1
    for season in seasons:
        # Simulate ~60 matches per season
        num_matches = 60 if season < 2022 else 74
        for i in range(num_matches):
            team1, team2 = random.sample(teams, 2)
            toss_winner = random.choice([team1, team2])
            toss_decision = random.choice(["bat", "field"])
            winner = random.choice([team1, team2])
            win_by_runs = random.randint(0, 50) if winner == team1 else 0
            win_by_wickets = random.randint(0, 10) if winner == team2 else 0
            player_of_match = f"Player_{random.randint(1, 100)}"
            venue = random.choice(venues)
            
            matches.append({
                "id": match_id,
                "season": season,
                "city": venue.split()[0],
                "date": f"{season}-04-{random.randint(1, 30):02d}",
                "team1": team1,
                "team2": team2,
                "toss_winner": toss_winner,
                "toss_decision": toss_decision,
                "result": "normal",
                "dl_applied": 0,
                "winner": winner,
                "win_by_runs": win_by_runs,
                "win_by_wickets": win_by_wickets,
                "player_of_match": player_of_match,
                "venue": venue
            })
            
            # Simulate a few deliveries per match for aggregate stats
            # Instead of 240 balls, let's do 120 per inning to keep it fast but realistic
            for inning, batting_team, bowling_team in [(1, team1, team2), (2, team2, team1)]:
                for over in range(1, 21):
                    for ball in range(1, 7):
                        batsman = f"Player_{random.randint(1, 50)}"
                        bowler = f"Player_{random.randint(51, 100)}"
                        batsman_runs = random.choices([0, 1, 2, 3, 4, 6], weights=[40, 30, 10, 2, 12, 6])[0]
                        extra_runs = random.choices([0, 1], weights=[95, 5])[0]
                        total_runs = batsman_runs + extra_runs
                        is_wicket = random.choices([0, 1], weights=[95, 5])[0]
                        dismissal_kind = random.choice(["caught", "bowled", "lbw", "run out"]) if is_wicket else np.nan
                        
                        deliveries.append({
                            "match_id": match_id,
                            "inning": inning,
                            "batting_team": batting_team,
                            "bowling_team": bowling_team,
                            "over": over,
                            "ball": ball,
                            "batsman": batsman,
                            "non_striker": f"Player_{random.randint(1, 50)}",
                            "bowler": bowler,
                            "is_super_over": 0,
                            "wide_runs": extra_runs if random.random() < 0.5 else 0,
                            "bye_runs": 0,
                            "legbye_runs": 0,
                            "noball_runs": extra_runs if random.random() >= 0.5 else 0,
                            "penalty_runs": 0,
                            "batsman_runs": batsman_runs,
                            "extra_runs": extra_runs,
                            "total_runs": total_runs,
                            "player_dismissed": batsman if is_wicket else np.nan,
                            "dismissal_kind": dismissal_kind,
                            "fielder": f"Player_{random.randint(1, 50)}" if dismissal_kind == "caught" else np.nan
                        })
            match_id += 1

    df_matches = pd.DataFrame(matches)
    df_deliveries = pd.DataFrame(deliveries)

    df_matches.to_csv("matches.csv", index=False)
    df_deliveries.to_csv("deliveries.csv", index=False)
    print("Sample datasets created: matches.csv and deliveries.csv")

if __name__ == "__main__":
    generate_sample_data()
