class Demo:
    a = 22

b = Demo()

b.a = 9 # This will create a new instance variable a and set it's value to 9. This won't update the value of class attribute

print(Demo.a) # The value of class attribute won't change 

Demo.a = 99 # This will change the value of the class attribute
print(Demo.a)
