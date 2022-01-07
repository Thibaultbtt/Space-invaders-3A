import tkinter as tk
import random as rd



Application = tk.Tk()

renne=tk.PhotoImage(file ="renne.png")
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
vie = []
label_vie = tk.Label(text ="Nb de fois touché : " + str(len(vie)) ,font=("Helvetica", 20),bg = "green")
label_vie.place(x=0, y=150)
fin_du_jeu = 0

opt_menu = tk.OptionMenu(Application, variable, *OptionList)
opt_menu.config(width = 11, font = ('Helvetica', 20), bg="green")
opt_menu.place(x=20,y=80)
label_menu= tk.Label(text ="Niveau",font=("Helvetica", 20),bg = "green")
label_menu.place(x=55,y=45)
pere_noel=tk.PhotoImage(file ="pere_noel.png")
papa=can_jeu.create_image(570,520,image=pere_noel)
can_jeu.config(highlightthickness=0)


def droite (event):
  if can_jeu.coords(papa)[0]<1050 :
      can_jeu.move(papa, 20 , 0 )

can_jeu.bind_all('<Right>', droite)

def gauche (event):
  if can_jeu.coords(papa)[0]>50 :
      can_jeu.move(papa, -20 , 0 )
can_jeu.bind_all('<Left>', gauche)

lutin=tk.PhotoImage(file ="lutin.png")
flocon=tk.PhotoImage(file ="flocon.png")
x=6

def chute_flocon ():
   if liste_elfes == [] :
          return
   lutin_random = rd.choice(liste_elfes)
   abscisse = can_jeu.coords(lutin_random)[0]
   ordonee = can_jeu.coords(lutin_random)[1]
   neige = can_jeu.create_image(abscisse,ordonee,image=flocon)
   deplacement_flocon(neige)
   Application.after(1500,chute_flocon)

def deplacement_flocon (neige) :
   global fin_du_jeu
   can_jeu.move(neige, 0 , 10 )
   Application.after(70,lambda : deplacement_flocon(neige))
   coordonnees = can_jeu.coords(papa)
  
   if can_jeu.coords(neige) :
        if coordonnees[0]-40 < can_jeu.coords(neige)[0] < coordonnees[0]+40 and coordonnees[1]-40 < can_jeu.coords(neige)[1] < coordonnees[1]+40 :
            can_jeu.delete(neige)
            print('Vous avez perdu une vie!!!!')
            can_jeu.coords(papa, 570,520)
            vie.append(1)
            label_vie.config(text = "Nb de fois touché : " + str(len(vie)))
   if len(vie) == 3 :
       if fin_du_jeu ==0 :
       #print ("Vous avez perdu !!")
       #if fin_du_jeu != 10 :
         #  fin_du_jeu=1
       #if fin_du_jeu == 1 :
            echec()
            fin_du_jeu = 10
            return
       #return
liste_elfes = []
abscisse = 60
ordonnee = 100
for i in range(5) :
    elfe = can_jeu.create_image(abscisse,ordonnee,image=lutin)
    liste_elfes.append(elfe)
    abscisse += 200

chute_flocon ()

def deplacement_lutin(elfe) :
  global x
  peut_bouger = False
  if liste_elfes == [] :
      return
  for gnome in liste_elfes :
      dx = can_jeu.coords(gnome)[0]
      if dx<50 or dx>1050:
          peut_bouger = True
  if peut_bouger == True :
      x=-1*x
      for gnome in liste_elfes :
          can_jeu.move(gnome, 0 , 10 )
  for gnome in liste_elfes :
      can_jeu.move(gnome, x , 0 )
  Application.after(700,lambda : deplacement_lutin(elfe))

for elfe in liste_elfes :
   deplacement_lutin(elfe)

cadeau=tk.PhotoImage(file ="cadeau.png")

def tire(event):
  abscisse = can_jeu.coords(papa)[0]
  ordonee = 430
  gift=can_jeu.create_image(abscisse,ordonee,image=cadeau)
  deplacement_cadeau (gift)

def deplacement_cadeau (gift) :
  can_jeu.move(gift, 0 , -20 )
  if can_jeu.coords(gift)[1] <= 25 :
      can_jeu.delete(gift)
      return
  if liste_elfes == [] :
      print('Gagné !!!!')
      return
  for elfe in liste_elfes :
      coordonnees = can_jeu.coords(elfe)
      if coordonnees[0] < can_jeu.coords(gift)[0] < coordonnees[0]+30 and coordonnees[1] < can_jeu.coords(gift)[1] < coordonnees[1]+30 :
          liste_elfes.remove(elfe)
          can_jeu.delete(gift)
          can_jeu.delete(elfe)
          return
  Application.after(80,lambda : deplacement_cadeau(gift))

can_jeu.bind_all('<space>', tire)

def echec() :
    print("fonction echec")
    popup = tk.Toplevel(Application)
    popup.geometry("420x290")
    #popup.overrideredirect(1)
    can_echec = tk.Canvas(popup) 
    can_echec.create_text(210,160,font=("Helvetica", 15), text= "Vous avez perdu") 
    can_echec.pack(expand='Yes')
    bouton_recommencer = tk.Button(popup, text= 'Recommencer',width='7', height='1',font=("Helvetica", 20),) 
    bouton_recommencer.place(x=150, y=255)
    bouton_arreter = tk.Button(popup, text= 'Arreter',width='7', height='1',font=("Helvetica", 20),command = Application.destroy) 
    bouton_arreter.place(x=150, y=255)
    #popup.transient()  
    #popup.grab_set() 
    popup.update()

def placement_rennes (liste_rennes,ordonnee,nbre) :
    liste=[]
    liste_coord = []
    for i in range (nbre) :
        abscisse = rd.randint(50,1050)
        while abscisse%50 != 0 :
            abscisse = rd.randint(50,1050)
        for animal in liste :
            liste_coord.append(can_jeu.coords(animal)[0])
        while abscisse in liste_coord :
            print('while')
            abscisse = rd.randint(50,1050)
            while abscisse%50 != 0 :
                abscisse = rd.randint(50,1050)
        cerf = can_jeu.create_image(abscisse,ordonnee,image=renne)
        liste.append(cerf)
    liste_rennes.append(liste)

liste_rennes = []
placement_rennes (liste_rennes,400,10)
placement_rennes (liste_rennes,350,10)
placement_rennes (liste_rennes,300,10)

Application.title("Space Invaders")
Application.geometry("1400x900")
Application.configure(bg='green')




##----- Programme principal -----##
Application.mainloop()# Boucle d'attente des événements