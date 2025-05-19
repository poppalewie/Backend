#Ask for length & width to calculate area
def area_rectangle():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of the rectangle is {area}")
    except ValueError:
        print("Please enter valid numbers")

area_rectangle()
#Ask for number and returns if prime
def is_prime(number):

    if number <= 1:
        return False
    for i in range (2, int(number ** 0.5) + 1):
        return False
    return True
try:
    number= int(input("Enter a number: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Enter a valid number")

#print multiplication table for a given number

def multiplication_table():
    try:
        number = int(input("Enter a number: "))
        print(f"\nMultiplication table for {number}:")
        for i in range(1, 11):
            result = number * i
            print(f"{number} x {i} = {result}")
    except ValueError:
        print("Please enter a valid integer.")

multiplication_table()

# 1. Cube a number using a lambda function
def cube_number():
    try:
        number = float(input("Enter a number to cube: "))
        cube = (lambda x: x ** 3)(number)
        print(f"The cube of {number} is {cube}")
    except ValueError:
        print("Please enter a valid number.")

cube_number()

#Use map to triple all numbers in a list
def triple_list_numbers():
    numbers = [1, 2, 3, 4, 5]
    tripled = list(map(lambda x: x * 3, numbers))
    print(f"Original list: {numbers}")
    print(f"Tripled list: {tripled}")

triple_list_numbers()

#Use filter to get numbers greater than 5 from a list
def filter_greater_than_five():
    numbers = [2, 5, 6, 8, 1, 3, 9]
    filtered = list(filter(lambda x: x > 5, numbers))
    print(f"Original list: {numbers}")
    print(f"Numbers greater than 5: {filtered}")

filter_greater_than_five()

#clean code with menu for all these functions

def area_rectangle():
    try:
        length = float(input("Enter the length: "))
        width = float(input("Enter the width: "))
        area = length * width
        print(f"The area of the rectangle is {area}")
    except ValueError:
        print("Please enter valid numbers")

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def check_prime():
    try:
        number = int(input("Enter a number: "))
        if is_prime(number):
            print(f"{number} is a prime number.")
        else:
            print(f"{number} is not a prime number.")
    except ValueError:
        print("Enter a valid number")

def multiplication_table():
    try:
        number = int(input("Enter a number: "))
        print(f"\nMultiplication table for {number}:")
        for i in range(1, 11):
            print(f"{number} x {i} = {number * i}")
    except ValueError:
        print("Please enter a valid integer.")

def cube_number():
    try:
        number = float(input("Enter a number to cube: "))
        cube = (lambda x: x ** 3)(number)
        print(f"The cube of {number} is {cube}")
    except ValueError:
        print("Please enter a valid number.")

def triple_list_numbers():
    numbers = [1, 2, 3, 4, 5]
    tripled = list(map(lambda x: x * 3, numbers))
    print(f"Original list: {numbers}")
    print(f"Tripled list: {tripled}")

def filter_greater_than_five():
    numbers = [2, 5, 6, 8, 1, 3, 9]
    filtered = list(filter(lambda x: x > 5, numbers))
    print(f"Original list: {numbers}")
    print(f"Numbers greater than 5: {filtered}")

def main():
    while True:
        print("\nChoose an option:")
        print("1. Calculate area of a rectangle")
        print("2. Check if a number is prime")
        print("3. Print multiplication table")
        print("4. Cube a number")
        print("5. Triple numbers in a list")
        print("6. Filter numbers greater than 5 from a list")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")
        if choice == '1':
            area_rectangle()
        elif choice == '2':
            check_prime()
        elif choice == '3':
            multiplication_table()
        elif choice == '4':
            cube_number()
        elif choice == '5':
            triple_list_numbers()
        elif choice == '6':
            filter_greater_than_five()
        elif choice == '7':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()
