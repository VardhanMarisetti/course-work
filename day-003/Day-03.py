
# 1. Concatenation using commas
# 2. String concatenation using +
# 3. str.format() method
# 4. f-strings method (python 3.6+ version)
# 5. Escape sequences
# 6. End and Sep parameters in print()

# ## Concatenation using commas


Name = "VM"
Pin = 500090
Place = "Hyderabad"

print(Name, Pin, Place)

# ## String concatenation using +


First_name = "John"
Last_name = "Smith"
Age = 24

print(First_name + " " + Last_name + " " + str(Age))

# ## str.format() method


Name = "John"
Age = 24

print("Name: {}  Age: {}".format(Name, Age))
print("Name: {1}  Age: {0}".format(Age, Name))

# ## f-strings


Name = "John"
Age = 24

print(f"Name: {Name}  Age: {Age}")

# ## Escape sequences


Name = "VM"
Pin = 500090
Place = "Hyderabad"

print(f"Name: {Name} \nPin: {Pin} \nPlace: {Place}")

print(f"Name: {Name} \tPin: {Pin} \tPlace: {Place}")

print(f"Name: \"{Name}\" Pin: \"{Pin}\" Place: \"{Place}\"")

# ## End and Sep parameters in print()


Name = "VM"
val = "004"

print(Name, end = " 004")
print()
print(Name, end = "")
print(val)
print(Name, val,  sep = " + ")

# end parameter is used to decide how the print statement will END
# sep parameter decides how the multiple values will be SEPARATED

# # Conditional Statements


# Example-1: if condition

a = 10
if a % 2 == 0:
    print(a)

# Example-2: if-else condition

a = 11
if a % 2 == 0:
    print("EVEN")
else:
    print("ODD")

# Ternary condition
# value_if_true if condition else value_if_false 

print("EVEN") if a % 2 == 0 else print("ODD")

a = 15

print("Hello") if a % 3 == 0 else print("World")

# Example-3: elif condition

Number = input("Enter a number from 1 - 10")

if Number == "2":
    print(f"{Number} is even prime")
elif Number == "4":
    print(f"{Number} is square of even prime")
elif Number == "9":
    print(f"{Number} is largest one digit number")
else:
    print(Number)

Number = input("Enter a number from 1 - 10")

if Number == "2":
    print(f"{Number} is even prime")
else:
    if Number == "4":
        print(f"{Number} is square of even prime")
    else:
        if Number == "9":
            print(f"{Number} is largest one digit number")
        else:
            print(Number)

Number = input("Enter a number from 1 - 10")

print(f"{Number} is even prime") if Number == "2" else print(f"{Number} is square of even prime") if Number == "4" else print(f"{Number} is largest one digit number") if Number == "9" else print(Number)

Number = input("Enter a number from 1 - 10")

(
print(f"{Number} is even prime") if Number == "2" else
print(f"{Number} is square of even prime") if Number == "4" else
print(f"{Number} is largest one digit number") if Number == "9" else
print(Number)
)

# ## Match case


# Match case is used to replace multiple if-else conditions
# Match case is more powerful than the Switch case statement
# Match case works with variables and data structures

# Example-1

num = int(input("Enter a number"))

match num:
    case 10:
        print("You entered 10")
    case 20:
        print("You entered 20")
    case 30:
        print("You entered 30")
    case _:
        print("Something else")

Number = input("Enter a number from 1 - 10")

match Number:
    case "2":
        print("2 is even prime")
    case "4":
        print("4 is square of even prime")
    case "9":
        print("9 is largest one digit number")
    case _:
        print(Number)

# Example-2: data struc with match case

data = [1, 2, 3, 4]

match data:
    case [4, 3, 2, 1]:
        print("Hello")
    case [1, 2, 3, 4]:
        print("World")

# Example-3: if condition with match case

val = int(input("Enter a number"))

match val:
    case x if x > 0:
        print("It is a positive number")
    case y if y < 0:
        print("It is a negative number")
    case _:
        print("It is a zero")

# Practice Question

x = 15

if x > 3:
    print("A")
    if x % 3 == 0 and x:
        print("B")
    elif x == 15:
        print("D")
    else:
        print("E")
else:
    print("C")
