from fltk import *

nb_cases = 3


def dessine_quadrillage(largeur: int, hauteur: int, n: int):
    texte(largeur/2, hauteur/2,
          f"Taille de la fenêtre : {hauteur} x {largeur}",
          ancrage='c')
    hauteur_case = hauteur / n
    largeur_case = largeur / n
    x_courant = y_courant = 0.
    for i in range(1, n):
        x_courant += largeur_case
        ligne(x_courant, 0, x_courant, hauteur)
        y_courant += hauteur_case
        ligne(0, y_courant, largeur, y_courant)


if __name__ == "__main__":
    l_init = 600
    h_init = 400
    cree_fenetre(l_init, h_init, redimension=True)
    dessine_quadrillage(l_init, h_init, nb_cases)
    while True:
        ev = attend_ev()
        tev = type_ev(ev)
        if tev == "Quitte":
            ferme_fenetre()
            break
        elif tev == 'Redimension':
            efface_tout()
            dessine_quadrillage(largeur_fenetre(), hauteur_fenetre(), nb_cases)
        elif tev == 'Touche':
            tch = touche(ev)
            if tch == 'plus':
                larg = largeur_fenetre() * 1.2
                haut = hauteur_fenetre() * 1.2
                redimensionne_fenetre(larg, haut)
            elif tch == 'minus':
                larg = largeur_fenetre() / 1.2
                haut = hauteur_fenetre() / 1.2
                redimensionne_fenetre(larg, haut)
