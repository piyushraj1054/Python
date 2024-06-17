# Strings are immutable
# upper() :
# The upper() method converts a string to upper case.
world = "Hash Code !"
print(world.upper())
# lower()
# The lower() method converts a string to lower case.
print(world.lower())
# rstrip() :
# the rstrip() removes any trailing characters. no strip for leading characters
print(world.rstrip("!"))
# replace() :
# The replace() method replaces all occurences of a string with another string. Example:
print(world.replace("Hash","Hello"))
# capitalize() :
# The capitalize() method turns only the first character of the string to uppercase and the rest other characters of
# the string are turned to lowercase.
# The string has no effect if the first character is already uppercase.
a = "hash Code"
print(a.capitalize())
# center() :
# The center() method aligns the string to the center as per the parameters given by the user.
print(world.center(50))
# count() :
# The count() method returns the number of times the given value has occurred within the given string.
str="aabcdekkfjhvjsdhgvskj"
print(str.count("k"))
# endswith() :
# The endswith() method checks if the string ends with a given value. If yes then return True, else return False
print(world.endswith("!"))
print(world.endswith("e"))
# We can even also check for a value in-between the string by providing start and end index positions.
print(world.endswith("od",1,4))
print(world.endswith("od",1,8))
# find() :
# The find() method searches for the first occurrence of the given value and returns the index where it is present.
# If given value is absent from the string then return -1.
print(world.find("od"))
print(world.find("ap"))
# index() :
# The index() method searches for the first occurrence of the given value and returns the index where it is present.
# If given value is absent from the string then raise an exception.
print(world.index("Code"))
#print(world.index("code"))
# isalnum() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z, 0-9.
# If any other characters or punctuations are present, then it returns False.
print(world.isalnum())
print(a.isalnum())
print(str.isalnum())
# isalpha() :
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z.
# If any other characters or punctuations or numbers(0-9) are present, then it returns False.
print(world.isalpha())
# islower() :
# The islower() method returns True if all the characters in the string are lower case, else it returns False.
print(world.islower())
# isprintable() :
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.
print(world.isprintable())
# isspace() :
# The isspace() method returns True only and only if the string contains white spaces, else returns False.
print(world.isspace())
print(str.isspace())
# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.
print(world.istitle())
print(str.istitle())
# isupper() :
# The isupper() method returns True if all the characters in the string are upper case, else it returns False.
print(world.isupper())
# startswith() :
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.
print(world.startswith("Hash"))
# swapcase() :
# The swapcase() method changes the character casing of the string.
# Upper case are converted to lower case and lower case to upper case.
print(world.swapcase())
# title() :
# The title() method capitalizes each letter of the word within the string.
str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())