# Syntax for Creating a dictionary

myDict = {
    "Fast": "In a Quick Manner",
    "Kai": "A Programmer",
    "marks": [77, 98, 42],
    "anotherDict": {
        "jackie": "another programmer",
        "tyson": "a coder"
    }
}

# Accessing the elements in the dictionary
# print(myDict["Fast"])
# print(myDict['Kai'])
# print(myDict['marks'])
# print(myDict["anotherDict"]) # This will print the complete anotherDict
print(myDict["anotherDict"]['jackie']) # This will print the value for jackie in the anotherDict

# Dictionary is unordered 

# Dictionary is mutable 
# Modifying the elements in the Dictionary
myDict['marks'] = [89, 98, 79] # This will change the value of marks to a list 
print(myDict)
print(myDict['marks'])

# We cannot store duplicate keys in the dictionary 



