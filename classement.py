from MySQL import *
from Player import *

def maj_ratio(player):
    """
    Mise à jour du ratio
    """
    defaite = MySQL.askOne("SELECT défaites FROM statistiques WHERE idJoueur='"+str(player)+"'")
    victoire = MySQL.askOne("SELECT victoires FROM statistiques WHERE idJoueur='"+str(player)+"'")
    if defaite[0] == 0 :
        MySQL.askNoReturn("UPDATE statistiques SET ratiovd='"+str(victoire[0])+"' WHERE idJoueur='"+str(player)+"'")
    else :    
        MySQL.askNoReturn("UPDATE statistiques SET ratiovd='"+str(victoire[0]/defaite[0])+"' WHERE idJoueur='"+str(player)+"'")

def maj_classement():
    """
    Mise à jour du classement
    """
    classe = MySQL.askAll("SELECT joueur.idJoueur FROM joueur, statistiques WHERE statistiques.idJoueur = joueur.idJoueur ORDER BY ratiovd DESC")
    for i in range(len(classe)):
        MySQL.askNoReturn("UPDATE statistiques SET classement='"+str(i+1)+"' WHERE idJoueur='"+str(classe[i][0])+"'")

