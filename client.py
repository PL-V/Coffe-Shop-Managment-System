from tkinter import *
from tkinter import ttk, messagebox
import sqlite3, random
from typing import Dict
import buttons
from datetime import date
from facturation import *
con = sqlite3.connect("C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/coffee.db")
cur=con.cursor()


fenetre = 0
    # create and locate background and icon :

#cur.execute("SELECT prix FROM items where nom = 'cola'").fetchall()[0][0]
def GetItems(fenetre):
    Items = {}
    if fenetre.cola_counter_label.cget("text") != 0:
        Items['cola'] = fenetre.cola_counter_label.cget("text")
    if fenetre.cofe_counter_label.cget("text") != 0:
        Items['cofe'] = fenetre.cofe_counter_label.cget("text")
    if fenetre.cofec_counter_label.cget("text") != 0:
        Items['cofec'] = fenetre.cofec_counter_label.cget("text")  
    if fenetre.orange_counter_label.cget("text") != 0:
        Items['orange'] = fenetre.orange_counter_label.cget("text")          
    return Items  
        
         

def Confirmer(fenetre,Total,Piece,name):
    if Piece:
     if int(Piece) >= Total:
      reste = int(Piece) - Total
      fenetre.reste_label = Label(fenetre, bg="white",text='Reste:  ' + str(reste), font='Times 20 bold')
      fenetre.reste_label.place(x=420, y=405)
      Items = GetItems(fenetre)
      Facturation(Items,Total,fenetre,name)
     else:
        return 


def increase_stat(fenetre,Total,label,counter):
    if  label  == "cola":
     prix = cur.execute("SELECT prix FROM items where nom = 'cola'").fetchall()[0][0]   
     counter.set(counter.get()+1)
     fenetre.cola_counter_label.configure(text=counter.get())
     Total.set(Total.get() + prix )
    
    elif  label  == "cofe":
     prix = cur.execute("SELECT prix FROM items where nom = 'cofe'").fetchall()[0][0]   
     counter.set(counter.get()+1)
     fenetre.cofe_counter_label.configure(text=counter.get())
     Total.set(Total.get() + prix )
     
    elif  label  == "cofec":
     prix = cur.execute("SELECT prix FROM items where nom = 'cofec'").fetchall()[0][0] 
     counter.set(counter.get()+1)
     fenetre.cofec_counter_label.configure(text=counter.get())
     Total.set(Total.get() + prix ) 
    elif  label  == "orange":
     prix = cur.execute("SELECT prix FROM items where nom = 'orange'").fetchall()[0][0]    
     counter.set(counter.get()+1)
     fenetre.orange_counter_label.configure(text=counter.get())
     Total.set(Total.get() + prix )  
    
    fenetre.Total_count_label.configure(text=Total.get())
        
     
  

    

def decrease_stat(fenetre,Total,label,counter):
    if counter.get() > 0:
      if  label  == "cola":   
       counter.set(counter.get()-1)
       fenetre.cola_counter_label.configure(text=counter.get())
       Total.set(Total.get() - 7 )
      elif label  == "cofe":
       counter.set(counter.get()-1)
       fenetre.cofe_counter_label.configure(text=counter.get())
       Total.set(Total.get() - 11 )  
      elif label  == "cofec":
       counter.set(counter.get()-1)
       fenetre.cofec_counter_label.configure(text=counter.get())
       Total.set(Total.get() - 11 )
      elif label  == "orange":
       counter.set(counter.get()-1)
       fenetre.orange_counter_label.configure(text=counter.get())
       Total.set(Total.get() - 15 ) 
      
      fenetre.Total_count_label.configure(text=Total.get())
       
       
       

#fenetre=Tk()       
def Client(name,Master):  
 today = date.today()
 print(today)
 fenetre = Toplevel(Master)     
 
 counter_cola=IntVar()
 counter_cola.set(0)
 Total = IntVar()
 Total.set(0)  
 
 fenetre.cola_counter_label = Label(fenetre, text=counter_cola.get(), font='Times 30 bold')
 fenetre.cola_counter_label.place(x=305, y=115)
 fenetre.decrease_button = Button(fenetre, text='+', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:increase_stat(fenetre,Total,"cola",counter_cola))
 fenetre.decrease_button.place(x=350, y=120)
 fenetre.increase_button = Button(fenetre, text='-', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:decrease_stat(fenetre,Total,"cola",counter_cola))
 fenetre.increase_button.place(x=250, y=120)

 counter_cofe = IntVar()

 fenetre.cofe_counter_label = Label(fenetre, text=counter_cofe.get(), font='Times 30 bold')
 fenetre.cofe_counter_label.place(x=305, y=195)
 fenetre.decrease_cofe_button = Button(fenetre, text='+', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:increase_stat(fenetre,Total,"cofe",counter_cofe))
 fenetre.decrease_cofe_button.place(x=350, y=200)
 fenetre.increase_cofe_button = Button(fenetre, text='-', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:decrease_stat(fenetre,Total,"cofe",counter_cofe))
 fenetre.increase_cofe_button.place(x=250, y=200)

    
 counter_cofec = IntVar()

 fenetre.cofec_counter_label = Label(fenetre, text=counter_cofec.get(), font='Times 30 bold')
 fenetre.cofec_counter_label.place(x=305, y=275)
 fenetre.decrease_cofec_button = Button(fenetre, text='+', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:increase_stat(fenetre,Total,"cofec",counter_cofec))
 fenetre.decrease_cofec_button.place(x=350, y=280)
 fenetre.increase_cofec_button = Button(fenetre, text='-', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:decrease_stat(fenetre,Total,"cofec",counter_cofec))
 fenetre.increase_cofec_button.place(x=250, y=280)   
    
 
    
  
 counter_orange = IntVar()

 fenetre.orange_counter_label = Label(fenetre, text=counter_orange.get(), font='Times 30 bold')
 fenetre.orange_counter_label.place(x=305, y=355)
 fenetre.decrease_orange_button = Button(fenetre, text='+', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:increase_stat(fenetre,Total,"orange",counter_orange))
 fenetre.decrease_orange_button.place(x=350, y=360)
 fenetre.increase_orange_button = Button(fenetre, text='-', width=2, height=1, font='Times 12 bold',bd=5, command=lambda:decrease_stat(fenetre,Total,"orange",counter_orange))
 fenetre.increase_orange_button.place(x=250, y=360)      
    
 
    
    
    
    
    
    

 fenetre.cola_icon = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/icons/cold-drink.png')
 cola_button = Button(fenetre, text='Cola', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn, image=fenetre.cola_icon,
                                   compound=LEFT, padx=10, command=fenetre)
 cola_button.place(x=buttons.x_distance, y=buttons.y_distance)



 fenetre.cafe_icon = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/icons/tasse-a-cafe.png')
 cafe_button = Button(fenetre, text='Cafe Noire', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn, image=fenetre.cafe_icon,
                                   compound=LEFT, padx=10, command=fenetre)
 cafe_button.place(x=buttons.x_distance, y=buttons.y_distance+80)

 fenetre.cafec_icon = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/icons/cafe.png')
 cafec_button = Button(fenetre, text='Cafe Creme', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn, image=fenetre.cafec_icon,
                                   compound=LEFT, padx=10, command=fenetre)
 cafec_button.place(x=buttons.x_distance, y=buttons.y_distance+80*2)

 fenetre.orange_icon = PhotoImage(file='C:/Users/TAWFIK/Desktop/MASTER DSBD/PYTHON/Mini-Projet/icons/orange.png')
 orange_button = Button(fenetre, text='Jus D orange', font=buttons.font_btn, bd=buttons.bd_btn,
                                   height=buttons.height_btn, width=buttons.width_btn, image=fenetre.orange_icon,
                                   compound=LEFT, padx=10, command=fenetre)
 orange_button.place(x=buttons.x_distance, y=buttons.y_distance+80*3)




 fenetre.coffee_label = Label(fenetre, text='Cafe BSB ',font='Times 30 bold')
 fenetre.coffee_label.place(x=30, y=20)

 frame = Frame(fenetre, width=250, height=70, bg="white", padx=20, relief=SUNKEN, borderwidth=2)
 frame.pack(side=RIGHT, fill=Y)


 fenetre.Total_label = Label(fenetre, text='Total: ' , font='Times 30 bold')
 fenetre.Total_label.place(x=20, y=500)
 fenetre.Total_count_label = Label(fenetre, text=Total.get() , font='Times 30 bold')
 fenetre.Total_count_label.place(x=200, y=500)


 fenetre.Server_name_label = Label(fenetre, bg="white",text=name, font='Times 30 bold')
 fenetre.Server_name_label.place(x=460, y=20)

 fenetre.date_label = Label(fenetre, bg="white",text=str(today.strftime("%m/%d/%Y")), font='Times 20 bold')
 fenetre.date_label.place(x=450, y=70)

 fenetre.Piece_label = Label(fenetre, bg="white",text='Piece:', font='Times 20 bold')
 fenetre.Piece_label.place(x=420, y=345)
 fenetre.Piece_label_entry = Entry(fenetre, bd=5,font='Times 20 bold')
 fenetre.Piece_label_entry.insert(0, "")
 fenetre.Piece_label_entry.place(x=510, y=348,width=120,height=40)



 fenetre.refresh_button = Button(frame, text='Confirmer',font='Times 12 bold', bd=6, height=1, width=21,command=lambda:Confirmer(fenetre,Total.get(),fenetre.Piece_label_entry.get(),name))
 fenetre.refresh_button.place(x=2, y=500)

 fenetre.user_name_label = Label(fenetre, bg="white",text='Piece:', font='Times 20 bold')
 fenetre.user_name_label.place(x=420, y=345)


 

    # create login button and place it
    # on the app .

 fenetre.geometry("650x550+350+200")
 fenetre.mainloop()