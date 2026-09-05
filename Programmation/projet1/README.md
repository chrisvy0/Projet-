# Gestion des employés

Ce projet Python permet de gérer une liste d'employés à partir d'un fichier JSON, puis d'afficher et modifier leurs salaires.

## Objectif

Le programme vise à :
- charger des données d'employés depuis un fichier JSON ;
- créer des objets `Employe` à partir de ces données ;
- afficher les informations de chaque employé ;
- appliquer des augmentations de salaire et des primes ;
- démontrer l'utilisation de décorateurs en Python.

## Structure du projet

- `main.py` : script principal qui charge les employés et applique les traitements.
- `part1.py` : contient la classe `Employe` ainsi que les décorateurs.
- `part2.py` : contient la fonction de chargement des données depuis `employes.json`.
- `employes.json` : stockage des employés au format JSON.

## Description des fichiers

### 1. `part1.py`
Ce fichier définit :
- `decorateur` : un décorateur qui affiche le début et la fin d'une opération.
- `autorisation(role)` : un décorateur qui vérifie si l'utilisateur a le bon rôle.
- `Employe` : une classe qui contient les informations de chaque employé, avec les méthodes :
  - `afficher()` : affiche le nom, le prénom et le salaire ;
  - `augmenter(pourcentage)` : augmente le salaire selon un pourcentage ;
  - `prime(montant)` : ajoute une prime forfaitaire.

### 2. `part2.py`
Ce fichier lit le fichier JSON et crée des objets `Employe` à partir des données enregistrées.

### 3. `main.py`
Le script principal :
- charge la liste des employés depuis le JSON ;
- affiche les informations de chaque employé ;
- applique une augmentation au premier employé et une prime au deuxième ;
- réaffiche la liste pour vérifier les changements.

## Exemple de données
Le fichier `employes.json` contient des objets sous cette forme :

```json
[
  {
    "nom": "Mbaye",
    "prenom": "Mamadou",
    "salaire": 350000
  }
]
```

## Comment exécuter le projet

Ouvrez un terminal dans le dossier du projet puis lancez :

```bash
python main.py
```

## Résultat attendu

Le programme affichera les employés, puis appliquera les modifications suivantes :
- 10 % d'augmentation pour le premier employé ;
- une prime de 25 000 pour le deuxième employé ;
- un affichage final des salaires mis à jour.

## Remarque

Ce projet sert à illustrer :
- la programmation orientée objet ;
- la manipulation de fichiers JSON ;
- l'utilisation des décorateurs en Python.
