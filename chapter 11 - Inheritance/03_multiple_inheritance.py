'''
Multiple Inheritance

        Parent1        Parent2
              \        /
                Child 
        In Multiple Inheritance one class is derived from two classes. All the attributes and methods from both the classes are imported in the child class 
'''

class Employee:
    company = "Visa"
    eCode = 120

class Freelancer:
    company = "Fiverr"
    level = 0

    def upGradeLevel(self):
        self.level += 1

class Programmer(Employee, Freelancer): # The attributes and methods of the class Employee will get Priority as the class Employee is written first and then class Freelancer
    name = "Rohit"

p = Programmer()

print(p.level)
p.upGradeLevel()
print(p.level)

print(p.company)