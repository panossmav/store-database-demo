from tkinter import *
import tkinter
from database import add_customer,delete_customer
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
        if '@' not in email:
            error_label.pack()
        else:
            add_customer(f_name,l_name,email,phone,vat)
            added = Label(app,text='Ο πελάτης προστέθηκε επιτυχώς')
    sbt_btn = Button(app,text='Προσθήκη',comand=sbt)
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


intro_label.pack()
add_btn.pack()
delete_btn.pack()
app.mainloop()









