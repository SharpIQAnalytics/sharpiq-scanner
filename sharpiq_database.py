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
               closing_away REAL,
               UNIQUE(date,home_team,away_team))
               ''')
conn.commit()
cursor.execute('''
               CREATE TABLE IF NOT EXISTS scans(
               date TEXT,
               home_team TEXT,
               away_team TEXT,
               edge_home REAL,
               edge_away REAL,
               verdict_home TEXT,
               verdict_away TEXT)
               ''')
conn.commit()
cursor.execute('SELECT * FROM scans')
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table'")
for row in cursor.fetchall():
    print(row)
conn.commit()
cursor.execute('''UPDATE games SET closing_home = 1.84,closing_away = 2.16,result ='away' WHERE home_team = 'Dolphins' AND date = '2026-07-11' 
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.69, closing_away = 2.40, result = 'away' WHERE home_team = 'Canterbury Bulldogs' AND date = '2026-07-11'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.33, closing_away = 3.90, result = 'home' WHERE home_team = 'Sydney Roosters' AND date = '2026-07-11'
               ''')
conn.commit()
cursor.execute('SELECT date,home_team,away_team,result,closing_home,closing_away FROM games')
for row in cursor.fetchall():
    print(row)