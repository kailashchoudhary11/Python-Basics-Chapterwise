import math

class Calculator:

    def square(self):
        print(f"The square of the number is {self.num ** 2}")
    
    def cube(self):
        print(f"The cube of the number is {self.num ** 3}")

    def squareRoot(self):
        print(f"The square root of the number is {math.sqrt(self.num)}")

    @staticmethod
    def greet():
        print("************** Namaste! **************")

calc = Calculator()
calc.greet()
calc.num = int(input("Enter a number: "))

calc.square()
calc.cube()
calc.squareRoot()