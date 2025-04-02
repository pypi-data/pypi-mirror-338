from fltk import *

cree_fenetre(400, 400)
  
rectangle(10, 10, 100, 50, remplissage="red")
rectangle(200, 100, 300, 150, remplissage="blue")

attend_ev()
ferme_fenetre()
