# ### read/write mode - "r+"


# r+ mode doesn't create a new file, file must already exist

with open("new_file2.txt", "r+") as f:
    f.write("newer line 1")
    f.seek(0)
    print(f.read())

# ### append/read mode - "a+"
# a+ : Append/Read

with open("pavan_reddy.txt", "a+") as f:
    f.write("pawan reddy file")
    f.seek(0)
    print(f.read())