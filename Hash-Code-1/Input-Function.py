# we can take user input directly by using input() function.This input function gives a return value as
# string/character hence we have to pass that into a variable
# Input function took everything as a string. We need to modify as per our need
name = input(" Enter your name: ")
print("Welcome onboard " + name)
# Arithmatic operation using input function
a = input("First number is :")
b = input("Second number is :")
c=int(a)+int(b)
print("Addition of a and b:" "is", c)
c=int(a)-int(b)
print("Subtraction of a and b:" "is", c)
c=int(a)*int(b)
print("Multiplication of a and b:" "is", c)
c=int(a)/int(b)
print("Division of a and b:" "is", c)
c=int(a)//int(b)
print("Floor division of a and b:" "is", c)
c=int(a)**int(b)
print("Exponential value of a and b:" "is", c)
c=int(a)%int(b)
print("Modulus value of a and b:" "is", c)
