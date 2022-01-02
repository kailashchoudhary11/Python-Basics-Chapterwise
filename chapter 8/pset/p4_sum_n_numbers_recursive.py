def sumNNumbers(n):
    if n == 1: return 1
    return n + sumNNumbers(n - 1)

n = int(input("Enter the value of n: "))

print(f"The sum of first {n} natural numbers is {sumNNumbers(n)}")