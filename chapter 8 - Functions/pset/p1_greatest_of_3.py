def greatestNumber(n1, n2, n3):
    if n1 > n2:
        if n1 > n3:
            return n1
        else:
            return n3
    elif n2 > n3:
        return n2
    else:
        return n3

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))
n3 = int(input("Enter number 3: "))

print("The greatest number of 3 is: " + greatestNumber(n1, n2, n3))
