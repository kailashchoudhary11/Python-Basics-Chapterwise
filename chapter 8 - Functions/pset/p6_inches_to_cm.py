def inchToCm(inch):
    return inch * 2.54

inches = float(input("Enter the value in inches: "))
print(f"{inches} inches to cm is {inchToCm(inches)}")