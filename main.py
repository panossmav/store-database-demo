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
def home():
    clear_app()
    tk.Label(app,text='Καλωσορίσατε {} ! \n Επιλέξτε ενέργεια'.format(user)).pack()

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
            

       # def remove_customer():
            #code goes here ...
       # def find_product():
            #Code goes here ... 
       # def new_product():
            #Code goes here ...
       # def remove_product():
            #Code goes here ... 
       # def manage_users():
            #Code goes here ...
      #      def add_users():
                #Code goes here
      #      def remove_users():
                #Code goes here



tk.Button(app,text='Σύνδεθείτε', command=login).pack()

app.mainloop() #GUI APP END