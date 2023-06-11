# -*- coding: utf-8 -*-
"""
Created on Fri May  5 15:30:23 2023

@author: lydie
"""

from sudoku import *
from tkinter import *
from random import *
from time import *
from tkinter import filedialog as TkFileDialog
from fenetre1cp import *
from tkinter import messagebox as tkMessageBox
from MySQL import *
from Player import *
from classement import *



#création fenetre principale
fenetre=Tk()

fenetre.geometry('1000x600+100+10')


#frame pour choisir la difficulté
framediff= Frame (fenetre, width=100,height=0)
framediff.place(x=10, y=20)


#label dans le frame de la diff pour le title
titre1=Label(framediff,bg='white', text='Difficulté',width=20)
titre1.pack()

#curseur pour la diff
diff=Scale(framediff,orient='horizontal',bg='white', from_ =1, to =9)
diff.pack()


#frame bouton jouer
framejouer=Frame(fenetre)
framejouer.place(x=200, y=30)

#frame bouton abandonner
frameabandonner=Frame(fenetre)
frameabandonner.place(x=300, y=30)

#Création de la frame pour afficher le compte à rebours
frame_compte_a_rebours = Frame(fenetre)
frame_compte_a_rebours.place(x=570, y=15)


#compteur de vie
compteur = 3

    
#Durée du compte à rebours en secondes
duree = 3 * 60  # 3 minutes

    









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
        

def abandonner(tex=''):
    """
    Gère l'abandon ou la défaite du joueur
    """
    global compteur
    compteur = 3
    Button.destroy(boutabandonner)
    boutjouer.config(state="normal")
    for cle in listentry:
        cle.config(state='disable',disabledbackground="#ff556c")
    gameover=Toplevel(fenetre)
    gameover.geometry("500x160+380+190")
    lab3=Label(gameover, text="GAME OVER", font=('impact',50), fg='red')
    lab3.pack()
    if tex!='':
        lab4=Label(gameover, text=tex, font=("Times New Roman", 20))
        lab4.pack()
    perdu()
    maj_ratio(Player.get_idJoueur(user))
    maj_point_def(diff.get(), Player.get_idJoueur(user))
    maj_classement()
    label_compte_a_rebours.destroy()
    pperd2.destroy()
    pperd3=Label(info,text= nb_def(),fg="black",bg='ivory',font=('arial 11'))
    pperd3.grid(row=2,column=1)
    classement2.destroy()
    classement3=Label(info,text= get_classement(),fg="black",bg='ivory',font=('arial 11'))
    classement3.grid(row=5,column=1)
    try :
        lab2
        if lab2!=[]:
            for la in lab2:
                la[0].destroy()
    except NameError:
        pass
    
    

def perdu() :
    """
    Le joueur a perdu, on ajout 1 au compteur de défaite sur la BDD
    """
    defaite = MySQL.askOne("SELECT défaites FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'") 
    MySQL.askNoReturn("UPDATE statistiques SET défaites='"+str(defaite[0]+1)+"' WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")    #Incrémente le nombre de défaites
    partie_j()
        
def gagner():
    """
    Le joueur a gagné, on ajout 1 au compteur de victoire sur la BDD
    """
    victoire = MySQL.askOne("SELECT victoires FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'") 
    MySQL.askNoReturn("UPDATE statistiques SET victoires='"+str(victoire[0]+1)+"' WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")    #Incrémente le nombre de victoires
    partie_j()

def partie_j():
    """
    Le joueur a joué une partie, on ajout 1 au compteur de partie joué sur la BDD
    """
    nbpart = MySQL.askOne("SELECT nbparties FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'") 
    MySQL.askNoReturn("UPDATE statistiques SET nbparties='"+str(nbpart[0]+1)+"' WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")    #Incrémente le nombre de partie jouée



def tempo(tc):
    mins, secs = divmod(tc, 60)
    timer = '{:02d}:{:02d}'.format(mins, secs)
    label_compte_a_rebours['text'] = f"Temps restant : {timer}"
    if tc:
        fenetre.after(1000, lambda: tempo(tc-1))
    else:
        ecouler='Temps écoulé'
        abandonner(ecouler)
        


#créer la grille, ce qui s'active quand on clique sur jouer
def jouer(taille:int=3) -> None:
#grille de 9 carré gris
    
    global label_compte_a_rebours
    #Création du label pour afficher le compte à rebours
    label_compte_a_rebours = Label(frame_compte_a_rebours, font=("Arial", 18))
    label_compte_a_rebours.pack()
    diffi=(diff.get())
    if taille==3:
        temps=90+20*(diffi-1)
    else:
        temps=300
    tempo(temps)
    #bouton jouer
    boutjouer.config(state="disabled")
    global boutabandonner
    boutabandonner=Button(frameabandonner, bg="#FF3333", text='abandoner', fg='white', font='impact', command=abandonner)
    boutabandonner.grid()
    sudo1=sudo(taille)
    sudoku=sudo1.board
    solution=sudo1.solve()
    listsol=solution.board
    global lab
    lab=[] #liste contenant les labels
    global lab2
    lab2=[]
    frameprincipale=Frame(fenetre)
    frameprincipale.place(x=440, y=50)
    blanc=0
    nbcolumn=0
    if taille==3:
        for j in range(9):
            nbrow=0
            for i in range(9):
                l=Label(frameprincipale,bg='#858585',width=6,height=3,relief="groove",borderwidth=4)
                l.grid(row=nbrow,column=nbcolumn)
                lab.append([l,(j,i)]) 
                blanc+=1
                if blanc%3==0:
                    nbrow+=1
                    lablanc=Label(frameprincipale,  text='', width=1,height=1)
                    lablanc.grid(row=nbrow,column=nbcolumn)
                nbrow+=1
            if blanc==27 or blanc==54:
                for it in range(11):
                    nbcolumn+=1
                    lablanc2=Label(frameprincipale, text='',width=1,height=1)
                    lablanc.grid(row=nbrow,column=nbcolumn)
            nbcolumn+=1
       
        
    
    else:   
             
        for j in range(16):
            nbrow=0
            for i in range(16):
                l=Label(frameprincipale,bg='#858585',width=3,height=1,relief="groove",borderwidth=4)
                l.grid(row=nbrow,column=nbcolumn)
                lab2.append([l,(j,i)]) 
                blanc+=1
                if blanc%4==0:
                    nbrow+=1
                    lablanc=Label(frameprincipale,  text='', width=1,height=1)
                    lablanc.grid(row=nbrow,column=nbcolumn)
                nbrow+=1
            if blanc==64 or blanc==128 or blanc==192:
                for it in range(11):
                    nbcolumn+=1
                    lablanc=Label(frameprincipale, text='',width=1,height=1)
                    lablanc.grid(row=nbrow,column=nbcolumn)
            nbcolumn+=1
            
            
    global listentry
    listentry={}

    if taille==4:
        lab=lab2
    for l in lab:
        label=l[0]
        texte=str(remplir(sudoku)[0])
        if texte=='0':
            entree=Entry(label, bg='#a1a1a1',cursor='cross', justify='center')
            if taille==3:
                w=44
                h=45
            else:
                w=17
                h=17
            entree.place(width=w,height=h)
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
                    if len(listentry)==1:
                        gagner()
                        maj_ratio(Player.get_idJoueur(user))
                        maj_point_vict(diff.get(), Player.get_idJoueur(user))
                        maj_classement() 
                        boutabandonner.destroy()
                        boutjouer.config(state='normal')
                        gagne=Toplevel(fenetre)
                        gagne.geometry("500x160+380+190")
                        lab4=Label(gagne, text="PARTIE GAGNE", font=('impact',50), fg='green')
                        lab4.pack()
                        label_compte_a_rebours.destroy()
                        pgagne2.destroy()
                        pgagne3=Label(info,text= nb_vict(),fg="black",bg='ivory',font=('arial 11'))
                        pgagne3.grid(row=1,column=1)
                        classement2.destroy()
                        classement3=Label(info,text= get_classement(),fg="black",bg='ivory',font=('arial 11'))
                        classement3.grid(row=5,column=1)
                        
                    del(listentry[cle])
                else:
                    global compteur
                    compteur=compteur-1
                    if compteur<1:
                        boutjouer.config(state="normal")
                        abandonner()
                            #ajouter variable qui stock les vicctoire et les défaites
                    else:
                        faux=Toplevel(fenetre)
                        faux.geometry("400x200+380+190")
                        lab=Label(faux, text=f"Mauvaise Réponse \n\n Il vous reste {compteur} vie(s)", font='arial',width=400)
                        lab.pack()
        #maj nombre de vie
        viereste2.destroy()
        viereste3=Label(info,text= compteur,fg="black",bg='ivory',font=('arial 11'))
        viereste3.grid(row=4,column=1)
    pjoue2.destroy()
    pjoue3=Label(info,text= nb_parties(),fg="black",bg='ivory',font=('arial 11'))
    pjoue3.grid(row=3,column=1)
   
                        
    fenetre.bind_all("<Return>", on_return)

#bouton jouer
boutjouer=Button(framejouer, bg='#45e325', text='Jouer', fg='white', font='Impact', command=jouer)
boutjouer.grid()


def nb_def():
    """
    Prend le nombre de défaites
    """
    defaite = MySQL.askOne("SELECT défaites FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")
    return defaite[0]

def nb_vict():
    """
    Prend le nb de victoires
    """
    victoire = MySQL.askOne("SELECT victoires FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")
    return victoire[0]

def nb_parties():
    """
    Prend le nb de parties
    """
    parties = MySQL.askOne("SELECT nbparties FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")
    return parties[0]

def get_classement():
    """
    Prend le classement
    """
    classem= MySQL.askOne("SELECT classement FROM statistiques WHERE idJoueur='"+str(Player.get_idJoueur(user))+"'")
    return classem[0]

info=Frame(fenetre, width=500, height=400, bg='ivory')
info.place(x=60,y=150)

#####################Affichage statistiques##########################
infojoueur=Label(info,text= "Info joueur \n",fg="black",bg='ivory',font=('Helvetica 12 bold italic underline'))
infojoueur.grid(row=0,column=0)
pgagne=Label(info,text= "Parties gagnées :",fg="black",bg='ivory',font=('arial 11'))
pgagne.grid(row=1,column=0)
pperd=Label(info,text= "Parties perdues :",fg="black",bg='ivory',font=('arial 11'))
pperd.grid(row=2,column=0)
pjoue=Label(info,text= "Parties jouées :",fg="black",bg='ivory',font=('arial 11'))
pjoue.grid(row=3,column=0)
viereste=Label(info,text= "Vie restante : ",fg="black",bg='ivory',font=('arial 11'))
viereste.grid(row=4,column=0)
classement=Label(info,text= "Classement : ",fg="black",bg='ivory',font=('arial 11'))
classement.grid(row=5,column=0)


pgagne2=Label(info,text= nb_vict(),fg="black",bg='ivory',font=('arial 11'))
pgagne2.grid(row=1,column=1)
pperd2=Label(info,text= nb_def(),fg="black",bg='ivory',font=('arial 11'))
pperd2.grid(row=2,column=1)
pjoue2=Label(info,text= nb_parties(),fg="black",bg='ivory',font=('arial 11'))
pjoue2.grid(row=3,column=1)
viereste2=Label(info,text= compteur,fg="black",bg='ivory',font=('arial 11'))
viereste2.grid(row=4,column=1)
classement2=Label(info,text= get_classement(),fg="black",bg='ivory',font=('arial 11'))
classement2.grid(row=5,column=1)



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

def defquotidien():
    if lab!=[]:
        for la in lab:
            la[0].destroy()
    jouer(4)
    



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
     lab=Label(fen, text="Voici les règles du Sudoku \n Il faut remplir les cases, \n Sans qu'un chiffre apparaisse \n Deux fois sur la même ligne ou \n Même colonne \n Bonne chance!\n",font='arial',width=100)
     lab.pack() 
     lab1=Label(fen, text='Par Elouan, Léopold et Lydie', font=("Times New Roman", 10, "italic"))
     lab1.pack()

# stop_quit permet de fermer et détruire la fenetre

def stop_quit():
    if tkMessageBox.askokcancel("Quitter", "Voulez vous vraiment quitter ?"):
        fenetre.quit()
        fenetre.destroy()


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
menuResolution.add_command(label="Défi quotidien", command=defquotidien)
menuResolution.add_separator() 
menuResolution.add_command(label="Abandonner", command=abandonner)
                                                                 


menuInfo = Menu(barreDeMenus) 
barreDeMenus.add_cascade(label="Règle du jeu", command=menuAPropos)# menu=menuInfo





fenetre.mainloop()
