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
        return 1
    else:
        return 0


def email_check(email):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE email = ?",(email,)
    )
    email_server = cursor.fetchone()
    conn.close()
    if email_server:
        return True
    else:
        return False



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
    
def search_product(sku):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM products WHERE sku=?", (sku,)
    )
    product = cursor.fetchone()
    conn.close()
    if product:
        return product
    else:
        product = 'Product not found!'
        return product
    

def create_product(sku,title,price):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (sku,product_name,price) VALUES(?, ?, ?)",(sku,title,price)
    )
    conn.commit()
    conn.close()

def check_sku(sku):
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM products WHERE sku = ?",(sku,)
    )
    product = cursor.fetchone()
    conn.close()
    return product

conn.close()
    