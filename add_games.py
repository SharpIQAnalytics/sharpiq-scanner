import sqlite3
conn=sqlite3.connect('sharpiq.db')
cursor=conn.cursor()
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-05','Newcastle Knights','Dolphins',2.05,1.82,2.10,1.88,NULL,NULL,NULL)
               ''')
conn.commit()
print("Newcastle added")