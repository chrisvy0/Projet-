import csv
import matplotlib.pyplot as plt
import datetime
def menu():
    print("=============== Menu Principal ===============")
    print("1.Ajouter une dépense")
    print("2.Afficher les dépenses du mois")
    print("3.Afficher le total des dépenses du mois")
    print("4.Trouver la catégorie avec le plus de dépenses")
    print("5. Exporter les dépenses du mois dans un fichier CSV")
    print("6. Graphiques des dépenses par catégorie")
    print("q. Quitter")

def charger_fichier(fichier):
    with open(fichier, "r") as f:
        reader = csv.DictReader(f)
        for depense in reader:
            depenses.append(Depense(int(depense["Montant"]), depense["Catégorie"], depense["Date"]))

class Depense:
    def __init__(self, montant, categorie, date):
        self.montant = montant
        self.categorie = categorie
        self.date = date

depenses = []
charger_fichier("depenses.csv")

while True:
    menu()
    choix = input("Veuillez choisir une option (1-6) ou 'q' pour quitter : ")
    match choix:
        case "1":
            montant =  int(input("Entrez le montant de la dépense : "))
            categorie = input("Entrez la catégorie de la dépense : ")
            date = input("Entrez la date de la dépense (format AAAA-MM-JJ) : ")
            depense = Depense(montant, categorie, date)
            depenses.append(depense)
        case "2":
            print("Dépenses du mois :")
            maintenant = datetime.datetime.now()
            for depense in depenses:
                date_depense = datetime.datetime.strptime(depense.date, "%Y-%m-%d")
                if(date_depense.month == maintenant.month and date_depense.year == maintenant.year):
                    print("===============================")
                    print(f"Montant : {depense.montant}, Catégorie : {depense.categorie}, Date : {depense.date}")
        case "3":
            total = sum(depense.montant for depense in depenses)
            print(f"Total des dépenses du mois : {total}")
        case "4":
            categories = {}
            for depense in depenses:
                if(depense.categorie in categories):
                    categories[depense.categorie] += depense.montant
                else:
                    categories[depense.categorie] = depense.montant

            if categories:
                cat_max = max(categories, key=categories.get)
                montant_max = categories[cat_max]
                print(f"La catégorie avec le plus de depense est {cat_max} et les dépenses s'élèvent à {montant_max}")

        case "5":
            with open("depenses.csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["Montant", "Catégorie", "Date"])
                for depense in depenses:
                    writer.writerow([depense.montant, depense.categorie, depense.date])
            print("Les dépenses du mois ont été exportées dans le fichier 'depenses.csv'.")
        case "6":
            categories = {}
            for depense in depenses:
                if depense.categorie in categories:
                    categories[depense.categorie] += depense.montant
                else:
                    categories[depense.categorie] = depense.montant

            plt.bar(categories.keys(), categories.values())
            plt.xlabel("Catégories")
            plt.ylabel("Montant total des dépenses")
            plt.title("Dépenses par catégorie")
            plt.show()
        case "q":
            print("Au revoir !")
            break