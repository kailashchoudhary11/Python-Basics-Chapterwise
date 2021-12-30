# greeting = "Suprabhat, "
# name = "kai"
# print(type(name))

# This will add both the strings and store them in c
# Concatenating two strings 
# c = greeting + name
# print(c)

name = "kai"

# Accessing single character in a string 
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])

# We cannot change the characters in a string 
# Strings are immutable in python
# name[2] = 'r'  # --> does not work 

# This will print the characters from 0 to 3. Character at 3 will not be included in this
# print(name[0:3])
# print(name[0:4]) # --> This will not give error but print all characters  
# print(name[1:3])  # This will give the characters at 1 and 2
# print(name[2:3])  # This will give the character at index 2

# print(name[:3])   # This will be same as name[0:3]  0 is the lowest index of the string name
# print(name[1:])   # This will be same as name[1:3] 3 is the length of the string name

# We can access the last index of the string using -1 similarly 2nd last by using -2 and so on
# print(name[-1]) # same as name[2]
# print(name[-2]) # same as name[1]
# print(name[-3]) # same as name[0]

# print(name[-3:-1]) # same as name[0:2]
# print(name[0:2])
# print(name[-3:]) # prints the entire string. same as name[0]

name = "kaiisawesome"
d = name[1:8:2] # This will print every 2nd character of the string from 1 to 8 
print(d)
e = name[1:8:3] # This will include every 3rd character of the string from 1 to 8
print(e)
f = name[0::3]
print(f)