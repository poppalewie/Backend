name = (input("Enter Your Name: "))
age = int(float(input("Enter Your Age: ")))
height_feet = int(float(input("Enter Your Height: ")))

age_in_5_years = age + 5
height_cm = height_feet * 30.48 #convert to cm
is_adult = age > 18

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
else:
    print("Adult")
#for loop(1-10)
for i in range(1, 11):
    print(i)
#while loop(even numbers 1-10)
num = 2
while num <= 10:
    print(num)
    num += 2
    
print(f"Your name is: {name}")
print(f"Age in 5 years: {age_in_5_years}")
print(f"Your Height in Cm: {height_cm}")
print(f"Is adult?: {is_adult}")

#lists
numbers = list(range(1, 11))
squares = [x**2 for x in numbers]
even_numbers = [x for x in numbers if x % 2 == 0]

print(f"Numbers: {numbers}")
print(f"Squares: {squares}")
print(f"Even numbers: {even_numbers}")