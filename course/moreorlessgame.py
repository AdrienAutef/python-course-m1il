#Le programme tire un nombre aléatoire entre 0 et 100.
#La personne doit trouver le nombre en recevant comme inidcation si le nombre est trop grand ou trop petit
#A la fin le programme doit dire combien de coups ont été joués

import random

def difficulty_choice():
    print("Choisissez la difficulté :")
    print("1. Facile (0 à 10)")
    print("2. Moyen (0 à 100)")
    print("3. Difficile (0 à 1000)")
    
    choix = int(input("Entrez le numéro de la difficulté : "))
    if choix == 1:
        return (0, 10)
    elif choix == 2:
        return (0, 100)
    elif choix == 3:
        return (0, 1000)
    else:
        print("Choix invalide. Sélectionnez une option valide.")
        return difficulty_choice()

min_range, max_range = difficulty_choice()

number_to_guess = random.randint(min_range, max_range)

try_number = 0

while True:
    essai = int(input(f"Devinez le nombre entre {min_range} et {max_range} : "))
    try_number += 1
    
    if essai < number_to_guess:
        print("Trop petit, essayez à nouveau.")
    elif essai > number_to_guess:
        print("Trop grand, essayez à nouveau.")
    else:
        print(f"Félicitations ! Vous avez deviné le nombre en {try_number} coups.")
        break
