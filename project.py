import psycopg2
conn = psycopg2.connect(dbname="news")
cur = conn.cursor()
cur.execute("""SELECT a.slug, count(a.slug) as count 
               FROM log l JOIN articles a 
               ON l.path = concat('/article/', a.slug) 
               GROUP BY a.slug 
               ORDER BY count DESC 
               LIMIT 3;""")
print("What are the most popular three articles of all time?")
for record in cur:
    print(record)
cur.close()
cur2 = conn.cursor()
cur2.execute("""SELECT a.slug, count(a.slug) as count, au.name 
                FROM articles a JOIN log l ON l.path = concat('/article/', a.slug) 
                JOIN authors au 
                ON au.id = a.author 
                GROUP BY a.slug, au.name 
                ORDER BY count DESC 
                LIMIT 3; """)
print("Who are the most popular article authors of all time? " + "\n")
for record in cur2:
    print(record)
cur2.close()
cur3 = conn.cursor()
cur3.execute("""WITH query3 AS (WITH query1 as 
                (select time, status as s1 
                from log 
                where status ='404 NOT FOUND'), 
                query2 as 
                (select time, status as s2 from log)
                select  q1.time as time, count(s1) / (count(s2)) as ratio 
                from query1 as q1 
                INNER JOIN query2 as q2 
                on q1.time = q2.time
                GROUP BY q1.time)
                SELECT time, ratio
                FROM query3
                WHERE ratio > 0.01
                LIMIT 3;""")
print("On which days did more than 1% of requests lead to errors?")
for record in cur3:
    print(record)
cur3.close()
conn.close()
