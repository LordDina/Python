numbers = []

input_len = int(input("Enter the number of values: "))

for i in range(input_len):
    val = float(input(f"Enter number {i+1}: "))
    numbers.append(val)

numbers.sort()

n = len(numbers)

if n % 2 == 1:   
    median = numbers[n // 2]
else:            
    median = (numbers[n//2 - 1] + numbers[n//2]) / 2

print("La médiane est :", median)
