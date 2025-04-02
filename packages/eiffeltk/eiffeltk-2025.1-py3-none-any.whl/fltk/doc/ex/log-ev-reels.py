from fltk import *

cree_fenetre(400, 400)

while True:
    # On récupère le plus ancien événement en attente
    ev = donne_ev()

    # S'il ne vaut pas None, on affiche son type
    if ev is not None:
        print(type_ev(ev))

    # Important : on met à jour pour détecter les nouveaux événements
    mise_a_jour()
