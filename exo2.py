# Exercice 02 – Ambiance autour du stade (sections A a H) (gabarit)
"""
Objectif :
- Lire 8 entiers (un par ligne) : personnes dans les sections A, B, C, D, E, F, G, H (dans cet ordre)
- Valider : chaque valeur est un entier >= 0
    -> sinon afficher EXACTEMENT : "Erreur - donnees invalides."
- Calculer l'intensite brute par section : intensite = personnes * facteur
- Normaliser sur 0..10 avec un arrondi half-up :
    - maxI = max(intensites)
    - si maxI == 0 : niveaux = [0]*8
    - sinon : niveau = int((intensite / maxI) * 10 + 0.5), borne dans [0,10]
- Afficher une grille verticale :
    - lignes 10 a 1
    - colonnes A a H
    - afficher "❚" si niveau_section >= niveau_ligne sinon "."
    - un espace entre chaque cellule
    - format de ligne : "{ligne:2} | <8 cellules>"
    - derniere ligne : "     A B C D E F G H"
"""

FACTEURS = [1.30, 1.15, 1.05, 0.95, 0.95, 1.05, 1.15, 1.30]
personnes = [-1, -1, -1, -1, -1, -1, -1, -1]

# TODO: Lire 8 entiers (un par ligne) dans une liste personnes
#       En cas d'erreur de conversion ou valeur negative -> afficher le message d'erreur et quitter

for i in range(len(personnes)):
    match i:
        case 0:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section A: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case 1:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section B: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case 2:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section C: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case 3:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section D: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case 4:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section E: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case 5:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section F: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case 6:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section G: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")
        case _:
            while personnes[i] < 0:
                try:
                    personnes[i] = int(input(f"Entrez le nombre de personnes dans la section H: "))
                    print("Erreur - donnees invalides.") if personnes[i] < 0 else None
                except ValueError:
                    print("Erreur - donnees invalides.")

# TODO: Calculer les intensites brutes (liste de 8 floats)
intensites = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
for i in range(len(personnes)):
    intensites[i] = personnes[i] * FACTEURS[i]

# TODO: Calculer les niveaux normalises (liste de 8 entiers dans [0,10])
niveaux = [0, 0, 0, 0, 0, 0, 0, 0]
maxI = max(intensites)
if not maxI == 0:
     for i in range(len(personnes)):
        niveaux[i] = int((intensites[i] / maxI) * 10 + 0.5)

# TODO: Afficher la grille (10 lignes) puis la ligne des labels
for i in range(10):
    celllules = ""
    for j in range(len(personnes)):
        celllules += " ❚" if intensites[j] >= (10 - i) else " ."
    print(f"{10 - i:2} |{celllules}")

print("     A B C D E F G H")