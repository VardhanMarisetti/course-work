# ## Tuple


t1 = (10, 10, 20.5, 4, "Hello", 8)
print(t1)
print(t1[-2])

# ### Creating different types of tuples


empty_tuple = ()
empty_tuple1 = tuple()
empty_tuple2 = tuple("hello")

print(empty_tuple, type(empty_tuple))
print(empty_tuple1, type(empty_tuple1))
print(empty_tuple2, type(empty_tuple2))

tuple1 = ([0, 0], [0, 0], {4, 4}, 1, 2, (3, 4))
print(tuple1)

help(tuple)

# Converting list and set to tuple

l1 = [2, "Hello", 1, 2, 4]
print(l1, type(l1))

t1 = tuple(l1)
print(t1, type(t1))

s1 = set(t1)
print(s1, type(s1))

t2 = tuple(s1)
print(t2, type(t2))

values = range(1, 11)
t3 = tuple(values)
print(t3, type(t3))

print(tuple(range(1, 11)))

t4 = t1 + t2 + t3
print(t4)

t5 = tuple(i for i in range(10))
print(t5)

tuple

t6 = tuple()
print(type(t6))
t6 = [i for i in range(10)]
print(t6, type(t6))

# ### Accessing the tuple items


veg_tuple = ("tomato", "potato", "onion", "chilli")

print(veg_tuple[::])
veg_tuple[-1:-2:-1]

# ### Insert, delete and update operations indirectly


tuple1 = (10, 20.5, "Hello", [10, 20, 30])
tuple1[3][2]
tuple1[3] = 5000
tuple1[3][2] = 5000
print(tuple1)

# tuple item cannot be updated directly
# complete item in tuple cannot be updated directly
# but if item is mutable then elements inside the mutable item can be updated

tuple2 = (10, 20, 30)
print(tuple2)

list1 = list(tuple2)
list1.append(40)
list1.remove(30)
list1.pop(0)
list1.clear()
list1.extend([10, 20, 30, 40])
list1.insert(0, 0)
del list1[4]
tuple2 = tuple(list1)
print(tuple2)
del tuple2
print(tuple2)

# ### in-built tuple functions


salary = (24, 30, 40, 80, 28, 40, 25)

print(len(salary))
print(min(salary))
print(max(salary))
print(sum(salary))
print(reversed(salary))
print(tuple(reversed(salary)))

# sort() function sorts the data in the same data structure without needing extra space
# sorted() function requires extra space to sort the data
# sort() function doesn't return anything
# sorted() function returns a list by default

sorted_list = sorted(salary)
print(sorted_list)
sorted_list = tuple(sorted(salary, reverse = True))
print(sorted_list)
