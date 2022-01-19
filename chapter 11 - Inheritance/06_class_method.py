class Employee:
    company = "Camel"
    salary = 100
    location = "delhi"

    def changeSalary(self, salary): # This method won't change the class attribute but add a new instance attribute
        self.salary = salary    

    # def updateSalary(self, salary):
        # self.__class__.salary = salary # This will update the value of class attribute salary

    # Decorator is a function that takes function as input and modifies the function     
    @classmethod
    def updateSalary(cls, sal):
        cls.salary = sal

e = Employee()

# Changing the value of instance variables
# print(e.salary)
# print(Employee.salary)

e.changeSalary(200) # Will create a new instance variable salary and set it's value to 200

# print(e.salary)
# print(Employee.salary)

# Changing the value of class attributes

print(e.salary)
print(Employee.salary)

e.updateSalary(500)

print(e.salary)
print(Employee.salary)

