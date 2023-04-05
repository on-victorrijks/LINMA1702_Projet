# Test imports
import highspy
import numpy as np
import cvxpy as cp

h = highspy.Highs()

data = np.load('Temperatures-Montreal.npy')
print(len(data))

"""
Tache 1

Description:
On souhaite dans un premier temps que la température du bâtiment reste
comprise dans une certaine plage admissible de températures, et on cherche à minimiser le
coût total de l'électricité consommée par la pompe à chaleur. Formulez ce problème
comme un problème d'optimisation linéaire, puis résolvez le.
Pour des raisons de temps de calcul, votre modèle considérera uniquement une période de 7
jours consécutifs. Il fera l'hypothèse que la température initiale au début de la période est
égale à la valeur central de la plage admissible, et fera en sorte que la température finale à la
fin de la période revienne à la même valeur. Votre code prendra donc en entrée un
paramètre indiquant le numéro de l'intervalle de temps qui début la période, qui s'étendra
sur intervalles de temps.

A faire:
    - Calculer le cout minimal
    - Faire un graphique de l'évolution des températures
    - Faire un graphique représentant l'utilisation de la pompe à chaleur (en distinguant le fonctionnement normal du reverse)
    - Faire deux graphes côte à côte de deux périodes:
        1) Période pré-déterminée (fichier de données ?)
        2) Pédiode choisie en fonction de son intêret
    - Calculer le temps de calcul
    - Discuter des résultats (max 4 lignes)
"""

"""
Tache 2

Description:
On souhaite réduire le coût d'utilisation de la pompe à chaleur, et on va fixer le
budget maximal à une certaine proportion du coût minimal identifié lors de la première
tâche. Pour diminuer les coût, on va permettre aux températures de sortir de la plage
admissible définie plus haut. On va cependant alors comptabiliser la quantité d'inconfort
éventuellement subi durant chaque intervalle de temps, qui sera proportionnel au
dépassement de la température maximale admissible, ou au dépassement par le bas de la
température minimale admissible. On cherche alors à minimiser l'inconfort total (somme
des inconforts sur toute la période considérée) tout en respectant la contrainte de
budget. Formulez ce problème comme un problème d'optimisation linéaire, puis résolvez le.

A faire:
    - Calculer l'inconfort minimal pour un budget donné
    - Faire un graphique de l'évolution des températures
    - Faire un graphique représentant l'utilisation de la pompe à chaleur (en distinguant le fonctionnement normal du reverse)
    - Faire deux graphes côte à côte de deux périodes:
        1) Période pré-déterminée (fichier de données ?)
        2) Pédiode choisie en fonction de son intêret
    - Calculer le temps de calcul
    - Discuter des résultats (max 4 lignes)
"""

"""
Tache 3

Description:
On voudrait à présent mieux comprendre le compromis qui existe entre le budget
alloué et l'inconfort total qui en résulte. Proposez un graphique représentant au mieux
cette relation entre budget et inconfort, où on fera varier le budget entre entre zéro et le
coût minimal identifié lors de la tâche 1 (ce budget sera indiqué en pourcentage, de 0 à
100%). Ceci nécessitera la résolution de plusieurs problèmes, et il sera judicieux d'utiliser la
fonctionnalité warm start du solver pour accélérer les calculs.


A faire:
    - Faire un graphique qui représente la relation entre le budget et l'inconfort 
    (budget de 0 à 100% du budget minimal trouvé dans la tache 1)
    - Faire deux graphes côte à côte de deux périodes:
        1) Période pré-déterminée (fichier de données ?)
        2) Pédiode choisie en fonction de son intêret
    - Calculer le temps de calcul (total et moyen par problème?)
    - Discuter des résultats (max 4 lignes)
"""
