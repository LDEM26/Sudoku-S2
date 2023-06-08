import tkinter as tk

class Chrono:
    def init(self, fenetre):
        self.fenetre = fenetre
        self.temps = 0
        self.label_chrono = tk.Label(self.fenetre, text="0:00:00", font=("Helvetica", 24))
        self.label_chrono.pack()
        self.bouton_start = tk.Button(self.fenetre, text="Start", command=self.start_chrono)
        self.bouton_start.pack()
        self.bouton_stop = tk.Button(self.fenetre, text="Stop", command=self.stop_chrono)
        self.bouton_stop.pack()
        self.chrono_actif = False
        self.mise_a_jour_chrono()

    def mise_a_jour_chrono(self):
        if self.chrono_actif:
            self.temps += 1
        minutes = self.temps // 60
        secondes = self.temps % 60
        heures = minutes // 60
        minutes %= 60
        temps_formatte = f"{heures}:{minutes:02d}:{secondes:02d}"
        self.label_chrono.config(text=temps_formatte)
        self.fenetre.after(1000, self.mise_a_jour_chrono)

    def start_chrono(self):
        self.chrono_actif = True

    def stop_chrono(self):
        self.chrono_actif = False