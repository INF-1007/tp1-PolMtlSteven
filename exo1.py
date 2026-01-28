# -*- coding: utf-8 -*-
# Exercice 01 - Bilan de visionnage Carabins (gabarit)
"""
Objectif :
- DEMANDER : nom complet, matchs football, duree football, matchs soccer, duree soccer
- Valider : matchs >= 0 et durees > 0 (entiers)
- Convertir les minutes en format HhMM (minutes sur 2 chiffres)
- Afficher EXACTEMENT 4 lignes :
    Bonjour {nom}
    Football (Carabins): {A} match(s), {Hf}h{Mf:02d} de visionnage
    Soccer (Carabins): {B} match(s), {Hs}h{Ms:02d} de visionnage
    Total: {Ht}h{Mt:02d}

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Prompts EXACTS a utiliser :
1) "Entrez votre nom complet : "
2) "Entrez le nombre de matchs de football des Carabins suivis cet automne : "
3) "Entrez la duree moyenne d'un match de football suivi (en minutes) : "
4) "Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "
5) "Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "
"""

# TODO: Lire le nom (str)
nom_comp = input("Entrez votre nom complet : ")
# TODO: Lire les 4 valeurs (int)
# TODO: Valider les donnees (matchs >= 0, durees > 0)
matchs_foot = -1
duree_foot = 0
matchs_soccer = -1
duree_soccer = 0

while matchs_foot < 0:
    try:
        matchs_foot = int(input("Entrez le nombre de matchs de football des Carabins suivis cet automne : "))
        print("Erreur - donnees invalides.") if matchs_foot < 0 else None
    except ValueError:
        print("Erreur - donnees invalides.")

while duree_foot <= 0:
    try:
        duree_foot = int(input("Entrez la duree moyenne d'un match de football suivi (en minutes) : "))
        print("Erreur - donnees invalides.") if duree_foot <= 0 else None
    except ValueError:
        print("Erreur - donnees invalides.")

while matchs_soccer < 0:
    try:
        matchs_soccer = int(input("Entrez le nombre de matchs de soccer feminin des Carabins suivis cet automne : "))
        print("Erreur - donnees invalides.") if matchs_soccer < 0 else None
    except ValueError:
        print("Erreur - donnees invalides.")

while duree_soccer <= 0:
    try:
        duree_soccer = int(input("Entrez la duree moyenne d'un match de soccer suivi (en minutes) : "))
        print("Erreur - donnees invalides.") if duree_soccer <= 0 else None
    except ValueError:
        print("Erreur - donnees invalides.")


# TODO: Calculer les minutes totales (football, soccer, total)
mins_total_foot = matchs_foot * duree_foot
mins_total_soccer = matchs_soccer * duree_soccer
mins_total = mins_total_foot + mins_total_soccer

# TODO: Convertir en heures/minutes et afficher exactement 4 lignes
heures_foot = mins_total_foot // 60
minutes_foot = mins_total_foot % 60
heures_soccer = mins_total_soccer // 60
minutes_soccer = mins_total_soccer % 60
heures_total = mins_total // 60
minutes_total = mins_total % 60

print(f"Bonjour {nom_comp}")
print(f"Football (Carabins): {matchs_foot} match(s), {heures_foot}h{minutes_foot:02d} de visionnage")
print(f"Soccer (Carabins): {matchs_soccer} match(s), {heures_soccer}h{minutes_soccer:02d} de visionnage")
print(f"Total: {heures_total}h{minutes_total:02d}")