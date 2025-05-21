#attributes 
#phone class,2 attributes,my_phone as object &print
class Phone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

# Creating an object with values
my_phone = Phone("Samsung", "Galaxy S21")
# Accessing attributes
print(my_phone.brand)  # Output: Samsung
print(my_phone.model)  # Output: Galaxy S21

#methods
#method to make phone ring
class Phone:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def ring(self):
        print(f"{self.brand} {self.model} is ringing!")
    def describe(self):
        print(f"This phone is a {self.color} {self.brand} {self.model} ")

# Create an object
my_phone = Phone("Samsung", "Galaxy S21", "Black")

# Call the method
my_phone.ring()
my_phone.describe()

#class laptop,attributes & method info() that uses self to print
class Laptop:
    def __init__(self, brand, processor):
        self.brand = brand
        self.processor = processor

    def info(self):
        print(f"This is a {self.brand} laptop with an {self.processor} processor")
laptop1 = Laptop("Dell", "Intel i5")  
laptop1.info()  

#class student,attributes,method introduce
class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print(f"Hi, my name is {self.name}. I'm {self.age} years old and studying {self.course}")

student1 = Student("Alice", 20, "CS")
student1.introduce()

#Bank acc class with classes,objects,attributes,methods,__init__,self
class BankAccount:
    def __init__(self, account_holder, balance, account_type):
        self.account_holder = account_holder
        self.balance = balance
        self.account_type = account_type

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{amount} deposited. New Balance: {self.balance}")
        else:
            print("Deposit amount must be positive!")
    def withdraw(self, amount):
        if amount <= self.balance:
            print(f"{amount} withdrawn. New Balance: {self.balance}")
        else:
            print("Insufficient funds.")
    def check_balance(self):
        print(f"{self.account_holder}, your account balance is: {self.balance}")

account1 = BankAccount("Lewis", 50000, "savings")

account1.deposit(10)
account1.withdraw(5)
account1.check_balance()

#class person
class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person1 = person("Lewis", 25)
person2 = person("JOhn", 24)

person1.introduce()
person2.introduce()

#class book
class Book:
    library_name = "city square"

    def __init__(self,title, author):
        self.title = title
        self.author = author
    def get_book_info(self):
        print(f"{self.title} by {self.author}, available at {self.library_name} ")
book = Book("thc", "Lewis")
book.get_book_info ()


'''
🌟 Challenge 1: Library Book System
Goal: Create a Book class with the following:
Attributes: title, author, available
Method borrow() – sets available = False and prints a message
Method return_book() – sets available = True and prints a message
Method status() – shows whether the book is available or borrowed
📌 Bonus: Add logic to prevent borrowing an already borrowed book.

🌟 Challenge 2: Online Shopping Cart
Goal: Create a Product class and a Cart class.
Product has name, price
Cart stores a list of Product objects
Method add_product(product) adds a product to the cart
Method total_price() calculates and prints the total
Method show_cart() lists all product names in the cart
📌 Bonus: Add a method to remove a product by name.

🌟 Challenge 3: Student Grading System
Goal: Create a Student class with:
Attributes: name, grades (a list)
Method add_grade(score)
Meth
Method print_summary() that shows name and average grade
📌 Bonus: Add logic to ensure only numbers between 0 and 100 are accepted.

🌟 Challenge 4: Simple Bank Transfer (Object Interaction)
Goal: Expand your BankAccount class to support transfers.
Add a method transfer(amount, target_account) that:
Deducts from the current account
Adds to the target_account
Prints success/failure messages
'''