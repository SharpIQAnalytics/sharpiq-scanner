import sqlite3
conn = sqlite3.connect('sharpiq.db')
cursor = conn.cursor()
cursor.execute("UPDATE games SET clv_home=-0.0185, clv_away=0.0140 WHERE home_team='Parramatta Eels' AND date='2026-08-30'")
conn.commit()
print("Updated")