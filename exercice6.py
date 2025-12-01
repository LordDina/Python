temp = float(input("Entrez la tempErature : "))
unite = input("Entrez l'unité C OU F: ")
if unite == "F" or unite == "f":
    celsius = (temp - 32) * 5/9
    print("La température en Celsius est :", celsius, "degrés.")

elif unite == "C" or unite == "c":
    fahrenheit = (temp * 9/5) + 32
    print("La température en Fahrenheit est :", fahrenheit, "degrés.")
else:
    print("Tapez C ou F.")
