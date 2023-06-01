# -*- coding: utf-8 -*-
"""
Created on Mon May 22 11:22:08 2023

@author: lydie
"""
from tkinter import *
#from pickdata import verif_connexion   inutile pour l'instant 


fenetre1 = Tk()
fenetre1.geometry('800x500')
fenetre1.title("Connection")


def recup():
    """
    Récupère mdp et login
    """
    res=(user_Entry.get(),user_mdp.get())
    user_Entry.delete(0, END)
    user_mdp.delete(0, END)
    fenetre1.destroy()
    return res

def recupid():
    res=(user_Entry.get(),user_mdp.get())
    user_Entry.delete(0, END)
    user_mdp.delete(0, END)
    fenetre1.destroy()
    return res


frame1= Frame (fenetre1, width=100,height=0,)
frame1.place(x=350, y=100)

boutonvalid=Button(fenetre1, bg='#45e325', text='valider', fg='black',height=0, command=recup)
boutonvalid.place(x=350, y=200)

#boutonid
boutonid=Button(fenetre1, bg='#45e325', text='Se connecter', fg='black',height=0, command=recupid)
boutonid.place(x=410, y=200)



user_Entry = Entry(frame1,)
user = Label(frame1, text = "identifiant")
user.pack()
user_Entry.pack()

user_mdp = Entry(frame1, show="*")
use = Label(frame1, text = "mot de passe")
use.pack()
user_mdp.pack()







fenetre1.mainloop()