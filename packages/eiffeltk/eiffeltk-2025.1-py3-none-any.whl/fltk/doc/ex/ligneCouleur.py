from fltk import *

cree_fenetre(400, 400)

ligne(0, 0, 399, 399, couleur="red")  # ligne rouge
ligne(0, 399, 399, 0, couleur="blue")  # ligne bleue
ligne(0, 200, 399, 200, epaisseur=2, couleur="green")  # ligne verte
ligne(200, 0, 200, 399, couleur="yellow", epaisseur=2)  # ligne jaune

attend_ev()
ferme_fenetre()
