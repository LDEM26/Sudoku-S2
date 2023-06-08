from CredentialsCtxRessources.BaseCtx import BaseCtx
from tkinter import Button, Toplevel


class LoginCtx(BaseCtx):
    def get_title(self):
        return "Connexion"


    def go_to_registration(self):
        registration_ctx = self.get_registration_ctx()
        registration_ctx.generate()


    def generate(self):
        super().generate()  # Appelle la méthode generate de la classe parente

        btnRegistration = Button(
            self.ctx, text="Inscription", command=self.go_to_registration)
        btnRegistration.pack()

        self.ctx.mainloop()

    def get_registration_ctx(self):
        from CredentialsCtxRessources.RegistrationCtx import RegistrationCtx
        return RegistrationCtx(self.ctx)
