f = open("sample.txt")

# .readline() method will read a single complete line at a time 
line = f.readline() # this will read only the first line from the file

line2 = f.readline() # this will ready the second line as it has already read first line

print(line, end = "")
print(line2)
