#Écrire un programme qui demande en continue à 
#l’utilisateur d’entrer des notes d’élèves. La boucle se 
#termine seulement si l’utilisateur entre une valeur 
#négative. Lorsque cela arrive, afficher le nombre de notes 
#entrées, et calculer la moyenne de toutes les notes.
#Si l’utilisateur entre autre chose qu’un nombre, l’erreur 
#doit être traitée.
#Si l’utilisateur ne rentre aucune note et quitte le 
#programme immédiatement, l’erreur doit également être 
#traitée.

# Initialisation des variables
total_notes = 0
somme_notes = 0

while True:
    try:
        note = float(input("Entrez une note (négative pour quitter) : "))
        if note < 0:
            break 
        else: somme_notes += note
        total_notes += 1
    except ValueError:
        print("Erreur : Entrez un nombre valide.")
        
if total_notes == 0:
    print("Aucune note n'a été entrée.")
else:
    moyenne = somme_notes / total_notes
    print(f"Nombre de notes entrées : {total_notes}")
    print(f"Moyenne des notes : {moyenne}")
