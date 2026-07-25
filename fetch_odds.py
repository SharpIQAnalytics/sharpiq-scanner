import sqlite3
import requests
import config
from datetime import datetime,timezone,timedelta
conn = sqlite3.connect('sharpiq.db')
cursor = conn.cursor()
print(datetime.now())
url ="https://api.the-odds-api.com/v4/sports/rugbyleague_nrl/odds"
params={
    "apiKey":config.ODDS_API_KEY,
    "regions":"au",
    "markets":"h2h",
}
response=requests.get(url,params=params)
games=response.json()
print(len(games))
for game in games:
    print(game['home_team'],game['away_team'],game['commence_time'])
    date=datetime.strptime(game['commence_time'],'%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d')
    kickoff_time=datetime.strptime(game['commence_time'],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    kickoff_utc=kickoff_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    print(kickoff_time-datetime.now(timezone.utc))
    if kickoff_time-datetime.now(timezone.utc)>timedelta(hours=3):
        print("Too early to scan reliably")
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
                    INSERT INTO games
                    (date,kickoff_utc,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away)
                    VALUES(?,?,?,?,?,?,?,?) 
                    ON CONFLICT(date,home_team,away_team)
                    DO UPDATE SET
                    kickoff_utc=excluded.kickoff_utc,home_odds=excluded.home_odds,away_odds=excluded.away_odds,best_price_home=excluded.best_price_home,best_price_away=excluded.best_price_away
                   ''',
                    (date,kickoff_utc,game['home_team'],game['away_team'],sportsbet_home,sportsbet_away,best_home,best_away))
conn.commit()
print("Games updated")