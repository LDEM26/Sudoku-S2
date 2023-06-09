#Importer le module "cryptography"
from cryptography.fernet import Fernet

def generer_cle():
    """Génère une clé de chiffrement aléatoire"""
    return Fernet.generate_key()

def sauvegarder_cle(cle, nom_fichier):
    """Sauvegarde la clé dans un fichier, vous êtes la seule personne à disposer de
    la clé de déchiffrement
    """
    with open(nom_fichier, 'wb') as fichier:
        fichier.write(cle)

def charger_cle(nom_fichier):
    """Charge la clé à partir d'un fichier, vous êtes la seule personne à disposer de
    cette clé
    """
    with open(nom_fichier, 'rb') as fichier:
        return fichier.read()

def crypter_mot_de_passe(cle, mot_de_passe):
    """Crypte un mot de passe avec la clé spécifiée"""
    cipher_suite = Fernet(cle)
    mot_de_passe_crypte = cipher_suite.encrypt(mot_de_passe.encode())
    return mot_de_passe_crypte

def decrypter_mot_de_passe(cle, mot_de_passe_crypte):
    """Décrypte un mot de passe avec la clé spécifiée"""
    cipher_suite = Fernet(cle)
    mot_de_passe = cipher_suite.decrypt(mot_de_passe_crypte)
    return mot_de_passe.decode()


###########TESTS########


# Générer une clé
cle = generer_cle()

# Sauvegarder la clé dans un fichier
sauvegarder_cle(cle, 'cle.txt')

# Charger la clé à partir du fichier
cle_chargee = charger_cle('cle.txt')

mot_de_passe_original = "MotDePasse123"

mot_de_passe_crypte = crypter_mot_de_passe(cle_chargee, mot_de_passe_original)

print("Mot de passe crypté :", mot_de_passe_crypte)

mot_de_passe_decrypte = decrypter_mot_de_passe(cle_chargee, mot_de_passe_crypte)

print("Mot de passe décrypté :", mot_de_passe_decrypte)
