import psycopg2
import csv

conn = psycopg2.connect("host=localhost port=5432 dbname=odscourse user=postgres password=secret")
cursor = conn.cursor()

query = """
CREATE TABLE IF NOT EXISTS telecom_churn (
    id SERIAL PRIMARY KEY,
    name VARCHAR,
    sex VARCHAR,
    age REAL,
    height REAL,
    weight REAL,
    team VARCHAR,
    noc VARCHAR,
    games VARCHAR,
    year INTEGER,
    season VARCHAR,
    city VARCHAR,
    sport VARCHAR,
    event VARCHAR,
    medal VARCHAR,
)
"""
cursor.execute(query)
conn.commit()

with open('homework11/athlete_events.csv', 'r') as f:
    reader = csv.reader(f)
    # Skip the header row
    next(reader)
    for Id, row in enumerate(reader):
        cursor.execute(
            "INSERT INTO athlete_events VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
            [Id] + row
        )
conn.commit()

cursor.execute("SELECT * FROM telecom_churn LIMIT 5")
records = cursor.fetchall()
print(records)
