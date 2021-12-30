num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))
num4 = int(input("Enter the forth number: "))

# Method 1
 
# if (num1 > num2 and num1 > num3 and num1 > num4):
#     print("The greatest number is", num1)
# elif(num2 > num3 and num2 > num4):
#     print("The greatest number is", num2)
# elif(num3 > num4):
#     print("The greatest number is", num3)
# else:
#     print("The greatest number is", num4)

# Method 2

if (num1 > num4):
    f1 = num1
else:
    f1 = num4

if (num2 > num3):
    f2 = num2
else:
    f2 = num3

if (f1 > f2):
    print("The greatest number is", f1)
else:
    print("The greatest number is", f2)
