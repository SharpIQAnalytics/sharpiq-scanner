import sqlite3
conn=sqlite3.connect('sharpiq.db')
cursor=conn.cursor()
cursor.execute(''' 
               CREATE TABLE IF NOT EXISTS games(
               date TEXT,
               home_team TEXT,
               away_team TEXT,
               home_odds REAL,
               away_odds REAL,
               best_price_home REAL,
               best_price_away REAL,
               result TEXT,
               closing_home REAL,
               closing_away REAL)
               ''')
cursor.execute('DELETE FROM games')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-06-28','Newcastle','West Tigers',1.44,2.80,1.50,2.90,'home',1.35,3.70)
               ''')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-03','Penrith Panthers','South Sydney Rabbitohs',1.77,2.00,1.83,2.15,NULL,NULL,NULL)
               ''')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-04','Brisbane Broncos','Cronulla Sharks',2.47,1.55,2.55,1.55,NULL,NULL,NULL)
               ''')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-05','Parramatta Eels','Manly Warringah',1.35,3.20,1.40,3.22,NULL,NULL,NULL)
               ''')
cursor.execute('''
                INSERT INTO games
                (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
                VALUES('2026-07-05','Newcastle Knights','Dolphins',2.19,1.65,2.30,1.70,NULL,NULL,NULL)
                ''')
conn.commit()
cursor.execute('''
               UPDATE games
               SET result = NULL,closing_home = NULL,closing_away = NULL
               WHERE home_team = "Penrith Panthers"
               ''')
conn.commit()
cursor.execute('SELECT home_team,away_team,date,home_odds FROM games ORDER BY date ASC,home_odds DESC')
cursor.execute('SELECT COUNT (*) FROM games WHERE result IS NULL')
for row in cursor.fetchall():
    print(row)