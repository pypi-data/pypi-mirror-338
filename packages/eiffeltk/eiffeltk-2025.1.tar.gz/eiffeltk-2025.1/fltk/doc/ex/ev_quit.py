from fltk import *


def jeu():
	cree_fenetre(100, 100)
	texte(50, 50, "jeu", ancrage='center')

	while True:
		ev = attend_ev()
		tev = type_ev(ev)
		if tev == 'ClicGauche':
			print("C'est un clic !")
		elif tev == "Quitte":
			ferme_fenetre()
			break


def menu():
	cree_fenetre(100, 100)
	texte(50, 50, "menu", ancrage='center')

	while True:
		ev = attend_ev()
		tev = type_ev(ev)
		if tev == 'ClicGauche':
			print("C'est un clic !")
		elif tev == "Quitte":
			ferme_fenetre()
			break


if __name__ == "__main__":
	menu()