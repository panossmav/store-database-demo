import sqlite3 as sql

conn = sql.connect('database.db')

cursor=conn.cursor()

with open('commands.sql','r') as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()


def add_customer(f_name,l_name,email,phone,vat):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (f_name,l_name,email,phone,vat) VALUES (? , ? , ?, ?, ?)",
        (f_name,l_name,email,phone,vat,))
    conn.commit()
    conn.close()

def delete_customer(phone,email):
    email_server = getEmail(phone)
    if email == email_server:
        conn = sql.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM customers WHERE phone = ?",(phone)
        )
        conn.commit()
        conn.close()
    else:
        print('Error')





def getEmail(phone):
    conn = sql.connect('databse.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT email FROM customers WHERE phone = ?",(phone)
    )
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return None
conn.close()
    