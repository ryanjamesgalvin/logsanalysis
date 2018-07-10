#!/usr/bin/env python3
import psycopg2
conn = psycopg2.connect(dbname="news")
cur = conn.cursor()
cur.execute("""SELECT a.title, a.slug, count(a.slug) as count 
               FROM log l JOIN articles a 
               ON l.path = concat('/article/', a.slug) 
               GROUP BY a.slug, a.title 
               ORDER BY count DESC 
               LIMIT 3;""")
print("What are the most popular three articles of all time?" + "\n")
for record in cur:
    print(record[0] + " -- " + str(record[2]) + " views")
cur.close()
cur2 = conn.cursor()
cur2.execute("""SELECT count(l.id) as count, au.name 
                FROM articles a JOIN log l ON l.path = concat('/article/', a.slug) 
                JOIN authors au 
                ON au.id = a.author 
                GROUP BY au.name
                ORDER BY count DESC 
                LIMIT 3; """)
print("Who are the most popular article authors of all time? " + "\n")
for record in cur2:
    print(record[1] + " -- " + str(record[0]) + " views")
cur2.close()
cur3 = conn.cursor()
cur3.execute("""SELECT date
                FROM error_log_view
                WHERE "Percent Error" > 1""")
print("On which days did more than 1% of requests lead to errors?" + "\n")
for record in cur3:
    print(record[0])
cur3.close()
conn.close()
