from fltk import *

cree_fenetre(400, 400)

chaine = "Texte !!"
police = "Courier"
taille = 72
texte(200, 200, chaine,
      police=police, taille=taille, couleur="red",
      ancrage='center')

longueur, hauteur = taille_texte(chaine, police, taille)
rectangle(200 - longueur//2, 200 - hauteur//2,
          200 + longueur//2, 200 + hauteur//2,
          couleur="blue")

attend_ev()
ferme_fenetre()
