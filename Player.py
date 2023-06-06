class Player():
    idJoueur:int = None
    pseudo:str = None

    def __init__(self, idJoueur:int, pseudo:str):
        self.idJoueur = idJoueur
        self.pseudo = pseudo
        
    def __str__(self):
        return "Player("+str(self.idJoueur)+","+str(self.pseudo)+")"
    
    def __repr__(self):
        return self.__str__()
    
    def get_idJoueur(self) -> int:
        return self.idJoueur
    
    def get_pseudo(self) -> str:
        return self.pseudo