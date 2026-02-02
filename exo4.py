# -*- coding: utf-8 -*-
# Exercice 04 - Verification d'une rampe d'accessibilite (gabarit)
"""
Objectif :
- DEMANDER : hauteur (cm, float) et longueur (m, float)
- Valider : hauteur >= 0 et longueur > 0
- Calculer :
    hauteur_m = hauteur_cm / 100
    pente = (hauteur_m / longueur_m) * 100
    angle = atan(hauteur_m / longueur_m) en degres
- Verifier la conformite : pente <= 8.00

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT :
    Pente: PP.PP%
    Angle: AA.AA deg
    Conforme: OUI|NON
Si NON, afficher une 4e ligne :
    Depassement: DD.DD%

Prompts EXACTS :
1) "Entrez la hauteur a franchir (en centimetres) : "
2) "Entrez la longueur horizontale (en metres) : "
"""

# TODO: Importer math
import math
# TODO: Lire hauteur_cm et longueur_m
# TODO: Validation
hauteur_cm = -1
longueur_m = 0

while hauteur_cm < 0.0 or longueur_m <= 0.0: 
    if hauteur_cm < 0:  
        try:
            hauteur_cm = float(input("Entrez la hauteur a franchir (en centimetres) : "))
            print("Erreur - donnees invalides.") if hauteur_cm < 0 else None
        except ValueError:
            print("Erreur - donnees invalides.")
    elif longueur_m <= 0:
        try:
            longueur_m = float(input("Entrez la longueur horizontale (en metres) : "))
            print("Erreur - donnees invalides.") if longueur_m <= 0 else None
        except ValueError:
            print("Erreur - donnees invalides.")
# TODO: Calcul pente et angle
hauteur_m = hauteur_cm / 100
pente = (hauteur_m / longueur_m) * 100
angle = math.degrees(math.atan(hauteur_m / longueur_m))
est_conforme = pente <= 8.00


# TODO: Affichage exact (+ ligne depassement si necessaire)
print(f"Pente: {pente:.2f}%")
print(f"Angle: {angle:.2f} deg")
print(f"Conforme: {"OUI" if est_conforme else "NON"}") 
if not est_conforme:
    print(f"Depassement: {(pente - 8.00):.2f}%")
