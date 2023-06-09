from tkinter import *
from MySQL import MySQL
from cryptographiemdp import *

class BaseCtx:
    ctx: Tk = None
    pswd: Entry = None
    usr: Entry = None
    connected = False

    def __init__(self, ctx: Tk = None):
        self.ctx = ctx
        
    def show_error(self, message):
        error_label = Label(self.ctx, text=message, fg="red")
        error_label.pack()

    def generate(self):
        if self.ctx == None:
            self.ctx = Tk()
            self.ctx.geometry('800x500')
            self.ctx.title(self.get_title())
        frame = Frame(self.ctx, width=100, height=0)
        frame.place(x=350, y=100)

        user = Label(frame, text="Identifiant")
        self.usr = Entry(frame)
        user.pack()
        self.usr.pack()

        paswd = Label(frame, text="Mot de passe")
        self.pswd = Entry(frame, show="*")
        paswd.pack()
        self.pswd.pack()

        btnValid = Button(frame, bg='#45e325', text='Valider', fg='black', height=0, command=self.check)
        btnValid.place(x=350, y=200)
        btnValid.pack()

        self.error_label = Label(self.ctx, text="", fg="red")
        self.error_label.pack()

    def get_ctx(self) -> Tk:
        return self.ctx

    def get_pswd(self) -> str:
        return self.pswd.get()

    def get_usr(self) -> str:
        return self.usr.get()

    def show_error(self, message):
        self.error_label.config(text=message)

    def check(self):
        usr = self.get_usr()
        pswd = self.get_pswd()
        #cle = charger_cle('cle.txt')

        passwd = MySQL.askOne(f"SELECT idJoueur, mdp FROM joueur WHERE pseudo = '{usr}'")
        if passwd is None:
            self.show_error("L'utilisateur n'existe pas")
            return

        if passwd[1] != pswd:          #decryptage non fonctionnel à inserer.
            self.show_error("Le mot de passe est incorrect")
            return

        self.ctx.destroy()
        self.connected = (passwd[0], usr)
        return True

    def get_connected(self):
        return self.connected

    def get_title(self):
        raise NotImplementedError("La méthode get_title doit être implémentée dans la classe enfant.")