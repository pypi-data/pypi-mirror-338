from fltk import *


def carre(x, y, cote):
    rectangle(x, y, x + cote, y + cote,
              "red", "red", tag='carre')


cree_fenetre(400, 400)

# dessin initial du carré
cx, cy, taille = 0, 0, 10
carre(cx, cy, taille)

# déplacement en pixels à chaque flèche pressée
dep = 5

while True:
    ev = donne_ev()
    tev = type_ev(ev)
    if tev == 'Quitte':
        break

    # déplacement du carré
    dx = 0
    dy = 0
    if touche_pressee('Left'):
        dx -= min(dep, cx)
    if touche_pressee('Right'):
        dx += min(dep, 399 - cx - taille)
    if touche_pressee('Down'):
        dy += min(dep, 399 - cy - taille)
    if touche_pressee('Up'):
        dy -= min(dep, cy)

    if dx != 0 or dy != 0:
        cx = cx + dx
        cy = cy + dy
        deplace('carre', dx, dy)

    mise_a_jour()    
ferme_fenetre()