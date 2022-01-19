import math as mt

num = int(input("Enter a number: "))
numRoot = int(mt.sqrt(num))
isPrime = True
for i in range(2, numRoot + 1):
    if (num % i == 0):
        isPrime = False
        break

if (isPrime):
    print(f"{num} is a Prime Number")
else:
    print(f"{num} is Not a Prime Number")