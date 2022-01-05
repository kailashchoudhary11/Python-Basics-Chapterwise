'''
Single inheritance in Python

            Parent Class
                |
            Child Class
'''

class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

class Programmer(Employee):
    language = "python"
    
    def getLanguage(self):
        print(f"The language is {self.language}")

e = Employee()
e.showDetails()

p = Programmer()
p.showDetails() # This will print This is an employee when we comment out the showDetails method in the Programmer class


