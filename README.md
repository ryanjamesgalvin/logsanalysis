***INTRODUCTION***

This is a program that answers a few questions about the news database, such as who are 
the most popular authors and what are the most popular articles. It uses python to query
a PostgreSQL database.

***Downloading and Running***

Clone or download the files to your computer, then in your terminal inside the virtual machine
(with current directory to the project.py location), type

`psql`

then type

`CREATE VIEW error_log_view AS SELECT date(TIME), round(100.0 * sum(CASE LOG.status WHEN '200 OK' THEN 0 ELSE 1 END) / count(LOG.status), 2) AS "Percent Error" FROM log GROUP BY date(TIME) ORDER BY "Percent Error" DESC;`

to create the SQL view necessary for the third query. Reopen the virtual machine and type:

`python project.py`

to run the program. You should see the programs output in the terminal.