numbers = [2,5,3,4,5] #list of 5 numbers
numbers.append(7) #add 7 to the list
numbers.pop(0)  #remove first element from the list
numbers.sort()
print(numbers[:3]) #outputs sorted list(first 3 numbers)


#dictionary
#dict for student name, age and grades as list
student = {"name": "Alice", "age": 20, "grades": [90,85,88]}
#get() to safely access a non existent key
print(student.get("email", "No email")) #output : no email
print(student.keys()) #output dict_keys(['name', 'age', 'grades'])
print(student.values()) #output dict_values(['alice', 20, [90,85,88]])

#tuples
#tuple for a point (x,y)
point = (3,4)
print(f"Point: {point}")
#two sets of numbers and find their intersection
set1 = {1,2,3,4,5}
set2 = {7,8,9,4,3}
common = set1.intersection(set2)
print(f"Common elements: {common}") #output: {3,4}


'''
💻 PRACTICE (4 HOURS)
🔸 Hour 1: Lists — Exercises
Write a Python program that:
Adds items to a list
Reverses and sorts a list
Uses list comprehension to get even numbers
🛠️ Practice Platform:
HackerRank Python Lists
Exercism.io Lists Track
🔸 Hour 2: Tuples — Exercises
Create a program to:
Store coordinates as tuples
Unpack values from a tuple
Swap values using tuple unpacking
🛠️ Practice:
W3Schools Python Tuples Quiz
Create a mini address book using a list of tuples.
🔸 Hour 3: Dictionaries — Exercises
Create a dictionary of student names and grades.
Add, remove, and update values.
Find the student with the highest grade.
🛠️ Practice:
HackerRank: Dictionaries and Maps
Exercism.io: Dict Practice
🔸 Hour 4: Mini Project – Student Report Card App
Project Description:
Build a small Python program that:
Accepts student names and marks as input
Stores data in a dictionary
Calculates average, highest, and lowest scores
Displays report for each student
Features:
Use dict for students
Use list for marks
Use tuple for fixed-grade levels (("A", "B", "C", ...))


'''