class Employee:
    company = "Bharat Gas"
    salary = 5000
    salaryBonus = 800
    # totalSalary = 5800

    @property # This is also called as getter method
    def totalSalary(self): # This is a function but seems like a property or attribute
        return self.salary + self.salaryBonus

    @totalSalary.setter # This is used to set the value of salary
    def totalSalary(self, val):
        self.salaryBonus = val - self.salary
    
  

e = Employee()
print(e.totalSalary)
e.totalSalary = 5000
print(e.totalSalary) 