# ## Types of Errors


try:
    print(x)
except NameError:
    print("NameError")
except:
    print("SomeError")


try:
    print(10/0)
except NameError:
    print("NameError")
except ZeroDivisionError:
    print("ZeroDivisionError")
except:
    print("SomeError")

try:
    l1 = [2, 3, 4, 5]
    print(l1[5])
except Exception as e:
    print(e)
    print(type(e))

try:
    d1 = {"name" : "VM"}
    print(d1["age"])
except Exception as e:
    print(e)
    print(type(e))

try:
    num = int("abc")
except Exception as okay:
    print(okay)
    print(type(okay))

