import sqlite3 as sql

conn = sql.connect('database.db')

cursor=conn.cursor()

with open('commands.sql','r') as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()


def add_users(name,age,dob,email):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute( "INSERT INTO users (name,age,dob,email) VALUES(?, ?, ?, ?)",
    (name,age,dob,email)

    )
    conn.commit()
    conn.close()

conn.close()
    