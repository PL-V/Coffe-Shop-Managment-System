from tkinter import *

from tkinter.ttk import *

import sqlite3

import sys

import traceback

# fenêtre principale

fenetre = Tk()

fenetre.title('Cafe BSB')

# libellé

libelle = Label(fenetre, text='Équipe de travail', font=20)

libelle.pack(padx=10, pady=10)

# tableau

tableau = Treeview(fenetre, columns=('serveur', 'barman', 'horaire'))

tableau.heading('serveur', text='Serveur')

tableau.heading('barman', text='Barman')

tableau.heading('horaire', text='Horaire')

tableau[
    'show'] = 'headings'  # sans ceci, il y avait une colonne vide à gauche qui a pour rôle d'afficher le paramètre "text" qui peut être spécifié lors du insert

tableau.pack(padx=10, pady=(0, 10))

# bouton pour terminer le programme



bouton_modifier = Button(fenetre, text='Ajouter', command=Ajouter)

bouton_modifier.place(x=150, y=280)

bouton_supprimer = Button(fenetre, text='Modifier', command=Modifier)

bouton_supprimer.place(x=300, y=280)

bouton_ajouter = Button(fenetre, text='Supprimer', command=Supprimer)

bouton_ajouter.place(x=450, y=280)


# lecture et affichage des données


fenetre.geometry("700x320+10+10")
fenetre.mainloop()