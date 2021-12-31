n = int(input("Enter the value of n: "))
sum = 0
i = 1
while i <= n:
    sum += i
    i += 1

print(f"The sum of first {n} natural numbers is {sum}")
print(f"The sum of first {n} natural numbers is {n * (n + 1) / 2}")