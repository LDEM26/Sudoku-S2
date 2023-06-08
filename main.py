# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:30:23 2023

@author: lydie
"""
#from fenetre1 import *
from sudoku import *
from tkinter import *
from random import *
from time import *
from tkinter import filedialog as TkFileDialog
#from fenetre1cp import *
from tkinter import messagebox as tkMessageBox



#création fenetre principale
fenetre=Tk()
fenetre.geometry('850x538')


#frame pour choisir la difficulté
framediff= Frame (fenetre, bg='#f1d7f3', width=100,height=0)
framediff.place(x=10, y=20)


#label dans le frame de la diff pour le title
titre1=Label(framediff,bg='#f1d7f3', text='Difficulté',width=20)
titre1.pack()

#curseur pour la diff
diff=Scale(framediff,orient='horizontal', from_ =1, to =9)
diff.pack()


#frame bouton jouer
framejouer=Frame(fenetre, bg='red')
framejouer.place(x=200, y=30)

#frame bouton abandonner
frameabandonner=Frame(fenetre)
frameabandonner.place(x=200, y=480)

#compteur de vie
compteur = 3



def remplir(listesudo:list) -> tuple:
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

#générer aléatoirement des listes de sudoku
def sudo(taille:int = 3):
    valdiff=(diff.get())/10
    #créer graine aléatoire
    graine=randint(0,10000)
    #créer la grille avec la graine
    sudoku=Sudoku(taille, seed=graine).difficulty(valdiff) 
    # returner la grille      
    return sudoku
        

def abandonner():
    frameabandonner.destroy()
   # frameprincipale.destroy() #en commentaire pour l'instant mais dois a terme fonctioner
    boutjouer.config(state="normal")


#créer la grille, ce qui s'active quand on clique sur jouer
def jouer(diff:float=0.5, taille:int=3) -> None:
#grille de 9 carré gris
    boutabandonner=Button(frameabandonner, bg="#FF3333", text='abandoner', fg='white', font='impact', command=abandonner)
    boutabandonner.grid()
    boutjouer.config(state="disabled")
    sudo1=sudo()
    sudoku=sudo1.board
    solution=sudo1.solve()
    listsol=solution.board
    lab=[] #liste contenant les labels
    frameprincipale=Frame(fenetre)
    frameprincipale.place(x=500, y=170)
    for j in range(9):
        for i in range(9):
            l=Label(frameprincipale,bg='#858585',width=4,height=2,relief="groove",borderwidth=4)
            l.grid(row=i,column=j)
            lab.append([l,(j,i)])
    
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
    
    
   # boucle infini
    def on_return(event):
    
        for cle in listentry:
            valcle=listentry[cle]
            ligne=valcle[0]
            colonne=valcle[1]
            valeur=cle.get()
            if valeur== '':
                pass                    
                #clairement ne marche pas mais si on a suprimer toutes les valeur d'entry
                #et donc que le
                #jeu est terminer il faut ajouter plus 1 victoire dans la variable et Victoire et 
            else :
                if listsol[ligne][colonne]==int(valeur):
                    cle.config(state="disabled",disabledbackground="#BEFFB9")
                    del(listentry[cle])
                    if len(lisentry)==0:
                        boutjouer.config(state="normal")
                            
                        
                
                    
                else:
                    global compteur
                    compteur=compteur-1
                    if compteur<1:
                        boutjouer.config(state="normal")
                            #ajouter variable qui stock les vicctoire et les défaites
                        
                        
                    else:
                        faux=Toplevel(fenetre)
                        faux.geometry("200x200")
                        lab=Label(faux, text=f"Mauvaise Réponse il vous reste : {compteur} mauvaises réponses", font='impact',width=400)
                        lab.pack()
                    
                    
    fenetre.bind_all("<Return>", on_return)
    



    
#bouton jouer
boutjouer=Button(framejouer, bg='#45e325', text='Jouer', fg='white', font='Impact', command=jouer)
boutjouer.grid()






def sauve():
      myFormats =[('Fichier Texte','*.txt')]
      fileName = TkFileDialog.asksaveasfilename(parent=fen,filetypes=myFormats,title='Enregistrer sous...')
      if fileName !='':
            f=open(fileName, 'w')
            f.write(str(grilleSudo))
            tkMessageBox.showinfo('Fichier sauvegardé','Fichier sauvegardé')
            f.close
      else:
            tkMessageBox.showinfo('Fichier non sauvegardé','Fichier non sauvegardé')

# ouvrir est dans le menu Édition et permet d'ouvrir une grille

def ouvrir():
    global grilleSudo,modeJeu
    modeJeu=1
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    myFormats =[('Fichier Texte','*.txt')]
    fileOpen = TkFileDialog.askopenfilename(parent=fen,filetypes=myFormats,title='Choisir fichier')
    if fileOpen !='':
        f=open(fileOpen, 'r')
        grilleSudo=eval(f.read())
        f.close
        new()
        
# ouvrirResolution est dans le menu Resolution et permet d'ouvrir une grille en mode résolution

def ouvrirResolution():
    global grilleSudo,modeJeu,typeJeu
    modeJeu=1
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    myFormats =[('Fichier Texte','*.txt')]
    fileOpen = TkFileDialog.askopenfilename(parent=fen,filetypes=myFormats,title='Choisir fichier')
    if fileOpen !='':
        f=open(fileOpen, 'r')
        grilleSudo=eval(f.read())
        f.close
        new()
    typeJeu=1
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()
    

def facile():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleFacile
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def moyen():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleMoyen
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def difficile():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleDifficile
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def diabolique():
    global grilleSudo,typeJeu,modeJeu
    t.delete("0.0",END)
    can.delete(ALL)
    grilleSudo=grilleDiabolique
    typeJeu=1
    modeJeu=0
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    genere()

def genere():
    global grilleSudo,typeJeu,bloqueSudo
    bloqueSudo=[[0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    t.delete("0.0",END)
    can.delete(ALL)
    for i in range(nb):
            for j in range(nb):
                if bloqueSudo[i][j]!=grilleSudo[i][j]:
                    bloqueSudo[i][j]+=10
    typeJeu=1
    grille()

def bactive():
    global modeJeu
    bactive.configure(state=DISABLED)
    bdesactive.configure(state=ACTIVE)
    modeJeu=1

def bdesactive():
    global modeJeu
    bdesactive.configure(state=DISABLED)
    bactive.configure(state=ACTIVE)
    modeJeu=0

# MenuAPropos est dans le menu '?' et permet d'afficher
# des informations le programme et son concepteur

def menuAPropos():
     fen=Toplevel(fenetre)
     fen.geometry("500x500")
     lab=Label(fen, text="Voici les règles du Sudoku \n Il faut remplir les cases. \n Bonne chance!\n",font='arial',width=100)
     lab.pack() 
     lab['text','font'] +=( 'Par Elouan, Léopold et Lydie' ,'impact')                                                


# stop_quit permet de fermer et détruire la fenetre

def stop_quit():
    if tkMessageBox.askokcancel("Quitter", "Voulez vous vraiment quitter ?"):
        fen.quit()
        fen.destroy()


barreDeMenus=Menu(fenetre)                                                             
fenetre.config(menu=barreDeMenus)

menuFichier=Menu(barreDeMenus)

barreDeMenus.add_cascade(label="Changer de session", menu=menuFichier)
menuFichier.add_command(label="Ouvrir...", command=ouvrir)                          
menuFichier.add_command(label="Enregistrer sous...", command=sauve)
menuFichier.add_separator()                                                                  
menuFichier.add_command(label="Quitter", command=stop_quit)

menuResolution=Menu(barreDeMenus)                                                             
barreDeMenus.add_cascade(label="Menu 1", menu=menuResolution)
menuResolution.add_command(label="Grille Facile", command=facile)
menuResolution.add_command(label="Grille Moyen", command=moyen)
menuResolution.add_command(label="Grille Difficile", command=difficile)
menuResolution.add_command(label="Grille Diabolique", command=diabolique)
menuResolution.add_separator()                                                                  
menuResolution.add_command(label="Ouvrir une grille en mode résolution", command=ouvrirResolution)

menuInfo = Menu(barreDeMenus) 
barreDeMenus.add_cascade(label="Règle du jeu", command=menuAPropos)# menu=menuInfo





fenetre.mainloop()
