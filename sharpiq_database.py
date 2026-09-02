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
try:
    cursor.execute('ALTER TABLE games ADD COLUMN kickoff_utc TEXT')
    conn.commit()
except:
    pass
try:
    cursor.execute('ALTER TABLE games ADD COLUMN best_home_bookmaker TEXT')
    cursor.execute('ALTER TABLE games ADD COLUMN best_away_bookmaker TEXT')
    conn.commit()
except:
    pass
try:
    cursor.execute('ALTER TABLE games ADD COLUMN clv_home REAL')
    cursor.execute('ALTER TABLE games ADD COLUMN clv_away REAL')
    conn.commit()
except:
    pass
try:
    cursor.execute('ALTER TABLE games ADD COLUMN pinnacle_home REAL')
    cursor.execute('ALTER TABLE games ADD COLUMN pinnacle_away REAL')
    conn.commit()
except:
    pass
try:
    cursor.execute('ALTER TABLE games ADD COLUMN betfair_home REAL')
    cursor.execute('ALTER TABLE games ADD COLUMN betfair_away REAL')
    conn.commit()
except:
    pass
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
cursor.execute('DELETE FROM scans')
conn.commit()
try:
    cursor.execute('ALTER TABLE scans ADD COLUMN best_price_home REAL')
    cursor.execute('ALTER TABLE scans ADD COLUMN best_price_away REAL')
    conn.commit()
except:
    pass
cursor.execute('CREATE UNIQUE INDEX IF NOT EXISTS idx_scans_unique ON scans(date, home_team, away_team) ')
conn.commit()
cursor.execute('SELECT * FROM scans')
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT name FROM sqlite_master WHERE type ='table'")
for row in cursor.fetchall():
    print(row)
conn.commit()
cursor.execute('''UPDATE games SET closing_home = 1.35,closing_away = 3.70,result = 'home' WHERE home_team = 'Newcastle' AND date = '2026-06-28'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.57,closing_away = 2.60,result = 'home' WHERE home_team = 'Penrith Panthers' AND date = '2026-07-03'
               ''')
cursor.execute('''UPDATE games SET closing_home = 2.22,closing_away = 1.73,result = 'home' WHERE home_team = 'St George Dragons'AND date = '2026-07-04'
               ''')
cursor.execute('''UPDATE games SET closing_home = 2.78,closing_away = 1.55,result = 'away' WHERE home_team = 'Brisbane Broncos' AND date = '2026-07-04'
               ''')
cursor.execute('''UPDATE games SET closing_home = 3.85,closing_away = 1.33, result = 'home' WHERE home_team = 'Parramatta Eels' AND date = '2026-07-05'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.83,closing_away = 1.92, result = 'home' WHERE home_team = 'Newcastle Knights' AND date = '2026-07-05'
               ''')
cursor.execute('''UPDATE games SET closing_home = 3.29,closing_away = 1.39,result = 'away' WHERE home_team = 'Wests Tigers' AND date = '2026-07-10'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.84,closing_away = 2.16,result = 'away' WHERE home_team = 'Dolphins' AND date = '2026-07-11'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.69,closing_away = 2.40,result = 'away' WHERE home_team = 'Canterbury Bulldogs' AND date = '2026-07-11'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.33,closing_away = 3.90,result = 'home' WHERE home_team = 'Sydney Roosters' AND date = '2026-07-11'
               ''')
cursor.execute('''UPDATE games SET closing_home = 2.25,closing_away = 1.78,result = 'home' WHERE home_team = 'South Sydney Rabbitohs' AND date = '2026-07-12'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.50,closing_away = 2.88,result = 'away' WHERE home_team = 'Manly Warringah Sea Eagles' AND date = '2026-07-12'
               ''')
cursor.execute('''UPDATE games SET closing_home = 1.34,closing_away = 3.60,result = 'home' WHERE home_team = 'Melbourne Storm' AND date = '2026-07-12'
               ''')
cursor.execute('''UPDATE games SET closing_home = 3.60,result = 'away' WHERE home_team = 'Newcastle Knights' AND date = '2026-07-24'
               ''')
cursor.execute('''UPDATE games SET closing_home = 2.00,closing_away = 1.90,result = 'home' WHERE home_team = 'South Sydney Rabbitohs' AND date = '2026-07-24'
               ''' )
cursor.execute('''UPDATE games SET closing_home = 1.18,closing_away = 5.60, result ='home' WHERE home_team = 'Canberra Raiders' AND date = '2026-07-25'
               ''')
cursor.execute('''UPDATE games SET clv_home = 0.0138 WHERE home_team = 'Newcastle Knights' AND date = '2026-07-24'
               ''')
cursor.execute('''UPDATE games SET clv_home = 0, clv_away = 0 WHERE home_team = 'South Sydney Rabbitohs' AND date = '2026-07-24'
               ''')
cursor.execute('''UPDATE games SET clv_home = 0.0169, clv_away = 0.0535 WHERE home_team = 'Canberra Raiders' AND date = '2026-07-25'
               ''')
cursor.execute('''UPDATE games SET closing_home = 2.58,closing_away = 1.62,result = 'away' WHERE home_team = 'North Queensland Cowboys' AND date = '2026-07-30'
               ''')
cursor.execute('''UPDATE games SET closing_home = 5.50,closing_away = 1.18, result = 'away' WHERE home_team = 'St George Illawarra Dragons' AND date = '2026-07-31'
               ''')
cursor.execute('''UPDATE games SET closing_home = 3.40,closing_away = 1.36, result = 'away' WHERE home_team = 'Melbourne Storm' AND date = '2026-07-31'
               ''')
conn.commit()
cursor.execute("UPDATE games SET result='home', clv_home=0.0256, clv_away=-0.0173 WHERE home_team='New Zealand Warriors' AND date='2026-08-07'")
cursor.execute("UPDATE games SET result='home', clv_home=0.0132, clv_away=-0.0345 WHERE home_team='Sydney Roosters' AND date='2026-08-07'")
cursor.execute("UPDATE games SET result='home', clv_home=0.0227, clv_away=-0.1026 WHERE home_team='South Sydney Rabbitohs' AND date='2026-08-08'")
cursor.execute("UPDATE games SET result='home', clv_home=-0.1875, clv_away=0.0177 WHERE home_team='St George Illawarra Dragons' AND date='2026-08-09'")
conn.commit()
cursor.execute("SELECT date,home_team,away_team,best_price_home,best_price_away,closing_home,closing_away FROM games WHERE closing_home IS NOT NULL AND clv_home IS NULL")
columns=['date','home_team','away_team','best_price_home','best_price_away','closing_home','closing_away']
games=[dict(zip(columns,row))for row in cursor.fetchall()]
for game in games:
    clv_home=round((game['best_price_home']/game['closing_home'])-1,4)
    clv_away=round((game['best_price_away']/game['closing_away'])-1,4)
    cursor.execute("UPDATE games SET clv_home=?,clv_away=? WHERE date=? AND home_team=?",(clv_home,clv_away,game['date'],game['home_team']))
conn.commit()
cursor.execute('SELECT date,home_team,away_team,result,closing_home,closing_away,clv_home,clv_away FROM games')
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT date,home_team,away_team,best_price_home,best_price_away,closing_home,closing_away,clv_home,clv_away FROM games WHERE clv_home IS NOT NULL")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT home_team,away_team,best_price_home,best_price_away FROM games WHERE date='2026-07-30' AND home_team='North Queensland Cowboys'")
for row in cursor.fetchall():
    print(row)
cursor.execute("SELECT home_team,away_team,best_price_home,best_home_bookmaker,best_price_away,best_away_bookmaker FROM games WHERE date = '2026-08-01'")
for row in cursor.fetchall():
    print(row)    
cursor.execute("SELECT date,home_team,away_team,result,clv_home,clv_away FROM games WHERE clv_home IS NOT NULL ORDER BY date")
for row in cursor.fetchall():
    print(row)