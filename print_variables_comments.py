print("This is an example of printing a string")

string = "This is a string stored inside a variable"

# This is a comment
# Below is an example of an integer and float stored inside variables
integer = 3
float = 3.0

print(integer, float)

"""
This is supposed to be a 'multi-line comment', which Python should ignore
because this string literal is not stored inside a variable
Python does not have an intended syntax for multi-line comments.
"""

# You can check the type of a variable with the type() function
print(type(string))
print(type(integer))
print(type(float))

# Variables are case sensitive
a = 1
A = 1

print(a,A)

# Conventional methods of naming variables
camelCaseVariableNaming = 33
PascalCaseVariableNaming = 22
snake_case_variable_naming = 11
# Variable names can only use A-Z, 0-9 and _
# You cannot name a variable starting with a number or use a hyphen -

# You can assign many values to multiple variables in one go as follows:
aa, bb, cc = "Blue", "Green", "Yellow"
print (aa,bb,cc)

# Or one value to many variables
dd = ee = ff = "Potato"
print(dd,ee,ff)

# Unpacking from a list, tuple etc
fruits = ["apple", "banana", "cherry"]
gg, hh, ii = fruits
print(gg)
print(hh)
print(ii)

# Variables have a 'global' keyword which can be used inside functions to
# make them belong to the global scope rather than the function code block