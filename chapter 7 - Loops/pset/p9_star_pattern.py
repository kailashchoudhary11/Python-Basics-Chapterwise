# For n = 4
# * * * *
# *     *
# * * * *

# * * *
# *   *
# * * *

n = int(input("Enter a number: "))

for i in range(n):
    print("*", end="")
    if i == 0 or i == n - 1:
        print(" *" * (n - 2), end = '')
    else:
        print("  " * (n - 2), end = '')
    print(" *")