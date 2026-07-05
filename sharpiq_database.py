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
conn.commit()
cursor.execute('''
               UPDATE games
               SET result = 'home',closing_home = 1.83,closing_away = 1.92 WHERE home_team = "Newcastle Knights"
               ''')
conn.commit()
cursor.execute('SELECT home_team,away_team,result,closing_home,closing_away FROM games')
for row in cursor.fetchall():
    print(row)