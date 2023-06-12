# Sudoku-S2
Projet sudoku info S2 pour la prépa
Ce projet a été réalisé par Lydie ARCHIDOIT, Elouan MOULIN et Léopold DE MARCO.
Il est codé entièrement sous la dernière version de python (3.11.x), et nécessite une base de donnée mySQL pour fonctionner.
Il vous faudra les scripts de la base de données ou bien les droits d'accès.


Avant de lancer : Nécessite le module mysql (mysql.connector), tkinter, sudoku (py-sudoku), datetime et cryptography.

Pour le lancer (en cas de problème avec laucher.bat) : Executer le fichier main.py

Une fenêtre tkinter s'ouvrira et demandera identifiant et mot de passe, une fois connecté il est possible de jouer.

Pour relier la base de données : Remplir le fichier "Credentials" contenant toutes les
informations pour relier BDD et la connexion MySQL sur python. Il s'agit d'une sécurité Github.
(Par défaut username = 'root' et host = '127.0.0.1' (ip locale)).