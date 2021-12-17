import tkinter as tk
from random import randint as rd



Application = tk.Tk()

can_jeu=tk.Canvas(bg='brown', width=1100, height=600)
can_jeu.place(x=200,y=50)
label_title = tk.Label(text ="Bienvenue sur notre Space Invader !",font=("Helvetica", 30),bg = "green")
label_title.place(x=470,y=3)
bouton_start = tk.Button(text='Start', width='9', height='1',font=("Helvetica", 30),fg="red" )
bouton_start.place(x=40, y=730)
bouton_quit = tk.Button(text='Exit', width='9', height='1',font=("Helvetica", 30),fg="red", command = Application.destroy)
bouton_quit.place(x=1200, y=730)
OptionList = ["sucre d'orge", "boule de neige"]
variable = tk.StringVar(Application)
variable.set(OptionList[0])

opt_menu = tk.OptionMenu(Application, variable, *OptionList)
opt_menu.config(width = 11, font = ('Helvetica', 20), bg="green")
opt_menu.place(x=20,y=80)
label_menu= tk.Label(text ="Niveau",font=("Helvetica", 20),bg = "green")
label_menu.place(x=55,y=45)
pere_noel=tk.PhotoImage(file ="pere_noel.png")
papa=can_jeu.create_image(570,520,image=pere_noel)
can_jeu.config(highlightthickness=0)


def déplacement (event):
    global coords
    if (can_jeu.coords(pere_noel)[3]<1100 or can_jeu.coords(pere_noel)[1]<0) :
        dy = -1 * dy

        can_jeu.move(papa, 10 , 0 )

can_jeu.bind_all('<Right>', droite)

def gauche (event):
    can_jeu.move(papa, -10 , 0 )
can_jeu.bind_all('<Left>', gauche)

Application.title("Space Invaders")
Application.geometry("1400x900")
Application.configure(bg='green')



##----- Programme principal -----##
Application.mainloop()# Boucle d'attente des événements
