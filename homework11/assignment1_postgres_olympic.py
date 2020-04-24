import psycopg2
from tabulate import tabulate

conn = psycopg2.connect("host=192.168.99.100 port=5432 dbname=odscourse user=postgres password=secret")
cursor = conn.cursor()

"""
1. How old were the youngest male and female participants of the 1996 Olympics?

— 16 and 15
— *14 and 12*
— 16 and 12
— 13 and 11
"""

cursor.execute("SELECT MIN(age) FROM athlete_event WHERE age > 0 and sex = 'M' and year = 1996")
print("Question 1: youngest male participant: {}".format(cursor.fetchall()), end=', ')
cursor.execute("SELECT MIN(age) FROM athlete_event WHERE age > 0 and sex = 'F' and year = 1996")
print("youngest female participant: {}".format(cursor.fetchall()))


"""
2. What was the percentage of male gymnasts among all the male participants of the 2000 Olympics? Round the answer to the first decimal.

Hint: here and further if needed drop duplicated sportsmen to count only unique ones.

— 0.2
— *1.5*
— 2.5
— 7.7
"""

cursor.execute("SELECT ROUND((SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE sex = 'M' and sport = 'Gymnastics' and year = '2000')::numeric / (SELECT COUNT (DISTINCT athlete_id) FROM athlete_event WHERE sex = 'M' and year = '2000')::numeric*100, 1)")
print("Question 2: percentage = {}".format(cursor.fetchall()))


"""
3. What are the mean and standard deviation of height for female basketball players participated in the 2000 Olympics? Round the answer to the first decimal.

— 178.5 and 7.2
— 179.4 and 10
— 180.7 and 6.7
— *182.4 and 9.1*
"""

cursor.execute("SELECT ROUND((SELECT AVG(height) FROM athlete_event WHERE sex = 'F' and sport = 'Basketball' and year = 2000)::numeric, 1)")
print("Question 3: mean deviation = {}".format(cursor.fetchall()), end=', ')
cursor.execute("SELECT ROUND((SELECT STDDEV(height) FROM athlete_event WHERE sex = 'F' and sport = 'Basketball' and year = 2000)::numeric, 1)")
print("standard deviation = {}".format(cursor.fetchall()))


"""
4. Find a sportsperson participated in the 2002 Olympics, with the highest weight among other participants of the same Olympics. What sport did he or she do?

— Judo
— *Bobsleigh*
— Weightlifting
— Boxing
"""

cursor.execute("SELECT sport FROM athlete_event WHERE weight = (SELECT MAX(weight) FROM athlete_event WHERE year = 2002) and year = 2002")
print("Question 4: sport: {}".format(cursor.fetchall()))


"""
5. How many times did Pawe Abratkiewicz participate in the Olympics held in different years?

— 0
— 1
— 2
— *3*
"""

cursor.execute("SELECT COUNT(DISTINCT year) FROM athlete_event WHERE name = 'Pawe Abratkiewicz'")
print("Question 5: times = {}".format(cursor.fetchall()))


"""
6. How many silver medals in tennis did Australia win at the 2000 Olympics?

— 0
— 1
— *2*
— 3
"""

cursor.execute("SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE medal = 'Silver' and sport = 'Tennis' and year = 2000 and team = 'Australia'")
print("Question 6: medals = {}".format(cursor.fetchall()))


"""
7. Is it true that Switzerland won fewer medals than Serbia at the 2016 Olympics? Do not consider NaN values in Medal column.

— *Yes*
— No
"""

cursor.execute("SELECT CASE WHEN (SELECT COUNT(medal) FROM athlete_event WHERE team = 'Switzerland' and year = 2016 and medal <> '0') < (SELECT COUNT(medal) FROM athlete_event WHERE team = 'Serbia' and year = 2016 and medal <> '0') THEN 'Yes' ELSE 'No' END")
print("Question 7: {}".format(cursor.fetchall()))


"""
8. What age category did the fewest and the most participants of the 2014 Olympics belong to?

— *[45-55] and [25-35) correspondingly*
— [45-55] and [15-25) correspondingly
— [35-45] and [25-35) correspondingly
— [45-55] and [35-45) correspondingly
"""

cursor.execute("""
    CREATE TABLE temp (
        age varchar,
        fewest integer,
        most integer
    );
    INSERT INTO temp (age, most) VALUES ('15-25', (SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE year = 2014 and age >= 15 and age < 25));
    INSERT INTO temp (age, most) VALUES ('25-35', (SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE year = 2014 and age >= 25 and age < 35));
    INSERT INTO temp (age, fewest, most) VALUES ('35-45', (SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE year = 2014 and age >= 35 and age <= 45), (SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE year = 2014 and age >= 35 and age < 45));
    INSERT INTO temp (age, fewest) VALUES ('45-55', (SELECT COUNT(DISTINCT athlete_id) FROM athlete_event WHERE year = 2014 and age >= 45 and age <= 55));
    SELECT age FROM temp WHERE fewest = (SELECT MIN(fewest) FROM temp);
""")
print("Question 8: fewest participants: {}".format(cursor.fetchall()), end=", ")
cursor.execute("SELECT age FROM temp WHERE most = (SELECT MAX(most) FROM temp)")
print("most participants: {}".format(cursor.fetchall()))

"""
9. Is it true that there were Summer Olympics held in Lake Placid? Is it true that there were Winter Olympics held in Sankt Moritz?

— Yes, Yes
— Yes, No
— *No, Yes*
— No, No
"""

cursor.execute("SELECT CASE WHEN (SELECT COUNT(city) FROM athlete_event WHERE city = 'Lake Placid' and season = 'Summer') = 0 THEN 'No' ELSE 'Yes' END")
print("Question 9: {}".format(cursor.fetchall()), end=', ')
cursor.execute("SELECT CASE WHEN (SELECT COUNT(city) FROM athlete_event WHERE city = 'Sankt Moritz' and season = 'Winter') = 0 THEN 'No' ELSE 'Yes' END")
print("{}".format(cursor.fetchall()))


"""
10. What is the absolute difference between the number of unique sports at the 1995 Olympics and 2016 Olympics?

— 16
— 24
— 26
— *34*
"""

cursor.execute("SELECT ABS((SELECT COUNT(DISTINCT sport) FROM athlete_event WHERE year = 1995) - (SELECT COUNT(DISTINCT sport) FROM athlete_event WHERE year = 2016))")
print("Question 10: difference = {}".format(cursor.fetchall()))