from datetime import datetime,timezone,timedelta
import sqlite3
conn=sqlite3.connect('sharpiq.db')
cursor=conn.cursor()
cursor.execute('DELETE FROM scans')
conn.commit()
cursor.execute('SELECT kickoff_utc,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away FROM games WHERE result IS NULL')
columns=['kickoff_utc','home_team','away_team','home_odds','away_odds','best_price_home','best_price_away']
games=[dict(zip(columns,row))for row in cursor.fetchall()]
for game in games:
    if game['kickoff_utc']is None:
        print("NO kickoff time recorded for",game['home_team'],"vs",game['away_team'])
        continue
    kickoff_time=datetime.strptime(game['kickoff_utc'],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    if kickoff_time-datetime.now(timezone.utc)>timedelta(hours=3):
        print("too early to scan reliably-",game['home_team'],"vs",game['away_team'])
    else:
        total=1/game['home_odds']+1/game['away_odds']
        fair_home=game['home_odds']*total
        fair_away=game['away_odds']*total
        edge_home=game['best_price_home']/fair_home-1
        edge_away=game['best_price_away']/fair_away-1
        if edge_home>0.04:
            verdict_home = "VALUE"
        else:
            verdict_home = "SKIP"
        if  edge_away>0.04:
            verdict_away = "VALUE"
        else:
            verdict_away = "SKIP"
        cursor.execute('''
               INSERT INTO scans
               (date,home_team,away_team,edge_home,edge_away,verdict_home,verdict_away)
               VALUES(?,?,?,?,?,?,?)
               ''',(datetime.now().strftime('%Y-%m-%d'),game['home_team'],game['away_team'],round(edge_home,4),round(edge_away,4),verdict_home,verdict_away))
        print(game['home_team'],round(edge_home*100,2),verdict_home,'|',game['away_team'],round(edge_away*100,2),verdict_away)
        conn.commit()