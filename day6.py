#Inheritance
#Syntax & basic example(dog inherits from animal and uses it's methods)
#parent class
class Animal:
    def speak(self):
        print("Animal speaks")

#child class
class Dog(Animal):
    def bark(self):
        print("Dog barks")

dog = Dog()
dog.speak()  #inherited from Animal
dog.bark()  #Defined in Dog

#Using __init__()
class Animals:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")
class Dog(Animals):
    def __init__(self, name, breed):
        super().__init__(name)  #call parent class's constructor
        self.breed = breed

    def show_info(self):
        print(f"{self.name} is a {self.breed}")

d = Dog("Tusker", "German")
d.speak()
d.show_info()

#class vehicle
class Vehicle:
    def start_engine(self):
        print(f"Engine started.")

class Car(Vehicle):

    def play_music(self):
        print(f"Playing music")

car = Car()
car.start_engine()
car.play_music()
    
#encapsulation
'''
Public	        name	    Accessible from anywhere
Protected   	_name	    Accessible within class & subclasses
Private     	__name	    Name mangled; internal use only
'''
#private attribute(prefixed with double underscores) with getter
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  #private attribute

    def deposit(self, amount):
        if amount > 0:
             self.__balance += amount
             print(f"Deposited {amount}. New balance: {self.__balance}")
        
        else:
            print("Invalid amount")

    def get_balance(self):
        return self.__balance

acc = BankAccount("Alice", 1000)
acc.deposit(500) 
print(acc.get_balance())
#Gives error since it's a private attribute
#print(acc.__balance)

#Using setters & getters
class Student:
    def __init__(self, name):
        self.__grades = []
        self.name = name

    def add_grade(self, grade):
        self.__grades.append(grade)

    def get_grades(self):
        return self.__grades
    
#class student with private attribute as a list
class Student:
    def __init__(self, name):
        self.name = name
        self.__grades = []
#method to add grade
    def add_grade(self, grade):
        self.__grades.append(grade)
#method to return grades
    def get_grades(self):
        return self.__grades
#create an instance
student1 = Student("Alice")
#add grades
student1.add_grade(87)
student1.add_grade(90)
student1.add_grade(78)

print(student1.get_grades())

#polymorphism
#Circles with area() method,print area() function,Input
class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
def print_area(shape):
    print("Area:", shape.area())

width = float(input("Enter the width of the rectangle: "))
length = float(input("Enter the length of the rectangle: "))
rect = Rectangle(width, length)
print_area(rect)

radius = float(input("Enter the radius of the circle: "))
circle = Circle(radius)
print_area(circle)

#method overriding
class Animal:
    def make_sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def make_sound(self): #overriding the parent method
        print("Dog barks")

a = Animal()
d = Dog()

a.make_sound()
d.make_sound()

#calling parent method with super()
class Bird:
    def fly(self):
        print("Bird is flying")

class EAgle(Bird):
    def fly(self):
        super().fly() #call the parent method
        print("Eagle soars high in the sky")

e = EAgle()
e.fly()

#zoo system with inheritance,encapsulation,polymorphism & method overriding
class Animal:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

    def make_sound(self):
        print("Some generic sound")

#class inherits from animal & overrides make_sound
class Dog(Animal):
    def make_sound(self):
        print("Bark")

class Cat(Animal):
    def make_sound(self):
        print("Meow")

#zoo class using encapsulation
class Zoo:
    def __init__(self):
        self.__animals = []

    def add_animal(self, animal):
        self.__animals.append(animal)

    def make_all_sounds(self):
        for animal in self.__animals:
            animal.make_sound()                 #polymorphism

zoo = Zoo()

zoo.add_animal(Dog("Buddy", 4))
zoo.add_animal(Cat("whiskers", 2))

zoo.make_all_sounds()

#encapsulation
class Library:
    def __init__(self):
        self.__books = [] 

    def add_book(self,book):
        self.__books.append(book)
        print(f"Added '{book}' from the library.")

    def remove_book(self, book):
        if book in self.__books:
            self.__books.remove(book)
            print(f"REmoved '{book}' from the library.")
        else:
            print(f"'{book}' not found in the library.")

    def get_books(self):
        return self.__books
    
library = Library()
library.add_book("python 101")
library.add_book("Data Science basics")
print(library.get_books())
library.remove_book("python 101")
print(library.get_books())

#POLYMORPHISM
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

class Rectangle(Shape):
    def __init__(self, width , length):
        self.width = width
        self.length = length

    def area(self):
        return self.width * self.length
    
def print_area(shape):
    print(f"Area: {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(4, 6)
print_area(circle)
print_area(rectangle)

#METHOD OVERRIDING & CLASS/STATIC METHODS
class Employee:
    company = "Tech Corp"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_info(self):
        return f"{self.name} earns {self.salary}"

    @classmethod
    def get_company(cls):
        return cls.company
    
    @staticmethod
    def is_valid_salary(salary):
        return salary > 0
    
class Manager(Employee):
    def __init__(self, name, salary, department):
        super().__init__(name, salary)
        self.department = department

    def get_info(self):
        base_info = super().get_info()
        return f"{base_info} and manages the {self.department} department"

emp = Employee("Alice", 50000)
mgr = Manager("Bob", 80000, "Engineering")
print(emp.get_info())
print(mgr.get_info())
print(Employee.get_company())
print(Employee.is_valid_salary(50000))