'''
Multilevel Inheritance in Python

            Class 1
               |
            Class 2
               |
            Class 3

In this class 2 is inherited from class 1 and class 3 is inherited from class 2
'''

class Person:
    country = "India"

    def __init__(self):
        print("Initializing Person ...")

    def takeBreath(self):
        print("Breathing")

class Employee(Person):
    company = "Honda"

    def __init__(self):
        super().__init__()
        print("Initializing Employee ...")

    def getSalary(self):
        print(f"Salary is {self.salary}")
    
    def takeBreath(self):
        super().takeBreath()
        print("Employee is breathing")

class Programmer(Employee):
    company = "Fiverr"

    def __init__(self):
        super().__init__()
        print("Initializing Programmer ...")

    def getSalary(self):
        print("No salary to programmers")

    def takeBreath(self):
        super().takeBreath()
        print("Programer Breathing")
# p = Person()
# e = Employee()
pr = Programmer()

# p.takeBreath()
# e.takeBreath()
# pr.takeBreath()

# print(p.company) # This will throw an error 
# print(e.company)
# print(pr.company)
# print(p.country)
# print(e.country)
# print(pr.country)