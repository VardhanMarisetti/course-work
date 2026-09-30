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

# ## Encapsulation


# Encapsulation refers to the binding of data (attributes) and functions into one unit (class)
# Encapsulation restrict direct access of the data
# We can access the variable/data/attributes through object outside the class
# We can access the variable/data/attributes through functions defined inside the class

class Bike:
    No_tyre = 2 # class variable / attribute

    def __init__(self, name, price):
        self.bike_name = name
        self.bike_price = price

    def details(self):
        print(self.bike_name, self.bike_price)

obj1 = Bike("RE", 2.5)
obj1.details()
print(obj1.bike_name)
obj1.bike_name
print(obj1.No_tyre)
obj1.No_tyre
obj1.No_tyre

# ### Access specifiers / types of attributes in encapsulation


class marvel:
    def __init__(test, name, power, weapon):
        test.Name = name # public instance variable
        test._Power = power # protected instance variable
        test.__Weapon = weapon # private instance variable

    def show(test):
        print(test.Name, test._Power, test.__Weapon)

obj1 = marvel("Iron-Man", 3000, "Suit")
obj1.show()

print(obj1.Name)
print(obj1._Power)

# Protected variables can be accessed outside the class but you shouldn't do it
# In python public, protected, private concept is used just as a sign or warning

# print(obj1.__Weapon)
print(obj1._marvel__Weapon) # obj._ClassName__PrivateVariable

