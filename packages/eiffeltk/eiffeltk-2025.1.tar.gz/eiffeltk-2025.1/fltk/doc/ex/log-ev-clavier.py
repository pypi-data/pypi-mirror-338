from fltk import *

cree_fenetre(400, 400)

while True:
    ev = donne_ev()
    tev = type_ev(ev)

    # Action dépendant du type d'événement reçu :

    if tev == 'Touche':  # on indique la touche pressée
        print('Appui sur la touche', touche(ev))

    elif tev == 'Quitte':  # on sort de la boucle
        break

    else:  # dans les autres cas, on ne fait rien
        pass

    mise_a_jour()

ferme_fenetre()