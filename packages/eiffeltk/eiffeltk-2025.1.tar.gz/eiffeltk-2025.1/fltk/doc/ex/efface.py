from fltk import *

cree_fenetre(400, 400)

rect1 = rectangle(50, 50, 200, 200,
                  remplissage="red", tag="rectangle_rouge")
rect2 = rectangle(100, 100, 300, 300,
                  remplissage="blue")

attend_ev()
efface(rect2)
attend_ev()
efface("rectangle_rouge")
attend_ev()

ferme_fenetre()
