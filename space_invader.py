import tkinter as tk
from random import randint as rd



Application = tk.Tk()

can_jeu=tk.Canvas(bg='brown', width=906, height=650)
can_jeu.place(x=10,y=12)







Application.title("Space Invaders")
Application.geometry("1400x900")
#Application.configure(background='green')
Application['background'] = 'green'


##----- Programme principal -----##
Application.mainloop()# Boucle d'attente des événements
