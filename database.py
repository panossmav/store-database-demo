import sqlite3 as sql
import hashlib
import sys
import os

def resource_path(relative_path):
    """Λήψη σωστού path για PyInstaller ή κανονικό run"""
    try:
        base_path = sys._MEIPASS  # όταν είναι πακεταρισμένο σε .exe
    except AttributeError:
        base_path = os.path.abspath(".")  # όταν τρέχεις ως .py

    return os.path.join(base_path, relative_path)



conn = sql.connect(resource_path('database.db'))

cursor=conn.cursor()

with open(resource_path("commands.sql"), "r") as f:
    sql_script = f.read()
cursor.executescript(sql_script)
conn.commit()

def check_logins(user,password):
    encrypted_pass=hashlib.sha256(password.encode()).hexdigest()
    conn = sql.connect(resource_path('database.db'))
    cursor=conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username=? AND passw=?",(user,encrypted_pass)
    )
    result = cursor.fetchone()

    conn.close()
    if result:
        return True #Correct Credentials
    else:
        return False #Wrong Credentials
    

def check_username(username):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username = ?",(username,)
    )
    res_exist = cursor.fetchone()
    if res_exist:
        return True #USERNAME IS IN DB
    else:
        return False #USERNAME NOT IN DB



def add_customer(f_name,l_name,email,phone,vat):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute("INSERT INTO customers (f_name,l_name,email,phone,vat) VALUES (? , ? , ?, ?, ?)",
        (f_name,l_name,email,phone,vat,))
    conn.commit()
    conn.close()

def delete_customer(phone,email):
    email_server = getEmail(phone)
    if email == email_server:
        conn = sql.connect(resource_path('database.db'))
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM customers WHERE phone = ?",(phone,)
        )
        conn.commit()
        conn.close()
        return True # Success 
    else:
        return False #Not correct combo


def email_check(email):
    conn = sql.connect(resource_path('database.db'))
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

def create_user(username,password):
    password_encrypted = hashlib.sha256(password.encode()).hexdigest()
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO users (username,passw) VALUES (? , ?)",(username,password_encrypted,)
    )
    conn.commit()
    conn.close()
    creation_result = check_username(username)
    if creation_result == True:
        return 'Ο χρήστης προστέθηκε επιτυχώς! \n'
    else:
        return 'Προέκυψε σφάλμα! Δοκιμάστε ξανά! '

def getEmail(phone):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT email FROM customers WHERE phone = ?",(phone,)
    )
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        return None
    
def search_product(sku):
    conn = sql.connect(resource_path('database.db'))
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
    
def delete_user(username,password):
    result = check_logins(username,password)
    if result == True:
        conn = sql.connect(resource_path('database.db'))
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM users WHERE username = ?",(username,)
        )
        conn.commit()
        final_res = check_username(username)
        conn.close()
        if final_res == False:
            return 'Ο χρήστης διαγράφηκε επιτυχώς'
        else:
            return 'Σφάλμα κατά την διαγραφή. Δοκιμάστε ξανά'
    else:
        return 'Ο συνδιασμός Username και Password είναι λάθος!'
        


def create_product(sku,title,price):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO products (sku,product_name,price) VALUES(?, ?, ?)",(sku,title,price)
    )
    conn.commit()
    conn.close()

def check_sku(sku):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM products WHERE sku = ?",(sku,)
    )
    product = cursor.fetchone()
    conn.close()
    return product

def delete_product(sku):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "DELETE FROM products WHERE sku = ?",(sku,)
    )
    conn.commit()
    conn.close()

def phone_check(phone):
    conn = sql.connect(resource_path('database.db'))
    cursor=conn.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE phone = ?",(phone,)
    )
    result=cursor.fetchone()
    conn.close()
    return result

def find_order(order_no):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders WHERE order_no = ?",(order_no,)
    )
    result = cursor.fetchone()
    if result:
        return result
    else:
        return 'Δεν βρέθηκε παραγγελία!'

def create_order(sku,vat):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO orders (prod_sku,customer_vat) VALUES(?, ?)",(sku,vat)
    )
    conn.commit()

def check_vat(vat):
    conn = sql.connect(resource_path('database.db'))
    cursor=conn.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE vat = ?",(vat,)
    )
    search_res = cursor.fetchone()
    conn.close()
    if search_res:
        return True #Υπάρχει πελάτης
    else:
        return False #Δεν υπάρχει πελάτης

def check_sku_order(sku):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM products WHERE sku = ?",(sku,)
    )
    sku_res = cursor.fetchone()
    conn.close()
    if sku_res:
        return True #Υπάρχει προϊόν
    else:
        return False #Δεν υπάρχει προϊόν


def edit_order_status(order,status):
    order_check = find_order(order)
    if order_check == 'Δεν βρέθηκε παραγγελία!':
        return order_check
    else:
        conn = sql.connect(resource_path('database.db'))
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE orders SET order_status = ? WHERE order_no = ?",(status,order)
        )
        conn.commit()
        return 'Έγινε αλλαγή κατάστασης σε %s'%status

def search_client(vat):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM customers WHERE vat = ?",(vat,)
    )
    result = cursor.fetchone()
    if result:
        return result
    else:
        return 'Ο πελάτης με ΑΦΜ %s δεν βρέθηκε'%vat
    
def view_client_orders(vat):
    conn = sql.connect(resource_path('database.db'))
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders WHERE customer_vat = ?",(vat,)
    )
    res = cursor.fetchall()
    if res:
        return res
    else:
        return 'Ο πελάτης δεν έχει κάνει καμία παραγγελία!'

def see_all_orders():
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM orders"
    )
    res = cursor.fetchone()
    if res:
        return res
    else:
        return 'Δεν έχουν γίνει παραγγελίες'


def format_db():
    conn = sql.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM customers")
    cursor.execute("DELETE FROM orders")
    cursor.execute("DELETE FROM products")
    conn.commit()
    conn.close()


def