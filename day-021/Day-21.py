# # File Handling


import os
os.getcwd()

# ### read mode - "r"


f = open("file.txt", "r")  # open("file_name", "mode") & f is file object

print(type(f))

for line in f:
    print(line)

f.close()  # closing the file or deleting from RAM

# with statement closes the file automatically

with open("file.txt", "r") as f:
    for line in f:
        print(line)

# read() to get all lines from the file

with open("file.txt", "r") as f:
    print(f.read())  # read the entire file

# readlines() to get all the lines into a list and to access a particular data line

with open("file.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print(lines[0])
    print(*lines)  # unpacking of list

# ### write mode - "w"


with open("new_file.txt", "w") as f:
    f.write("new line 0\nnew line 1")

with open("new_file.txt", "r") as f:
    print(f.read())

# In "w" mode new data overwrites the previous data

with open("new_file.txt", "w") as f:
    f.write("new line 2\nnew line 3")

with open("new_file.txt", "r") as f:
    print(f.read())
