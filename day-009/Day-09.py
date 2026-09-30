# ## Dictionary


empty_dict0 = {}
empty_dict1 = dict()

print(empty_dict0, type(empty_dict0))
print(empty_dict1, type(empty_dict1))

# tuple can be used as a key
# list and set cannot be used as a key
# keys must be immutable
# list, tuple or set can be used as values
# values are mutable

int_dict = { 1 : 'Mango', 2 : 'Banana', 3 : 'Orange' }
float_dict = { 1.1 : 'Mango', 2.1 : 'Banana', 3.1 : 'Orange' }
str_dict = { 'A' : 'Mango', 'B' : 'Banana', 'C' : 'Orange' }
hetero_dict = { 1 : 'Mango', 'B' : 'Banana', 3.1 : 'Orange' }
tuple_dict0 = { (10) : 'Mango', 'B' : 'Banana', 3.1 : 'Orange' }
tuple_dict1 = { (10, 20) : 'Mango', 'B' : 'Banana', 3.1 : 'Orange' }
# list_dict = { (10) : 'Mango', 'B' : 'Banana', [10, 20] : 'Orange' }
# set_dict = { (10) : 'Mango', {30, 40} : 'Banana', [10, 20] : 'Orange' }

print(int_dict)
print(float_dict)
print(str_dict)
print(hetero_dict)
print(tuple_dict0)
print(tuple_dict1)
# print(list_dict)
# print(set_dict)

# dictionary as list comprehension

dict_comp = {x : x**2 for x in range(1, 11)}
print(dict_comp)

dict0 = { 1 : 'Mango', 2 : 'Banana', 3 : 'Orange' }
print(dict0)

# dict0[0]
dict0[1]

loft = [('A', 1), ('B', 2), ('C', 3)]
dict1 = dict(loft)
print(dict1)

lofl = [['A', 1], ['B', 2], ['C', 3]]
dict2 = dict(lofl)
print(dict2)

toft = (('A', 1), ('B', 2), ('C', 3))
dict3 = dict(toft)
print(dict3)

# toft2 = (('A', 1, 10), ('B', 2, 20), ('C', 3))
# dict4 = dict(toft2)
# print(dict4)

# sofl = {['A', 1], ['B', 2], ['C', 3]}
soft = {('A', 1), ('B', 2), ('C', 3)}
dict4 = dict(soft)
print(dict4)

# ### Accessing dictionary items


drinks = {
            "Beer" : 200,
            "Water" : 20,
            "Redbull" : 125,
            "Milk" : 50
}

val = drinks["Water"]
print(val)

val2 = drinks.get("Redbull")
print(val2)

# val3 = drinks["Monster"]
# print(val3)

val4 = drinks.get("Monster")
print(val4)

val5 = drinks.get("Monster", "custom value")
print(val5)

for i in drinks:
    print(i, drinks[i])

print()

print(drinks.keys())
print(drinks.values())
print(drinks.items())

print()

for key, value in drinks.items():
    print(f"{key}: {value}")

# nested dictionary
nest_dict = {
                100 : {"Hello" : 10, "World" : 20},
                200 : {"A" : 50, "B" : 60}
}

nest_dict[100]["World"]

# ### inset & update operations on dictionary


x_dict = {"name" : "MV", "age" : 24}
print(x_dict)

# if key already exists it updates the value
x_dict["age"] = 27
print(x_dict)

# if key doesn't exist it adds (or) inserts the items
x_dict["city"] = "Rajahmundry"
print(x_dict)

# update() funtion can insert and update multiple items together
x_dict.update({"age" : 25, "occupation" : "student", "name" : "VM"})
print(x_dict)

# ### delete operation on dictionary


# pop(), popitem(), clear(), del

x_dict

# pop() removes the item whose key is specified

x_dict.pop("occupation")
print(x_dict)

# popitem() removes the last element

x_dict.popitem()
print(x_dict)

# clear() removes all elements

x_dict.clear()
print(x_dict)

# del deletes the variable or data structure

del x_dict
