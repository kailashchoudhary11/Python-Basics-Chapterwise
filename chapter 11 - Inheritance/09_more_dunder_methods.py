class Number:

    # __init__ is also called as an dunder method as it has two underscores

    def __init__(self, num):
        self.num = num

    def __add__(self, num2): # This method is used for overloadind +
        print(f"Lets add {self.num} and {num2.num}")
        return self.num + num2.num

    def __mul__(self, num2): # This method is used for overloadind *
        print(f"Lets multiply {self.num} and {num2.num}")
        return self.num * num2.num

    def __sub__(self, num2): # This method is used for overloadind -
        print(f"Lets subtract {self.num} and {num2.num}")
        return self.num - num2.num

    def __truediv__(self, num2):
        print(f"Let's divide {self.num} and {num2.num}")
        return self.num / num2.num

    def __floordiv__(self, num2):
        print(f"Let's divide {self.num} and {num2.num} and get floor value")
        return self.num // num2.num

    def __str__(self): 
        return (f"Decimal number {self.num}")

    def __len__(self):
        return 1
        
n = Number(8)
print(n)
print(len(n))