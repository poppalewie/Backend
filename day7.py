'''
"mode" tells Python what to do with the file:
'r' → read
'w' → write (will overwrite if file exists)
'a' → append
'x' → create (error if file exists)
'b' → binary mode
't' → text mode (default)
'''

#create a file,write into it, read the content and print it
with open("my_note.txt", "w") as file:
    file.write("my note\n")
    file.write("I'm good")

with open("my_note.txt", "r") as file:
    content = file.read()
    print(content)

#read and print each name using a loop(for line in file)
with open("friends.txt", "w") as file:
    file.write("Jonte\n")
    file.write("Voke\n")
    file.write("Ann\n")

#append adds alex to the list
with open("friends.txt", "a") as file:
    file.write("Alex\n")

with open("friends.txt", "r") as file:
    for line in file:
        print(line.strip())
    
#Basic exception handling with try,except
'''
Exception	            When it happens
FileNotFoundError	    Trying to read a file that doesn't exist
PermissionError     	No permission to access a file
IsADirectoryError   	Trying to open a folder like a file
ValueError	            Wrong data type
ZeroDivisionError	    Dividing by zero
'''

'''
Define a custom exception called TooShortError.
Write a function write_note(text) that:
Raises TooShortError if text has fewer than 10 characters.
Otherwise, writes the text to note.txt.
Use a try/except block to test it with a short string.
'''
#Define custom exception
class TooShortError(Exception):
    pass

#define function that uses the exception
def write_note(text):
    if len(text) < 10:
        raise TooShortError("The note is too short. Please write at least 10 characters.")

    with open("note.txt", "w") as file:
        file.write(text)
    print("Note written succesfully!")

#test with try except
try:
    user_input = "Hi"
    write_note(user_input)
except TooShortError as e:
    print("Custom Error Caught:", e)

'''
🏁 Final Summary Project: Smart Note Keeper
🎯 Goal:
Build a small program that:
Asks the user for a note.
Checks if it’s long enough.
Appends it to a file with a timestamp.
Displays the full content of the note file.
Handles all major exceptions gracefully (file not found, empty note, etc).

🔧 Requirements:
✅ Use with open(...) for file handling.
✅ Use try/except to handle:File not found
Custom exception for short notes
✅ Use "a" mode to append notes
✅ Show all notes at the end
'''
from datetime import datetime
import os

class TooShortNoteError(Exception):
    pass

NOTES_FILE = "smart_notes.txt"
PASSWORD = "1234"  # you can change this

def add_note():
    text = input("📝 Enter your note: ").strip()
    if len(text) < 10:
        raise TooShortNoteError("Note too short. Please write at least 10 characters.")
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"{timestamp} - {text}\n"

    with open(NOTES_FILE, "a") as file:
        file.write(entry)
    print("✅ Note saved.\n")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    
    print("\n📚 All Notes:")
    with open(NOTES_FILE, "r") as file:
        for line in file:
            print(line.strip())
    print()

def menu():
    while True:
        print("===== Smart Note Keeper =====")
        print("1. Add Note")
        print("2. View All Notes")
        print("3. Search Notes")
        print("4. Filter by Date")
        print("5. Edit Last Note")
        print("6. Delete All Notes")
        print("7. Exit")
        print("=============================")

        choice = input("Choose an option (1–7): ").strip()

        try:
            if choice == "1":
                add_note()
            elif choice == "2":
                view_notes()
            elif choice == "3":
                search_notes()
            elif choice == "4":
                filter_by_date()
            elif choice == "5":
                edit_last_note()
            elif choice == "6":
                delete_all_notes()
            elif choice == "7":
                print("👋 Goodbye!")
                break
            else:
                print("❗Invalid choice. Try again.\n")
        except TooShortNoteError as e:
            print("❌", e)
        except Exception as e:
            print("❗Unexpected error:", e)

# Placeholders for upcoming features
def search_notes():
    print("🔍 Search feature coming next...")

def filter_by_date():
    print("🗓️ Date filter coming next...")

def edit_last_note():
    print("✏️ Edit feature coming next...")

def delete_all_notes():
    print("🧹 Delete all notes feature coming next...")

# Start the app
menu()


#create file,write to it,read&print contents
#writing to a file
with open("notes.txt", "w") as file:
    file.write("Day 7 notes:\n")
    file.write("Learning file handling.\n")
    file.write("python is fun\n")

#reading the file
with open("notes.txt", "r") as file:
    print("Initial content:")
    for line in file:
        print(line.strip())

#appending to the file
with open("notes.txt", "a") as file:
    file.write("Adding a new line\n")

#reading again
with open("notes.txt", "r") as file:
    print("\nUpdated content:")
    for line in file:
        print(line.strip())

#create csvfile with student data, read and print contents
import csv

#writing to a csv
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "Grade"])
    writer.writerow(["Alice", 90])
    writer.writerow(["Bob", 85])
    writer.writerow(["Charlie", 92])

#reading from the csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

#custom exception,fuction that raises error if condition fails & handles multiple exceptions
class NegativeNumberError(Exception):
    pass

def calculate_square_root(number):
    if number < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number")
    return number ** 0.5

try:
    number = float(input("Enter a number to calculate it's square root: "))
    result = calculate_square_root(number)
except NegativeNumberError as e:
    print(f"Error: {e}")
except ValueError:
    print(f"Please enter a valid number!")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"Square root of {number} is {result}")
finally:
    print("Calculation attempt finished")