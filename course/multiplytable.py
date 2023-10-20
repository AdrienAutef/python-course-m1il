#L’utilisateur entre un nombre. Le programme stock 
#les 10 premiers résultats de la table de 
#multiplication choisie par l’utilisateur dans une 
#liste puis affiche cette liste.
#BONUS
#Signaler au passage, à l’aide d’une astérisque, 
#ceux qui sont des multiples de 3 


def multiply_table(nombre):
    table = []
    for i in range(1, 11):
        resultat = nombre * i
        marqueur = '*' if resultat % 3 == 0 else ''  
        table.append(f"{nombre} x {i} = {resultat}{marqueur}")
    return table

nombre = int(input("Entrez un nombre : "))
resultats = multiply_table(nombre)
for resultat in resultats:
    print(resultat)
