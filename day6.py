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