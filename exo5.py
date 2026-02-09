# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
# Fait par Steven et Nancy
"""
Objectif :
- DEMANDER : n (int) et statut etudiant (O/N)
- Options :
    24 billets : 66.00$
    12 billets : 36.00$
     5 billets : 15.75$
     1 billet  :  3.60$
- Reduction : si etudiant = O, appliquer 12% de reduction sur le cout des forfaits uniquement.
  Les billets unitaires ne sont pas reduits.

But :
- Acheter au moins n billets
- Minimiser le prix total
- En cas d'egalite sur le prix : choisir le plus petit total de billets, puis le plus petit nombre de billets unitaires

Si invalide, afficher exactement :
    Erreur - donnees invalides.

Sinon, afficher EXACTEMENT 6 lignes :
    Forfaits de 24 billets - A
    Forfaits de 12 billets - B
    Forfaits de 5 billets - C
    Billets unitaires - D
    Total billets - T
    Prix total - PPP.PP$

Prompts EXACTS :
1) "Entrez le nombre de billets necessaires : "
2) "Entrez le statut etudiant (O/N) : "

Conseil :
- Une solution simple consiste a tester plusieurs combinaisons de forfaits avec des boucles (bruteforce).
"""

nb_billets = -1
statut_etudiant = "X"

# TODO: Lire n (int) et statut (str)
while nb_billets < 0 or statut_etudiant not in {"O", "N"}:
    if nb_billets < 0: # On demande la lecture seulement si nb_billets est négatif
        try:
            nb_billets = int(input(f"Entrez le nombre de billets necessaires : "))
            print("Erreur - donnees invalides.") if nb_billets < 0 else None
        except ValueError:
            print("Erreur - donnees invalides.")
    if statut_etudiant not in {"O", "N"}: # On demande la lecture seulement si nb_billets est négatif
        try:
            statut_etudiant = str(input(f"Entrez le statut etudiant (O/N) : "))
            print("Erreur - donnees invalides.") if statut_etudiant not in {"O", "N"} else None
        except ValueError:
            print("Erreur - donnees invalides.")

prix = 0
reste_billets = nb_billets
combinaison = {
    "forfait_24": 0,
    "forfait_12": 0,
    "forfait_5": 0,
    "forfait_unit.": 0
}

if reste_billets >= 24 :
    nb_forfait_24=reste_billets // 24
    combinaison["forfait_24"] =nb_forfait_24
    prix += nb_forfait_24 * 66 * (0.88 if statut_etudiant == "O" else 1)
    reste_billets %= 24

if reste_billets >= 12 :
    nb_forfait_12=reste_billets // 12
    combinaison["forfait_12"] =nb_forfait_12
    prix += 36 * nb_forfait_12 * (0.88 if statut_etudiant == "O" else 1)
    reste_billets %= 12
    

 # TODO Ajouter logique pour forfait de 5 billets
if reste_billets >= 5: 
    nb_forfait_5=reste_billets // 5
    combinaison["forfait_5"]=nb_forfait_5
    prix += 15.75 * nb_forfait_5 * (0.88 if statut_etudiant=="O" else 1)
    reste_billets%=5
 
 # TODO Ajouter logique pour billet unitaire
if reste_billets > 0:
    combinaison["forfait_unit."]=reste_billets
    prix += 3.60 * reste_billets 
    reste_billets=0
              
# TODO: Calculer et afficher le resultat exact (6 lignes)
somme = sum(prix for prix in combinaison.values()) 

print(f"Forfaits de 24 billets - {combinaison['forfait_24']}")
print(f"Forfaits de 12 billets - {combinaison['forfait_12']}")
print(f"Forfaits de 5 billets - {combinaison['forfait_5']}")
print(f"Billets unitaires - {combinaison['forfait_unit.']}")
print(f"Total billets - {sum(combinaison.values())}")
print(f"Prix total - {somme:2f}")
