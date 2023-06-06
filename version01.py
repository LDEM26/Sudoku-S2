# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:30:23 2023

@author: lydie
"""
from fenetre1 import *
from sudoku import *
from tkinter import *
from random import *




#création fenetre principale
fenetre=Tk()
fenetre.geometry('500x500')

#frame pour choisir la difficulté
framediff= Frame (fenetre, bg='#f1d7f3', width=100,height=0)
framediff.place(x=10, y=20)


#label dans le frame de la diff pour le title
titre1=Label(framediff,bg='#f1d7f3', text='Difficulté',width=20)
titre1.pack()

#curseur pour la diff
diff=Scale(framediff,orient='horizontal', from_ =1, to =9)
diff.pack()



#frame bouton
framejouer=Frame(fenetre, bg='red')
framejouer.place(x=200, y=30)





#générer aléatoirement des listes de sudoku
def sudo(taille=3):
    valdiff=(diff.get())/10
    #créer graine aléatoire
    graine=randint(0,10000)
    #créer la grille avec la graine
    sudoku=Sudoku(taille, seed=graine).difficulty(valdiff) 
    # returner la grille      
    return sudoku

def remplir(listesudo):
    for i in range(len(listesudo)):
        #on parcours les cases du sudoku
        for j in range(len(listesudo[i])):
            val=listesudo[i][j]
            # on parcours les sous-cases du sudoku
            if val==None:
                del(listesudo[i][j])
                return ('0', listesudo)
            else:
                del(listesudo[i][j])
                return (val, listesudo)


#mettre les labels en ligne
def lignelabel(lab):
    nb=len(lab)/3
    for i in range(nb):
        none
        
sudo=sudo()
sudoku=sudo.board
solution=sudo.solve()
lissol=solution.board

#créer la grille, ce qui s'active quand on clique sur jouer
def jouer(diff=0.5, taille=3 ,sudoku=sudoku, sol=solution):
#grille de 9 carré gris
    lab=[] #liste contenant les labels
    frameprincipale=Frame(fenetre)
    frameprincipale.place(x=500, y=170)
    for j in range(9):
        for i in range(9):
            l=Label(frameprincipale,bg='#858585',width=4,height=2,relief="groove",borderwidth=4)
            l.grid(row=i,column=j)
            lab.append([l,(i,j)])
    
    listentry={}
    
    for l in lab:
        label=l[0]
        texte=str(remplir(sudoku)[0])
        if texte=='0':
            entree=Entry(label, width=0, bg='#a1a1a1')
            entree.grid(ipadx=10, ipady=6)
            listentry[entree]=l[1]
        else:
            label['text'] += texte
    
    print(sol)
#    for cle in listentry:
 #       a=entree.get()
    

    
        
#bouton jouer
boutjouer=Button(framejouer, bg='#45e325', text='Jouer', fg='white', font='Impact', command=jouer)
boutjouer.grid()









fenetre.mainloop()