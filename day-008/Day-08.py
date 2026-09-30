# ## Set 


empty_set = set()
empty_set1 = {}

print(empty_set, type(empty_set))
print(empty_set1, type(empty_set1))

set0 = set()
set1 = set([10, 20, 30])
set2 = set((10, 20, 30))

# Frozen set is immutable (cannot perform insert, delete and update)
fr_set = frozenset([10, 20, 30])

nested_set0 = {10, 20, (30, 40), "Hello"}
# nested_set1 = {10, 20, [30, 40], "Hello"}
# nested_set2 = {10, 20, {30, 40}, "Hello"}
nested_set3 = {10, 20, fr_set, "Hello"}

# IMP: Mutable items cannot be stored inside a set
# Only immutable items can be stored in a set

print(set0, type(set0))
print(set1, type(set1))
print(set2, type(set2))
print(fr_set, type(fr_set))
print(nested_set0, type(nested_set0))
# print(nested_set1, type(nested_set1))
# print(nested_set2, type(nested_set2))
print(nested_set3, type(nested_set3))

# ### insert in set (add(), update())


set1 = {10, 20.5, "Hello"}

# add() function is used to insert one item in the set

set1.add("World")
print(set1)

set1.add((10, 20, 30))
print(set1)

# update() function is used for inserting multiple items together

set1.update((100, 200))
print(set1)

set1.update([100, 200])
print(set1)

set1.update({100, 200})
print(set1)

set1.update(((100, 200)))
print(set1)

set1.update({(100, 200)})
print(set1)

set1.update([(300, 400)])
print(set1)

# ### delete operation on set (remove(), discard(), pop(), clear())


dinner_set = {"Rice", "Biryani", "Chapati", "Fish", "Chicken"}

# remove() function removes an item that is passed to it
# remove() outputs an error if the item is missing

dinner_set.remove("Fish")
print(dinner_set)

# discard() DOESN'T output an error or interrupt the execution flow if the item is missing

dinner_set.discard("Chicken")
print(dinner_set)

# pop() function deletes a random item since there is no indexing or order of items in set

dinner_set.pop()
print(dinner_set)

dinner_set.clear()
print(dinner_set)

del dinner_set

# ### in-built set functions


set2 = {10, 20, 30, 40, 50}

print(set2)
print(len(set2))
print(min(set2))
print(max(set2))
print(sum(set2))

l1 = sorted(set2)
print(l1)

l1 = sorted(set2, reverse = True)
print(l1)

# ### containment operation on set


festivals = {"Pongal", "Diwali", "Onam", "Dussehra"}

if "Holi" in festivals:
    print("Happy Holi")
elif "Pongal" not in festivals:
    print("Happy pongal")
elif "Diwali" in festivals:
    print("Happy Diwali")
else:
    print("Happy Day")
