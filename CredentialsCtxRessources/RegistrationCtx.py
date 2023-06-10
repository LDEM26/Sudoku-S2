from CredentialsCtxRessources.BaseCtx import BaseCtx
from tkinter import Button, Frame, Label, Entry, Toplevel
from datetime import datetime
from MySQL import MySQL
from cryptographiemdp import *


class RegistrationCtx(BaseCtx):
    def get_title(self):
        return "Inscription"

    def register(self):
        usr = self.get_usr()
        pswd = self.get_pswd()

        if usr == "" or pswd == "":
            self.show_error("Veuillez remplir tous les champs")
            return

        r = self.set_user(usr, pswd)
        if r:
            self.ctx.destroy()
            super().set_connected(r[1], usr)
            return True
        else:
            self.show_error("L'utilisateur existe déjà")

    def generate(self):
        registration_window = Toplevel(self.ctx)
        registration_window.geometry('400x300')
        registration_window.title(self.get_title())

        frame = Frame(registration_window)
        frame.pack(padx=20, pady=20)

        user_label = Label(frame, text="Identifiant")
        user_label.pack()

        self.usr = Entry(frame)
        self.usr.pack()

        pswd_label = Label(frame, text="Mot de passe")
        pswd_label.pack()

        self.pswd = Entry(frame, show="*")
        self.pswd.pack()

        btnRegister = Button(frame, text="S'inscrire", command=self.register)
        btnRegister.pack()

        btnClose = Button(registration_window, text="Fermer", command=registration_window.destroy)
        btnClose.pack()

        self.error_label = Label(registration_window, text="", fg="red")  # Ajout du label d'erreur
        self.error_label.pack()

        registration_window.mainloop()

        return super().get_connected()

    @staticmethod
    def set_user(pseudo: str, mdp: str):
        #cle_chargee = charger_cle('cle.txt')               non fonctionnel.
        if RegistrationCtx.verif_pseudo_unique(pseudo):
            #print(crypter_mot_de_passe(cle_chargee, mdp))
            date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
            res = MySQL.askNoReturn(f"INSERT INTO joueur(idJoueur, pseudo, mdp, date_inscription) VALUES (NULL, '{pseudo}', '{mdp}', '{date}')", True) #cryptage non fonctionnel
            last_id = res.lastrowid
            MySQL.askNoReturn(f"INSERT INTO statistiques VALUES ({last_id}, 0, 0, 0, 0, 0, NULL, 0)")
            return True, last_id
        return False

    @staticmethod
    def verif_pseudo_unique(pseudo: str) -> bool:
        count = MySQL.askOne(f"SELECT COUNT(pseudo) FROM joueur WHERE pseudo = '{pseudo}'")
        return True if count[0] == 0 else False

    def show_error(self, message):
        self.error_label.config(text=message)

