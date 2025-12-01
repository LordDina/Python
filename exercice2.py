a = int(input("Input the first number: "))
b = int(input("Input the first number: "))
c = int(input("Input the first number: "))

if (a >= b and a <= c) or (a >= c and a <= b):
    median = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    median = b
else:
    median = c

print("La median est")
print(median)
