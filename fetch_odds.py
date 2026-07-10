import sqlite3
import requests
import config
from datetime import datetime
conn = sqlite3.connect('sharpiq.db')
cursor = conn.cursor()
url ="https://api.the-odds-api.com/v4/sports/rugbyleague_nrl/odds"
params={
    "apiKey":config.ODDS_API_KEY,
    "regions":"au",
    "markets":"h2h",
}
response=requests.get(url,params=params)
games=response.json()
for game in games:
    date=datetime.strptime(game['commence_time'],'%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
    best_home = 0
    best_away = 0
    sportsbet_home = 0
    sportsbet_away = 0
    for bookmaker in game['bookmakers']:
        if bookmaker['key']=='sportsbet':
            for market in bookmaker['markets']:
                if market['key']=='h2h':
                    for outcome in market['outcomes']:
                        if outcome['name']==game['home_team']:
                            sportsbet_home = outcome['price']
                        if outcome['name']==game['away_team']:
                            sportsbet_away = outcome['price']
        for market in bookmaker['markets']:
            if market['key']=='h2h':
                for outcome in market['outcomes']:
                    if outcome['name']==game['home_team']:
                        if outcome['price']>best_home:
                            best_home=outcome['price']
                    if outcome['name']==game['away_team']:
                        if outcome['price']>best_away:
                            best_away=outcome['price']
cursor.execute('''
                   INSERT OR IGNORE INTO games
                   (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away)
                   VALUES(?,?,?,?,?,?,?)''',
                   (date,game['home_team'],game['away_team'],sportsbet_home,sportsbet_away,best_home,best_away))
conn.commit()
print("Games updated")