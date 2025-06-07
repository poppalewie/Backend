'''
#utils module,functions
def to_uppercase(string):
    return string.upper()
def reverse_string(string):
    return string[::-1]

import math_utils

#test uppercase function
uppercase_result = math_utils.to_uppercase("Hello world")
print("Uppercase:", uppercase_result)

#test reverse string function
reversed_result = math_utils.reverse_string("welcome")
print("Reversed:" , reversed_result)
'''