import pandas as pd
data=[
    {'home_team':'Canberra Raiders','away_team':'St George Dragons','home_odds':1.34,'away_odds':3.30,'best_price_home':1.35,'best_price_away':3.35},
    {'home_team':'South Sydney','away_team':'Parramatta','home_odds':1.58,'away_odds':2.55,'best_price_home':1.58,'best_price_away':2.55},
    {'home_team':'Gold Coast','away_team':'Canterbury','home_odds':1.91,'away_odds':1.93,'best_price_home':1.94,'best_price_away':1.97},
    {'home_team':'Brisbane','away_team':'Sydney Roosters','home_odds':2.74,'away_odds':1.46,'best_price_home':2.92,'best_price_away':1.50},
    {'home_team':'Dolphins','away_team':'NZ Warriors','home_odds':1.45,'away_odds':2.78,'best_price_home':1.48,'best_price_away':2.96},
    {'home_team':'Cowboys','away_team':'Penrith','home_odds':4.00,'away_odds':1.26,'best_price_home':4.35,'best_price_away':1.27},
    {'home_team':'Manly','away_team':'Melbourne','home_odds':1.50,'away_odds':2.63,'best_price_home':1.53,'best_price_away':2.60},
    {'home_team':'Newcastle','away_team':'West Tigers','home_odds':1.44,'away_odds':2.80,'best_price_home':1.50,'best_price_away':2.90}   
]
df=pd.DataFrame(data)
print(df)
df['total']=1/df['home_odds']+1/df['away_odds']
print(df)
df['fair_home']=df['home_odds']*df['total']
df['fair_away']=df['away_odds']*df['total']
print(df)
df['edge_home']=df['best_price_home']/df['fair_home']-1
df['edge_away']=df['best_price_away']/df['fair_away']-1
print(df)
print(df[df['edge_home']>0][['home_team','edge_home']])
print(df[df['edge_away']>0][['away_team','edge_away']])
df.to_csv('sharpiq_results.csv')