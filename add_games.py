import sqlite3
conn=sqlite3.connect('sharpiq.db')
cursor=conn.cursor()
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-12','Melbourne Storm','Gold Coast Titans',1.36,3.12,1.37,3.45,NULL,NULL,NULL)
               ''')
conn.commit()
print("Melbourne Storm")