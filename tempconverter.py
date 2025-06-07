#ask user for conversion type
print("Welcome to temperature converter!")
print("Choose the conversion type:")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to celsius")

choice = input("Enter 1 or 2: ")

#logic based on user's choice 

if choice == "1":
    celsius = float(input("Enter temperature in celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius} is equal to {fahrenheit}")

elif choice == "2":
    fahrenheit = float(input("Enter temperature in fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit} is equal to {celsius}")

else:
    print("Invalid input. Please enter 1 or 2. ")


#REPEAT & HANDLE ERRORS
print("🌡️ Welcome to the Temperature Converter 🌡️")

while True:
    print("\nChoose conversion type:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Exit")

    choice = input("Enter 1, 2, or 3: ")

    if choice == "1":
        try:
            celsius = float(input("Enter temperature in Celsius: "))
            fahrenheit = (celsius * 9/5) + 32
            print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif choice == "2":
        try:
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            celsius = (fahrenheit - 32) * 5/9
            print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")
        except ValueError:
            print("⚠️ Please enter a valid number.")

    elif choice == "3":
        print("👋 Exiting. Stay cool or warm!")
        break

    else:
        print("❌ Invalid option. Please enter 1, 2, or 3.")
