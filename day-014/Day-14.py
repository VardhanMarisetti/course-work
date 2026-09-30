# ## Inheritance


# Inheritance allows us to define a class that inherits the properties or functions of the parent class
# Parent class - Base class
# Child class - Derived class

# ### Single Inheritance


# One parent One child

# parent class
class hyd_food:
    taste = "Good"

    def Biryani(self):
        print("Decent")

# child class
class PistaHouse(hyd_food):
    pass

obj_child = PistaHouse()  # object of child class

# child class object can access the properties & functions of parent class
print(obj_child.taste)
obj_child.Biryani()

# super() function
# super() is used to access the parent properties and functions from inside the child class

class hyd_food:
    taste = "Good"

    def Biryani(self):
        print("Decent")

class PistaHouse(hyd_food):
    def display(self):
        super().Biryani()
        print(super().taste, self.taste)

obj_child = PistaHouse()
obj_child.display()

# constructor function

class hyd_food:
    taste = "Good"

    def __init__(self):
        print("Parent Class")

    def Biryani(self):
        print("Decent")

class PistaHouse(hyd_food):
    '''
    def __init__(self):
        print("Child Class")
    '''

obj_child = PistaHouse()

# if child class constructor function is not defined then parent class constructor function is called

# ### Multiple Inheritance


# Many parent One child

class parent1:
    name = "P1"
    name1 = "P1"

    def __init__(self):
        print("cons of parent1")

    def fun(self):
        print("Parent1")

    def fun1(self):
        print("Parent1")

class parent2:
    name = "P2"
    name2 = "P2"

    def __init__(okay):
        print("cons of parent2")
        
    def fun(self):
        print("Parent2")

    def fun2(self):
        print("Parent2")

class child1(parent2, parent1):
    # name = "C1"
    pass
    
'''
    def fun(self):
        print("Child1")
'''

obj = child1()

print(obj.name)
print(obj.name1)
print(obj.name2)

obj.fun()
obj.fun1()
obj.fun2()

# parent class mentioned first when creating the child class takes priority
# second parent class doesn't overwrite the properties of first class

# super()
# super() follow the MRO approach

class A:
    def display(self):
        print("A class")
        super().display()

class B:
    def display(self):
        print("B class")

class C(A, B):
    def all(self):
        super().display()

obj = C()
obj.all()

# MRO - Method Resolution Order
print([i.__name__ for i in C.__mro__])
print(C.__mro__)
