# ## Bitwise operators (<<, >>, ^, ~, &, |)


# Bitwise operators works on binary number
# Bitwise operators are faster than arithmatic operators
# Bitwise operators perform many operations easier due to binary number system

a = 10
b = 3

print(a & b)
print(a | b)
print(a ^ b)

a = 10
b = 3
c = 2
"""
1010
0011
0010
"""
print(a & b & c)
print(a | b | c)
print(a ^ b ^ c)

# #### Left shift (<<), Right shift (>>)


# Def : Left shift : Inset new bits (0) right to the LSB
# Def : Right shift :  Delete bits from the LSB

# Left shift  
# a << k  
# a * 2 ** k  
# Number is doubled  


a = 10

print(a << 1)
print(a << 8)

# Right shift  
# a >> k  
# a / 2 ** k  
# Floor of the value  
# Number is halved


a = 400

print(a >> 1)
print(a >> 7)

# #### Bitwise Not (~)


# Def : Flip the bits
# 

a = 10
print(~a)

a = -10
print(~a)

# ## Assignment operators (+=, -=, *=, /=,...)


a = 10

a += 5 # a = a + 5
print(a)

a -= 5 # a = a - 5
print(a)

a *= 5 # a = a * 5
print(a)

a /= 5 # a = a / 5
print(a)

# &=, |=, ^=, <<=, >>=, :=

a = 10
a &= 3
print(a)

a = 10
a |= 3
print(a)

a = 10
a ^= 3
print(a)

a = 10
a <<= 3
print(a)

a = 10
a >>= 2
print(a)


# Walrus operator (:=)
# walrus operator wiil first assign the value of the variable then pass it to outer function

print(a := 2)
# print(a = a : 2)

 ## Comparison operators (==, >=, <=, !=, <, >)


a = 10
b = 5

print(a == b)
print(a >= b)
print(a <= b)
print(a != b)
print(a < b)
print(a > b)

# ## Logical operators (and, or, not)


a = True
b = False

print(a and b)
print(a or b)
print(not a)
print(not b)

# ## Identity operators (is, is not)


a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a == b)
print(a is b)
print(a is c)
print(a is not b)

# ## Membership operators (in, not in)


Fruits = ['Mango', 'Apple', 'Orange', 'Banana']

print('Papaya' in Fruits)
print('Papaya' not in Fruits)

# ## Interview Questions - Operators


# Variable Swap with XOR without temp variable

a = 100
b = 20
a = a ^ b
b = a ^ b
a = a ^ b
print(a, b)

# XOR or three numbers

p1 = 245
p2 = 982
p3 = 245

print(p1 ^ p2 ^ p3)

# Find even or odd

a = 1187974233
if (a & 1):
    print("ODD")
else:
    print("EVEN")

# # Input in Python


val = input("Enter your phone number")

# Default data type of input function is string

print(val)
print(type(val))

val = int(input("Enter your phone number"))
print(val, type(val))

val = float(input("Enter your phone number"))
print(val, type(val))

# Recieving multiple inputs
x1, x2, x3 = input("Enter 3 names").split()

print(x1, x2, x3)

# Default method for spliting the inputs is giving 'space'
# To change the character for spliting, we can insert the character in braces of split function

x1, x2, x3 = input("Enter 3 words").split(',')

print(x1, x2, x3)

# Map function is used to typecast using split function

x1, x2, x3 = map(int, input("Enter 3 numbers").split(','))

x1, x2, x3 = map(float, input("Enter 3 numbers").split(','))

print(type(x1), type(x2), type(x3))

