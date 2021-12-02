from tkinter import *
import sqlite3
con = sqlite3.connect("C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/coffee.db")
cur=con.cursor()
from datetime import date
# fenêtre principale



def Facturation(Items,Total,Master,name):
 fenetre = Toplevel(Master)
 today = date.today()  
 fenetre.title('Cafe BSB')
 fenetre.user_name_label = Label(fenetre, text=name, font='Times 16 bold')
 fenetre.user_name_label.place(x=1, y=1)
 fenetre.user_name_label = Label(fenetre, text=str(today.strftime("%m/%d/%Y")), font='Times 16 bold')
 fenetre.user_name_label.place(x=350, y=1)
 fenetre.user_name_label = Label(fenetre, text='Cafe BSB', font='Times 16 bold')
 fenetre.user_name_label.place(x=180, y=80)
# libellé
 
 x=0
 pas = 50
 y=180
 
 for i in Items.keys():
     quan = Items[i]
     prix = cur.execute("SELECT prix FROM items where nom =" + "'"+ i +"'").fetchall()[0][0]
     itemNom = cur.execute("SELECT Item_Nom FROM items where nom =" + "'"+ i +"'").fetchall()[0][0]
     fenetre.item_label = Label(fenetre, text="x" +str(Items[i])+"      " +  itemNom    +": " + str(prix*quan) + "dh", font='Times 16 bold')
     fenetre.item_label.place(x=115, y=y+x)
     x=x+pas
  
 fenetre.Total_label = Label(fenetre, text='Total: ' + str(Total), font='Times 20 bold')
 fenetre.Total_label.place(x=300, y=400)
 fenetre.merci_label = Label(fenetre, text='nous vous attendons a nouveau', font='Times 12 bold')
 fenetre.merci_label.place(x=130, y=500)

 fenetre.geometry("450x550+350+200")
 fenetre.mainloop()