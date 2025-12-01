a = int(input("entrer le premier nombre: "))
b = int(input("entrer le deuxieme nombre: "))
c = int(input("entrer le troisiem nombre: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    median = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    median = b
else:
    median = c

print("La median est")
print(median)
