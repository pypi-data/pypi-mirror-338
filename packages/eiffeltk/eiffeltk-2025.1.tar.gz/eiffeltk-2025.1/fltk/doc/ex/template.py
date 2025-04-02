#BEGIN TEMPLATE BASE
from fltk import *

cree_fenetre(400, 300)
# votre code ici!
...
ferme_fenetre()
#END TEMPLATE BASE

#BEGIN TEMPLATE IMPORT
import fltk

fltk.cree_fenetre(400, 300)
# votre code ici!
...
fltk.ferme_fenetre()
#END TEMPLATE IMPORT

#BEGIN TEMPLATE ATTENTE
from fltk import *

cree_fenetre(400, 300)
attend_ev()  # bloque l'exécution jusqu'à un clic ou une touche
ferme_fenetre()
#END TEMPLATE ATTENTE
