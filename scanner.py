from datetime import datetime,timezone,timedelta
from colorama import Fore,Style,init
init()
import sqlite3
conn=sqlite3.connect('sharpiq.db')
cursor=conn.cursor()
cursor.execute('''
    DELETE FROM scans 
    WHERE (home_team, away_team, date) IN (SELECT home_team, away_team, date FROM games WHERE result IS NULL)
    ''')
conn.commit()
cursor.execute('SELECT kickoff_utc,home_team,away_team,betfair_home,betfair_away,best_price_home,best_price_away FROM games WHERE result IS NULL')
columns=['kickoff_utc','home_team','away_team','betfair_home','betfair_away','best_price_home','best_price_away']
games=[dict(zip(columns,row))for row in cursor.fetchall()]
for game in games:
    if game['kickoff_utc']is None:
        print("NO kickoff time recorded for",game['home_team'],"vs",game['away_team'])
        continue
    kickoff_time=datetime.strptime(game['kickoff_utc'],'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    if kickoff_time-datetime.now(timezone.utc)>timedelta(hours=3):
        print("too early to scan reliably-",game['home_team'],"vs",game['away_team'])
    elif kickoff_time-datetime.now(timezone.utc) < timedelta(0):
        print("game already started, skipping-", game['home_team'],"vs",game['away_team'])
    else:
        if game ['betfair_home']is None or game['betfair_away']is None:
            print("No live odds available for",game['home_team'],"vs",game['away_team'])
            continue
        print(game['home_team'],"best_price",Fore.BLUE+str(game['best_price_home'])+Style.RESET_ALL,"|",game['away_team'],"best_price:",Fore.BLUE+str(game['best_price_away'])+Style.RESET_ALL)
        total=1/game['betfair_home']+1/game['betfair_away']
        fair_home=game['betfair_home']*total
        fair_away=game['betfair_away']*total
        edge_home=game['best_price_home']/fair_home-1
        edge_away=game['best_price_away']/fair_away-1
        if edge_home>0.04:
            verdict_home = "VALUE"
            color_home=Fore.GREEN
        else:
            verdict_home = "SKIP"
            color_home=Fore.YELLOW
        if  edge_away>0.04:
            verdict_away = "VALUE"
            color_away=Fore.GREEN
        else:
            verdict_away = "SKIP"
            color_away=Fore.YELLOW
        if  edge_home>0:
             edge_color_home=Fore.GREEN
        else:
             edge_color_home=Fore.RED
        if edge_away>0:
             edge_color_away=Fore.GREEN
        else:
             edge_color_away=Fore.RED

        cursor.execute('''
               INSERT INTO scans
               (date,home_team,away_team,best_price_home,best_price_away,edge_home,edge_away,verdict_home,verdict_away)
               VALUES(?,?,?,?,?,?,?,?,?)
               ON CONFLICT(date,home_team,away_team)
               DO UPDATE SET
               best_price_home=excluded.best_price_home,best_price_away=excluded.best_price_away,edge_home=excluded.edge_home,edge_away=excluded.edge_away, verdict_home=excluded.verdict_home,verdict_away=excluded.verdict_away
               ''',(datetime.now().strftime('%Y-%m-%d'),game['home_team'],game['away_team'],game['best_price_home'],game['best_price_away'],round(edge_home,4),round(edge_away,4),verdict_home,verdict_away))
        print(game['home_team'],edge_color_home+str(round(edge_home*100,2))+Style.RESET_ALL,color_home+verdict_home+Style.RESET_ALL,'|',game['away_team'],edge_color_away+str(round(edge_away*100,2))+Style.RESET_ALL,color_away+verdict_away+Style.RESET_ALL)
        conn.commit()