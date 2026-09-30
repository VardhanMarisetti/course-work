 ### Multilevel Inheritance


# Multiple parent and child generations/levels

class minus:
    def __init__(self):
        print("MINUS")
        
    def funmin(self):
        print("Minus")

    def fun(self):
        print("Okay-")

class zero(minus):
    def __init__(self):
        print("ZERO")
        
    def funzer(self):
        print("Zero")

    def fun(self):
        print("Okay0")
        
class plus(zero):
    def __init__(self):
        print("ZERO")
        
    def funpl(self):
        print("Plus")
        super().funzer()

    def fun(self):
        print("Okay+")
        
class plus_plus(plus):
    def __init__(self):
        print("PLUS PLUS")
        
    def funplpl(self):
        print("Plus Plus")
        super().fun()
        
    def fun(self):
        print()
        print("Okay++")
        super().funpl()
        super().fun()
        super().funpl()
        
obj_plus_plus = plus_plus()

obj_plus_plus.funplpl()
obj_plus_plus.funpl()
obj_plus_plus.funzer()
obj_plus_plus.funmin()
obj_plus_plus.fun()

print()

obj_plus = plus()

obj_plus.funpl()
obj_plus.funzer()
obj_plus.funmin()
obj_plus.fun()

# ### Hierarchical Inheritance


# Many child One parent

class Parent:
    def __init__(self):
        print("cons_parent")
        
    def funP(self):
        print("parent")

class Child1(Parent):
    def __init__(self):
        print("cons_child1")
        
    def funC1(self):
        print("child1")

class Child2(Parent):
    def __init__(self):
        print("cons_child2")
        
    def funC2(self):
        print("child2")

obj_c2 = Child2()

obj_c2.funC2()
obj_c2.funP()

print([i.__name__ for i in Child2.__mro__])
