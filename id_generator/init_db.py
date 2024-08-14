import sqlite3

connection = sqlite3.connect('schema.sql')


#after first run comment it
with open('schema.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()


