myDict = {
    "fast" : "In a Quick Manner",
    "kai" : "A Programmer",
    "marks" : [77, 98, 42],
    "anotherDict" : {
        "jackie" : "another programmer",
        "tyson" : "a coder"
    },
    1 : 11
}

# Dictionary Methods 

# print(myDict.keys()) # This will print all the keys in the form of list. Although it's class won't be list

# print(type(myDict.keys())) # The class is dict_keys

# print(list(myDict.keys())) # Converting it to list

# print(type(list(myDict.keys()))) # Getting the class type

# print(myDict.values()) # This will print all the values in the dictionary

# print(myDict.items()) # Prints key and value for all the items in the dictionary in the form of tuple

# Both .get and [] will return the value if the key is present in the dictionary 
# print(myDict.get('kai')) # Will print the value of the given key
# print(myDict['kai'])

# If the key is not present in the list then [ ] will throw an error while .get will return none
print(myDict.get('kai2')) # This will return none as the key kai2 is not present in the dictionary
print(myDict['kai2']) # This will throw an error as the key is not present in the list


updateDict = {
    'apple' : 'red',
    'orange' : 'orange',
    'grapes' : 'green',
    'mango' : 'yellow'
}
# myDict.update(updateDict) # This will add all the elements from the provided dictionary to the dictionary on which the update method is called 

# myDict.update({'unknown' : 'nickname'}) # Will add new key and value to the dictionary

# myDict.clear() # Will remove all the elements from the dictionary

# print(myDict.pop('anotherDict')) # Will return the value at the given key and remove the key, value pair from the dictionary

# print(myDict.popitem()) # This will remove and return any random key value pair from the dictionary
# print(myDict)