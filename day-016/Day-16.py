# ### Hybrid Inheritance


# Many parent and many child. combination of two or more types of inheritance

class A:
    def __init__(self):
        print("cons_A")

    def fun(self):
        print("class A")

class B(A):
    def __init__(self):
        print("cons_B")

    def fun(self):
        print("class B")
        super().fun()

class C(B):
    def __init__(self):
        print("cons_C")

    def fun(self):
        print("class C")
        super().fun()

class D(B):
    def __init__(self):
        print("cons_D")

    def fun(self):
        print("class D")
        super().fun()

class E(C, D):
    '''
    def __init__(self):
        print("cons_E")
    '''
    def fun(self):
        print("class E")
        super().fun()
    
print([i.__name__ for i in E.__mro__])
print()
obj = E()
print()
obj.fun()

class A:
    def fun(self):
        print("A")

class B(A):
    def fun(self):
        print("B")
        
class C(A):
    def fun(self):
        print("C")

class D(C):
    def fun(self):
        print("D")

class E(D, B):
    def fun(self):
        print("E")
        A.fun(self)

print([i.__name__ for i in E.__mro__])
obj = E()
obj.fun()

# ## Polymorphism


# the word polymorphism means "Many forms"
# same function or operator can perform many different tasks

# ### Function overloading


# this type of function overloading is supported in c++ & java
# based upon number of arguments passed to function, c++ & java can differentiate the functions

def fun(var1):
    print(var1)

def fun(var1, var2):
    print(var2)

#fun(10)

# #### Using default arguments for function overloading


def fun(var1, var2 = None):
    if var2 is not None:
        print(var1, var2)
    else:
        print(var1)

fun(10)
fun(10, 20)

def calc(a = 0, b = 0, c = 0, d = 0):
    return a + b + c + d

print(calc())
print(calc(100, 200))
print(calc(100, 200, 100))
print(calc(100, 300, 100, 200))
