#Écrire dans un nouveau fichier shifumi.py, un programme 
#qui permettra de jouer à Pierre / Feuille / Ciseaux contre 
#l'ordinateur en 2 manches gagnantes [BO3].

import random

def jouer_shifumi():
    choix = ["Pierre", "Feuille", "Ciseaux"]
    manches_joueur = 0
    manches_ordinateur = 0

    while manches_joueur < 2 and manches_ordinateur < 2:
        print("Choisissez :")
        print("1. Pierre")
        print("2. Feuille")
        print("3. Ciseaux")
        choix_joueur = int(input("Entrez le numéro de votre choix : ")) - 1

        if choix_joueur < 0 or choix_joueur > 2:
            print("Choix invalide. Veuillez choisir à nouveau.")
            continue

        choix_ordinateur = random.randint(0, 2)

        print("Vous avez choisi : " + choix[choix_joueur])
        print("L'ordinateur a choisi : " + choix[choix_ordinateur])


        if choix_joueur == choix_ordinateur:
            print("Égalité !")
        elif (choix_joueur == 0 and choix_ordinateur == 2) or (choix_joueur == 1 and choix_ordinateur == 0) or (choix_joueur == 2 and choix_ordinateur == 1):
            print("Vous gagnez cette manche !")
            manches_joueur += 1
        else:
            print("L'ordinateur gagne cette manche !")
            manches_ordinateur += 1


    if manches_joueur > manches_ordinateur:
        print("Vous avez gagné le Best of 3 !")
    else:
        print("L'ordinateur a gagné le Best of 3 !")

if __name__ == "__main__":
    jouer_shifumi()
