#Écrire un programme qui épellera un numéro de 
#téléphone en toute lettre.

dictionary = {
    '0': 'Zero',
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '+': 'Plus'
}
phone_number = input("Entrez un numéro de téléphone : ")

resultat = ''
for i, chiffre in enumerate(phone_number):
    if chiffre in dictionary:
        resultat += dictionary[chiffre]
        if i < len(phone_number) - 1:
            resultat += ' '

print(resultat)
