.. currentmodule:: fltk

Gestion de la souris et du clavier
==================================   

La bibliothèque fltk fournit pour l'instant des commandes simples permettant
uniquement de gérer les clics de souris ou l'appui sur les touches du clavier.
La gestion du clavier et de la souris peut se faire au moyen de la boucle
suivante:

.. literalinclude:: ex/template-ev.py

À intervalles réguliers, ce programme récupère avec la fonction
:py:func:`donne_ev` le premier événement qui s'est produit sur la
fenêtre depuis le dernier appel à cette fonction, ou un événement vide
indiquant l'absence d'un autre événement. Cette fonction renvoie en fait un
*objet* représentant un événement, comme par exemple un clic droit au point
de coordonnées (50,50).

Si ``ev`` est un tel objet, l'appel ``type_ev(ev)`` renvoie une chaîne
de caractères représentant le type de l'événement ``ev``. Il y a six
principaux types d'événements :

* ``'Touche'`` lorsque l'événement est un appui sur une touche ;
* ``'ClicGauche'`` lorsque l'événement est un clic gauche ;
* ``'ClicDroit'`` lorsque l'événement est un clic droit ;
* ``'Redimension'`` lorsque l'événement est un redimensionnement de la
  fenêtre ;
* ``'Quitte'`` lorsque l'événement est un clic sur le bouton de fermeture de la
  fenêtre ;
* ``None`` lorsqu'il ne s'est rien passé.

**Exemple :** On souhaite écrire un petit programme ouvrant une fenêtre et
affichant sur le terminal chaque événement qui se produit au cours de
l'exécution. Voici une première tentative :

.. literalinclude:: ex/log-ev-ou-none.py

Ce programme ne fonctionne pas, et affiche très rapidement et un grand
nombre de fois ``None``. Ceci est dû au fait que, quand aucun événement ne
s'est encore produit, la fonction :py:func:`donne_ev` renvoit le résultat
``None``. La version ci-dessous n'affiche que les *vrais* événements.

.. literalinclude:: ex/log-ev-faux.py

Lorsqu'on teste ce programme, on se rend compte que la fenêtre semble
"figée", et qu'aucun événement ne s'affiche. Le problème est qu'on a oublié de
mettre à jour la fenêtre, ce qui a pour autre effet que les événements ne
sont pas détectés. Le programme ci-dessous affiche correctement le type de
tous les événements qui se produisent :

.. literalinclude:: ex/log-ev-reels.py

Cet exemple fonctionne mieux, mais ne permet pas de fermer la fenêtre
correctement. Pour cela, on va sortir de la boucle quand on rencontre
un événement de type ``'Quitte'``, et fermer la fenêtre à l'aide de
:py:func:`ferme_fenetre` :

.. literalinclude:: ex/log-ev-quitte.py

.. warning::

   Pour que les frappes au clavier soient prises en compte, il faut que la
   fenêtre ait le *focus*, c'est à dire qu'elle soit active.

Nous allons maintenant voir comment traiter les événements récupérés.

Événement ``'Touche'``
----------------------

Lorsque l'événement ``ev`` est de type ``'Touche'``, on peut utiliser la
fonction :py:func:`touche` qui renvoie une chaîne de caractères donnant le
nom de la touche qui a été pressée. Le programme ci-dessous affiche le nom de
toutes les touches pressées.

.. literalinclude:: ex/log-ev-clavier.py

Par exemple, on peut voir que:

* la touche ``A`` a pour nom ``'a'``
* la barre d'espace  a pour nom ``'space'``
* la flèche droite a pour nom ``'Right'``
* la flèche gauche a pour nom ``'Left'``
* la flèche du haut a pour nom ``'Up'``
* la flèche du bas a pour nom ``'Down'``

Le programme suivant permet de déplacer un carré sur la fenêtre
avec les flèches.

.. literalinclude:: ex/petit-carre.py

Événement ``'ClicDroit'`` ou ``'ClicGauche'``
---------------------------------------------

Pour connaitre les coordonnées correspondant à un evenement de
type ``'ClicDroit'`` ou ``'ClicGauche'``, on utilise les
fonctions :py:func:`abscisse` et :py:func:`ordonnee`.

Par exemple, le programme suivant affiche les coordonnées des points
cliqués.

.. literalinclude:: ex/log-ev-souris.py

Événement ``'Redimension'``
---------------------------------------------

Cet événement se produit quand la fenêtre est redimensionnée. Pour connaître
les nouvelles dimensions de la fenêtre, on utilise les fonctions
:py:func:`hauteur_fenetre` et :py:func:`largeur_fenetre`.

Par exemple, le programme suivant dessine un quadrillage 3 x 3 sur la fenêtre
et le redessine dynamiquement lorsque la fenêtre est redimensionnée.

.. literalinclude:: ex/ev_redim.py

Liste des fonctions
-------------------

.. autofunction:: donne_ev

.. autofunction:: type_ev

.. autofunction:: attente

.. autofunction:: attend_ev

.. autofunction:: attend_clic_gauche

.. autofunction:: attend_fermeture

.. autofunction:: abscisse

.. autofunction:: ordonnee

.. autofunction:: abscisse_souris

.. autofunction:: ordonnee_souris

.. autofunction:: touche

.. autofunction:: touche_pressee
