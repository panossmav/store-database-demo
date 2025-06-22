from tkinter import *
import tkinter as tk
from database import *
def clear_app():
    for widgets in app.winfo_children():
        widgets.pack_forget()


app = tk.Tk() #GUI APP START
app.title('Συνδεθείτε')
app.minsize(600,400)
tk.Label(app,text="Enter username \n").pack()
user_e = Entry(app)
user_e.pack()
tk.Label(app,text="Enter password \n").pack()
passw_e = Entry(app,show='*')
passw_e.pack()


def login():
    global user
    user = user_e.get()
    password = passw_e.get()
    final = check_logins(user,password)
    if final == True: #Start of main product
        app.title('Πληροφορίες βάσης')
        clear_app()
        home()
    else:
        tk.Label(app,text='Wrong Credentials! \n').pack()



def new_customer():
    clear_app()
    tk.Label(app,text='Προσθήκη πελάτη \n \n').pack()
    tk.Label(app,text='Όνομα πελάτη:').pack()
    f_name_e = Entry(app)
    f_name_e.pack()
    tk.Label(app,text='Επίθετο πελάτη:').pack()
    l_name_e = Entry(app)
    l_name_e.pack()
    tk.Label(app,text='Email πελάτη:').pack()
    email_e = Entry(app)
    email_e.pack()
    tk.Label(app,text='Τηλέφωνο πελάτη:').pack()
    phone_e = Entry(app)
    phone_e.pack()
    tk.Label(app,text='ΑΦΜ πελάτη:').pack()
    vat_e = Entry(app)
    vat_e.pack()
    def new_customer_sbt():
        f_name = f_name_e.get()
        l_name = l_name_e.get()
        email = email_e.get()
        phone = int(phone_e.get())
        vat = int(vat_e.get())
        if '@' not in email:
            tk.Label(app,text='Σφάλμα! Ελέγξτε τα στοιχεία σας και δοκιμαστε ξανα').pack()
        else:
            if email_check(email) == True:
                tk.Label(app,text='Το email χρησιμποιείται ήδη! Δοκιμάστε ξανά \n').pack()
            else:
                add_customer(f_name,l_name,email,phone,vat)
                tk.Label(app,text='Ο πελάτης αποθηκεύτηκε! ').pack()
    tk.Button(app,text='Προσθήκη',command=new_customer_sbt).pack()
         
def remove_customer():
    clear_app()
    tk.Label(app,text='Δώσε email').pack()
    email_e = Entry(app)
    email_e.pack()
    tk.Label(app,text='Δώσε τηλέφωνο').pack()
    phone_e = Entry(app)
    phone_e.pack()
    def remove_customer_sbt():
        email = email_e.get()
        phone = int(phone_e.get())
        result = delete_customer(phone,email)
        if result == True:
            tk.Label(app,text='Ο πελάτης διαγράφηκε!').pack()
        else:
            tk.Label(app,text='Σφάλμα!')
    tk.Button(app,text='Διαγραφή',command=remove_customer_sbt).pack()
       
def find_products():
    clear_app()
    tk.Label(app,text='Δώσε SKU\n').pack()
    sku_e = Entry(app)
    sku_e.pack()
    def search_product_sbt():
        sku = int(sku_e.get())
        result = search_product(sku)
        var = tk.StringVar(value=result)
        tk.Label(app,textvariable=var).pack()

    tk.Button(app,text='Αναζήτηση',command=search_product_sbt).pack()

def new_product():
    clear_app()
    tk.Label(app,text='Δώσε Τίτλο προϊόντος \n').pack()
    title_e = Entry(app)
    title_e.pack()
    tk.Label(app,text='Δώσε SKU').pack()
    sku_e = Entry(app)
    sku_e.pack()
    tk.Label(app,text='Δώσε τιμή').pack()
    price_e = Entry(app)
    price_e.pack()
    def new_product_sbt():
        title = title_e.get()
        sku = int(sku_e.get())
        price = float(price_e.get())
        product = check_sku(sku)
        if not product: #No other product with this SKU
            create_product(sku,title,price)
            tk.Label(app,text='Το προϊόν {} προστέθηκε'.format(title)).pack()
        else:
            exist_product = product
            tk.Label(app,text='Ο κωδικός ανήκει στο: {} '.format(exist_product)).pack()
    tk.Button(app,text='Προσθήκη',command=new_product_sbt).pack()

def remove_product():
    clear_app()
    tk.Label(app,text='Δώσε SKU').pack()
    sku_e = Entry(app)
    sku_e.pack()
    def remove_product_sbt():
        sku = int(sku_e.get())
        result = check_sku(sku)
        if result:
            delete_product(sku)
            tk.Label(app,text='Διαγράφηκε επιτυχώς!').pack()
        else:
            tk.Label(app,text='Δεν υπάρχει προϊόν με αυτόν τον κωδικό').pack()
    tk.Button(app,text='Διαγραφή',command=remove_product_sbt).pack()

def new_user():
    clear_app()
    tk.Label(app,text='Δώσε username \n').pack()
    user_e = Entry(app)
    user_e.pack()
    tk.Label(app,text='Δώσε κωδικό \n').pack()
    passw_e = Entry(app,show='*')
    passw_e.pack()
    def new_user_sbt():
        user = user_e.get()
        passw = passw_e.get()
        if check_username(user) == True:
            tk.Label(app,text='Υπάρχει χρήστης με αυτό το όνομα \n').pack()
        else:
            creation_user = create_user(user,passw)
            var = tk.StringVar(value=creation_user)
            tk.Label(app,textvariable=var).pack()
    tk.Button(app,text='Προσθήκη',command=new_user_sbt).pack()

def remove_user():
    clear_app()
    tk.Label(app,text='Δώσε username\n').pack()
    user_e = Entry(app)
    user_e.pack()
    tk.Label(app,text='Δώσε password \n').pack()
    passw_e = Entry(app,show='*')
    passw_e.pack()
    def remove_user_sbt():
        user = user_e.get()
        passw = passw_e.get()
        final = delete_user(user,passw)
        var = tk.StringVar(value=final)
        tk.Label(app,textvariable=var).pack()
    tk.Button(app,text='Διαγραφή',command=remove_user_sbt).pack()


def home():
    clear_app()
    tk.Label(app,text='Καλωσορίσατε {} ! \n Επιλέξτε ενέργεια'.format(user)).pack()
    tk.Button(app,text='Προσθήκη Πελάτη ',command=new_customer).pack()
    tk.Button(app,text='Διαγραφή πελάτη',command=remove_customer).pack()
    tk.Button(app,text='Αναζήτηση προϊόντος',command=find_products).pack()
    tk.Button(app,text='Προσθήκη προϊόντος',command=new_product).pack()
    tk.Button(app,text='Διαγραφή Προϊόντος',command=remove_product).pack()
    tk.Button(app,text='Προσθήκη χρήστη εφαρμογής',command=new_user).pack()
    tk.Button(app,text='Διαγραφή χρήστη εφαρμογής',command=remove_user).pack()

tk.Button(app,text='Σύνδεθείτε', command=login).pack()

app.mainloop() #GUI APP END