import tkinter as tk
import random as rd



Application = tk.Tk()

class Santa_claus ():
   def __init__(self,liste_elfes,can_jeu,lutin,papa):
       self.vie = 3
       self.cadeau=tk.PhotoImage(file ="cadeau.png")
       self.liste_elfes = liste_elfes


   def tire(self, event):
     abscisse = can_jeu.coords(papa)[0]
     ordonee = 430
     gift = can_jeu.create_image(abscisse,ordonee,image=self.cadeau)
     self.deplacement_cadeau (gift)

   def deplacement_cadeau (self,gift) :
     can_jeu.move(gift, 0 , -20 )
     if can_jeu.coords(gift)[1] <= 25 :
         can_jeu.delete(gift)
         return
     if self.liste_elfes == [] :
         print('Gagné !!!!')
         return
     for elfe in self.liste_elfes :
         coordonnees = can_jeu.coords(elfe)
         if coordonnees[0]-30 < can_jeu.coords(gift)[0] < coordonnees[0]+30 and coordonnees[1]-30 < can_jeu.coords(gift)[1] < coordonnees[1]+30 :
             self.liste_elfes.remove(elfe)
             can_jeu.delete(gift)
             can_jeu.delete(elfe)
             return
     Application.after(80,lambda : self.deplacement_cadeau(gift))

   def droite (self,event):
         if can_jeu.coords(papa)[0]<1050 :
             can_jeu.move(papa, 20 , 0 )

   def gauche (self,event):
         if can_jeu.coords(papa)[0]>50 :
             can_jeu.move(papa, -20 , 0 )


class Alien () :
   def __init__(self,lutin,papa):
       self.liste_elfes = []
       self.flocon=tk.PhotoImage(file ="flocon.png")

   def chute_flocon (self):
      if self.liste_elfes == [] :
             echec("Vous avez gagné")
             return
      lutin_random = rd.choice(self.liste_elfes)
      abscisse = can_jeu.coords(lutin_random)[0]
      ordonee = can_jeu.coords(lutin_random)[1]
      neige = can_jeu.create_image(abscisse,ordonee,image=self.flocon)
      self.deplacement_flocon(neige)
      Application.after(1500,self.chute_flocon)

   def deplacement_flocon (self,neige) :
      can_jeu.move(neige, 0 , 10 )
      if liste_rennes==[] :
           return
      for j in range(len(liste_rennes)) :
           for animal in liste_rennes[j] :
               coordonnees = can_jeu.coords(animal)
               if coordonnees[0]-30 < can_jeu.coords(neige)[0] < coordonnees[0]+30 and coordonnees[1]-30 < can_jeu.coords(neige)[1] < coordonnees[1]+30 :
                   liste_rennes[j].remove(animal)
                   can_jeu.delete(animal)
                   can_jeu.delete(neige)
                   return
      global fin_du_jeu
      Application.after(70,lambda : self.deplacement_flocon(neige))
      coordonnees = can_jeu.coords(papa)

      if can_jeu.coords(neige) :
           if coordonnees[0]-40 < can_jeu.coords(neige)[0] < coordonnees[0]+40 and coordonnees[1]-40 < can_jeu.coords(neige)[1] < coordonnees[1]+40 :
               can_jeu.delete(neige)
               print('Vous avez perdu une vie!!!!')
               can_jeu.coords(papa, 570,540)
               santa.vie = santa.vie - 1
               label_vie.config(text = "Vies restantes : " + str(santa.vie) + "/3" )
      if santa.vie == 0 :
          if fin_du_jeu == 0 :
               fin_du_jeu = 10
               echec("Vous avez perdu")
               return

   def deplacement_lutin(self,elfe) :
     global x
     peut_bouger = False
     if self.liste_elfes == [] :
         return
     for gnome in self.liste_elfes :
         dx = can_jeu.coords(gnome)[0]
         dy = can_jeu.coords(gnome)[1]
         if dx<50 or dx>1050:
             peut_bouger = True
         elif dy > 330 :
             return
     if peut_bouger == True :
         x=-1*x
         for gnome in self.liste_elfes :
             can_jeu.move(gnome, 0 , 10 )
     for gnome in self.liste_elfes :
         can_jeu.move(gnome, x , 0 )
     Application.after(1000,lambda : self.deplacement_lutin(elfe))

##### ----- Fonctions ----- #####

def echec(texte) :
   print("fonction echec")
   popup = tk.Toplevel(Application)
   popup.geometry("420x290")
   can_echec = tk.Canvas(popup)
   can_echec.create_text(210,160,font=("Helvetica", 15), text= texte)
   can_echec.pack(expand='Yes')
   bouton_recommencer = tk.Button(popup, text= 'Recommencer',width='7', height='1',font=("Helvetica", 20),)
   bouton_recommencer.place(x=150, y=255)
   bouton_arreter = tk.Button(popup, text= 'Arreter',width='7', height='1',font=("Helvetica", 20),command = Application.destroy)
   bouton_arreter.place(x=150, y=255)
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

def placement_lutins (liste_elfes,ordonnee) :
    abscisse = 60
    for i in range(8) :
        elfe = can_jeu.create_image(abscisse,ordonnee,image=lutin)
        alien.liste_elfes.append(elfe)
        abscisse += 70

def deplacement_pain (can_jeu,pain):
   abscisse = can_jeu.coords(pain)[0]
   if abscisse > 1300 :
       can_jeu.delete(pain)
       pain = can_jeu.create_image(20,40,image=pain_epice)
   else :
       can_jeu.move (pain, 8,0)
   Application.after(80,lambda : deplacement_pain (can_jeu,pain))

###### ----- Relatif à Tkinter ----- #####

can_jeu=tk.Canvas(bg='brown', width=1100, height=600)
can_jeu.place(x=200,y=50)
x=1

lutin=tk.PhotoImage(file ="lutin.png")
pere_noel=tk.PhotoImage(file ="pere_noel.png")

pain_epice = tk.PhotoImage(file ="pain_epice.png")
pain = can_jeu.create_image(20,40,image=pain_epice)

deplacement_pain (can_jeu,pain)

papa = can_jeu.create_image(570,540,image=pere_noel)

alien = Alien(lutin,papa)
santa = Santa_claus(alien.liste_elfes,can_jeu,lutin,papa)

label_title = tk.Label(text ="Bienvenue sur notre Space Invader !",font=("Helvetica", 30),bg = "green")
label_title.place(x=470,y=3)
label_vie = tk.Label(text ="Vies restantes : " + str(santa.vie) + "/ 3" ,font=("Helvetica", 20),bg = "green")
label_vie.place(x=0, y=150)
label_menu= tk.Label(text ="Niveau",font=("Helvetica", 20),bg = "green")
label_menu.place(x=55,y=45)

bouton_start = tk.Button(text='Start', width='9', height='1',font=("Helvetica", 30),fg="red" )
bouton_start.place(x=40, y=730)
bouton_quit = tk.Button(text='Exit', width='9', height='1',font=("Helvetica", 30),fg="red", command = Application.destroy)
bouton_quit.place(x=1200, y=730)

OptionList = ["sucre d'orge", "boule de neige"]
variable = tk.StringVar(Application)
variable.set(OptionList[0])
fin_du_jeu = 0

renne=tk.PhotoImage(file ="renne.png")

opt_menu = tk.OptionMenu(Application, variable, *OptionList)
opt_menu.config(width = 11, font = ('Helvetica', 20), bg="green")
opt_menu.place(x=20,y=80)

can_jeu.config(highlightthickness=0)


Application.title("Space Invaders")
Application.geometry("1400x900")
Application.configure(bg='green')

###### ----- Programme principal ----- #####

liste_rennes = []
placement_rennes (liste_rennes,460,10)
placement_rennes (liste_rennes,420,10)
placement_rennes (liste_rennes,380,10)


placement_lutins (alien.liste_elfes,100)
placement_lutins (alien.liste_elfes,160)
placement_lutins (alien.liste_elfes,220)

alien.chute_flocon ()

for elfe in alien.liste_elfes :
  alien.deplacement_lutin(elfe)



##### ----- Réaction avec le clavier / écran ----- #####

can_jeu.bind_all('<Right>', santa.droite)
can_jeu.bind_all('<Left>', santa.gauche)
can_jeu.bind_all('<space>', santa.tire)


##### ----- Boucle principale ----- #####

Application.mainloop()# Boucle d'attente des événements