#Le Fizz Buzz est un exercice courant en entretien d'embauche.
#Pour chaque multiple de 3 : Afficher Fizz
#Pour chaque multiple de 5 : Afficher Buzz
#Pour les multiples de 3 et 5 : Afficher Fizz Buzz
#Pour tous les autres : Afficher le nombre

def fizz_buzz(n):
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            print("Fizz Buzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


n = int(input("Entrez un nombre jusqu'auquel vous voulez faire le Fizz Buzz : "))
fizz_buzz(n)
