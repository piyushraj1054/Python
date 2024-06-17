# Typecasting = The conversion of one data type into the other data type. Python supports a wide variety of functions
# or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type
# casting in python.
# Two Types of Typecasting:
# Explicit Conversion (Explicit type casting in python) => Conversion doing by developer or user
# Implicit Conversion (Implicit type casting in python) => Python do it by itself
#Explicit Conversion
a="1"
print(type(a))
b="3"
print(type(b))
c=int(a)+int(b)
print(type(c))
print(c)
# Implicit Conversion
a = 2
print(type(a))
b = 5.4
print(type(b))
c = a + b
print(c)
print(type(c))