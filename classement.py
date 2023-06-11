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

def maj_point_vict(diff:int, player):
    """
    Met à jour les points en cas de victoire
    Si facile (entre 1 et 3) : +1 
    Si moyen (entre 4 et 6) : +3   
    Si difficile (entre 7 et 9) : +5
    """
    points = MySQL.askOne("SELECT points FROM statistiques WHERE idJoueur='"+str(player)+"'")
    if diff<=3 :
        MySQL.askNoReturn("UPDATE statistiques SET points='"+str(points[0]+1)+"' WHERE idJoueur='"+str(player)+"'")
    elif diff>3 and diff<=6:
        MySQL.askNoReturn("UPDATE statistiques SET points='"+str(points[0]+3)+"' WHERE idJoueur='"+str(player)+"'")
    elif diff>6 and diff<=9:
        MySQL.askNoReturn("UPDATE statistiques SET points='"+str(points[0]+5)+"' WHERE idJoueur='"+str(player)+"'")

def maj_point_def(diff:int, player):
    """
    Met à jour les points en cas défaite
    Si facile (entre 1 et 3) : -5*ratio
    Si moyen (entre 4 et 6) : -2*ratio   
    Si difficile (entre 7 et 9) : -1*ratio
    """
    points = MySQL.askOne("SELECT points FROM statistiques WHERE idJoueur='"+str(player)+"'")
    ratio = MySQL.askOne("SELECT ratiovd FROM statistiques WHERE idJoueur='"+str(player)+"'")
    if diff<=3 :
        MySQL.askNoReturn("UPDATE statistiques SET points='"+str((points[0])-(ratio[0]*5))+"' WHERE idJoueur='"+str(player)+"'")
    elif diff>3 and diff<=6:
        MySQL.askNoReturn("UPDATE statistiques SET points='"+str(points[0]-(ratio[0]*2))+"' WHERE idJoueur='"+str(player)+"'")
    elif diff>6 and diff<=9:
        MySQL.askNoReturn("UPDATE statistiques SET points='"+str(points[0]-(ratio[0]*1))+"' WHERE idJoueur='"+str(player)+"'")


def maj_classement():
    """
    Mise à jour du classement
    """
    classe = MySQL.askAll("SELECT joueur.idJoueur FROM joueur, statistiques WHERE statistiques.idJoueur = joueur.idJoueur ORDER BY points DESC")
    for i in range(len(classe)):
        MySQL.askNoReturn("UPDATE statistiques SET classement='"+str(i+1)+"' WHERE idJoueur='"+str(classe[i][0])+"'")



