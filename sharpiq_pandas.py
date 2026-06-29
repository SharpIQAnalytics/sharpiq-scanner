import pandas as pd
df=pd.read_csv('games.csv')

df['total']=1/df['home_odds']+1/df['away_odds']

df['fair_home']=df['home_odds']*df['total']
df['fair_away']=df['away_odds']*df['total']

df['edge_home']=df['best_price_home']/df['fair_home']-1
df['edge_away']=df['best_price_away']/df['fair_away']-1

print(df[df['edge_home']>0][['home_team','edge_home']])
print(df[df['edge_away']>0][['away_team','edge_away']])
print(df.sort_values('edge_home',ascending=False)[['home_team','edge_home']])
print(df.sort_values('edge_away',ascending=False)[['away_team','edge_away']])      
      
df.to_csv('sharpiq_results.csv')
