from fltk import *

cree_fenetre(400, 400)

texte(0, 0, "Bonjour", couleur="red", taille=40)
texte(200, 300, "Au revoir", couleur="green", taille=18, police='Courier')

attend_ev()
ferme_fenetre()
