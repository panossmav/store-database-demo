from tkinter import *
from database import add_users
import tkinter

app=tkinter.Tk()
name_label = Label(app,text='Δώσε όνομα')
name_entry = Entry(app)
age_label = Label(app,text='Δώσε ηλικία')
age_entry = Entry(app)
dob_label = Label(app,text='Δώσε ημ γεννησης (YYYY-MM-DD)')
dob_entry = Entry(app)
email_label = Label(app,text='Δώσε email')
email_entry = Entry(app)
added = Label(app,text='Τα δεδομένα αποθηκεύτηκαν')
def sbt():
    name = name_entry.get()
    age = age_entry.get()
    dob = dob_entry.get()
    email = email_entry.get()
    add_users(name,age,dob,email)
    added.pack()

sbt = Button(app,text="Υποβολή",command=sbt)

name_label.pack()
name_entry.pack()
age_label.pack()
age_entry.pack()
dob_label.pack()
dob_entry.pack()
email_label.pack()
email_entry.pack()
sbt.pack()
app.mainloop()