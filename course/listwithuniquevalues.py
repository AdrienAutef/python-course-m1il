input_list = input("Entrez une liste de valeurs séparées par des espaces : ")
input_list = input_list.split()
unique_list = []
for item in input_list:
    if item not in unique_list:
        unique_list.append(item)


print("Liste avec des valeurs uniques : ", unique_list)
