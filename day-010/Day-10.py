# # Functions


# A function is a block of code that performs a specific task which can be reusable later

def fun():
    print("Hello", end = " ")
    print("World")

fun()

def fun(val1, val2):
    print("Hello " * val1 + val2)

fun(2, "World")

def outer():
    print("Outer")
    def inner():
        print("Inner")
    inner()

outer()

def fun(a, b):
    c = a + b
    return c, 2*c, 3*c, a - b

val = fun(10, 20)
print(val)
print(type(fun(20, 30)))

val1, val2, val3, val4 = fun(20, 5)
print(val1, val2, val3, val4)

def get_something1():
    return

def get_something2():
    return None

def get_something3():
    pass

def get_something4():
    a = 10
    b = 20
    c = a + b

print(get_something1())
print(get_something2())
print(get_something3())
print(get_something4())

def fun():
    n1 = 20
    n2 = 20
    l1 = [1, 2, 3]
    t1 = (2, 3, 4, 2)
    return n1, n2, l1, l1, t1

fun()

def outer():
    def inner():
        print("Hello")
    return inner

print(outer)
inner = 100
f = outer()
print(f)
outer()()
f2 = outer
f2()()

def fun(var = "Nothing"):
    print(var)

fun()
fun("okay")

def fun(x = 10, y = 20):
    print(x + y)

fun()
fun(100)
fun(100, 200)

# ## passing arbituary number of arguements using *args


def fun(*var):
    for i in var:
        print(i)

fun()
fun("A")
fun("A", "B", "C")
