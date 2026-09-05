# Ce fichier sert à lire les données stockées dans un fichier JSON.
# Il transforme ces données en objets Employe utilisables dans le reste du projet.

import json
from part1 import Employe

# La fonction charger_employes lit le fichier JSON et convertit chaque enregistrement en objet Employe.
def charger_employes(fichier):
    # Ouverture du fichier JSON en mode lecture.
    with open(fichier, 'r') as f:
        # Lecture de tout le contenu JSON et conversion en structure Python (liste de dictionnaires).
        donnee = json.load(f)

        # Création de la liste d'employés à partir des données JSON.
        # Chaque dictionnaire contient : nom, prenom, salaire.
        employes = [Employe(emp['nom'], emp['prenom'], emp['salaire']) for emp in donnee]

        # Retour de la liste complète des objets Employe.
        return employes

# Cette fonction permet de séparer les données brutes du code métier.
# Le JSON sert de source de données, tandis que la classe Employe permet de manipuler les employes dans Python.
