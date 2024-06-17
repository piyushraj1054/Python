# A string is essentially a sequence of characters also called an array.
# we can access the elements of this array
world = "HashCode"
print(len(world))
print(world[1:6]) # including 1 and excluding 6.
print(world[-1]) # - starts from end of line. including only -1
print(world[0:-2]) # 8-2 =6 => till 6 including 0 not -2
# print(world[-1:-5]) # 8-1 = 7 and 8-5 = 3 , 7:3 not possible
print(world[-5:-1])
# Excercise
name = "Piyush"
print(len(name))
print(name[-4:-2]) # 6-4 = 2 and 6-2 = 4, therefore 2:4