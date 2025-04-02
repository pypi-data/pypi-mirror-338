from fltk import *

cree_fenetre(400, 400)

ligne(0, 0, 200, 200)  
fleche(0, 0, 200, 200, couleur="black")  

ligne(0, 0, 100, 50, couleur="red")  
fleche(0, 0, 100, 50, couleur="red")  

attend_ev()
ferme_fenetre()
