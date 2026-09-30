
# # Exception Handling


# Exception handling allows us to respond to error without crashing the running application
# with exception handling we can create user error message

try:
    print(x)

except:
    print("Error")

print("hello")
a, b = 10, 20
print(a + b)

# Exception as e

try:
    print(x)

except Exception as e:
    print(f"Error: {e}")
    print(type(e))

try:
    print(x)
    
except TypeError:
    print("TypeError")
    
except:
    print("SomeError")
    
else:
    print("NoError")
    
finally:
    print("FinalLine")

print(x)

try:
    print(x)

age = -22

if age < 0:
    raise Exception("Age cannot be negative")

