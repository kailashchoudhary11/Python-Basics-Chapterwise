# For n = 3
# *
# **
# ***

n = int(input("Enter the value of n: "))

# Method 1 
# for i in range(n):
    # for j in range(i + 1):
        # print("*", end='')
    # print()

# Method 2

for i in range(n):
    print("*" * (i + 1))