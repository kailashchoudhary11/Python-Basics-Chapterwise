class Employee:
    company = "Google"
    def getSalary(self):  # This is an object method as it accepts object as an argument
        print(f"Salary is {self.salary}")
    def getCompany(self):
        print(f"Company of the employee is {self.company}")

kai = Employee()
kai.salary = 100000
kai.getSalary()
# This is internally done in the following way 
# Employee.getSalary(kai)

kai.getCompany()