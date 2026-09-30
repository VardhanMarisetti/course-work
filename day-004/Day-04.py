
# # While loop


# Example-1

i = 1  #initialization
while i <= 10:  # i <= 10 or (i <= 10) is condition
    print(i)
    i += 1

i = 1
while i <= 10:
    i += 1
    print(i)

# Example-2: break statement
# Break statement helps exiting the loop

i = 1
while i <= 10:
    print(i)
    if i == 5:
        break
    i += 1

# Example-3: continue statement
# Continue will take the control to the start of the loop
# Skip the current iteration

i = 1
while i < 10:
    i += 1
    if i < 5:
        continue
    print(i)

i = 1
while i < 10:
    i += 1
    print(i)
    if i < 5:
        continue

# infinite loop

i = 1
while i < 10:
    if i < 5:
        continue
    i += 1
    print(i)

i = 1
while i < 10:
    i += 1
    if i < 5:
        continue
    print(i)
    if i > 8:
        break

# Example-4: else statement with while loop
# else statement executes only if loop is successfully completed

i = 1
while i <= 10:
    print(i)
    i += 1
    if i == 11:
        break
else:
    print("Loop is completely executed")

# Example-5: pass statement
# pass statement is just a placeholder

i = 0
while  i <= 10:
    if i == 5:
        pass
    else:
        print(i)
    i += 1

# # For loop


animals = ["Tiger", "Cat", "Dog", "Pig", "Monkey"]

for animal in animals:
    print(animal)

food_name = "Chicken_Biryani"

for letter in food_name:
    print(letter)

# for loop with range()
# range() funtion is used to generate list of elements
# syntax of range(): range(start, end, step)
# start = 0
# end = end - 1
# step = 1

for i in range(10): # start
    print(i)

for i in range(4, 10): # start, end
    print(i)

for i in range(4, 10, 2): # start, end , step
    print(i)

# break statement with for loop

for num in range(1, 6):
    if num == 3:
        break
    print(num)

# continue statement with for loop

for num in range(1, 6):
    if num == 3:
        continue
    print(num)

# nested loop
# time complexity - O(n * m)

for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)

for i in range(1, 4):
    for j in range(i, 4):
        print(i, j)

# else statement with for loop

for i in range(10):
    if i == 2:
        continue
    elif i == 4:
        break
    else:
        print(i)
    pass
else:
    print("Successful")

for i in range(10):
    print(i)
    if i == 9:
        break
else:
    print("Okay")
