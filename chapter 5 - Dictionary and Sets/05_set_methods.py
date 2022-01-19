# Creating empty set 
s = set()

# To add elements to a set use this method 
s.add(33) # This will add 33 to the set
s.add(9) # This will add 9 to the set
s.add(28) # This will add 28 to the set

s.add(9) # This won't work as set cannot contain duplicate elements

# Since list are mutable we cannot add list to a set 
# s.add([1, 2, 8]) # This will throw error. 

# Similarly we cannot add dictionary as well to a set. As it is also mutable
# s.add({'kai' : 'coder'})

# We can add tuple to a set because tuple are immutable 
# s.add((1, 2, 8)) # This will not throw error

# Length of a set 
# print(len(s)) # Will print the length of the set

# Removal of an element 
# s.remove(9) # Used to remove an element from the set. 
# s.remove(93) # Removing an element which is not present in the set will throw an error 

# print(s.pop()) # This will remove an random element from the tuple and return it 

# s.clear() # Will remove all the elements from the set
# print(s)

# print(s.union({3, 4, 5})) # This will return the union of set with the given set 

# print(s.intersection({33, 38, 23})) # This will return the intersection of the set with the given set

