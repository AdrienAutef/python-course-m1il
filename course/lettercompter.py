#Faire une analyse statistique d'un texte, celle-ci affichera un 
#dictionnaire avec le décompte de chaque lettre.

text = "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth."

alphabet = "abcdefghijklmnopqrstuvwxyz"
result={}

for char in alphabet:
    result[char] = text.count(char)

print(result)