# Patterns

for i in range(5):
    print("* " * 5)

for i in range(5):
    print("* " * (i + 1))

for i in range(5):
    print("* " * (5 - i))

for i in range(5):
    print("  " * (5 - i - 1) + "* " * (i + 1))

for i in range(5):
    print("  " * i + "* " * (5 - i))

for i in range(5):
    print(" " * (5 - i - 1) + "* " * (i + 1))

# # Strings in Python


# Different ways to define a string in python

s1 = "Hello World"
s2 = 'Hello World'
s3 ='''
Multi
line
string
'''
s4 ="""
Multi
line
string
"""

print(s1)
print(s2)
print(s3)
print(s4)

# Basic interview question - String is Mutable or Immutable?
# ANS: String is IMMUTABLE

# Mutable: insert, delete and update operations CAN be performed
# Immutable: insert, delete and update operations CANNOT be performed

x1 = "HelloWorld"

x1[0]
print(x1[0])

x1[0] = "W"

# ## Operations on strings


# ### 1. Concatenation (+)


str1 = "Uncle "
str2 = "likes "
str3 = "Aunt"
str4 = str1 + str2 + str3

print(str4)

# ### 2. Repetition (*)


str5 = "yolo"
print(10 * str5)

# ### 3. Membership (in, not in)


str6 = "HelloWorld"
print("oWo" in str6)
print("iWi" not in str6)

# ### 4. Indexing & Slicing


Site_Name = slice(8,-4)
website_0 = "HTTPS://google.com"
website_1 = "HTTPS://wikipedia.com"
print(website_0[Site_Name])
print(website_1[Site_Name])

# string[start:end:step]
# Positive step always traverses from left to right
# Negative step always traverses from right to left

Text = "Test Input"
Half_Text = Text[0:4]
Half_Text = Text[4:]
Half_Text = Text[10::-2]
Half_Text = Text[5::-1]
Half_Text = Text[::]
Half_Text = Text[-15:10:]
Half_Text = Text[0:20]
print(Half_Text)


# Reversing the string

Text = "Hello World"
rev = ""
for i in range(len(Text) - 1, -1, -1):
    rev += Text[i]
print(rev)


# Reversing the string - Optimized

Text = "Hello World"
rev = ""
for char in Text:
    rev = char + rev
print(rev)
