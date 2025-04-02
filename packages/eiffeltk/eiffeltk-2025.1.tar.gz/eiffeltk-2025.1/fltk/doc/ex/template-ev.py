from fltk import *

cree_fenetre(400,400)
while True:
    ev = donne_ev()
    tev = type_ev(ev)

    # Code traitant l'évènement
    ...

    mise_a_jour()    
ferme_fenetre()