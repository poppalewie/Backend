#lists
'''#common list methods
append(x)	    Add x to end of list	fruits.append('grape')
insert(i, x)	Insert x at index i	fruits.insert(1, 'pear')
remove(x)	    Remove first item equal to x	fruits.remove('apple')
pop()	        Remove and return last item	fruits.pop()
len(list)	    Get number of items	len(fruits)
sort()	        Sort items in ascending order	numbers.sort()
reverse()   	Reverse order of items	fruits.reverse()

'''
numbers = [2,5,3,4,5] #list of 5 numbers
numbers.append(7) #add 7 to the list
numbers.pop(0)  #remove first element from the list
numbers.sort()
print(numbers[:3]) #outputs sorted list(first 3 numbers)

#fav movies list
my_favorite_movies = ["PB", "SOA", "GOT", "VIK", "BB"]
my_favorite_movies.append("ssSs")
my_favorite_movies.remove("SOA")
my_favorite_movies.insert(3, "FARGO")

print(my_favorite_movies)


#dictionary
'''
dict.get(key)	Returns value or None if key not found	d.get('name')
dict.keys()	    Returns all keys	                    d.keys()
dict.values()	Returns all values	                    d.values()
dict.items()	Returns list of (key, value) pairs	    d.items()
dict.update({})	Updates multiple values             	d.update({'age': 30})
'''

#dict for student name, age and grades as list
student = {"name": "Alice", "age": 20, "grades": [90,85,88]}
#get() to safely access a non existent key
print(student.get("email", "No email")) #output : no email
print(student.keys()) #output dict_keys(['name', 'age', 'grades'])
print(student.values()) #output dict_values(['alice', 20, [90,85,88]])

#student,add grade,change age,remove course,print
print(student['name'])           # John
print(student.get('age'))        # 21
student['age'] = 22              # Update age
student['grade'] = 'A'           # Add new key-value pair
del student['course']            # Remove key

#tuples
'''common operations
my_tuple[0]         # Access first item
len(my_tuple)       # Number of items
my_tuple.count(2)   # Count how many times 2 appears
my_tuple.index(3)   # Find index of 3
'''

#tuple that prints name,age,city
me_tuple = ("LEWIS", 23, "RONGAI")
print("\n")
print(f"Your name is: {me_tuple[0]}")
print(f"Your age is: {me_tuple[1]}")
print(f"Your city is: {me_tuple[2]}")

#tuple for a point (x,y)
point = (3,4)
print(f"Point: {point}")

#sets
'''common operations
add(x)	               Add element x	                        my_set.add(4)
remove(x)	           Remove element x (error if not found)	my_set.remove(2)
discard(x)	           Remove element x (no error if missing)	my_set.discard(10)
union(set2)	           Combine two sets	                        set1.union(set2)
intersection(set2) 	   Common items in both sets	            set1.intersection(set2)
difference(set2)	    Items in set1 but not in set2	        set1.difference(set2)
clear()	                Removes all elements	                my_set.clear()
'''

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