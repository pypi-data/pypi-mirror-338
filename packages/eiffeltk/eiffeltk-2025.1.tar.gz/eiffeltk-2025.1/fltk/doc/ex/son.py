import fltk

fltk.cree_fenetre(300, 300)
while True:
    fltk.mise_a_jour()
    ev = fltk.donne_ev()
    tev = fltk.type_ev(ev)
    if tev is not None:
        print(tev)
    if tev == 'Quitte':
        break
    elif tev == 'ClicGauche':
        print("Lecture du fichier ding.wav")
        fltk.joue_son('ding.wav')
    elif tev == 'ClicDroit':
        print("Lecture du fichier ding.mp3")
        fltk.joue_son('ding.mp3')
fltk.ferme_fenetre()
