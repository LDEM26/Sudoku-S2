import tkinter as tk
import time

# Durée du chronomètre en secondes
duree = 5 * 60  # 5 minutes

# Fonction pour mettre à jour le chronomètre
def mettre_a_jour_chronometre():
    temps_ecoule = int(time.time() - temps_debut)
    temps_restant = max(duree - temps_ecoule, 0)
    minutes = temps_restant // 60
    secondes = temps_restant % 60
    temps_texte = f"Temps restant : {minutes:02d}:{secondes:02d}"
    label_chronometre.config(text=temps_texte)
    if temps_ecoule < duree:
        fenetre.after(1000, mettre_a_jour_chronometre)
    else:
        label_chronometre.config(text="Chronomètre terminé.")

# Création de la fenêtre
fenetre = tk.Tk()
fenetre.title("Chronomètre")

# Création du label pour afficher le chronomètre
label_chronometre = tk.Label(fenetre, text="Temps restant : 05:00", font=("Arial", 24))
label_chronometre.pack(pady=20)

# Début du chronomètre
temps_debut = time.time()

# Démarrage de la mise à jour du chronomètre
fenetre.after(1000, mettre_a_jour_chronometre)

# Lancement de la boucle principale de la fenêtre
fenetre.mainloop()