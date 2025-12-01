numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9)

nb_pairs = 0
nb_impairs = 0

for n in numeros:
    
    if n % 2 == 0:
        nb_pairs += 1
    else:
        nb_impairs += 1

print("le nombre de nombres pairs :", nb_pairs)
print("le nombre de nombres impairs :", nb_impairs)
