.. currentmodule:: fltk 

Dessins et coloriages
=====================

Il est possible avec ``fltk`` de tracer des formes géométriques de différentes
tailles et couleurs. Avant de présenter les fonctions pour tracer des
lignes, rectangles et cercles, il faut comprendre comment parler des
différents points de la fenêtre.

Une fênetre de dimensions 400 par 300, comme celle qui est créée par
l'appel ``cree_fenetre(400, 300)``, est un tableau de 400 *pixels* de
large sur 300 *pixels* de haut. Les *pixels* sont désignés par leur
coordonnées comme suit:

* le pixel du coin supérieur gauche de l'image à les coordonnées ``(0,
  0)``
* le pixel immédiatement à la droite du pixel ``(0, 0)`` a les
  coordonnées ``(1, 0)``
* le pixel immédiatement en dessous du pixel ``(0, 0)`` a les
  coordonnées ``(0, 1)``

et ainsi de suite. Ainsi le coin inférieur droit a pour coordonnées
``(399, 299)``.

.. image:: images/pixels.png
   :width: 500 px
   :align: center

Pour se familiariser avec les coordonnées des pixels,
on peut passer le paramètre optionnel ``affichage_repere=True`` à la fonction.
Ainsi ``cree_fenetre(400, 300, affiche_repere=True)`` ouvre la fenêtre suivante :

.. image:: images/repere.png
   :width: 400 px
   :align: center

On peut également dessiner le repère à tout moment en appelant manuellement la fonction ``repere`` :

.. autofunction:: repere

.. warning:: Les objets ne sont pas dessinés immédiatement sur la
   fenêtre. Pour qu'ils apparaissent, il faut faire appel à la
   fonction :py:func:`mise_a_jour`. Les fonctions :py:func:`attente` et
   :py:func:`attend_ev` provoquent aussi l'affichage de tous les dessins en
   attente.

Lignes
-----------------

Pour tracer une ligne entre le point ``(ax, ay)`` et le point ``(bx,
by)``, on utilise la fonction :py:func:`ligne` :

.. autofunction:: ligne

La fonction :py:func:`ligne` doit recevoir au minimum quatre
paramètres ``ax``, ``ay``, ``bx`` et ``by``, qui désignent les
coordonnées des extrémités du segment à dessiner. Les autres
paramètres sont optionnels, ils prennent une valeur par défaut s'ils
sont omis. 

Appels simples
^^^^^^^^^^^^^^^^^^^^^^^^^

L'appel le plus simple, tel que ``ligne(0, 0, 399, 399)``, trace donc
un segment noir d'un pixel d'épaisseur. Par exemple, le programme
ci-dessous trace une ligne entre le coin supérieur gauche de la
fenêtre et le coin inférieur droit :

.. literalinclude:: ex/ligne.py

.. image:: images/ligne.png
   :width: 200 px
   :align: center

Variantes
^^^^^^^^^^^^^^^^^^^^^^^^^
 
Pour tracer une ligne de trois pixels d'épaisseur en
vert, il faudra utiliser l'appel ::

  ligne(0, 0, 399, 399, 'green', 3)

ou encore ::

  ligne(0, 0, 399, 399, couleur='green', epaisseur=3)

Voici un exemple utilisant ces paramètres optionnels :

.. literalinclude:: ex/ligneCouleur.py

.. image:: images/ligneCouleur2.png
   :width: 200 px
   :align: center

Étiquettes
^^^^^^^^^^^^^^^^^^^^^^^^^
 
Le paramètre ``tag`` joue un rôle particulier, c'est une chaîne de
caractères appelée *étiquette* (valeur par défaut : pas d'étiquette),
qui permet de désigner facilement par la suite l'objet ligne créé, par
exemple pour le détruire avec la fonction :func:`efface`. Pour plus de
détails, voir la section :doc:`effacer`.


Flèches
------------------

Pour dessiner une flèche entre le point ``(ax,ay)`` et le point
``(bx,by)``, on utilise la fonction :func:`fleche`:

.. autofunction:: fleche

Son comportement est le même que celui de la fonction :func:`ligne`,
elle peut recevoir les mêmes arguments optionnels ``couleur``,
``epaisseur`` et ``tag``, avec les mêmes valeurs par défaut. Par
exemple, le programme ci-dessous trace plusieurs flèches de couleurs
différentes partant du coin supérieur gauche de la fenêtre :

.. literalinclude:: ex/fleches.py

.. image:: images/fleches.png
   :width: 200 px
   :align: center


Rectangles
---------------------

Pour tracer un rectangle ayant le point ``(ax, ay)`` et le point
``(bx, by)`` pour coins opposés, on utilise la fonction
:func:`rectangle`:

.. autofunction:: rectangle

Comme pour les fonctions précédentes, les quatre premiers paramètres
sont obligatoires. La fonction peut en outre recevoir les arguments
optionnels ``couleur``, ``epaisseur`` et ``tag`` déjà décrits, ainsi
qu'un argument optionnel ``remplissage`` décrivant la couleur de fond
du rectangle.

.. literalinclude:: ex/rectangles.py

.. image:: images/rectangles.png
   :width: 200 px
   :align: center

Voici un autre exemple utilisant un argument optionnel :

.. literalinclude:: ex/rectanglesCouleur.py

.. image:: images/rectanglesCouleur.png
   :width: 200 px
   :align: center

Et un dernier exemple dessinant un rectangle plein :

.. literalinclude:: ex/rectanglesPlein.py

.. image:: images/rectanglesPlein.png
   :width: 200 px
   :align: center

Cercles, arcs et ovales
-----------------------

Pour tracer un cercle de centre ``(ax, ay)`` et de rayon ``r``, on
utilise la fonction :func:`cercle`:

.. autofunction:: cercle

Les trois premiers paramètres sont obligatoires. Comme pour les
fonctions précédentes, la fonction peut en outre recevoir les
arguments optionnels ``couleur``, ``remplissage``, ``epaisseur`` et
``tag`` déjà décrits.

.. literalinclude:: ex/cercle.py

.. image:: images/cercle.png
   :width: 200 px
   :align: center

.. literalinclude:: ex/cerclesCouleur.py

.. image:: images/cerclesCouleur.png
   :width: 200 px
   :align: center

Pour tracer un arc de cercle de centre ``(ax, ay)``, de rayon ``r`` et
possédant un angle de ``ouverture`` degrés à partir de l'angle ``depart``, on
utilise la fonction :func:`arc` :

.. autofunction:: arc

Les trois premiers paramètres sont obligatoires. Tous les autres paramètres
sont identiques à ceux de la fonction :func:`cercle`, à l'exception de
``ouverture`` (valeur par défaut : 90) et ``depart`` (valeur initiale 0 pour
'est').

Pour tracer un ovale inscrit dans le rectangle de coins opposés ``(ax, ay)``
et ``(bx, by)``, on utilise la fonction :func:`ovale` :

.. autofunction:: ovale

Les quatre premiers paramètres sont obligatoires. Tous les autres paramètres
sont identiques à ceux de la fonction :func:`cercle`.


Polygones
---------------------

Pour tracer un polygone ayant comme liste de points ``points`` (liste
de couples de coordonnées) on peut utiliser la fonction
:func:`polygone`:

.. autofunction:: polygone

Comme pour les fonctions précédentes, la fonction peut en outre
recevoir les arguments optionnels ``couleur``, ``remplissage``,
``epaisseur`` et ``tag`` déjà décrits.

Texte
---------------------------

Pour afficher du texte dans la fenêtre (et non dans la console
python), on dispose de la fonction :func:`texte`:

.. autofunction:: texte

La chaîne de caractères ``chaine`` est écrite sur la fenêtre de façon
à ce que le point ``(x,y)`` se trouve dans le coin supérieur gauche du
rectangle englobant le texte. Les arguments optionnels ``couleur``,
``ancrage``, ``police`` et ``taille`` permettent de spécifier la
couleur du texte, la position du point d'ancrage par rapport au texte,
la police de caractères et la taille du texte.

.. literalinclude:: ex/texte.py

.. image:: images/texte.png
   :width: 200 px
   :align: center

Points d'ancrage
^^^^^^^^^^^^^^^^^^^^^^^^ 

Les valeurs possibles pour l'argument optionnel ``ancrage`` sont les
chaînes ``'center'``, ``'n'``, ``'s'``, ``'e'``, ``'o'``, ``'nw'``, ``'sw'``,
``'ne'``, et ``'se'``, chacune désignant une position cardinale possible
du point ``(x, y)`` par rapport au texte.

.. literalinclude:: ex/texteCentre.py

.. image:: images/texteCentre.png
   :width: 200 px
   :align: center

Dimensions du texte
^^^^^^^^^^^^^^^^^^^^^^^^

Il est possible de connaître la hauteur et la largeur qu'occupe un
texte à l'écran grâce à la fonction :func:`taille_texte`. 

.. autofunction:: taille_texte

Par exemple :

.. code-block:: python

    >>> taille_texte('Bonjour')
    28, 91

Le programme ci-dessous utilise ces fonctions pour encadrer le texte.

.. literalinclude:: ex/texteEncadre.py

.. figure:: images/texteEncadre.png
   :width: 200 px
   :align: center

Image
---------------------------

Pour inclure une image dans la fenêtre, on dispose de la fonction
:func:`image`:

.. autofunction:: image

Le nom de fichier ``file`` doit désigner une image de type ``.gif``,
``.pgm`` ou ``.ppm`` (ou d'autres formats si la bibliothèque Pillow est
installée). L' argument optionnel ``ancrage`` accepte les mêmes valeurs que
celui de la fonction :func:`texte` et produit les mêmes résultats. Les
arguments optionnels ``largeur`` et ``auteur`` permettent de spécifier la
taille d'image désirée (l'effet est plus précis avec le module Pillow).

.. literalinclude:: ex/image.py

.. image:: images/image.png
   :width: 200 px
   :align: center
