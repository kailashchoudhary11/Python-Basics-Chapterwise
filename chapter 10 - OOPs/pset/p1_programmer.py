class Programmer:
    company = "Microsoft"

    def __init__(self, name, programmingLanguage, salary):
        self.name = name 
        self.programmingLanguage = programmingLanguage
        self.salary = salary
    
    def printDetails(self):
        print(f"The name of the programmer is {self.name}")
        print(f"The Programming Language of the programmer is {self.programmingLanguage}")
        print(f"The salary of the programmer is {self.salary}")
        print(f"The company of the programmer is {self.company}")
        
kai = Programmer("Kai", "Java", 2000000)
max = Programmer("Max", "Python", 30000000)
ray = Programmer("Ray", "C++", 4000000)

kai.printDetails()
max.printDetails()
ray.printDetails()