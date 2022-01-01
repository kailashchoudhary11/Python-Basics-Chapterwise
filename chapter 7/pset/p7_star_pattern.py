# Pattern for n = 4
#    *
#   ***
#  *****
# *******

n = int(input("Enter a number: "))

# Method 1 

# for i in range(n): 
    # for j in range(2 * n):
        # if (j <= n + i and j >= n - i):
            # print("*", end='')
        # else: 
            # print(" ", end='')
    # print()
    

# Method 2

for i in range(n):
    print(" " * (n - i - 1), end = "")
    print("*" * (2 * i + 1), end = '')
    print(" " * (n - i - 1))