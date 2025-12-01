a = 25
b = 15
c = 35
if (a >= b and a <= c) or (a >= c and a <= b):
    median = a
elif (b >= a and b <= c) or (b >= c and b <= a):
    median = b
else:
    median = c

print("La median entre les trois nombres est", median)