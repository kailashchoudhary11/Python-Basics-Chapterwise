# __init__() This is called constructor which takes self arguments and can also take further arguments
class Employee:
    company = "Google"

    def __init__(self, name, salary, branch):
        self.name = name
        self.salary = salary
        self.branch = branch 
        print("A new Employee object is created!")

    def getSalary(self):
        print(f"The salary of the Employee is {self.salary}")

    def getName(self):
        print(f"The name of the Employee is {self.name}")

    def getBranch(self):
        print(f"The branch of the Employee is {self.branch}")
    
# max = Employee() # This will throw error as we are not passing the required arguments to the constructor
kai = Employee("Kai", 200000, "Developer")
kai.getName()
kai.getSalary()
kai.getBranch()