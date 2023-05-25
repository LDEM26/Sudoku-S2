import mysql.connector
from datetime import datetime
from credentials import Credentials

############################# Connexion SGBD + création curseur######################################

db = mysql.connector.connect(
    host=Credentials.get_host(),
    user=Credentials.get_username(),
    password=Credentials.get_password(),
    database=Credentials.get_database()
)

curseur = db.cursor()

################################# Getter et fonction pour insérer des données#############################

########################################################     ATTENTION !!!!!!  #####################################################


##################### BIEN PENSER à UTILISER db.close() après avoir utiliser une fonction sinon ça marche pas !!!###################


########################################################     ATTENTION !!!!!!  #####################################################

def get_pseudo() -> list:
    """
    Getter des pseudos
    """
    curseur.execute("SELECT pseudo FROM joueur")
    row = curseur.fetchall()
    print(row, type(row))


def get_mdp(pseudo: str):
    """
    Getter du mdp
    """
    curseur.execute("SELECT mdp FROM Joueur WHERE pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(row[0][0])


def date_inscription(pseudo: str):
    """
    Getter date inscription
    """
    curseur.execute(
        "SELECT date_inscription FROM Joueur WHERE pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(row[0][0])


def set_grille_profil(idgrille: int, board: list, diff: float = 0, solution: list = None):
    """
    Permet de rentrer toutes les informations d'une grille dans la BDD
    """
    if solution == None:
        solution = "NULL"
    curseur.execute("INSERT INTO grille VALUES ('"+str(idgrille) +
                    "','"+str(board)+"','"+str(solution)+"','"+str(diff)+"')")
    db.commit()


def get_board(id: int):
    """
    Getter de la grille de départ
    """
    curseur.execute("SELECT board FROM grille WHERE idgrille="+str(id)+"")
    row = curseur.fetchall()
    print(row[0][0])


def get_solution(id: int):
    """
    Getter de la solution
    """
    curseur.execute("SELECT solution FROM grille WHERE idgrille="+str(id)+"")
    row = curseur.fetchall()
    print(row[0][0])


def get_nbparties(pseudo: str):
    """
    Getter du nbdeparties
    """
    curseur.execute(
        "SELECT nbparties FROM statistiques, joueur WHERE statistiques.idJoueur=joueur.idJoueur AND pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(list(row[0][0]))


def get_victoire(pseudo: str):
    """
    Getter nombre de victoire
    """
    curseur.execute(
        "SELECT victoires FROM statistiques, joueur WHERE statistiques.idJoueur=joueur.idJoueur AND pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(row[0][0])


def get_defaite(pseudo: str):
    """
    Getter nombre de défaites
    """
    curseur.execute(
        "SELECT défaites FROM statistiques, joueur WHERE statistiques.idJoueur=joueur.idJoueur AND pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(row[0][0])


def get_nul(pseudo: str):
    """
    Getter nombre de nuls
    """
    curseur.execute(
        "SELECT nuls FROM statistiques, joueur WHERE statistiques.idJoueur=joueur.idJoueur AND pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(row[0][0])


def calc_ratio(pseudo: str):
    """
    Calcul le ratio et le remplace par l'ancien
    """
    v = get_victoire(pseudo)
    d = get_defaite(pseudo)
    ratio = v/d
    curseur.execute(
        "INSERT INTO statistiques(ratiovd) VALUES ("+str(ratio)+")")


def get_ratio(pseudo: str):
    """
    Getter du ratio victoire/défaite
    """
    curseur.execute(
        "SELECT ratiovd FROM statistiques, joueur WHERE statistiques.idJoueur=joueur.idJoueur AND pseudo='"+str(pseudo)+"'")
    row = curseur.fetchall()
    print(row[0][0])


def set_user(pseudo: str, mdp: str):
    """
    Créer un nouvel utilisateur avec son profil statistiques, uniquement avec le pseudo et le mot de passe.
    Fait la vérification de l'unicité du pseudo.
    """
    if verif_pseudo_unique(pseudo, mdp) == True:  # vérifie l'unicité du pseudo
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        curseur.execute("INSERT INTO joueur(idJoueur, pseudo, mdp, date_inscription) VALUES (NULL, '" +
                        str(pseudo)+"', '"+str(mdp)+"', '"+str(date)+"')")
        db.commit()  # Envoie à la BDD le profil du joueur
        id = curseur.execute(
            "SELECT idJoueur FROM joueur WHERE pseudo='"+str(pseudo)+"'")
        row = curseur.fetchall()  # Prend le nouvel id du joueur
        curseur.execute("INSERT INTO statistiques VALUES ('" +
                        str(row[0][0])+"', '0', '0', '0', '0', '0', NULL)")
        db.commit()  # Créer son profil de statistiques


def verif_pseudo_unique(pseudo: str, mdp: str):
    """
    Vérifie que le pseudo est unique
    """
    try:
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        curseur.execute("INSERT INTO joueur(idJoueur, pseudo, mdp, date_inscription) VALUES (NULL, '" +
                        str(pseudo)+"', '"+str(mdp)+"', '"+str(date)+"')")
        db.commit()
        return True
    except:
        return "Le pseudo existe déjà."


def verif_connexion(pseudo: str, mdp: str):
    """
    Vérifie si l'utilisateur est le bon et le mdp aussi
    """
    try:
        # curseur.execute("SELECT pseudo, mdp FROM Joueur WHERE pseudo="+str(pseudo)" AND mdp="+str(mdp)+"")
        return True
    except:
        return "Pseudo ou mdp incorrect"


def get_classement(pseudo: str):
    """
    Getter du classement
    """
    curseur.execute("SELECT classement FROM Joueur WHERE pseudo='"+pseudo+"'")
    row = curseur.fetchall()
    print(row[0][0])


######################################################## TESTS#########################################################################


# curseur.execute("INSERT INTO joueur(idJoueur, pseudo, mdp, date_inscription) VALUES (NULL,'simple6','mdp6', '2023-05-11 09:04:00');")
# db.commit()
pseudo = get_pseudo()
# print(type(pseudo[0][0]))
get_mdp("Bg3")
get_defaite("Bg7")
liste = [None, None, 9, None, None, None, None, 1, 4], [1, None, 4, None, None, None, 6, 5, 2], [None, 3, 5, None, 2, None, None, None, 8], [None, 5, 7, None, 3, 1, 2, 6, 9], [None, 6, None, None, None, None,
                                                                                                                                                                                None, 3, None], [3, None, None, None, None, 2, None, 8, None], [None, None, 8, None, 9, None, None, 2, 1], [9, None, None, 7, None, None, 8, None, None], [None, 1, None, None, None, 8, None, None, None]
# set_grille_profil("0",str(liste))
# set_user("Bg8","mdpbien")
# set_profil_stat("Bg6")
get_board(0)
# print(verif_connexion("Bg7","mdpbien"))
# get_mdp("Benoit")
print(curseur.execute(
    "SELECT pseudo, mdp FROM Joueur WHERE pseudo='Bg7' AND mdp='mdpbien'"))
db.close()
