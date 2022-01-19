# defining a class 

class Employee:
    company = "Google" # This is class attribute

# Instantiating objects of the class 
kai = Employee()
ray = Employee()

# Accessing the attributes of the class
print(kai.company)
print(ray.company)

# Changing the value of class Attribute
Employee.company = "YouTube"

print(kai.company)
print(ray.company)