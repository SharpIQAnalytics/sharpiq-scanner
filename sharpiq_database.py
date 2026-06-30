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
    closing_away REAL
)
''')
cursor.execute('''
INSERT INTO games(date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-06-28','Newcastle','West Tigers',1.44,2.80,1.50,2.90,'home',1.35,3.70)''')
conn.commit()
