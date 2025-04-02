.. currentmodule:: fltk 

Créer une fenêtre
=======================

Tous les programmes utilisant ``fltk`` sont de la forme suivante :

.. literalinclude:: ex/template.py 
   :start-after: #BEGIN TEMPLATE BASE
   :end-before: #END TEMPLATE BASE

La premiere ligne importe toutes les définitions (variables globales,
fonctions...) du module ``fltk``.  Pour que cela fonctionne, il faut
donc avoir une copie du fichier ``fltk.py`` dans le même répertoire
que votre programme.

L'appel à ``cree_fenetre(400, 300)`` crée une fenêtre de 400 *pixels*
de large sur 300 *pixels* de haut. Dans la suite, on verra comment y
dessiner des formes (lignes, rectangle, cercles, ...).

L'appel à ``ferme_fenetre()`` détruit la fenêtre.

L'appel à ``mise_a_jour()`` rafraîchit l'affichage de la fenêtre,
c'est-à-dire dessine tous les nouveaux objets ajoutés à l'aide d'une
des fonctions de dessin appelées précédemment (voir la rubrique
:doc:`dessins`), ou supprime les objets effacés à l'aide d'une des
fonctions de suppression d'objets (voir la rubrique :doc:`effacer`).

.. autofunction:: cree_fenetre

.. autofunction:: ferme_fenetre

.. autofunction:: redimensionne_fenetre

.. autofunction:: mise_a_jour

Une autre possibilité pour importer le module est de remplacer la
première ligne par ``import fltk``. Pour faire appel aux fonctions
du module, il faut dans ce cas les faire précéder du nom du module
suivi d'un point :

.. literalinclude:: ex/template.py 
   :start-after: #BEGIN TEMPLATE IMPORT
   :end-before: #END TEMPLATE IMPORT

.. warning:: Si vous exécutez le programme ci-dessus, vous ne verrez
   rien car la fenêtre sera affichée puis immédiatement détruite. La
   fonction :func:`attend_ev` permet de bloquer l'exécution du
   programme jusqu'à ce que l'utilisateur clique sur la fenêtre ou appuie sur
   une touche du clavier.

   .. literalinclude:: ex/template.py 
      :start-after: #BEGIN TEMPLATE ATTENTE
      :end-before: #END TEMPLATE ATTENTE
