# # OOP - Object Oriented Programming


# OOP is a programming paradigm that organizes code around objects and classes rather than just functions and logic 

# class - blueprint
# object - actual data

# Procedure OPL vs Object OPL
# C is PL
# C++, Python are OOPL
# Java is pure OOPL
# Maintainance is expensive in PL compared to OOPL
# In POPL, data is not secure, any function can access global variable
# easy to scale the software with OOP

# class is a keyword, food is the class name
# class variable - the value of class variable is same for all the objects

class food:
    food_name = "Biryani"  # class variable

obj1 = food()  # creating the object of food() class
print(obj1.food_name)  # accessing the class variable
obj1.food_name

# class variable value can only be changed by class name
food.food_name = "Rice"

obj2 = food()
print(obj2.food_name)  # class object can access the class data

# access the class variable with class name
print(food.food_name)

# class variable value cannot be changed by object
obj3 = food()
obj3.food_name = "Noodles"  # creating it's own local variable with the same name
print(obj3.food_name)  # printing the new local variable
print(food.food_name)

# constructor function

# constructor function gets called automatically when the object is created
# constructor function is used for initializing the variables

# class variable value is SAME for all the ojects but instance variable can be DIFFERENT

# self is a variable which points to the current object

class Bike:
    No_tyre = 2  # class variable

    def __init__(self, name):
        self.bike_name = name  # instance variable
        print(self.bike_name)

obj1 = Bike("RE")
obj2 = Bike("HD")

# member functions

class Bike:
    No_tyre = 2  # class variable

    def __init__(self, name):
        self.bike_name = name  # instance variable
        print(self.bike_name)

    def display(self):
        print("Bike")

obj1 = Bike("RE")
obj2 = Bike("HD")
obj1.display()
