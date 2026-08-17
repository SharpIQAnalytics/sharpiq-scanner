import sqlite3
conn = sqlite3.connect('sharpiq.db')
cursor = conn.cursor()
cursor.execute("UPDATE games SET clv_home=-0.0256, clv_away=0.0149 WHERE home_team='Wests Tigers' AND date='2026-08-16'")
conn.commit()
print("Updated")