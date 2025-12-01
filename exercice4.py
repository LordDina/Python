chaine = input("Entrez chaine de caract : ")
nb_lettres = 0
nb_chiffres = 0
for char in chaine:

    if char >= '0' and char <= '9':
        nb_chiffres += 1

    elif char >= 'a' and char <= 'z':
        nb_lettres += 1

    elif char >= 'A' and char <= 'Z':
        nb_lettres += 1

print("nombre de lettres :", nb_lettres)
print("nombre de chiffres :", nb_chiffres)