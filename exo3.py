# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
# Fait par Nancy
"""
Objectif :
- DEMANDER : distance (km, float), attente_navette (min, float), temps_metro (min, float), controle (min, float)
- Valider : toutes les valeurs >= 0
- Calculer les temps bruts (minutes) :
    marche  = distance * 60 / 5 + controle
    navette = attente_navette + distance * 60 / 18 + controle
    metro   = temps_metro + controle
- Arrondir chaque temps a la minute superieure (ceil)
- Determiner la/les option(s) minimale(s)

Sortie :
- 1 option gagnante : "Option la plus rapide : marcher." ou "navette." ou "metro."
- 2 options ex-aequo (ordre : marcher, navette, metro) : "Egalite : X et Y."
- 3 options ex-aequo : "Egalite : marcher, navette et metro."

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS :
1) "Entrez la distance jusqu'au CEPSUM (en kilometres) : "
2) "Entrez le temps d'attente de la navette (en minutes) : "
3) "Entrez le temps du trajet en metro (en minutes) : "
4) "Entrez le temps de controle a l'entree (en minutes) : "
"""

# TODO: Importer math
import math
# TODO: Lire les 4 valeurs
distance=float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
attente_navette=float(input("Entrez le temps d'attente de la navette (en minutes) : "))
temps_metro=float(input("Entrez le temps du trajet en metro (en minutes) : "))
controle=float(input("Entrez le temps de controle a l'entree (en minutes) : "))

# TODO: Validation
if distance < 0 or attente_navette < 0 or temps_metro < 0 or controle < 0:
    print("Erreur - donnees invalides.")

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
else:   
    marche=(distance * 60 / 5 + controle)
    navette=(attente_navette + distance * 60 / 18 + controle)
    metro=(temps_metro + controle)

marche=math.ceil(marche)
navette=math.ceil(navette)
metro=math.ceil(metro)

 # Trouver le minimum
temps_min=min(marche, navette, metro)

# TODO: Afficher la phrase exacte
gagnants=[]
if marche==temps_min:
    gagnants.append("marcher")
if navette==temps_min:
    gagnants.append("navette")
if metro==temps_min:
    gagnants.append("metro")

if len(gagnants)==1:
    print(f"Option la plus rapide:{gagnants[0]}")
elif len==2:
    print(f"Egalite: {gagnants[0]} et {gagnants[1]}")
else:
    print(f"Egalite:marcher, navette et metro.")
