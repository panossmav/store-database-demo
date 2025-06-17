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



app.title("Επεξεργασία βάσης δεδομένων")
app.minsize(500,500)    
intro_label = Label(app,text='Παρακαλώ επιλέξτε: \n')
add_btn = Button(app,text='Προσθήκη Πελάτη',command=new_customer)


intro_label.pack()
add_btn.pack()
app.mainloop()









