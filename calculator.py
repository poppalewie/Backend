#Calculator using functions and control flow
#Defining functions

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

#show menu & get user's choice 

print("Welcome")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")
#process the input with error checks

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1,num2))

        except ValueError:
            print("Invalid number input.")

    elif choice == '5':
        print("Exiting")
        break
    

    else:
        print("Invalid choice.Please enter a number between 1 and 5")


'''
🧩 Bonus Extensions for the Simple Calculator
✅ Beginner-Level Enhancements
More Math Operations
Power (a ** b)
Modulo (a % b)
Integer division (a // b)
Square root (math.sqrt(a))
Rounding the Result
Let the user choose to round the result: round(result, 2)
Continue with Last Result
Allow using the last result as the first number in the next calculation.
Formatted Output
Display results like: 7 × 6 = 42

⚠️ Input Handling Improvements
Input Re-entry on Error
Instead of restarting, prompt again if input is invalid.
Accept Operation as Symbols
Let users type +, -, *, / instead of selecting numbers.
Support Negative Numbers and Decimals
Already possible using float()—ensure no restrictions.

📁 File & Data Features
Log Calculations to a Text File
Example: 7 * 6 = 42 saved in calculator_log.txt
Read Operations from File
Perform calculations listed in a file line-by-line.

📊 Intermediate Functional Additions
History Feature
Keep a list of past results in memory and print on demand.
Undo Last Operation
Let the user undo or re-run the previous calculation.
Chained Calculations
Example: 5 + 3 - 2 * 4 — use expression parsing (e.g., eval() carefully).

🎨 Advanced or GUI/UX Enhancements
GUI Calculator
Use tkinter or PyQt for buttons, input fields, and display area.
Command-Line Color Styling
Use libraries like colorama to highlight results or errors.
Voice Input and Output
Use speech_recognition and pyttsx3 for voice-based interaction.

💡 Challenging / Smart Features
Scientific Calculator Mode
Trigonometry, logarithms, factorials using math module.
Memory Slots
Store results in memory (M+, M-, MR functionality).
Graphing Capabilities
Use matplotlib to graph expressions like y = 2x + 3.
Unit Conversion Integration
Combine with the temperature converter: add length, weight, time conversions.
Natural Language Input
Parse sentences like “What’s the product of 7 and 6?” (via re or NLP tools).
'''