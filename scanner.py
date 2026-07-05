games=[
{'home_team':'Canberra Raiders','away_team':'St George Dragons','home_odds':1.32,'away_odds':3.80,'best_price_home':1.32,'best_price_away':3.80},
{'home_team':'South Sydney','away_team':'Parramatta','home_odds':1.58,'away_odds':2.55,'best_price_home':1.58,'best_price_away':2.55},
{'home_team':'Canterbury', 'away_team':'Gold Coast', 'home_odds':1.93,'away_odds':1.97,'best_price_home':1.93,'best_price_away':1.97},
{'home_team':'Sydney Roosters','away_team':'Brisbane','home_odds':1.50,'away_odds':2.70,'best_price_home':1.50,'best_price_away':2.70},
{'home_team':'NZ Warriors','away_team':'Dolphins','home_odds':2.78,'away_odds':1.49,'best_price_home':2.78,'best_price_away':1.49},
{'home_team':'Penrith','away_team':'Cowboys','home_odds':1.31,'away_odds':4.35,'best_price_home':1.31,'best_price_away':4.35},
{'home_team':'Melbourne','away_team':'Manly','home_odds':2.66,'away_odds':1.53,'best_price_home':2.66,'best_price_away':1.53},
{'home_team':'West Tigers','away_team':'Newcastle','home_odds':2.90,'away_odds':1.50,'best_price_home':2.90,'best_price_away':1.50}

]

for game in games:    
  total=1/game['home_odds']+1/game['away_odds']
  fair_home=game['home_odds']*total
  fair_away=game['away_odds']*total
  edge_home=game['best_price_home']/fair_home-1
  edge_away=game['best_price_away']/fair_away-1
  if edge_home>0.04:
      print(game['home_team'],("VALUE"))
  else:
      print(game['home_team'],("SKIP"))
  if edge_away>0.04:
      print(game['away_team'], ("VALUE"))
  else:
      print(game['away_team'],("SKIP"))
  print(game['home_team'],round(fair_home,2),'|',game['away_team'],
 round(fair_away,2))
 