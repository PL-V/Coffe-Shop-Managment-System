from tkinter import *
from tkinter import messagebox
import sqlite3
from createUser import *
from client import *



con = sqlite3.connect("C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/coffee.db")
print(con)
cur=con.cursor()

name = ""

fenetre = Tk()

def Login(fenetre,Username,Password):
    all_users = cur.execute("SELECT * FROM users").fetchall()
    found=0
    for user in all_users:
        if user[2]==Username and user[3] == Password:
                  found = 1
                  messagebox.showinfo("Success", "Login: " + Username + " Sucess")
                  name = user[1]
                  Client(name,fenetre)
                  
                  
                   
    if found == 0:
        messagebox.showinfo("Error", "Logins: " + Username + " N'existe pas ou mot de passe erronée")   
    return          

            
   
 

    # create and locate background and icon :
fenetre.background = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/backgrounds/first_screen_background.png')
fenetre.background_label = Label(fenetre, image=fenetre.background)
fenetre.background_label.pack()

fenetre.icon = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/icons/login.png')
fenetre.login_icon = Label(fenetre, image=fenetre.icon)
fenetre.login_icon.place(x=300, y=25)

    # create user name entry and label and locate them on the app .
fenetre.user_name_label = Label(fenetre, text='Username:', font='Times 16 bold')
fenetre.user_name_label.place(x=20, y=100)
fenetre.user_name_entry = Entry(fenetre, width=60, bd=5)
fenetre.user_name_entry.insert(0, "Entrer votre username")
fenetre.user_name_entry.place(x=160, y=103)

    # create password entry and label and locate it on the app .
fenetre.password_label = Label(fenetre, text='Password', font='Times 16 bold')
fenetre.password_label.place(x=20, y=140)
fenetre.password_entry = Entry(fenetre, width=60, bd=5)
fenetre.password_entry.insert(0, "Entrer votre password")
fenetre.password_entry.place(x=160, y=143)

    # create login button and place it on the app .
fenetre.login_button = Button(fenetre, text='Login', width=30, height=1, font='Times 12 bold', bd=5,command=lambda: Login(fenetre,fenetre.user_name_entry.get(),fenetre.password_entry.get()))
fenetre.login_button.place(x=190, y=200)

    # create a button to add a new user to the system , the button will user 'create_user' function calling other class.
fenetre.new_user_button = Button(fenetre, text='Create New User', width=30, height=1, font='Times 12 bold', bd=5,command=lambda: CreateUser(fenetre))
fenetre.new_user_button.place(x=190, y=240)

    # create help button to reset password/user name .
fenetre.help_button = Button(fenetre, text='Help', width=30, height=1, font='Times 12 bold',bd=5, command=fenetre)
fenetre.help_button.place(x=190, y=280)

    # create info button about my fenetre .
fenetre.information_button = Button(fenetre, text='Information', width=30, height=1, font='Times 12 bold',bd=5, command=fenetre)
fenetre.information_button.place(x=190, y=320)
fenetre.geometry("650x550+350+200")
fenetre.mainloop()




