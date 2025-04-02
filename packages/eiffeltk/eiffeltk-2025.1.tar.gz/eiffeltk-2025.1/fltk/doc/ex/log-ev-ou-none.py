from fltk import *

cree_fenetre(400, 400)

while True:
    # On récupère le plus ancien événement en attente
    ev = donne_ev()

    # On affiche son type
    print(type_ev(ev))
