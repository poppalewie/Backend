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

'''
🌡️ Bonus Extensions — Temperature Converter
✅ Basic Enhancements
Support More Temperature Scales
Add support for Kelvin, Rankine, Réaumur.
Example:
Celsius → Kelvin: K = C + 273.15
Fahrenheit → Kelvin: K = (F − 32) × 5/9 + 273.15
Reverse Conversion Option
Allow user to select both input and output units:
"Convert from X to Y" (e.g., Fahrenheit → Celsius, Celsius → Kelvin, etc.)
Loop for Multiple Conversions
Allow users to convert multiple temperatures in one session.
Batch Conversion
Let users input a list of temperatures (e.g., 20, 25, 30) and convert all of them at once.

💾 File Input/Output Enhancements
Save Conversions to File
Export results to a .txt or .csv file for reference.
Read Temperatures from a File
Input a file containing temperatures (and units) and process all entries.

🎨 Formatting and Output Styling
Formatted Tables
Display results in a neat tabular format with column headers.
Color-Coded Output
Use colorama to highlight temperatures by range (e.g., red for hot, blue for cold).

🧠 Smart and Scientific Features
Temperature Category
Classify temperature into categories (e.g., Cold, Moderate, Hot).
Conversion History
Maintain a session history showing all conversions made.
Graphical Display
Use matplotlib to plot converted values (e.g., Celsius vs Fahrenheit line chart).
Error Handling for Impossible Values
Example: Negative Kelvin is invalid — warn the user.

🖥️ Advanced Features
GUI Version
Use tkinter to create a dropdown-based temperature converter app.
Voice Input & Output
Use speech_recognition and pyttsx3 to allow voice-controlled conversion.
API Integration
Connect to a web API to get temperature ranges in cities, and convert between units.
'''