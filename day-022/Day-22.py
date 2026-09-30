# ### append mode - "a"


# "a" or append mode can add data to existing data in a file

with open("new_file.txt", "a") as f:
    f.write("\nnew line 4\nnew line 5")

with open("new_file.txt", "r") as f:
    print(f.read())

# ### writelines - write multiple lines together


with open("new_file.txt", "a") as f:
    f.writelines(["\nnew line 6\nnew line 7", "\nnew line 8"])

with open("new_file.txt", "r") as f:
    print(f.read())

# ### write/read mode - "w+"


# w+ mode creates a new file and overwrites the existing one

with open("new_file2.txt", "w+") as f:
    f.write("newer line 0")
    f.seek(0)  # brings the pointer to mentioned position
    print(f.read())
