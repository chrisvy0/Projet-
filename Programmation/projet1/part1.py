# Ce fichier contient la logique de gestion des employés.
# Il définit un décorateur de journalisation et un mécanisme de contrôle d'accès.
# Il permet aussi de créer des objets Employe avec des méthodes pour afficher et modifier leur salaire.

# Le décorateur 'decorateur' affiche le début et la fin d'une opération.
# Il enveloppe une autre fonction et s'exécute avant et après son appel.
def decorateur(augmenter):
    def wrapper(*args, **kwargs):
        print("===== Début de l'opération =====")
        augmenter(*args, **kwargs)
        print("===== Fin de l'opération =====")
    return wrapper

# Le décorateur 'autorisation' vérifie le rôle avant d'autoriser l'exécution.
# Si le rôle est 'admin', la fonction continue ; sinon, l'accès est refusé.
def autorisation(role):
    def decorateur(augmenter):
        def wrapper(*args, **kwargs):
            if role == "admin":
                augmenter(*args, **kwargs)
            else:
                print("Accès refusé.")
        return wrapper
    return decorateur

# La classe Employe représente un employé avec un nom, un prénom et un salaire.
class Employe:
    def __init__(self, nom, prenom, salaire):
        # On initialise les attributs de l'objet.
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

    # Cette méthode affiche les informations principales de l'employé.
    def afficher(self):
        print(f"Nom: {self.nom}")
        print(f"Prénom: {self.prenom}")
        print(f"Salaire: {self.salaire}")

    # La méthode augmenter applique un pourcentage d'augmentation au salaire.
    # Elle utilise deux décorateurs :
    # 1. autorisation("admin") -> vérifie si l'utilisateur a les droits nécessaires
    # 2. decorateur -> affiche le début et la fin de l'opération
    @decorateur
    @autorisation("admin")
    def augmenter(self, pourcentage):
        # Calcul du montant à ajouter selon le pourcentage.
        montant = (self.salaire * pourcentage) / 100
        self.salaire += montant
        print(f"Le salaire de {self.nom} {self.prenom} a été augmenté de {montant}. Nouveau salaire: {self.salaire}")

    # La méthode prime ajoute directement un montant forfaitaire au salaire.
    # Elle ne vérifie pas l'autorisation, contrairement à augmenter.
    def prime(self, montant=50000):
        self.salaire += montant
        print(f"Le salaire de {self.nom} {self.prenom} a été augmenté de {montant}. Nouveau salaire: {self.salaire}")

# Exemple d'utilisation en commentaire pour tester la classe.
# chrisvy = Employe("Chrisvy", "Ngondo", 1000000)
# chrisvy.augmenter(10)
