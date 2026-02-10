


#Classes : Class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
'''
class Point:
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point1 = Point()  # This creates an instance of the Point class and assigns it to the variable point1

point1.x = 10  # This adds an attribute x to the point1 object and assigns it the value 10
point1.y = 20  # This adds an attribute y to the point1 object and assigns it the value 20
print(point1.x)  # This prints the value of the x attribute of the point1 object, which is 10
print(point1.y)  # This prints the value of the y attribute of the point1 object, which is 20


point1.move()  # This calls the move method on the point1 object
point1.draw()  # This calls the draw method on the point1 object

'''

'''
class Person:
    def exercise(self):
        print("I am exercising")
    
    def eat(self):
        print("I am eating")

person1 = Person()

person1.exercise()  # This calls the exercise method on the person1 object
person1.eat()  # This calls the eat method on the person1 object

'''

#Constructor: A constructor is a special method in a class that is automatically called when an object of the class is created. It is used to initialize the attributes of the object.

# __init__ is the constructor method in Python. It is defined within a class and is used to initialize the attributes of an object when it is created. The __init__ method takes self as the first parameter, which refers to the instance of the class being created, and can also take additional parameters to initialize other attributes.
'''
class Person:
    def __init__(self, name, age):
        self.name = name  # This initializes the name attribute of the Person object with the value passed as an argument
        self.age = age  # This initializes the age attribute of the Person object with the value passed as an argument

person1 = Person("Sujal", 20)  # This creates an instance of the Person class with the name "Sujal" and age 20, and assigns it to the variable person1
print(person1.name)  # This prints the value of the name attribute of the person1 object, which is "Sujal"
print(person1.age)  # This prints the value of the age attribute of the person1 object, which is 20

'''

#EXERCISE:

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}")

person1 = Person("Sujal")
person1.talk()  # This calls the talk method on the person1 object, which prints a greeting message including the person's name

person2 = Person("Alice")
person2.talk()  # This calls the talk method on the person2 object, which prints a greeting message including the person's name


#Inheritance: Inheritance is a fundamental concept in object-oriented programming that allows a class (called the child class or subclass) to inherit attributes and methods from another class (called the parent class or superclass). This promotes code reusability and establishes a hierarchical relationship between classes.

class Animal:
    def speak(self):
        print("Animal speaks")


class Dog(Animal):  # Dog class inherits from Animal class
    def bark(self):
        print("Dog barks")

dog = Dog()  # This creates an instance of the Dog class and assigns it to the variable dog
dog.speak()  # This calls the speak method inherited from the Animal class, which prints "Animal speaks"
dog.bark()  # This calls the bark method of the Dog class, which prints "Dog barks"


class Cat(Animal):  # Cat class inherits from Animal class
    def meow(self):
        print("Cat meows")

cat = Cat()  # This creates an instance of the Cat class and assigns it to the variable cat
cat.speak()  # This calls the speak method inherited from the Animal class, which prints "Animal speaks"
cat.meow()  # This calls the meow method of the Cat class, which prints "Cat meows" "Animal speaks"

