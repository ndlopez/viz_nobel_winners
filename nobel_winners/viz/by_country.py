#Create a json file for every country
import pandas as pd
df_winners = pd.read_json('github_repo/nobel_winners_cleaned.json')
for name, group in df_winners.groupby('country'):
    group.to_json('data/winners_by_country/' + name + '.json',orient='records')
