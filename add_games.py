import sqlite3
conn=sqlite3.connect('sharpiq.db')
cursor=conn.cursor()
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-06-28','Newcastle','West Tigers',1.44,2.80,1.50,2.90,'home',1.35,3.70)
               ''')
conn.commit()
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-03','Penrith Panthers','South Sydney Rabbitohs',1.77,2.00,1.83,2.15,'home',1.57,2.60)
               ''')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-04','St George Dragons','West Tigers',2.10,1.76,2.36,1.79,'home',2.22,1.73)
               ''')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-04','Brisbane Broncos','Cronulla Sharks',2.47,1.55,2.55,1.55,'away',2.78,1.55)
               ''')
cursor.execute('''
               INSERT INTO games
               (date,home_team,away_team,home_odds,away_odds,best_price_home,best_price_away,result,closing_home,closing_away)
               VALUES('2026-07-05','Parramatta Eels','Manly Sea Eagles',3.04,1.39,3.45,1.41,NULL,NULL,NULL)
               ''')
conn.commit()
print("Parramatta added")
