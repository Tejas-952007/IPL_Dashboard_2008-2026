import pandas as pd
matches = pd.read_csv('matches.csv')
matches_sorted = matches.copy()
matches_sorted['date'] = pd.to_datetime(matches_sorted['date'])
matches_sorted = matches_sorted.sort_values('date')
champions = matches_sorted.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']]
title_counts = champions['winner'].value_counts().reset_index()
print(champions)
print(title_counts)
