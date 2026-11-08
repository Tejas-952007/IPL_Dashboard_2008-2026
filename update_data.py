import urllib.request
import zipfile
import io
import json
import pandas as pd
import os
from datetime import datetime

def download_and_process_cricsheet_data():
    print("Downloading Cricsheet IPL JSON data (This might take a minute)...")
    url = "https://cricsheet.org/downloads/ipl_json.zip"
    
    # Download the zip file
    try:
        response = urllib.request.urlopen(url)
        z = zipfile.ZipFile(io.BytesIO(response.read()))
    except Exception as e:
        print(f"Error downloading data: {e}")
        return

    print("Download complete. Processing JSON files...")
    
    matches_list = []
    deliveries_list = []
    
    # Iterate through each file in the zip
    for filename in z.namelist():
        if not filename.endswith('.json'):
            continue
            
        with z.open(filename) as f:
            try:
                data = json.load(f)
            except:
                continue
                
        info = data.get('info', {})
        match_id = filename.split('.')[0]
        
        season = info.get('season', 'Unknown')
        city = info.get('city', 'Unknown')
        dates = info.get('dates', [])
        date = dates[0] if dates else 'Unknown'
        match_type = info.get('match_type', 'Unknown')
        player_of_match = info.get('player_of_match', [''])[0] if info.get('player_of_match') else ''
        venue = info.get('venue', 'Unknown')
        teams = info.get('teams', ['', ''])
        team1 = teams[0] if len(teams) > 0 else ''
        team2 = teams[1] if len(teams) > 1 else ''
        
        toss = info.get('toss', {})
        toss_winner = toss.get('winner', '')
        toss_decision = toss.get('decision', '')
        
        outcome = info.get('outcome', {})
        winner = outcome.get('winner', '')
        result = outcome.get('result', '')
        by = outcome.get('by', {})
        result_margin = by.get('runs', by.get('wickets', ''))
        
        method = outcome.get('method', '')
        
        officials = info.get('registry', {}).get('people', {})
        # Note: Extracting umpires is tricky from registry, usually umpires are in info.officials
        umpires = info.get('officials', {}).get('umpires', [])
        umpire1 = umpires[0] if len(umpires) > 0 else ''
        umpire2 = umpires[1] if len(umpires) > 1 else ''
        
        matches_list.append({
            'id': match_id,
            'season': season,
            'city': city,
            'date': date,
            'match_type': match_type,
            'player_of_match': player_of_match,
            'venue': venue,
            'team1': team1,
            'team2': team2,
            'toss_winner': toss_winner,
            'toss_decision': toss_decision,
            'winner': winner,
            'result': result,
            'result_margin': result_margin,
            'target_runs': '', # target runs not trivially available in all json
            'target_overs': '',
            'super_over': 'Y' if 'super_over' in outcome else 'N',
            'method': method,
            'umpire1': umpire1,
            'umpire2': umpire2
        })
        
        # Process deliveries
        innings = data.get('innings', [])
        for inning_idx, inning_data in enumerate(innings):
            inning_num = inning_idx + 1
            batting_team = inning_data.get('team', '')
            bowling_team = team2 if batting_team == team1 else team1 # Approximation
            
            overs = inning_data.get('overs', [])
            for over_data in overs:
                over_num = over_data.get('over', 0)
                for ball_idx, delivery in enumerate(over_data.get('deliveries', [])):
                    ball_num = ball_idx + 1
                    
                    batter = delivery.get('batter', '')
                    bowler = delivery.get('bowler', '')
                    non_striker = delivery.get('non_striker', '')
                    
                    runs = delivery.get('runs', {})
                    batsman_runs = runs.get('batter', 0)
                    extra_runs = runs.get('extras', 0)
                    total_runs = runs.get('total', 0)
                    
                    extras = delivery.get('extras', {})
                    extras_type = next(iter(extras.keys())) if extras else ''
                    
                    wickets = delivery.get('wickets', [])
                    is_wicket = 1 if wickets else 0
                    
                    player_dismissed = ''
                    dismissal_kind = ''
                    fielder = ''
                    
                    if wickets:
                        wicket = wickets[0]
                        player_dismissed = wicket.get('player_out', '')
                        dismissal_kind = wicket.get('kind', '')
                        fielders = wicket.get('fielders', [])
                        if fielders:
                            fielder = fielders[0].get('name', '')
                            
                    deliveries_list.append({
                        'match_id': match_id,
                        'inning': inning_num,
                        'batting_team': batting_team,
                        'bowling_team': bowling_team,
                        'over': over_num,
                        'ball': ball_num,
                        'batter': batter,
                        'bowler': bowler,
                        'non_striker': non_striker,
                        'batsman_runs': batsman_runs,
                        'extra_runs': extra_runs,
                        'total_runs': total_runs,
                        'extras_type': extras_type,
                        'is_wicket': is_wicket,
                        'player_dismissed': player_dismissed,
                        'dismissal_kind': dismissal_kind,
                        'fielder': fielder
                    })

    print("Data processing complete. Saving to CSV...")
    
    matches_df = pd.DataFrame(matches_list)
    deliveries_df = pd.DataFrame(deliveries_list)
    
    matches_df.to_csv('matches.csv', index=False)
    deliveries_df.to_csv('deliveries.csv', index=False)
    
    print(f"Saved {len(matches_df)} matches and {len(deliveries_df)} deliveries.")
    print("Update complete! You can now run your dashboard.")

if __name__ == "__main__":
    download_and_process_cricsheet_data()
