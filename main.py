from tkinter import *
import tkinter
from database import add_customer,delete_customer,email_check,search_product,create_product,check_sku
import json
app = tkinter.Tk()




def clear_app():
    for widgets in app.winfo_children():
        widgets.pack_forget()
f_name_l = Label(app,text='Δώσε όνομα \n')
f_name_e = Entry(app)   
l_name_l = Label(app,text='Δώσε επίθετο \n')
l_name_e = Entry(app) 
email_l = Label(app,text='Δώσε email \n')
email_e = Entry(app) 
phone_l = Label(app,text='Δώσε τηλέφωνο \n')
phone_e = Entry(app) 
vat_l = Label(app,text='Δώσε ΑΦΜ \n')
vat_e = Entry(app)
error_label = Label(app,text='Σφάλμα κατα την εισαγωγή \n')
sku_l = Label(app,text='Δώσε τον κωδικό (SKU) Του προϊόντος \n')
sku_e = Entry(app)

def start_search_product():
    clear_app()
    sku_l.pack()
    sku_e.pack()
    def sbt_search():
        sku = int(sku_e.get())
        product_info = search_product(sku)
        tk_variable = tkinter.StringVar()
        tk_variable.set(product_info)
        product_label = Label(app,textvariable=tk_variable)
        product_label.pack()
    sbt_search_btn = Button(app,text='Αναζήτηση',command=sbt_search)
    sbt_search_btn.pack()

def new_product():
    clear_app()
    sku_l.pack()
    sku_e.pack()
    title_l = Label (app,text='Δώσε όνομα προϊόντος')
    title_l.pack()
    title_e = Entry (app)
    title_e.pack()
    price_l = Label (app,text='Δώσε τιμή προϊόντος')
    price_l.pack()
    price_e = Entry (app)
    price_e.pack()
    def submit_new():
        sku = int(sku_e.get())
        product_name = title_e.get()
        price = float(price_e.get())
        server_sku = check_sku(sku)
        if not server_sku:
            create_product(sku,product_name,price)
            added_l = Label(app,text='Το προϊόν αποθηκεύτηκε επιτυχώς! \n')
            added_l.pack()
        else:
            error_l = Label(app,text='Ο κωδικός υπάρχει ήδη! \n')
            error_l.pack()
    sbt_add_btn = Button(app,text='Προσθήκη',command=submit_new)
    sbt_add_btn.pack()


def new_customer():
    clear_app()
    f_name_l.pack()
    f_name_e.pack()
    l_name_l.pack()
    l_name_e.pack()
    email_l.pack()
    email_e.pack()
    phone_l.pack()
    phone_e.pack()
    vat_l.pack()
    vat_e.pack()
    def sbt():
        error_label.pack_forget()
        f_name = f_name_e.get()
        l_name = l_name_e.get()
        email = email_e.get()
        phone = int(phone_e.get())
        vat = int(vat_e.get())
        email_verify = email_check(email)
        if '@' not in email:
            error_label.pack()
        elif email_verify == True:
            email_in_use = Label(app,text='This email is already in use!')
            email_in_use.pack()
        else:
            add_customer(f_name,l_name,email,phone,vat)
            added = Label(app,text='Ο πελάτης προστέθηκε επιτυχώς')
    sbt_btn = Button(app,text='Προσθήκη',command=sbt)
    sbt_btn.pack()

def rmv_customer():
    clear_app()
    phone_l.pack()
    phone_e.pack()
    email_l.pack()
    email_e.pack()
    def sbt_del():
        phone = int(phone_e.get())
        email = email_e.get()
        if '@' not in email:
            error_label.pack()
        else:
            result = delete_customer(phone,email)
            if result == 1:
                deleted_lb = Label(app,text='Ο πελάτης διαγράφηκε επιτυχώς')
                delete_lb.pack()
            else:
                error_deleted = Label(app,text='Σφάλμα, ο συνδιασμός τηλεφώνου και email είναι λάθος \n')
                error_deleted.pack()
    del_btn = Button(app,text='Διαγραφή πελάτη \n',command=sbt_del)
    del_btn.pack()
app.title("Επεξεργασία βάσης δεδομένων")
app.minsize(500,500)    
intro_label = Label(app,text='Παρακαλώ επιλέξτε: \n')
add_btn = Button(app,text='Προσθήκη Πελάτη',command=new_customer)
delete_btn = Button(app,text='Διαγραφή Πελάτη',command=rmv_customer)
search_product_btn = Button(app,text='Αναζήτηση προιόντος',command=start_search_product)
new_product_btn = Button(app,text='Προσθήκη προϊόντος \n',command=new_product)





intro_label.pack()
add_btn.pack()
delete_btn.pack()
search_product_btn.pack()
new_product_btn.pack()

app.mainloop()









