from fltk import *

cree_fenetre(400, 400)

c = cercle(200, 200, 50)
attend_ev()

modifie(c, couleur='red', remplissage='grey')
attend_ev()

ferme_fenetre()
