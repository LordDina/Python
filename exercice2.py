a = 20
b = 25
c = 30
if (a >= b and a <= c) or (a >= c and a <= b):
    median = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    median = b
else:
    median = c

print("La median est", median)