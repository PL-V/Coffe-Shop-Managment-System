from tkinter import *
from tkinter import ttk, messagebox
import sqlite3, random

con = sqlite3.connect("C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/coffee.db")
print(con)
cur=con.cursor()



def SubmitInfo(Nom,Username,Password):
    
      query = "INSERT INTO 'users' (Nom,Username,Password) VALUES(?,?,?)"
      cur.execute(query,(Nom,Username,Password)) 
      con.commit()
      messagebox.showinfo("Success", "Success", "New user has been created !\nuser name : {}\nuser password : {}"
                                .format(Username, Password))

def CreateUser(master):  
   fenetre = Toplevel(master)
   fenetre.geometry("650x650+650+200")
   fenetre.title("Creer Utilisateur")
   fenetre.resizable(False, False)

    # background for this window .
   fenetre.background = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/backgrounds/coffee_menu_background.png')
   fenetre.background_label = Label(fenetre, image=fenetre.background)
   fenetre.background_label.pack()

    # icon new to the title .
   fenetre.new_user_icon = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/icons/add-group.png')
   fenetre.new_user_label = Label(fenetre, image=fenetre.new_user_icon)
   fenetre.new_user_label.place(x=120, y=30)

    # title .
   fenetre.title_label = Label(fenetre, text='Creer Utilisateur', font='Times 20 bold', bg='white')
   fenetre.title_label.place(x=230, y=50)

    # name , surname and date labels and entries .
   fenetre.name_label = Label(fenetre, text='Nom: ', font='Times 14 bold', bg='white')
   fenetre.name_label.place(x=25, y=140)
   fenetre.name_entry = Entry(fenetre, width=60, bd=5)
   fenetre.name_entry.place(x=140, y=141)

   fenetre.username_entry = Label(fenetre, text='Username: ', font='Times 14 bold', bg='white')
   fenetre.username_entry.place(x=25, y=180)
   fenetre.username_entry = Entry(fenetre, width=60, bd=5)
   fenetre.username_entry.place(x=140, y=181)

    # date label :
   fenetre.password_label = Label(fenetre, text='Password : ', font='Times 14 bold', bg='white')
   fenetre.password_label.place(x=25,y=220)
   fenetre.password_entry = Entry(fenetre,width=60, bd=5)
   fenetre.password_entry.place(x=140, y=221)
   
   fenetre.Submit= Button(fenetre, text='Submit', width=15, height=1, font='Times 12 bold',bd=5, command=lambda: SubmitInfo(fenetre.name_entry.get(),fenetre.username_entry.get(),fenetre.password_entry.get()))
   fenetre.Submit.place(x=255,y=270)
   
   