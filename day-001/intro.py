# # Python Indentation


# Indentation is used to define a block
# Unnecessary space is not allowed in python

x = 10
 y = 10.5
  z = "Hello"

print(x, y, z)

x = 10
if x == 10:
    print("Hello")

# Python compiler differentiates between tab space and multiple spaces
# It is not mandatory to have certain number of spaces.
# We should use uniform number of spaces within a block

# # Python Comments


# Comments can be written with '#' at the beginning of the line

"""
Python compiler ignores strings that are not assigned to any variables and are not operated upon.
We exploit this property and use triple quotes to use them as multiline comments
"""

print("Hello")

# # Type Casting


# Changing the data type of a variable or element

v1 = int(5.6)
print(v1)

v2 = True
v3 = False
print(type(str(v2)))
print(int(v2))
print(int(v3))

print(type(str(5)))

v4 = 5
print(float(v4))

v5 = True
print(float(v5))

v6 = int("1010", 2)
print(v6)

v7 = bool(1)
print(v7, type(v7))
