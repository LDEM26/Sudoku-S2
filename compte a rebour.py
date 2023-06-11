import tkinter as tk
import time

# Durée du compte à rebours en secondes
duree = 3 * 60  # 3 minutes

# Fonction à déclencher lorsque le compte à rebours atteint 0
def fonction_a_declencher():
    print("caca")

# Fonction pour mettre à jour le compte à rebours
def mettre_a_jour_compte_a_rebours():
    temps_ecoule = int(time.time() - temps_debut)
    temps_restant = max(duree - temps_ecoule, 0)
    minutes = temps_restant // 60
    secondes = temps_restant % 60
    temps_texte = f"Temps restant : {minutes:02d}:{secondes:02d}"
    label_compte_a_rebours.config(text=temps_texte)
    if temps_ecoule < duree:
        fenetre.after(1000, mettre_a_jour_compte_a_rebours)
    else:
        fonction_a_declencher()

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Compte à rebours")

# Création de la frame pour afficher le compte à rebours
frame_compte_a_rebours = tk.Frame(fenetre, padx=20, pady=20)
frame_compte_a_rebours.pack()

# Création du label pour afficher le compte à rebours
label_compte_a_rebours = tk.Label(frame_compte_a_rebours, text="Temps restant : 03:00", font=("Arial", 24))
label_compte_a_rebours.pack()

# Début du compte à rebours
temps_debut = time.time()

# Démarrage de la mise à jour du compte à rebours
fenetre.after(1000, mettre_a_jour_compte_a_rebours)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()
