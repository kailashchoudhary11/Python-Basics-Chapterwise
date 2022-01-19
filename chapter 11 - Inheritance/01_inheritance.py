# This class is called as Parent Class or Base Class 
class Employee:
    company = "Google"

    def showDetails(self):
        print("This is an employee")

# This class will be called as Derived class or Child class 
class Programmer(Employee):
    # company = "YouTube"
    language = "python"
    
    def getLanguage(self):
        print(f"The language is {self.language}")

    def showDetails(self):  # --> This will override the method in the employee class
        print("This is a programmer")

e = Employee()
e.showDetails()

p = Programmer()
p.showDetails() # This will print This is an employee when we comment out the showDetails method in the Programmer class
p.getLanguage()
# e.getLanguage() # --> This will throw error as there is no method called getLanguage in the Employee class

print(p.company) # There is no attribute called as company in the Programmer class yet it will be printed because the Programmer class is derived from the Employee class which has the attribute company

