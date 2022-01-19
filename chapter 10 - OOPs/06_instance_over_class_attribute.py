# defining a class 
class Employee:
    company = "Google" # This is class attribute
    salary = 200

# Instantiating objects of the class 
kai = Employee()
ray = Employee()

# Updating values of instance attributes
kai.name = "kai"
ray.name = "ray"

# This will create instance attribute of salary for kai and ray which will be preferred over class attribute
kai.salary = 250
ray.salary = 300

# Printing the values of instance attributes
# The values 250 and 300 will be printed respectively instead of 200 
print(kai.salary) # While printing this, the interpreter will first find whether there is an instance attribute named salary. If an instance attribute is present than it will print the value of instance attribute and if there is no such instance attribute than the interpreter will search for class attribute. Hence, the instance attributes are always preferred over class attributes.  
print(ray.salary)