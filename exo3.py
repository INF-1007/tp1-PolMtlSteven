# -*- coding: utf-8 -*-
# Exercice 03 - Choisir le meilleur trajet vers le CEPSUM (gabarit)
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
distance = -1
mins_attente_navette = -1
mins_trajet_metro = -1
mins_controle_entree = -1



while distance < 0.0 or mins_attente_navette < 0.0 or mins_trajet_metro < 0.0 or mins_controle_entree < 0.0: # Boucler tant qu'il y des valeurs invalides
                if distance < 0: # Lire donnée seulement si elle est invalide   
                    try:
                        distance = float(input("Entrez la distance jusqu'au CEPSUM (en kilometres) : "))
                        print("Erreur - donnees invalides.") if distance < 0 else None
                    except ValueError:
                        print("Erreur - donnees invalides.")
                elif mins_attente_navette < 0:
                    try:
                        mins_attente_navette = float(input("Entrez le temps d'attente de la navette (en minutes) : "))
                        print("Erreur - donnees invalides.") if mins_attente_navette < 0 else None
                    except ValueError:
                        print("Erreur - donnees invalides.")
                elif mins_trajet_metro < 0:
                    try:
                        mins_trajet_metro = float(input("Entrez le temps du trajet en metro (en minutes) : "))
                        print("Erreur - donnees invalides.") if mins_trajet_metro < 0 else None
                    except ValueError:
                        print("Erreur - donnees invalides.")
                elif mins_controle_entree < 0:
                    try:
                        mins_controle_entree = float(input("Entrez le temps de controle a l'entree (en minutes) : "))
                        print("Erreur - donnees invalides.") if mins_controle_entree < 0 else None
                    except ValueError:
                        print("Erreur - donnees invalides.")

# TODO: Validation

# TODO: Calculer, arrondir (ceil) et determiner le(s) meilleur(s)
marche  = math.ceil(distance * 60 / 5 + mins_controle_entree)
navette = math.ceil(mins_attente_navette + distance * 60 / 18 + mins_controle_entree)
metro   = math.ceil(mins_trajet_metro + mins_controle_entree)
choix = [marche, navette, metro]

trajet_plus_court = min(marche, navette, metro)
chaine = ""

for i in range(len(choix)):
     match i:
          case 0:
               chaine += "marche " if choix[i] == trajet_plus_court else ""
          case 1:
               chaine += "navette " if choix[i] == trajet_plus_court else ""
          case 2: 
               chaine += "metro" if choix[i] == trajet_plus_court else ""

options = chaine.strip().split(sep=" ")


# TODO: Afficher la phrase exacte

if len(options) == 1:
     print(f"Option la plus rapide : {options[0]}.")
elif len(options) == 2:
     print(f"Egalite : {options[0]} et {options[1]}.")
else:
     print("Egalite : marcher, navette et metro.")
