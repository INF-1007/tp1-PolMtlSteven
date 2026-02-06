# -*- coding: utf-8 -*-
# Exercice 05 - Planification d'achat de billets (gabarit)
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
    # TODO: Code pour lire et vérifier le statut étudiant

prix = 0
reste_billets = nb_billets
combinaison = {
    "forfait_24": 0,
    "forfait_12": 0,
    "forfait_5": 0,
    "forfait_unit.": 0
}

if reste_billets / 24 > 0:
    prix += 66 * (reste_billets / 24) * 0.88 if statut_etudiant == "O" else 66 * (reste_billets / 24)
    combinaison["forfait_24"] = reste_billets / 24
    reste_billets %= 24

if reste_billets / 12 > 0:
    prix += 36 * (reste_billets / 12) * 0.88 if statut_etudiant == "O" else 36 * (reste_billets / 12)
    combinaison["forfait_12"] = reste_billets / 12
    reste_billets %= 12

 # TODO Ajouter logique pour forfait de 5 billets
 # TODO Ajouter logique pour billet unitaire
            


  
# TODO: Calculer et afficher le resultat exact (6 lignes)
somme = sum(prix for prix in combinaison.values()) 

print(f"Forfaits de 24 billets - {combinaison['forfait_24']}")
print(f"Forfaits de 12 billets - {combinaison['forfait_12']}")
print(f"Forfaits de 5 billets - C")
print(f"Billets unitaires - D")
print(f"Total billets - T")
print(f"Prix total - {somme:2f}")
