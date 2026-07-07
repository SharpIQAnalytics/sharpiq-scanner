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
cursor.execute('DELETE FROM games WHERE home_team = "Wests Tigers" AND rowid NOT IN (SELECT MIN(rowid)FROM games WHERE home_team = "Wests Tigers")')
conn.commit()
cursor.execute('SELECT * FROM scans')
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table'")
for row in cursor.fetchall():
    print(row)
cursor.execute('SELECT home_team,away_team,result,closing_home,closing_away FROM games')
for row in cursor.fetchall():
    print(row)