import mysql.connector
from credentialsExample import Credentials

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
    def askAll(query: str):
        """
        Permet d'envoyer une requête à la BDD
        """
        db = MySQL.connect()
        curseur = db.cursor()
        curseur.execute(query)
        res = curseur.fetchall()
        db.close()
        return res
    
    @staticmethod
    def askOne(query: str):
        """
        Permet d'envoyer une requête à la BDD
        """
        db = MySQL.connect()
        curseur = db.cursor()
        curseur.execute(query)
        res = curseur.fetchone()
        db.close()
        return res
    
    @staticmethod
    def askNoReturn(query: str):
        """
        Permet d'envoyer une requête à la BDD
        """
        db = MySQL.connect()
        curseur = db.cursor()
        curseur.execute(query)
        db.commit()
        db.close()