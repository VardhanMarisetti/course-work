# #### Using *args for function overloading


def fun2(*var):
    for v in var:
        print(v)

fun2(30)
print()
fun2(30, 40, 50)

def calc2(*var):
    return sum(var)

print(calc2())
print(calc2(10, 20, 10))
print(calc2(10, 30, 10, 20))

# #### Using decorator for function overloading


from multipledispatch import dispatch

@dispatch(int)
def fun(var1):
    print(var1)

@dispatch(int, int)
def fun(var1, var2):
    print(var1, var2)

@dispatch(float, float, int)
def fun(var1, var2, var3):
    print(var1, var2, var3)

fun(10)
fun(10, 20)
fun(2.5, 5.5, 2)

# ### Operator overloading


# we will perform different operations on the user defined objects using operators

class Dosa:
    def __init__(self, variety, price):
        self.Variety = variety
        self.Price = price
    def __add__(self, d2_val):
        total_price = self.Price + d2_val.Price
        return total_price

    def __sub__(self, d2_val):
        total_price = self.Price - d2_val.Price
        return total_price

    def __mul__(self, d2_val):
        total_price = self.Price * d2_val.Price
        return total_price

    def __truediv__(self, d2_val):
        total_price = self.Price / d2_val.Price
        return total_price

    def __floordiv__(self, d2_val):
        total_price = self.Price // d2_val.Price
        return total_price

    def __mod__(self, d2_val):
        total_price = self.Price % d2_val.Price
        return total_price

    def __pow__(self, d2_val):
        total_price = self.Price ** d2_val.Price
        return total_price

d1 = Dosa("Masala", 60)
d2 = Dosa("Paneer", 80)

print(d1 + d2)
print(d1 - d2)
print(d1 * d2)
print(d1 / d2) # __truediv__
print(d1 // d2) # __floordiv__
print(d1 % d2) # __mod__
#print(d1 ** d2) # __pow__

# comparison operators for operator overloading

class Dosa:
    def __init__(self, variety, price):
        self.Variety = variety
        self.Price = price

    def __gt__(self, d2_val):
        final_val = self.Price > d2_val.Price
        return final_val

    def __lt__(self, d2_val):
        final_val = self.Price < d2_val.Price
        return final_val

    def __eq__(self, d2_val):
        final_val = self.Price == d2_val.Price
        return final_val

    def __ge__(self, d2_val):
        final_val = self.Price >= d2_val.Price
        return final_val

    def __le__(self, d2_val):
        final_val = self.Price <= d2_val.Price
        return final_val

d1 = Dosa("Masala", 60)
d2 = Dosa("Paneer", 80)

print(d1 > d2) # __gt__
print(d1 < d2) # __lt__
print(d1 == d2) # __eq__
print(d1 >= d2) # __ge__
print(d1 <= d2) # __le__
