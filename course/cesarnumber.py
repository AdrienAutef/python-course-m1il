#Écrire la fonction qui permet de réaliser le chiffre de César 
#avec un décalage de 1 dans un premier temps.
#Dans un second temps, ajouter le décalage en paramètre 
#de la fonction.

text = "Two roads diverged in a yellow wood, \
And sorry I could not travel both \
And be one traveler, long I stood \
And looked down one as far as I could \
To where it bent in the undergrowth"
decalage = int(input("Entrez un décalage pour votre codage cesar"))

def chiffre_de_cesar(text, decalage):
    resultat = ""
    for char in text:
        if char.isalpha():
            decalage_amount = 65 if char.isupper() else 97
            lettre_code = (ord(char) - decalage_amount + decalage) % 26 + decalage_amount
            resultat += chr(lettre_code)
        else:
            resultat += char
    return resultat

texte_chiffre = chiffre_de_cesar(text, decalage)
print(texte_chiffre)

