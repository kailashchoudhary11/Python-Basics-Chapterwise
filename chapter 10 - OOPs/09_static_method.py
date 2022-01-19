class Student:
    @staticmethod  # This is a decorator which is used to make static methods in Student
    def greet(): # This will make a static method 
        print("Good morning")

    @staticmethod
    def time():
        print("The time is 11 am in the morning")


kai = Student()
kai.greet() # This is used to call the static method
Student.greet() # We can also call static method using the class name

kai.time()
