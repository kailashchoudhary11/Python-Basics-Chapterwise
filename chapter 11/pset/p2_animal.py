class Animal:
    
    def eat(self):
        print("Eating ...")

class Pet (Animal):
    def walkWithMaster(self):
        print("Walking with master")

class Dog (Pet):
    
    @staticmethod
    def bark():
        print("Barking... ")

tommy = Dog()

tommy.bark()
tommy.walkWithMaster()
tommy.eat()