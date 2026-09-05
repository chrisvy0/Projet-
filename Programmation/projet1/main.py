# Importation de la fonction qui permet de lire les employés depuis le fichier JSON.
from projet1.part2 import charger_employes

# Chargement de la liste des employés depuis le fichier employes.json.
# Cette liste contient des objets de type Employe créés grâce à la classe définie dans part1.py.
liste = charger_employes("employes.json")

# On parcourt la liste pour appliquer des traitements spécifiques à certains employés.
count = 1
for i in liste:
    print(f"Employé {count}:")
    i.afficher()  # Affiche les informations de base de l'employé.

    # Premier employé : augmentation de salaire de 10 %.
    if count == 1:
        i.augmenter(10)

    # Deuxième employé : prime de 25 000 francs CFA.
    if count == 2:
        i.prime(25000)

    count += 1

# Séparation visuelle pour distinguer la première partie de l'affichage final.
print("==============================")

# Deuxième affichage : on réaffiche tous les employés pour voir le résultat final.
count = 1
for i in liste:
    print(f"Employé {count}:")
    i.afficher()
    count += 1

# Ce script sert à tester le chargement des données et les effets des méthodes sur les salaires.
# Il affiche d'abord les employés, applique des modifications, puis les réaffiche.

