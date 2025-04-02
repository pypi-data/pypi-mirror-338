from fltk import *

cree_fenetre(400, 400)

# sans redimensionnement
im = image(133, 200, 'emoji.png', largeur=100, hauteur=100, ancrage='center', tag='im')

while True:
    mise_a_jour()
    ev = donne_ev()
    tev = type_ev(ev)
    if tev == 'Quitte':
        break
    elif tev == 'Touche':
        sym = touche(ev)
        if sym == 'Left':
            rotation_image(im, 45)
        elif sym == 'Right':
            rotation_image(im, -45)
        elif sym == 'Up':
            redimensionne_image(im, 3/2)
        elif sym == 'Down':
            redimensionne_image(im, 2/3)

efface(im)
ferme_fenetre()
