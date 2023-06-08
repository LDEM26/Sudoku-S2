import mysql.connector
from Credentials import Credentials


class MySQL:

    @staticmethod
    def connect():
        """
        Permet de se connecter à la BDD
        """
        db = mysql.connector.connect(
            host=Credentials.get_host(),
            user=Credentials.get_username(),
            password=Credentials.get_password(),
            database=Credentials.get_database()
        )
        return db

    @staticmethod
    def askAll(query: str, withCursor: bool = False):
        """
        Permet d'envoyer une requête à la BDD
        """
        db = MySQL.connect()
        curseur = db.cursor()
        curseur.execute(query)
        res = curseur.fetchall()
        db.close()
        return {"res": res, "cursor": curseur} if withCursor else res

    @staticmethod
    def askOne(query: str, withCursor: bool = False):
        """
        Permet d'envoyer une requête à la BDD
        """
        db = MySQL.connect()
        curseur = db.cursor()
        curseur.execute(query)
        res = curseur.fetchone()
        db.close()
        return {"res": res, "cursor": curseur} if withCursor else res

    @staticmethod
    def askNoReturn(query: str, withCursor: bool = False):
        """
        Permet d'envoyer une requête à la BDD
        """
        db = MySQL.connect()
        curseur = db.cursor()
        curseur.execute(query)
        db.commit()
        db.close()
        if withCursor:
            return curseur
