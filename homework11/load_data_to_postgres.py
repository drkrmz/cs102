import psycopg2
import csv

conn = psycopg2.connect("host=192.168.99.100 port=5432 dbname=odscourse user=postgres password=secret")
cursor = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS athlete_event (
   id SERIAL PRIMARY KEY,
   athlete_id INTEGER,
   name VARCHAR,
   sex VARCHAR,
    age INTEGER,
    height INTEGER,
    weight INTEGER,
    team VARCHAR,
    noc VARCHAR,
    games VARCHAR,
    year INTEGER,
    season VARCHAR,
    city VARCHAR,
   sport VARCHAR,
   event VARCHAR,
   medal VARCHAR
)
"""
cursor.execute(query)
conn.commit()

with open('homework11/athlete_events.csv', 'r') as f:
   reader = csv.reader(f)
     #Skip the header row
   next(reader)
   for Id, row in enumerate(reader):
       for i in range(len(row)):
           if row[i] == 'NA':
               row[i] = 0
       cursor.execute(
           "INSERT INTO athlete_event (id, athlete_id, name, sex, age, height, weight, team, noc, games, year, season, city, sport, event, medal) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
           [Id] + row
        )
conn.commit()