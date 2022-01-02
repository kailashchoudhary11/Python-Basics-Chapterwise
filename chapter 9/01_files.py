# open content is used to open a file 
# f = open("sample.txt", 'r') # first argument is the file path and second one is mode of operation

f = open("sample.txt") # The default mode of operation is read

# .read() method is used to read the contents of the file 
# data = f.read()

# We can also specify the number of characters to be read 
data = f.read(8) # This will read the first 8 characters from the file

print(data)

# .close() method is used to close the file after we have successfully done the required operations on the file
f.close()

