import math

class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, c):
        return ComplexNumber(self.real + c.real, self.imaginary + c.imaginary)

    def __mul__(self, c):
        return ComplexNumber((self.real * c.real) - (self.imaginary * c.imaginary), (self.real * c.imaginary) + (self.imaginary * c.real))

    def __sub__(self, c):
        return ComplexNumber(self.real - c.real, self.imaginary - c.imaginary)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {abs(self.imaginary)}i"
        else:
            return f"{self.real} + {self.imaginary}i"


c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(8, 7)

sum = c1 + c2
print(sum)

product = c1 * c2
print(product)

difference = c1 - c2
print(difference)