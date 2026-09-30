def fun(**var):
    for i in var:
        print(f"{i} : {var[i]}")

fun()
fun(A = "Hello")
fun(A = "Hello", B = "World")

# ## Lamda function


# ## Recursive function


# ## Enumerate funtion


# enumerate function adds the counter (index) with the list items

fruits = ["Mango", "Orange", "Banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)

for index, fruit in enumerate(fruits, start = 2):
    print(index, fruit)



# ## Zip function


l1 = ["A", "B", "D", "F"]
l2 = ["C", "E", "G"]
l3 = ["H", "I", "J", "K"]

l4 = zip(l1, l2, l3)
print(list(l4))

# ## Decorators


'''
Decorator is a function that takes another function as input and adds extra functionality
and returns a modified function, without chaning the original function code
'''

def decorator_fun(func):
    def wrapper_fun():
        func()
        print("add cherry")
        print("add choco chips")
    return wrapper_fun

def cake():
    print("take some flour")
    print("add aggs and other ingredients")
    print("put it in the oven")

final_fun = decorator_fun(cake)
final_fun()

def decorator_fun2(func2):
    cake2()
    print("world")
    print("okay")

def cake2():
    print("hello")

final_fun2 = decorator_fun2(cake2)
final_fun2


def decorator_fun(func):
    def wrapper_fun():
        func()
        print("add cherry")
        print("add choco chips")
    return wrapper_fun

@decorator_fun

def cake():
    print("take some flour")
    print("add aggs and other ingredients")
    print("put it in the oven")

cake()

def decorator_fun1(func):
    def wrapper_fun():
        print("buy the ingredients")
        func()
    return wrapper_fun

def decorator_fun2(func):
    def wrapper_fun():
        func()
        print("add cherry")
        print("add choco chips")
    return wrapper_fun

@decorator_fun1
@decorator_fun2

def cake():
    print("take some flour")
    print("add aggs and other ingredients")
    print("put it in the oven")

cake()
