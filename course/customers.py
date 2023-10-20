#A l'aide de listes et de dictionnaires, 
#trouver le meilleur moyen de stocker 
#toutes les données ci-contre dans une 
#seule et unique variable

client1 = {
    "Nom": "Doe",
    "Prénom": "John",
    "Age": 21,
    "Email": "john.doe@xyz.com",
    "Hobbies": ["Karaté", "Tennis"]
}
liste_clients = [client1]

print(liste_clients[0]["Nom"])  
print(liste_clients[0]["Hobbies"]) 
