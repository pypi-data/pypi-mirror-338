from fltk import *

cree_fenetre(400, 400)

# sans redimensionnement
image(133, 200, 'emoji.png',
      largeur=150, hauteur=150, ancrage='center', tag='im')

# avec redimensionnement
image(250, 200, 'emoji.png',
      largeur=200, hauteur=200, ancrage='center', tag='im')

attend_ev()
efface('im')
ferme_fenetre()
