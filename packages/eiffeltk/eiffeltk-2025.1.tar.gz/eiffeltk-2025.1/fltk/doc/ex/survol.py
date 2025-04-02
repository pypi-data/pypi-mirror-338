from fltk import *

cree_fenetre(400, 400)

cercle(100, 150, 50, remplissage='black', epaisseur=4)
cercle(300, 150, 50, remplissage='black', epaisseur=4)
texte(200, 300, "Texte", taille=50, ancrage='c', couleur='black', tag="texte")
objet = ancien = None
ancien_remplissage = ''

while True:
    mise_a_jour()
    ev = donne_ev()
    tev = type_ev(ev)
    if tev == 'Quitte':
        break
    elif tev == 'ClicGauche':
        objet = objet_survole()
        if objet is None:
            continue
        if remplissage(objet) == 'black':
            modifie(objet, remplissage='blue')
        else:
            modifie(objet, remplissage='black')
    elif tev == 'ClicDroit':
        objet = objet_survole()
        if objet is None:
            continue
        if couleur(objet) == 'black':
            modifie(objet, couleur='red')
        else:
            modifie(objet, couleur='black')

    if est_objet_survole("texte"):
        modifie("texte", remplissage="red")
    else:
        modifie("texte", remplissage="black")

ferme_fenetre()
