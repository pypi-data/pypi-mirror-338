.. currentmodule:: fltk

Effacer ou modifier des objets
==============================

La fonction :func:`efface_tout`, comme son nom l'indique, efface tous
les objets présents sur la fenêtre.

.. autofunction:: efface_tout

La fonction :func:`efface` permet d'effacer un objet précis, ou bien
un ensemble d'objets (aucun, un ou plusieurs) possédant le même *tag*.

.. autofunction:: efface

Le paramètre ``objet`` peut être de deux types : soit il s'agit d'une
référence d'objet récupérée à la création de celui-ci, soit d'une
étiquette d'objet passée lors de la création grâce au paramètre
optionnel ``tag`` des fonctions :func:`ligne`, :func:`rectangle`,
etc., comme le montre l'exemple ci-dessous.

.. literalinclude:: ex/efface.py

Le programme affiche successivement:

.. image:: images/efface-anim.png
   :width: 700 px
   :align: center

.. warning:: Les objets ne sont pas effacés immédiatement de la
   fenêtre. Pour qu'ils disparaissent, il faut faire appel à la
   fonction ``mise_a_jour()``. La fonction ``attente_clic()`` et ses
   variantes provoquent aussi l'affichage de tous les dessins en
   attente.

La fonction :func:`modifie` permet de changer certaines caractéristiques
d'un objet, comme sa couleur ou son remplissage.

.. autofunction:: modifie

La fonction :func:`deplace` permet de déplacer un objet selon un certain
vecteur, spécifié par son amplitude en abscisse et en ordonnée.

.. autofunction:: deplace

