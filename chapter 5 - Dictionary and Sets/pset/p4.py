s = set()
s.add(20)
s.add(20.0) # Since 20.0 is equal to 20. Therefore it won't be added to the set
s.add('20') # This will be added as 20 is not equal to '20'

# Hence the length of the set will be 2 
print(len(s))